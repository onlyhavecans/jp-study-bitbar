#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-

# <bitbar.title>WaniKani BitBar</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Amelia Aronsohn</bitbar.author>
# <bitbar.author.github>onlyhavecans</bitbar.author.github>
# <bitbar.desc>Shows available lessons and reviews with links</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# To install, you will want to generate an API key and store the
# key in ~/.config/wanikani.com/api.key
# https://www.wanikani.com/settings/personal_access_tokens

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_KEY = os.path.expanduser("~/.config/wanikani.com/api.key")
SUMMARY_ENDPOINT = "https://api.wanikani.com/v2/summary"


def error(message):
    print("WK: X")
    print("---")
    print(message)
    exit()


def get(url, apikey):
    r = Request(url, method="GET")
    r.add_header("Authorization", f"Bearer {apikey}")
    r.add_header("Wanikani-Revision", "20170710")
    try:
        result = urlopen(r).read()
    except HTTPError as e:
        error(f"Status: {e.code}: {e.reason}")
    except URLError as e:
        error(f"Error {e.reason}")
    else:
        return json.loads(result)


def parse_counts(study_data):
    info = study_data["data"]
    lesson_count = len(info["lessons"][0]["subject_ids"])
    review_count = len(info["reviews"][0]["subject_ids"])
    return {"lessons": lesson_count, "reviews": review_count}


if __name__ == "__main__":
    if not os.path.exists(API_KEY):
        error("Missing API Key")

    with open(API_KEY) as key_file:
        key = key_file.read().strip()
        summary = get(SUMMARY_ENDPOINT, key)
        counts = parse_counts(summary)

        print(f"WK: L:{counts['lessons']} R:{counts['reviews']}")
        print("---")

        print("LESSONS & REVIEWS | size=10")

        print(f"Lessons - {counts['lessons']} | href=https://www.wanikani.com/lesson")
        print(f"Reviews - {counts['reviews']} | href=https://www.wanikani.com/review")
