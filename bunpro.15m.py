#!/usr/bin/env python3

# <xbar.title>BunPro</xbar.title>
# <xbar.version>v1.0</xbar.version>
# <xbar.author>Amelia Aronsohn</xbar.author>
# <xbar.author.github>onlyhavecans</xbar.author.github>
# <xbar.desc>Shows available lessons and reviews with links</xbar.desc>
# <xbar.dependencies>python</xbar.dependencies>
# <xbar.var>string(BUNPRO_API_KEY): Your Bunpro API key</xbar.environment>

# To generate an API key for this plugin's Settings
# https://bunpro.jp/settings/api

import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ENDPOINT = "https://bunpro.jp/api/user/{0}/study_queue"


def error(message: str):
    """Set the titlebar to BP: X, print the message in the dropdown menu"""
    print("BP: X")
    print("---")
    print(message)


def get(url: str, apikey: str) -> dict[str, dict[str, str]] | None:
    """Retrieve the API request and return parsed JSON, or report error and exit"""
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


def parse_queue(study_data: dict[str, dict[str, str]]) -> dict[str, str]:
    """Parse bunpro api request down to name, ghosts, & reviews available"""
    info: dict[str, str] = {}
    user = study_data["user_information"]
    info["name"] = user["username"]
    info["ghosts"] = user["ghost_review_count"]
    info["reviews"] = study_data["requested_information"]["reviews_available"]
    info["hour"] = study_data["requested_information"]["reviews_available_next_hour"]
    info["day"] = study_data["requested_information"]["reviews_available_next_day"]
    return info


if __name__ == "__main__":
    api_key = os.getenv("BUNPRO_API_KEY", None)
    if api_key is None:
        error("BUNPRO_API_KEY is unset in env")
        sys.exit()

    summary = get(ENDPOINT, api_key)
    if summary is None:
        sys.exit()

    counts = parse_queue(summary)

    print(f"BP: {counts['reviews']}")
    print("---")

    print("REVIEWS | size=10")
    print(f"Reviews Now: {counts['reviews']} | href=https://bunpro.jp/reviews")
    print(f"Reviews Next Hour: {counts['hour']}")
    print(f"Reviews Next Day: {counts['day']}")

    print("---")
    print(f"You have {counts['ghosts']} Ghosts!")
    print("Lessons | href=https://bunpro.jp/learn")
