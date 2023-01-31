# Japanese Study ~~BitBar~~ xBar Plugins

These are some plugins for helping keep on top of Japanese study resources I use.

## Requirements

You will need to install [xBar](https://xbarapp.com)

I tried to make this to use default python3 with no extra requirements. Many version of macOS do not come with python3, or may not have python at all. If you are having issues and are not sure try opening Terminal.app and running the command `python3 --version`. If that command gives you a sad, you may need to [install python3](https://www.python.org/downloads/)

## WaniKani (Kanji)

1. Get your read-only v2 api key [from WaniKani](https://www.wanikani.com/settings/personal_access_tokens)
1. Copy `wanikani.15m.py` into your xBar Folder
1. Click `Open Plugin` in the plugin's dropdown and fill out the API_KEY in settings

## Bunpro (Grammar)

1. Get your api key [from your Bunpro api page](https://bunpro.jp/settings/api)
1. Copy `bunpro.15m.py` into your xBar Folder
1. Click `Open Plugin` in the plugin's dropdown and fill out the API_KEY in settings

## Bonus

### Wanikani Wallpaper

[Wanikani Wallpaper](https://wkw.natural20design.com)

*Do not put this in bitbar!* Put this in cron or something.

wk-wallpaper is a shell script for saving out your wallpaper on a daily basis, so you can keep a history and have amazing wallpapers.
