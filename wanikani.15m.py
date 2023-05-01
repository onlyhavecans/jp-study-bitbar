#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-

# <xbar.title>WaniKani xbar</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Amelia Aronsohn</xbar.author>
# <xbar.author.github>onlyhavecans</xbar.author.github>
# <xbar.desc>Shows available lessons and reviews with links</xbar.desc>
# <xbar.dependencies>python</xbar.dependencies>
# <xbar.var>string(API_KEY): Your WaniKani API key</xbar.environment>

# To generate an API key for this plugin's Settings
# https://www.wanikani.com/settings/personal_access_tokens

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

SUMMARY_ENDPOINT = "https://api.wanikani.com/v2/summary"


def error(message):
    print("WK: X")
    print("---")
    print(message)


def get(url, apikey) -> dict | None:
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


def parse_counts(study_data) -> dict:
    info = study_data["data"]
    lesson_count = len(info["lessons"][0]["subject_ids"])
    review_count = len(info["reviews"][0]["subject_ids"])
    return {"lessons": lesson_count, "reviews": review_count}


if __name__ == "__main__":
    api_key = os.getenv("API_KEY", None)
    if api_key is None:
        error("Missing API Key")
        sys.exit()

    summary = get(SUMMARY_ENDPOINT, api_key)
    if summary is None:
        sys.exit()

    counts = parse_counts(summary)

    print(f"WK: L:{counts['lessons']} R:{counts['reviews']}")
    print("---")

    print("LESSONS & REVIEWS | size=10")

    print(f"Lessons - {counts['lessons']} | href=https://www.wanikani.com/lesson")
    print(f"Reviews - {counts['reviews']} | href=https://www.wanikani.com/review")
