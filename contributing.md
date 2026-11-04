# Contribution Guidelines

Thank you for helping keep this list complete and accurate. It aims to list every app that plays from a Plex, Jellyfin or Emby server, on every platform, so additions of small and regional apps are welcome too.

## How the list is built

All entries live in [data/clients.yaml](data/clients.yaml). `README.md`, `PLATFORMS.md` and `more-clients.md` are generated from it, so never edit those three files by hand.

1. Fork the repository and edit `data/clients.yaml`.
2. Run `python3 scripts/generate.py` (needs Python 3.8+ and PyYAML: `pip install pyyaml`). It validates the data and rewrites the Markdown files.
3. Commit the data change together with the regenerated files and open a pull request that says what you changed and where the facts come from.

CI runs `python3 scripts/generate.py --check` and fails if the data is invalid or the Markdown files are out of date.

## What belongs here

- **Clients only.** The app must browse and play (or read) media from at least one of Plex, Jellyfin or Emby through the server's own API. Apps that only reach a server through DLNA, SMB or a browser bookmark do not qualify. Remotes, admin tools and bridges go in the companion section with the matching `category`.
- **It must work.** No empty repositories, plans, READMEs without code, or projects that cannot play anything yet.
- **One entry per app.** An app on several platforms or stores is one entry: list its platforms and add the extra store links under `links`. A renamed app keeps one entry with the old name in `aliases`. Forks get their own entry only when they are a distinct app with their own name or releases.
- **Official links only.** The main `url` must be the app's own repository, store listing or website. Never link mirrors, re-uploads, APK sites or download portals.
- **No cracks or piracy.** Licence bypasses (Emby Premiere or Plex Pass "unlockers", patched official apps) and piracy or account-reseller services are not accepted.

### Beware of fake download repos

Some repositories on GitHub, GitLab and Codeberg use the Plex, Jellyfin and Emby names to push malware: "full version", "unlocked", "crack with license key" or "desktop helper" repos with no code and an off-site download link, often kept looking fresh by automated commits. Never add them and never download from them. The official apps come only from [plex.tv](https://www.plex.tv/apps-devices/), [jellyfin.org](https://jellyfin.org/downloads/) and [emby.media](https://emby.media/download.html).

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

- **description**: one plain line for users, at most about 110 characters: what the app is and what you get. No hype words, no star counts, and no need to repeat the servers or platforms, which are shown as tags.
- **platforms**: only values from `PLATFORMS` in [scripts/generate.py](scripts/generate.py), for example `android-tv` (also Google TV), `fire-tv`, `vega-os`, `tvos`, `webos`, `tizen`, `roku`, `ps4`, `switch`, `quest`, `carplay`, `wear-os`, `kodi`, `cli`. Tag `visionos` or `macos` only for real builds, not for iPad apps that the App Store merely allows on those devices.
- **category**: `player`, `music`, `audiobooks`, `books`, `photos`, `live-tv`, `shim` (plays server items in mpv or another external player), `remote`, `admin` or `bridge`.
- **links** keys: `repo`, `site`, `appstore`, `play`, `msstore`, `amazon`, `flathub`, `fdroid`, `snap`, `aur`, `roku`, `meta`, `appgallery`, `steam`, `testflight`, `lgstore`, `other`. Add a suffix for a second link of the same kind, such as `repo:Roku`.
- **long_tail: true** moves an entry to `more-clients.md`. Use it for GitHub-only projects with no release and under 10 stars.
- **distinct: true** is required on every entry whose name matches another entry's name, to confirm they are different apps.

Entries are sorted alphabetically by the generator; the order in the YAML file does not matter, but keep it alphabetical to make diffs easy to read.

## Updating an entry

If an app was renamed, changed its servers, moved to a new repository or was discontinued, update its entry, keep the old name in `aliases`, and mention your source in the pull request. When an app's links are all dead, set `status: discontinued` and remove the dead `url`.

## License Reminder

All contributions are subject to the repository's license: [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
