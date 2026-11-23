"""Check Pinterest pin publication and destination without logging in.

Usage (from any directory):
    python tools/check_pin.py listing
    python tools/check_pin.py movein moveout
    python tools/check_pin.py all

Read-only: fetches public profile JSON and public pin pages. It never edits files.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = "https://www.pinterest.com/JapanLivingNotes/"
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
}
TARGET = "payhip.com/b/4ak8D"
# Confirmed pin IDs. Pinterest may reprocess an image and change its signature,
# and the profile JSON does not always expose the title. Record the ID once a
# pin is confirmed so later checks can verify the detail page directly.
KNOWN_IDS = {
    "costs": "687995280623935762",
    "foreigners": "687995280623936667",
    "emails": "687995280623936675",
    "listing": "687995280624005769",
    "movein": "687995280624022670",
}
# Expected strings come from marketing/pinterest-schedule.md (the reservation record).
EXPECTED = {
    "costs": ("Japan apartment initial costs explained", "Deposit, key money, agency fee"),
    "foreigners": ("How foreigners can rent an apartment in Japan", "guarantor companies"),
    "emails": ("Email templates for Japanese real estate agents", "copy-and-paste English emails"),
    "listing": ("How to read a Japanese apartment listing", "walk minutes, building age"),
    "movein": ("Moving into your Japan apartment: the 14-day checklist", "address registration within 14 days"),
    "moveout": ("Moving out of a Japan apartment: get your deposit back", "move-out inspection"),
}


def now_jst() -> str:
    return (dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S JST")


def get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.status, response.read().decode("utf-8", "replace")


def signature(key: str) -> str:
    png = ROOT / "marketing" / "pins" / f"pin_{key}.png"
    return hashlib.md5(png.read_bytes()).hexdigest()


def pin_ids(key: str) -> tuple[list[str], str]:
    """Find public pins by title, falling back to the local PNG signature.

    Pinterest may reprocess the uploaded image, changing image_signature.
    The pin title is stable, so match on it first and use the signature only
    as a fallback for older pins whose title is not exposed in profile JSON.
    """
    title, _ = EXPECTED[key]
    sig = signature(key)
    _, page = get(PROFILE)
    match = re.search(
        r'<script id="__PWS_INITIAL_PROPS__" type="application/json">(.*?)</script>', page, re.S
    )
    if not match:
        raise RuntimeError("profile JSON not found")
    pins = json.loads(match.group(1)).get("initialReduxState", {}).get("pins", {})
    by_title = [
        str(v["id"])
        for v in pins.values()
        if v.get("title") == title and str(v.get("id", "")).isdigit()
    ]
    by_sig = [
        str(v["id"])
        for v in pins.values()
        if v.get("image_signature") == sig and str(v.get("id", "")).isdigit()
    ]
    known = [KNOWN_IDS[key]] if key in KNOWN_IDS else []
    ids = list(dict.fromkeys(by_title + by_sig + known))
    if by_title:
        method = "title"
    elif by_sig:
        method = "signature"
    elif known:
        method = "known_id"
    else:
        method = "none"
    return ids, method


def detail(pid: str, key: str) -> str:
    title, desc = EXPECTED[key]
    try:
        status, page = get(f"https://www.pinterest.com/pin/{pid}/")
    except urllib.error.HTTPError as exc:
        return f"http={exc.code}"
    click = ""
    match = re.search(r'data-test-id="clickthrough-link"[^>]*href="([^"]+)"', page, re.S)
    if match:
        click = html.unescape(match.group(1))
    return (
        f"http={status} title={'OK' if title in page else 'MISSING'} "
        f"desc={'OK' if desc in page else 'MISSING'} "
        f"pinid_in_page={'OK' if pid in page else 'MISSING'} "
        f"clickthrough={click or 'MISSING'} "
        f"destination={'OK' if TARGET in click else 'MISSING'}"
    )


def check(key: str) -> bool:
    sig = signature(key)
    ids, method = pin_ids(key)
    if not ids:
        print(f"RESULT {now_jst()} pin={key} status=unpublished pin_id=未取得 clickthrough=未取得 sig={sig} match=none", flush=True)
        return False
    ok = False
    for pid in ids:
        info = detail(pid, key)
        good = all(
            part in info
            for part in ("http=200", "title=OK", "desc=OK", "pinid_in_page=OK", "destination=OK")
        )
        ok = ok or good
        print(f"RESULT {now_jst()} pin={key} status={'published' if good else 'needs_review'} pin_id={pid} {info} sig={sig} match={method}", flush=True)
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pins", nargs="+", help="pin keys (costs/foreigners/emails/listing/movein/moveout) or 'all'")
    args = parser.parse_args()
    keys = list(EXPECTED) if "all" in args.pins else args.pins
    bad = [key for key in keys if key not in EXPECTED]
    if bad:
        parser.error(f"unknown pin key(s): {', '.join(bad)}")
    results = []
    for key in keys:
        try:
            results.append(check(key))
        except Exception as exc:  # keep checking the remaining pins
            print(f"ERROR {now_jst()} pin={key} {type(exc).__name__}:{exc}", flush=True)
            results.append(False)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
