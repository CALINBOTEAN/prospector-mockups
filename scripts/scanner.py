#!/usr/bin/env python3
"""
PROSPECTOR — Agent 1: Scanner
Finds Romanian businesses with no website (or social-media-only presence)
using Google Places API (New) Text Search.

Usage:
    export GOOGLE_PLACES_API_KEY="your-key"
    python3 scanner.py --categories data/categories_ro.txt \
                       --localities data/localities_cluj.txt \
                       --pipeline  data/pipeline.csv \
                       --out       data/

Cost model (verify current figures at https://mapsplatform.google.com/pricing/):
    The field mask below includes websiteUri / nationalPhoneNumber / rating,
    which bill every Text Search call at the ENTERPRISE SKU
    (approx. USD 35 / 1,000 calls; approx. 1,000 free calls per month).
    The --max-requests guard (default 250) keeps a run safely inside the
    free tier. Do not raise it above ~900/month without checking billing.

Note: the API has no email field, in any version (Legacy or New). This
scanner only ever produces phone numbers / Maps URLs / social URLs — email
discovery for the WhatsApp-first outreach flow is not needed downstream,
but if email is ever added back in, it requires a separate lookup step.
"""

import argparse
import csv
import datetime
import os
import sys
import time

import requests

ENDPOINT = "https://places.googleapis.com/v1/places:searchText"

FIELD_MASK = ",".join([
    "places.id",
    "places.displayName",
    "places.formattedAddress",
    "places.nationalPhoneNumber",
    "places.websiteUri",
    "places.rating",
    "places.userRatingCount",
    "places.types",
    "places.googleMapsUri",
    "nextPageToken",
])

# A "website" pointing at these domains is NOT a real website — it is a lead.
SOCIAL_DOMAINS = (
    "facebook.com", "fb.com", "instagram.com", "wa.me", "whatsapp.com",
    "linktr.ee", "olx.ro", "publi24.ro", "lajumate.ro", "google.com/maps",
)

request_count = 0


def search_page(session, api_key, query, page_token=None):
    """One Text Search request (one billable Enterprise call)."""
    global request_count
    body = {
        "textQuery": query,
        "languageCode": "ro",
        "regionCode": "RO",
        "pageSize": 20,
    }
    if page_token:
        body["pageToken"] = page_token
    resp = session.post(
        ENDPOINT,
        json=body,
        headers={
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": FIELD_MASK,
            "Content-Type": "application/json",
        },
        timeout=30,
    )
    request_count += 1
    if resp.status_code != 200:
        print(f"  ! HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        return {}
    return resp.json()


def classify_website(uri):
    """Returns (is_lead, status, social_url)."""
    if not uri:
        return True, "none", ""
    low = uri.lower()
    for dom in SOCIAL_DOMAINS:
        if dom in low:
            return True, "social_only", uri
    return False, "has_website", uri


def load_known_ids(pipeline_path):
    known = set()
    if pipeline_path and os.path.exists(pipeline_path):
        with open(pipeline_path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                pid = (row.get("place_id") or "").strip()
                if pid:
                    known.add(pid)
    return known


def main():
    ap = argparse.ArgumentParser(description="Prospector scanner")
    ap.add_argument("--categories", required=True)
    ap.add_argument("--localities", required=True)
    ap.add_argument("--pipeline", default="")
    ap.add_argument("--out", default=".")
    ap.add_argument("--max-pages", type=int, default=1,
                    help="Pages per query (20 results each). Default 1.")
    ap.add_argument("--max-requests", type=int, default=250,
                    help="Hard stop on billable calls this run. Default 250.")
    args = ap.parse_args()

    api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not api_key:
        sys.exit("ERROR: set GOOGLE_PLACES_API_KEY in the environment first.")

    with open(args.categories, encoding="utf-8") as f:
        categories = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    with open(args.localities, encoding="utf-8") as f:
        localities = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    planned = len(categories) * len(localities) * args.max_pages
    print(f"Plan: {len(categories)} categories x {len(localities)} localities "
          f"x {args.max_pages} page(s) = up to {planned} billable calls "
          f"(hard cap {args.max_requests}).")
    if planned > args.max_requests:
        print("NOTE: the cap will stop the run early; split categories or "
              "localities across weekly runs instead.")

    known_ids = load_known_ids(args.pipeline)
    seen_this_run = set()
    leads, skipped_known, had_website = [], 0, 0
    today = datetime.date.today().isoformat()
    session = requests.Session()

    stop = False
    for cat in categories:
        if stop:
            break
        for loc in localities:
            if request_count >= args.max_requests:
                print("Hard request cap reached — stopping cleanly.")
                stop = True
                break
            query = f"{cat} {loc}"
            token, page = None, 0
            while page < args.max_pages:
                if request_count >= args.max_requests:
                    stop = True
                    break
                data = search_page(session, api_key, query, token)
                for p in data.get("places", []):
                    pid = p.get("id", "")
                    if not pid or pid in seen_this_run:
                        continue
                    seen_this_run.add(pid)
                    if pid in known_ids:
                        skipped_known += 1
                        continue
                    is_lead, status, social = classify_website(p.get("websiteUri"))
                    if not is_lead:
                        had_website += 1
                        continue
                    leads.append({
                        "place_id": pid,
                        "scan_date": today,
                        "name": p.get("displayName", {}).get("text", ""),
                        "category_query": cat,
                        "locality": loc,
                        "address": p.get("formattedAddress", ""),
                        "phone": p.get("nationalPhoneNumber", ""),
                        "website_status": status,
                        "social_url": social,
                        "rating": p.get("rating", ""),
                        "review_count": p.get("userRatingCount", 0),
                        "maps_url": p.get("googleMapsUri", ""),
                        "types": "|".join(p.get("types", [])[:5]),
                    })
                token = data.get("nextPageToken")
                page += 1
                if not token:
                    break
                time.sleep(2)  # token needs a short delay before reuse
            print(f"  [{request_count:>4}] {query}: {len(leads)} leads so far")

    os.makedirs(args.out, exist_ok=True)
    out_path = os.path.join(args.out, f"scan_{today}.csv")
    fields = ["place_id", "scan_date", "name", "category_query", "locality",
              "address", "phone", "website_status", "social_url", "rating",
              "review_count", "maps_url", "types"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(leads)

    print("\n===== SCAN COMPLETE =====")
    print(f"Billable calls used : {request_count}")
    print(f"New leads found     : {len(leads)}")
    print(f"  - no website      : {sum(1 for l in leads if l['website_status'] == 'none')}")
    print(f"  - social only     : {sum(1 for l in leads if l['website_status'] == 'social_only')}")
    print(f"Already in pipeline : {skipped_known}")
    print(f"Had real website    : {had_website}")
    print(f"Output              : {out_path}")
    print("Next step: run the prospector-qualify skill on this file.")


if __name__ == "__main__":
    main()
