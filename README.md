# Japanese Study BitBar Plugins

These are some plugins for helping keep on top of Japanese study resources I use.

## Requirements

You will need to install [BitBar](https://github.com/matryer/bitbar)

I tried to make this to use default python3 with no extra requirements. However older macOS might not have python3. If you are having issues and are not sure try opening Terminal.app and running the command `python3 --version`. If that command gives you a sad, you may need to [install python3](https://www.python.org/downloads/)

## WaniKani (Kanji)

1. Get your read-only v2 api key [from WaniKani](https://www.wanikani.com/settings/personal_access_tokens)
1. Open Terminal.app and run `mkdir -p ~/.config/wanikani.com/ && open -a TextEdit.app ~/.config/wanikani.com/api.key`
1. Put the api key in the file and save, which will save to `~/.config/wanikani.com/api.key`
1. Copy `wanikani.15m.py` into your BitBar Folder (or use the included Enabled!)

## Bunpro (Grammar)

1. Get your api key [from your Bunpro settings page](https://bunpro.jp/)
1. Open Terminal.app and run `mkdir -p  ~/.config/bunpro.jp/ && open -a TextEdit.app ~/.config/bunpro.jp/api.key`
1. Put the api key in the file and save, which will save to `~/.config/bunpro.jp/api.key`
1. Copy `bunpro.15m.py` into your BitBar Folder (or use the included Enabled!)

## Bonus

### Wanikani Wallpaper

[Wanikani Wallpaper](https://wkw.natural20design.com)

*Do not put this in bitbar!* Put this in cron or something.

wk-wallpaper is a shell script for saving out your wallpaper on a daily basis, so you can keep a history and have amazing wallpapers.
