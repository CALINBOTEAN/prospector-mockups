"""
Fetch real photos for a single Places API (New) place_id, for use by
prospector-mockup (Agent 3).

Two-step Places API (New) flow:
  1. Place Details with FieldMask "photos" -> photo resource names,
     dimensions, and author attributions (required for display credit).
  2. Photo Media endpoint per resource -> actual image bytes, followed
     via HTTP redirect (no skipHttpRedirect) so we get raw bytes back
     directly rather than a time-limited signed URL. Bytes are embedded
     as base64 data URIs so the mockup stays a single self-contained file
     (no external image hosting, no expiring links).

Cost note: Photos live behind a billed tier of Place Details distinct
from the Enterprise-tier fields (rating, hours, businessStatus) already
used elsewhere in this pipeline -- verify current SKU pricing at
https://mapsplatform.google.com/pricing/ before relying on this at
volume. If the API key's project lacks that entitlement, Google returns
HTTP 200 with the `photos` field silently absent (not an error) --
callers MUST treat zero photos as "omit the gallery", never as a
reason to fabricate images.

Usage:
  python fetch_place_photos.py <place_id> [--max-photos 5] [--max-width 800] [--out out.json]
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

PLACES_BASE = "https://places.googleapis.com/v1"


def get_photo_refs(place_id, api_key):
    url = f"{PLACES_BASE}/places/{place_id}"
    req = urllib.request.Request(url, headers={
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "photos",
    })
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    return data.get("photos", [])


def fetch_photo_bytes(photo_name, api_key, max_width):
    # No skipHttpRedirect: urllib follows the 302 straight to image bytes,
    # avoiding a time-limited signed photoUri we'd have to re-fetch later.
    url = f"{PLACES_BASE}/{photo_name}/media?maxWidthPx={max_width}&key={api_key}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        content_type = resp.headers.get("Content-Type", "image/jpeg")
        body = resp.read()
    return content_type, body


def build_attribution(photo):
    attrs = photo.get("authorAttributions", [])
    names = [a.get("displayName") for a in attrs if a.get("displayName")]
    if names:
        return "Fotografii: " + ", ".join(dict.fromkeys(names)) + " (via Google Maps)"
    return "Fotografii preluate de pe profilul Google al afacerii."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("place_id")
    ap.add_argument("--max-photos", type=int, default=5)
    ap.add_argument("--max-width", type=int, default=800)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not api_key:
        print("GOOGLE_PLACES_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    photos = get_photo_refs(args.place_id, api_key)
    if not photos:
        result = {"place_id": args.place_id, "photo_count": 0, "photos": [],
                   "note": "No photos returned by Places API (either the listing has none, "
                           "or this API key's project lacks the billing entitlement for the "
                           "photos field -- Google returns 200 with the field silently absent "
                           "in both cases). Gallery section must be omitted, not faked."}
        out = json.dumps(result, ensure_ascii=False, indent=2)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(out)
        print(out)
        return

    picked = photos[: args.max_photos]
    out_photos = []
    for p in picked:
        name = p["name"]
        try:
            content_type, body = fetch_photo_bytes(name, api_key, args.max_width)
        except urllib.error.HTTPError as e:
            print(f"WARN: failed to fetch {name}: {e.code} {e.read().decode(errors='replace')}",
                  file=sys.stderr)
            continue
        b64 = base64.b64encode(body).decode("ascii")
        out_photos.append({
            "name": name,
            "content_type": content_type,
            "width_px": p.get("widthPx"),
            "height_px": p.get("heightPx"),
            "attribution": build_attribution(p),
            "data_uri": f"data:{content_type};base64,{b64}",
            "bytes": len(body),
        })

    result = {
        "place_id": args.place_id,
        "photo_count": len(out_photos),
        "photos": out_photos,
    }
    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"wrote {args.out} ({len(out_photos)} photos)")
    else:
        print(out)


if __name__ == "__main__":
    main()
