#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-

# <bitbar.title>BunPro BitBar</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Amelia Aronsohn</bitbar.author>
# <bitbar.author.github>onlyhavecans</bitbar.author.github>
# <bitbar.desc>Shows available lessons and reviews with links</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# To install, you will want to generate an API key and store the
# key in ~/.config/bunpro.jp/api.key
# https://bunpro.jp/ Click Account -> Setting

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_KEY = os.path.expanduser("~/.config/bunpro.jp/api.key")
ENDPOINT = "https://bunpro.jp/api/user/{0}/study_queue"


def error(message):
    print("BP: X")
    print("---")
    print(message)
    exit()


def get(url, apikey):
    u = url.format(apikey)
    r = Request(u, method="GET")
    r.add_header(
        "User-Agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
    )
    try:
        result = urlopen(r).read()
    except HTTPError as e:
        error(f"Status: {e.code}: {e.reason}")
    except URLError as e:
        error(f"Error {e.reason}")
    else:
        return json.loads(result)


def parse_queue(study_data):
    info = {}
    user = study_data["user_information"]
    info["name"] = user["username"]
    info["ghosts"] = user["ghost_review_count"]
    info["reviews"] = study_data["requested_information"]["reviews_available"]
    return info


if __name__ == "__main__":
    if not os.path.exists(API_KEY):
        error("Missing API Key")

    with open(API_KEY) as key_file:
        key = key_file.read().strip()
        summary = get(ENDPOINT, key)
        counts = parse_queue(summary)

        print(f"BP: {counts['reviews']}")
        print("---")

        print("REVIEWS | size=10")
        print(f"Reviews - {counts['reviews']} | href=https://bunpro.jp/study")

        print("---")
        print(f"You have {counts['ghosts']} Ghosts!")
        print("Lessons | href=https://bunpro.jp/learn")
