# Contribution Guidelines

Thank you for helping keep this list complete and right. It aims to list every app that plays from a Plex or Jellyfin or Emby server on every platform. Small and regional apps are welcome too.

## How the list is built

All entries live in [data/clients.yaml](data/clients.yaml). `README.md` and `PLATFORMS.md` and `more-clients.md` and the pages in `platforms/` are generated from it. Never edit them by hand.

1. Fork the repository and edit `data/clients.yaml`.
2. Run `python3 scripts/generate.py`. It needs Python 3.8 or newer and PyYAML (`pip install pyyaml`). It checks the data and rewrites the Markdown files.
3. Commit the data change together with the regenerated files. Open a pull request that says what you changed and where the facts come from.

CI runs `python3 scripts/generate.py --check`. It fails when the data is invalid or the Markdown files are out of date.

## What belongs here

- **Clients only.** The app must browse and play or read media from Plex or Jellyfin or Emby through the server's own API. An app that only reaches a server through DLNA or SMB or a browser bookmark does not count. The same goes for an app that only opens the server's own web interface. A packaged app that wraps that interface can stay. Examples are the official Jellyfin app for iOS and Emby for PS4. Remotes and admin tools and bridges go in the companion section with the matching `category`.
- **It must work.** No empty repositories. No plans or READMEs without code. No projects that cannot play anything yet.
- **One entry per app.** An app on several platforms or stores is one entry. List its platforms and add the extra store links under `links`. A renamed app keeps one entry with the old name in `aliases`. A fork gets its own entry only when it is a separate app with its own name or releases.
- **Official links only.** The main `url` must be the app's own repository or store listing or website. Never link mirrors or re-uploads or APK sites or download portals.
- **No cracks or piracy.** Licence bypasses are not accepted. That covers Emby Premiere or Plex Pass "unlockers" and patched official apps. Piracy and account-reseller services are not accepted either.

### Beware of fake download repos

Some repositories on GitHub and GitLab and Codeberg use the Plex and Jellyfin and Emby names to push malware. They promise a "full version" or an "unlocked" build or a "crack with license key" or a "desktop helper". They have no code and an off-site download link. Automated commits often keep them looking fresh. Never add them and never download from them. The official apps come only from [plex.tv](https://www.plex.tv/apps-devices/) and [jellyfin.org](https://jellyfin.org/downloads/) and [emby.media](https://emby.media/download.html).

## Entry format

```yaml
- name: Plezy                      # the app's own name
  url: https://github.com/edde746/plezy   # repository for open-source apps, else website or store listing
  links:                           # optional extra links, one per kind
    appstore: https://apps.apple.com/app/id6754315964
  servers: [plex, jellyfin, emby]  # which of the three it supports today
  also: [subsonic]                 # optional other back ends
  official: false                  # true only for Plex Inc., Jellyfin project and Emby LLC apps (then add vendor:)
  platforms: [windows, macos, linux, android, android-tv, ios, tvos]
  category: player
  media: [video]
  open_source: true                # null if unknown
  license: GPL-3.0                 # only for open-source apps
  price: paid                      # free, freemium, paid, subscription; omit if unknown
  status: active                   # active, beta, stale, discontinued, unknown
  status_year: 2026                # year of the last update, or the year it ended
  description: Multi-server client with cross-server search and Live TV.
```

- **description** is one plain line for users of about 110 characters at most. Say what the app is and what you get. No hype words and no star counts. The servers and platforms show as tags so there is no need to repeat them.
- **platforms** takes only values from `PLATFORMS` in [scripts/generate.py](scripts/generate.py). Examples are `android-tv` (also Google TV) and `fire-tv` and `vega-os` and `tvos` and `webos` and `tizen` and `roku` and `ps4` and `switch` and `quest` and `carplay` and `wear-os` and `kodi` and `cli`. The rules for each tag are under [Platform tags](#platform-tags).
- **category** is one of `player` `music` `audiobooks` `books` `photos` `live-tv` `shim` `remote` `admin` or `bridge`. A shim plays server items in mpv or another external player.
- **links** keys are `repo` `site` `appstore` `play` `msstore` `amazon` `flathub` `fdroid` `snap` `aur` `roku` `meta` `appgallery` `steam` `testflight` `lgstore` and `other`. Add a suffix for a second link of the same kind such as `repo:Roku`.
- **long_tail: true** moves an entry to `more-clients.md`. Use it for projects that live only on GitHub with no release and under 10 stars.
- **distinct: true** is needed on every entry whose name matches another entry's name. It confirms they are different apps.

The generator sorts entries by name so the order in the YAML file does not matter. Keeping it alphabetical makes diffs easier to read.

## Platform tags

Tag a platform only for a build that ships for it or that the app documents for it. Planned platforms and ones marked coming soon are never tagged.

- `ipados` needs an iPad build of its own. An iPhone app that runs on an iPad in compatibility mode does not get it. The same rule keeps iPad apps out of `macos` and `visionos` when the App Store merely allows them there.
- `chromecast` is only for Cast receiver apps. Casting from a phone app does not count. An app you install on a Chromecast with Google TV gets `android-tv`.
- `fire-tv` needs the app to say it runs on Fire TV or a listing of its own in the Amazon Appstore.
- `android-auto` means Android Auto itself. An Android head unit is not Android Auto. Android Automotive has its own tag `android-automotive`.
- `wear-os` needs an app that runs on the watch. A phone app that shows its controls on the watch does not count.
- Terminal apps get `cli` and no OS tags. A project that also ships a separate desktop app gets the OS tags of that app too.

## Updating an entry

Update the entry when an app was renamed or changed its servers or moved to a new repository or ended. Keep the old name in `aliases` and mention your source in the pull request. When all of an app's links are dead, set `status: discontinued` and remove the dead `url`.

## License Reminder

All contributions fall under the repository's license. That is the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
