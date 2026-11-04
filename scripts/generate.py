#!/usr/bin/env python3
"""Validate data/clients.yaml and render README.md, PLATFORMS.md and more-clients.md from it.

    python3 scripts/generate.py           validate, then write the Markdown files
    python3 scripts/generate.py --check   validate, then fail if the Markdown files are out of date
    python3 scripts/generate.py --test    run the URL normaliser self-test only

Needs Python 3.8+ and PyYAML (pip install pyyaml).
"""
import pathlib
import re
import sys
import unicodedata
from collections import defaultdict
from urllib.parse import parse_qsl, urlsplit

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "clients.yaml"

SERVERS = {"plex": "Plex", "jellyfin": "Jellyfin", "emby": "Emby"}
VENDORS = {"plex": "Plex Inc.", "jellyfin": "Jellyfin project", "emby": "Emby LLC"}
# Other back ends. Only the first group is shown as tags; the rest is kept as data.
ALSO_SHOWN = {"subsonic": "+Subsonic", "audiobookshelf": "+Audiobookshelf", "stremio": "+Stremio addons",
              "fnos": "+fnOS", "silo": "+Silo", "iptv": "+IPTV", "kodi": "+Kodi", "komga": "+Komga",
              "kavita": "+Kavita", "opds": "+OPDS"}
ALSO = set(ALSO_SHOWN) | {"smb", "webdav", "dlna", "ftp", "nfs", "cloud", "local", "streaming-services", "other"}

# Platform vocabulary: key -> (label, group). Groups decide where an app is filed.
PLATFORMS = {
    "windows": ("Windows", "desktop"), "macos": ("macOS", "desktop"), "linux": ("Linux", "desktop"),
    "web": ("Web", "web"),
    "android": ("Android", "android"), "ios": ("iOS", "apple"), "ipados": ("iPadOS", "apple"),
    "harmonyos": ("HarmonyOS", "android"),
    "android-tv": ("Android TV", "android"), "fire-tv": ("Fire TV", "android"), "tvos": ("tvOS", "apple"),
    "vega-os": ("Vega OS", "tv"), "roku": ("Roku", "tv"), "webos": ("webOS", "tv"), "tizen": ("Tizen", "tv"),
    "vidaa": ("VIDAA", "tv"), "vizio": ("Vizio", "tv"), "titan-os": ("Titan OS", "tv"),
    "enigma2": ("Enigma2", "tv"), "other-tv": ("Other TV", "tv"), "chromecast": ("Chromecast", "tv"),
    "xbox": ("Xbox", "console"), "xbox-360": ("Xbox 360", "console"), "xbox-original": ("Original Xbox", "console"),
    "ps2": ("PS2", "console"), "ps3": ("PS3", "console"), "ps4": ("PS4", "console"), "ps5": ("PS5", "console"),
    "ps-vita": ("PS Vita", "console"), "psp": ("PSP", "console"), "switch": ("Switch", "console"),
    "wii": ("Wii", "console"), "wii-u": ("Wii U", "console"), "3ds": ("3DS", "console"),
    "gamecube": ("GameCube", "console"), "retro-handheld": ("Retro handheld", "console"),
    "mister": ("MiSTer", "console"), "playdate": ("Playdate", "console"), "steam-deck": ("Steam Deck", "console"),
    "quest": ("Quest", "vr"), "pico": ("Pico", "vr"), "pc-vr": ("PC VR", "vr"), "visionos": ("visionOS", "vr"),
    "smart-glasses": ("Smart glasses", "vr"),
    "carplay": ("CarPlay", "car"), "android-auto": ("Android Auto", "car"),
    "android-automotive": ("Android Automotive", "car"), "tesla": ("Tesla", "car"),
    "watchos": ("watchOS", "watch"), "wear-os": ("Wear OS", "watch"), "garmin": ("Garmin", "watch"),
    "other-watch": ("Other watch", "watch"),
    "alexa": ("Alexa", "voice"), "google-assistant": ("Google Assistant", "voice"), "sonos": ("Sonos", "voice"),
    "kodi": ("Kodi", "kodi"), "cli": ("CLI", "cli"),
    "windows-phone": ("Windows Phone", "other"), "symbian": ("Symbian", "other"), "sailfish": ("Sailfish OS", "other"),
    "ubuntu-touch": ("Ubuntu Touch", "other"), "risc-os": ("RISC OS", "other"), "classic-mac": ("Classic Mac", "other"),
    "discord": ("Discord", "other"), "home-assistant": ("Home Assistant", "other"),
    "other-device": ("Other device", "other"),
}
MAINSTREAM = {"desktop", "web", "android", "apple"}
CATEGORIES = {"player", "music", "audiobooks", "books", "photos", "live-tv", "shim", "remote", "admin", "bridge"}
MEDIA = {"video", "music", "audiobooks", "podcasts", "books", "photos", "live-tv"}
STATUSES = {"active", "beta", "stale", "discontinued", "unknown"}
PRICES = {"free": "Free", "freemium": "Freemium", "paid": "Paid", "subscription": "Subscription"}
LINK_KINDS = {"repo": "Source", "site": "Website", "appstore": "App Store", "play": "Google Play",
              "msstore": "Microsoft Store", "amazon": "Amazon", "flathub": "Flathub", "fdroid": "F-Droid",
              "snap": "Snap", "aur": "AUR", "roku": "Roku", "meta": "Meta Store", "appgallery": "AppGallery",
              "steam": "Steam", "testflight": "TestFlight", "lgstore": "LG Store", "other": "Info"}
FIELDS = {"name", "url", "links", "servers", "also", "official", "vendor", "platforms", "category", "media",
          "open_source", "license", "price", "price_note", "status", "status_year", "aliases", "notes",
          "description", "long_tail", "distinct"}
REQUIRED = ("name", "servers", "platforms", "category", "media", "open_source", "status", "description")

# ---------------------------------------------------------------- URL and name normalisation

CODE_HOSTS = {"github.com", "gitlab.com", "codeberg.org", "gitee.com", "bitbucket.org", "git.sr.ht"}


def norm_url(url):
    """Return a key that is equal for two links to the same app page."""
    s = urlsplit(url.strip())
    host = (s.hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host
    path = re.sub(r"/+$", "", s.path)
    if path.endswith(".git"):
        path = path[:-4]
    query = dict(parse_qsl(s.query))
    if host in ("apps.apple.com", "itunes.apple.com"):
        m = re.search(r"/id(\d+)", path)
        app_id = m.group(1) if m else query.get("id", "").split(",")[0]
        if app_id.isdigit():
            return "appstore:" + app_id
    if host == "play.google.com" and query.get("id"):
        return "play:" + query["id"]
    if host in CODE_HOSTS:
        parts = [p for p in path.split("/") if p]
        if host == "github.com" and len(parts) >= 2:
            return f"github.com/{parts[0].lower()}/{parts[1].lower()}"
        return host + "/" + "/".join(p.lower() for p in parts)
    if host.endswith("microsoft.com"):
        m = re.search(r"/((?:9|xp)[0-9a-z]{10,13})(?:$|[/?])", path + "/", re.I)
        if m:
            return "msstore:" + m.group(1).upper()
    if re.match(r"(.+\.)?amazon\.[a-z.]+$", host):
        m = re.search(r"/dp/([A-Z0-9]{10})", path, re.I)
        if m:
            return "amazon:" + m.group(1).upper()
    if host == "flathub.org":
        m = re.search(r"/apps/(?:details/)?([\w.-]+)$", path)
        if m:
            return "flathub:" + m.group(1).lower()
    if host == "f-droid.org":
        m = re.search(r"/packages/([\w.]+)", path)
        if m:
            return "fdroid:" + m.group(1)
    if host in ("meta.com", "oculus.com"):
        m = re.search(r"/experiences/(?:[^/]+/)*(\d+)", path)
        if m:
            return "meta:" + m.group(1)
    kept = sorted((k, v) for k, v in query.items() if not k.startswith("utm_") and k not in ("hl", "gl", "ref"))
    q = "?" + "&".join(f"{k}={v}" for k, v in kept) if kept else ""
    return host + path.lower() + q


def norm_name(name):
    s = unicodedata.normalize("NFKC", name).casefold()
    return re.sub(r"[\W_]+", "", s)


def self_test():
    same = [
        ("http://www.GitHub.com/Edde746/Plezy.git/", "https://github.com/edde746/plezy"),
        ("https://github.com/edde746/plezy/releases/latest", "https://github.com/edde746/plezy"),
        ("https://apps.apple.com/us/app/plezy/id6754315964", "https://apps.apple.com/cn/app/id6754315964"),
        ("https://itunes.apple.com/lookup?id=6754315964&country=us", "https://apps.apple.com/app/id6754315964"),
        ("https://play.google.com/store/apps/details?id=org.moonfin.androidtv&hl=en",
         "https://play.google.com/store/apps/details?id=org.moonfin.androidtv"),
        ("https://apps.microsoft.com/detail/9plb327dd51d", "https://apps.microsoft.com/store/detail/moonfin/9PLB327DD51D?hl=en-us"),
        ("https://www.amazon.com/edde746-Plezy-for-Plex-Jellyfin/dp/B0GK65CVS1", "https://amazon.com/dp/B0GK65CVS1"),
        ("https://www.plex.tv/apps-devices/", "http://plex.tv/apps-devices"),
        ("https://flathub.org/apps/details/nl.g4d.Girens", "https://flathub.org/apps/nl.g4d.Girens"),
        ("https://codeberg.org/avery42/Delfin/", "https://codeberg.org/avery42/delfin"),
        ("https://www.meta.com/en-gb/experiences/lumenoir/1552281053325883/",
         "https://www.meta.com/experiences/lumenoir-movie-theater-video-player/1552281053325883"),
        ("https://example.com/app?utm_source=x", "https://example.com/app"),
    ]
    different = [
        ("https://github.com/edde746/plezy", "https://github.com/edde746/plezy-web"),
        ("https://apps.apple.com/app/id1", "https://apps.apple.com/app/id2"),
        ("https://play.google.com/store/apps/details?id=a.b", "https://play.google.com/store/apps/details?id=a.c"),
        ("https://example.com/a", "https://example.com/b"),
    ]
    for a, b in same:
        assert norm_url(a) == norm_url(b), (a, b, norm_url(a), norm_url(b))
    for a, b in different:
        assert norm_url(a) != norm_url(b), (a, b)
    assert norm_name("Plezy!") == norm_name("plezy") and norm_name("Dee Jellie") == norm_name("DeeJellie")
    assert norm_name("映屿 CineIsle") != norm_name("影屿 CineIsle")
    anchor = Slugger()
    assert [anchor("Web"), anchor("Web"), anchor("Android, Android TV and HarmonyOS"), anchor("Web")] == \
        ["web", "web-1", "android-android-tv-and-harmonyos", "web-2"]


# ---------------------------------------------------------------- validation

def validate(apps):
    errors = []
    by_url = defaultdict(list)
    by_name = defaultdict(list)
    for i, a in enumerate(apps):
        who = f"#{i} {a.get('name', '?')}"
        if not isinstance(a, dict):
            errors.append(f"{who}: not a mapping")
            continue
        for f in sorted(set(a) - FIELDS):
            errors.append(f"{who}: unknown field '{f}'")
        for f in REQUIRED:
            if a.get(f) in (None, "", []) and not (f == "open_source" and a.get(f) is False):
                if f == "open_source" and f in a:
                    continue  # null = unknown is allowed
                errors.append(f"{who}: missing '{f}'")
        if not a.get("url") and a.get("status") != "discontinued":
            errors.append(f"{who}: missing 'url' (only discontinued apps may have no link)")
        for s in a.get("servers") or []:
            if s not in SERVERS:
                errors.append(f"{who}: unknown server '{s}'")
        for s in a.get("also") or []:
            if s not in ALSO:
                errors.append(f"{who}: unknown back end '{s}' in also")
        for p in a.get("platforms") or []:
            if p not in PLATFORMS:
                errors.append(f"{who}: unknown platform '{p}'")
        if len(set(a.get("platforms") or [])) != len(a.get("platforms") or []):
            errors.append(f"{who}: repeated platform")
        if a.get("category") not in CATEGORIES:
            errors.append(f"{who}: unknown category '{a.get('category')}'")
        for m in a.get("media") or []:
            if m not in MEDIA:
                errors.append(f"{who}: unknown media '{m}'")
        if a.get("status") not in STATUSES:
            errors.append(f"{who}: unknown status '{a.get('status')}'")
        if a.get("price") not in (None, *PRICES):
            errors.append(f"{who}: unknown price '{a.get('price')}'")
        if a.get("open_source") not in (True, False, None):
            errors.append(f"{who}: open_source must be true, false or null")
        if a.get("license") and a.get("open_source") is not True:
            errors.append(f"{who}: has a licence but open_source is not true")
        if a.get("official"):
            if a.get("vendor") not in VENDORS or a["vendor"] not in (a.get("servers") or []):
                errors.append(f"{who}: official apps need vendor plex/jellyfin/emby matching servers")
        elif a.get("vendor"):
            errors.append(f"{who}: vendor set on a third-party app")
        y = a.get("status_year")
        if y is not None and not (isinstance(y, int) and 2000 <= y <= 2100):
            errors.append(f"{who}: bad status_year {y!r}")
        d = a.get("description") or ""
        if "\n" in d or len(d) > 200 or "`" in d:
            errors.append(f"{who}: description must be one line, at most 200 characters, without backticks")
        urls = [a["url"]] if a.get("url") else []
        links = a.get("links") or {}
        if not isinstance(links, dict):
            errors.append(f"{who}: links must be a mapping")
            links = {}
        for k, v in links.items():
            if k.split(":")[0] not in LINK_KINDS:
                errors.append(f"{who}: unknown link kind '{k}'")
            urls.append(v)
        for u in urls:
            if not isinstance(u, str) or not re.match(r"https?://[^\s/]+\.[^\s]+$", u):
                errors.append(f"{who}: bad URL {u!r}")
                continue
        keys = {norm_url(u) for u in urls if isinstance(u, str)}
        if len(keys) != len(urls):
            errors.append(f"{who}: the same link appears twice in one entry")
        for k in keys:
            by_url[k].append(who)
        by_name[norm_name(a.get("name", ""))].append((who, bool(a.get("distinct"))))
    for k, whos in by_url.items():
        if len(whos) > 1:
            errors.append(f"duplicate link {k}: {', '.join(whos)}")
    for k, items in by_name.items():
        if len(items) > 1 and not all(flag for _, flag in items):
            errors.append(f"duplicate name '{k}' (set distinct: true on each if they are different apps): "
                          + ", ".join(w for w, _ in items))
    return errors


# ---------------------------------------------------------------- filing

NICHE = [("console", "Consoles and homebrew"), ("vr", "VR and XR"), ("tv", "TV operating systems"),
         ("car", "Car"), ("watch", "Watches"), ("voice", "Voice assistants and speakers"),
         ("kodi", "Kodi add-ons"), ("cli", "Terminal"), ("shim", "Desktop shims and external players"),
         ("other", "Other devices and legacy systems")]
FAMILIES = [("cross", "Cross-platform"), ("android", "Android, Android TV and HarmonyOS"),
            ("apple", "Apple platforms"), ("desktop", "Desktop"), ("web", "Web"), ("other", "Other")]


def groups(a):
    return {PLATFORMS[p][1] for p in a["platforms"]}


def niche_group(a):
    g = groups(a)
    if a["category"] == "shim":
        return "shim"
    if g & MAINSTREAM:
        return None
    for key, _ in NICHE:
        if key in g:
            return key
    return "other"


def family(a):
    plats = set(a["platforms"])
    fams = {PLATFORMS[p][1] for p in plats} & MAINSTREAM
    if "desktop" in fams and plats & {"windows", "macos", "linux"} == {"macos"} and "apple" in fams:
        fams.discard("desktop")  # a Mac build of an Apple-only app
    if len(fams) > 1:
        return "cross"
    return next(iter(fams), "other")


def server_key(a):
    s = a["servers"]
    return "multi" if len(s) > 1 else s[0]


def section_of(a):
    """(section, subsection) where an entry is filed in README.md."""
    if a["status"] == "discontinued":
        return ("discontinued", None)
    if a.get("official"):
        return ("official", a["vendor"])
    if a["category"] in ("remote", "admin", "bridge"):
        return ("companions", a["category"])
    n = niche_group(a)
    if n:
        return ("niche", n)
    c = a["category"]
    if c == "music":
        return ("music", server_key(a))
    if c in ("audiobooks", "books", "photos"):
        return ("books", c)
    if c == "live-tv":
        return ("livetv", None)
    k = server_key(a)
    return ("multi", family(a)) if k == "multi" else (k, family(a))


SECTIONS = [
    ("official", "Official apps", "Apps made by Plex Inc. and the Jellyfin project and Emby LLC.",
     [("plex", "Plex"), ("jellyfin", "Jellyfin"), ("emby", "Emby")]),
    ("multi", "Multi-server players", "Video and general clients that play from two or all three servers.", FAMILIES),
    ("jellyfin", "Jellyfin video clients", "Third-party video and general clients for Jellyfin only.", FAMILIES),
    ("plex", "Plex video clients", "Third-party video and general clients for Plex only.", FAMILIES),
    ("emby", "Emby video clients",
     "Third-party video and general clients for Emby only. Many come from the large Chinese-language scene.", FAMILIES),
    ("music", "Music", "Music players and music-first clients.",
     [("multi", "Multi-server music"), ("plex", "Plex music"), ("jellyfin", "Jellyfin music"), ("emby", "Emby music")]),
    ("books", "Audiobooks, books and photos", "Audiobook players and book or comic readers and photo viewers.",
     [("audiobooks", "Audiobooks"), ("books", "Books, comics and manga"), ("photos", "Photos")]),
    ("livetv", "Live TV and channel apps",
     "IPTV players that also read media servers. Apps that turn a library into scheduled channels.", None),
    ("niche", "Niche platforms", "Apps for consoles and headsets and cars and watches. Also TV systems "
     "and Kodi and terminals and other less common platforms.", NICHE),
    ("companions", "Companion and remote apps", "These do not play media themselves. They control or manage a server "
     "or connect it to other software.", [("remote", "Remotes and controllers"),
                                              ("admin", "Admin, stats and requests"),
                                              ("bridge", "Bridges and integrations")]),
    ("discontinued", "Discontinued", "Apps that were withdrawn or archived or abandoned. Kept for reference.", None),
]


# ---------------------------------------------------------------- rendering

def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


class Slugger:
    """GitHub heading anchors for one document: a repeated heading gets -1, -2, ... in document order."""

    def __init__(self):
        self.seen = defaultdict(int)

    def __call__(self, heading):
        base = slug(heading)
        n = self.seen[base]
        self.seen[base] += 1
        return f"{base}-{n}" if n else base


def sort_key(a):
    return (norm_name(a["name"]) or a["name"].casefold(), a["name"], a.get("url") or "")


def md(text):
    return text.replace("[", "\\[").replace("]", "\\]")


def tags(a, with_platforms=True):
    out = [f"`{SERVERS[s]}`" for s in ("plex", "jellyfin", "emby") if s in a["servers"]]
    out += [f"`{ALSO_SHOWN[s]}`" for s in ALSO_SHOWN if s in (a.get("also") or [])]
    parts = [" ".join(out)]
    if with_platforms:
        parts.append(" ".join(f"`{PLATFORMS[p][0]}`" for p in PLATFORMS if p in a["platforms"]))
    meta = []
    if a.get("open_source"):
        meta.append(f"`{a['license']}`" if a.get("license") and a["license"] != "other" else "`Open source`")
    if a.get("price"):
        meta.append(f"`{PRICES[a['price']]}`")
    if a["status"] == "beta":
        meta.append("`Beta`")
    elif a["status"] == "stale":
        meta.append(f"`Stale {a['status_year']}`" if a.get("status_year") else "`Stale`")
    elif a["status"] == "discontinued":
        meta.append(f"`Ended {a['status_year']}`" if a.get("status_year") else "`Ended`")
    if meta:
        parts.append(" ".join(meta))
    return " · ".join(p for p in parts if p)


def link_label(key):
    kind, _, suffix = key.partition(":")
    label = LINK_KINDS[kind]
    return f"{label} {suffix}" if suffix.isdigit() else f"{label} ({suffix})" if suffix else label


def entry(a):
    name = md(a["name"])
    head = f"[{name}]({a['url']})" if a.get("url") else name
    extra = [f"[{link_label(k)}]({u})" for k, u in (a.get("links") or {}).items()]
    tail = " · " + " · ".join(extra) if extra else ""
    return f"- {head} - {a['description']} {tags(a)}{tail}"


INTRO = """# Awesome Media Server Clients [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Every app that plays from a [Plex](https://www.plex.tv/) or [Jellyfin](https://jellyfin.org/) or [Emby](https://emby.media/) server. Phones and TVs and desktops. Browsers and consoles and headsets. Cars and watches and terminals. The list has the official apps and {third:,} third-party ones. Some are polished store apps. Others are small open-source projects.

> **Want these apps to play straight from debrid or Usenet?** [rex](https://rex.debridmediamanager.com/) and [zurg](https://zurg.debridmediamanager.com/) are made by the team that keeps this list. [See what they do.](#from-the-maintainers)

Looking for a platform? [PLATFORMS.md](PLATFORMS.md) lists every app by device and links a full page for each one such as [Roku](platforms/roku.md) or [Apple TV](platforms/tvos.md) or [Android TV](platforms/android-tv.md). Smaller projects have a page of their own under More clients below.

Official downloads come only from [plex.tv](https://www.plex.tv/media-server-downloads/?cat=plex+desktop) and [jellyfin.org](https://jellyfin.org/downloads/) and [emby.media](https://emby.media/download.html). A repository that offers a "full version" or an "unlocked" build or an "installer" for these apps is a scam.
"""

MAINTAINERS = """## From the maintainers

This list is kept by the team behind Debrid Media Manager. We also make the projects below. They give the apps on this page a library to play.

- **[rex](https://rex.debridmediamanager.com/)** · Any source. Every Plex app. Your films and shows stay on a debrid service or a Usenet provider or any web server. rex shows them to the Plex apps as a normal server. When you press play it streams the file straight from where it lives. Nothing is downloaded first. [Docs](https://notes.debridmediamanager.com/rex/)
- **[zurg](https://zurg.debridmediamanager.com/)** · Every debrid account and Usenet in one folder. Plex and Jellyfin and Emby read the folder through rclone like a normal drive. Infuse reads it directly. The public release covers Real-Debrid. [Sponsors](https://gatekeeper.debridmediamanager.com/) also get TorBox and AllDebrid and Premiumize and Debrid-Link and Offcloud and Usenet in the same folder. [Docs](https://notes.debridmediamanager.com/zurg/)
- **[Debrid Media Manager](https://debridmediamanager.com/)** · Curate an infinite media library. A free and open source web app that adds films and shows to your debrid library. [Docs](https://notes.debridmediamanager.com/dmm/)

Questions? Ask in the rex-support or zurg-support or dmm-support forum on [Discord](https://discord.com/invite/7u4YjMThXP).
"""

LEGEND = """## Legend

| Tag | Meaning |
|---|---|
| `Plex` `Jellyfin` `Emby` | The servers the app plays from |
| `+Subsonic`, `+Audiobookshelf`, `+Stremio addons`, `+fnOS`, `+Silo`, `+IPTV` | Other back ends it also reads. Subsonic includes Navidrome |
| `Android TV` | Also Google TV and SHIELD |
| `Fire TV`, `Vega OS` | Fire OS, and the newer Fire TV OS |
| `tvOS` | Apple TV |
| `GPL-3.0`, `MIT`, `Open source` | The source code is public. No licence tag means closed source or unknown |
| `Free`, `Freemium`, `Paid`, `Subscription` | Freemium is free with paid extras. Paid means you pay up front |
| `Beta` | Pre-release, TestFlight or closed testing |
| `Stale 2024` | No update since that year |
| `Ended 2023` | Withdrawn or abandoned that year |

No status tag means the app was updated in the last year or its page shows no date. Store and source links follow each entry. Server support comes from each app's own repository or store listing or site. Apps change fast so check before you pay.
"""


def render_readme(main, more_count):
    by_sec = defaultdict(lambda: defaultdict(list))
    for a in main:
        sec, sub = section_of(a)
        by_sec[sec][sub].append(a)
    third = sum(1 for a in main if not a.get("official")) + more_count
    anchor = Slugger()
    anchor("Contents")
    out = [INTRO.format(third=third), "## Contents\n",
           f"- [From the maintainers](#{anchor('From the maintainers')})", f"- [Legend](#{anchor('Legend')})"]
    body = [MAINTAINERS, LEGEND]
    for key, title, blurb, subs in SECTIONS:
        if key not in by_sec:
            continue
        out.append(f"- [{title}](#{anchor(title)})")
        body.append(f"## {title}\n\n{blurb}\n")
        if subs is None:
            body += [entry(a) for a in sorted(by_sec[key][None], key=sort_key)] + [""]
            continue
        for sk, stitle in subs:
            items = by_sec[key].get(sk)
            if not items:
                continue
            out.append(f"  - [{stitle}](#{anchor(stitle)})")
            body.append(f"### {stitle}\n")
            body += [entry(a) for a in sorted(items, key=sort_key)] + [""]
    out += [f"- [More clients](#{anchor('More clients')})",
            f"- [Contribution Guidelines](#{anchor('Contribution Guidelines')})", ""]
    body.append(f"## More clients\n\n[more-clients.md](more-clients.md) lists {more_count:,} smaller projects "
                "by platform. They live only on GitHub with no release and under 10 stars.\n")
    body.append("## Contribution Guidelines\n\nContributions are welcome. Read the [contributing guidelines]"
                "(contributing.md) first. Entries live in [data/clients.yaml](data/clients.yaml) and the "
                "Markdown files are generated from it.\n")
    body.append(FOOTER)
    return "\n".join(out) + "\n" + "\n".join(body)


FOOTER = ("**More from DMM:** [Debrid Media Manager](https://debridmediamanager.com/) · "
          "[zurg](https://zurg.debridmediamanager.com/) · [rex](https://rex.debridmediamanager.com/) · "
          "[Docs](https://notes.debridmediamanager.com/) · [Sponsor](https://gatekeeper.debridmediamanager.com/) · "
          "[Discord](https://discord.com/invite/7u4YjMThXP) · [Reddit](https://www.reddit.com/r/debridmediamanager/)\n")

CALLOUT = ("> **Want these apps to play straight from debrid or Usenet?** "
           "[rex](https://rex.debridmediamanager.com/) and [zurg](https://zurg.debridmediamanager.com/) "
           "are made by the team that keeps this list. [See what they do.](README.md#from-the-maintainers)\n")

GENERATED = "<!-- Generated from data/clients.yaml by scripts/generate.py. Do not edit by hand. -->\n"


def more_group(a):
    n = niche_group(a)
    return ("niche", n) if n else ("family", family(a))


def render_more(more):
    out = [GENERATED, "# More clients\n",
           "Smaller Plex and Jellyfin and Emby clients. They live only on GitHub with no release and under 10 stars. "
           "Most are from 2025 and 2026. Many are one-person experiments so expect rough edges. "
           "The main list is in [README.md](README.md) and its legend applies here too.\n", CALLOUT]
    groups_ = defaultdict(list)
    for a in more:
        groups_[more_group(a)].append(a)
    order = [("family", k, t) for k, t in FAMILIES] + [("niche", k, t) for k, t in NICHE]
    toc, body = ["## Contents\n"], []
    for kind, k, title in order:
        items = groups_.get((kind, k))
        if not items:
            continue
        toc.append(f"- [{title}](#{slug(title)}) ({len(items)})")
        body.append(f"## {title}\n")
        body += [entry(a) for a in sorted(items, key=sort_key)] + [""]
    return "\n".join(out) + "\n" + "\n".join(toc) + "\n\n" + "\n".join(body) + "\n" + FOOTER


KINDS = [("Video and general", {"player", "shim", "live-tv"}), ("Music", {"music"}),
         ("Audiobooks, books and photos", {"audiobooks", "books", "photos"}),
         ("Companions", {"remote", "admin", "bridge"})]


def by_platform(apps):
    by_plat = defaultdict(list)
    for a in apps:
        if a["status"] != "discontinued" and a.get("url"):
            for p in a["platforms"]:
                by_plat[p].append(a)
    return by_plat


def render_platform_page(p, items):
    label = PLATFORMS[p][0]
    counts = " and ".join(f"{sum(1 for a in items if s in a['servers']):,} for {SERVERS[s]}"
                          for s in ("plex", "jellyfin", "emby"))
    out = [GENERATED, f"# {label}\n",
           f"Every app in this list that runs on {label}. That is {len(items):,} apps with {counts}. "
           "Apps for more than one server count once per server. The legend is in [README.md](../README.md#legend) "
           "and every other platform is in [PLATFORMS.md](../PLATFORMS.md).\n",
           CALLOUT.replace("(README.md", "(../README.md")]
    official = sorted((a for a in items if a.get("official")), key=sort_key)
    sections = [("Official apps", official)] + [
        (title, sorted((a for a in items if not a.get("official") and a["category"] in cats), key=sort_key))
        for title, cats in KINDS]
    for title, group in sections:
        if group:
            out += [f"## {title}\n"] + [entry(a) for a in group] + [""]
    return "\n".join(out) + "\n" + FOOTER


def render_platforms(apps):
    by_plat = by_platform(apps)
    kinds = KINDS
    out = [GENERATED, "# Apps by platform\n",
           "Every listed app grouped by the platform it runs on. Letters after a name show its servers. "
           "**P** is Plex. **J** is Jellyfin. **E** is Emby. An asterisk marks an official app. Full entries are in "
           "[README.md](README.md) and [more-clients.md](more-clients.md).\n", CALLOUT, "## Contents\n"]
    group_titles = {"desktop": "Desktop", "web": "Web", "android": "Android", "apple": "Apple", "tv": "TV",
                    "console": "Consoles", "vr": "VR and XR", "car": "Car", "watch": "Watch",
                    "voice": "Voice and speakers", "kodi": "Kodi", "cli": "Terminal", "other": "Other"}
    toc = defaultdict(list)
    body = []
    for p, (label, g) in PLATFORMS.items():
        items = by_plat.get(p)
        if not items:
            continue
        title = f"{label} ({len(items)})"
        toc[g].append(f"[{label}](#{slug(title)})")
        body.append(f"## {title}\n")
        body.append(f"[Full {label} entries with tags and store links](platforms/{p}.md)\n")
        for ktitle, cats in kinds:
            names = []
            for a in sorted((a for a in items if a["category"] in cats), key=sort_key):
                letters = "".join(SERVERS[s][0] for s in ("plex", "jellyfin", "emby") if s in a["servers"])
                star = "\\*" if a.get("official") else ""
                names.append(f"[{md(a['name'])}]({a['url']}) {letters}{star}")
            if names:
                body.append(f"**{ktitle}:** " + " · ".join(names) + "\n")
    for g, title in group_titles.items():
        if toc.get(g):
            out.append(f"- {title}: " + " · ".join(toc[g]))
    return "\n".join(out) + "\n\n" + "\n".join(body) + "\n" + FOOTER


def load():
    apps = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not isinstance(apps, list):
        sys.exit("data/clients.yaml must be a YAML list")
    return apps


def main(argv):
    self_test()
    if "--test" in argv:
        print("self-test passed")
        return 0
    apps = load()
    errors = validate(apps)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"{len(errors)} validation error(s)", file=sys.stderr)
        return 1
    main_list = [a for a in apps if not a.get("long_tail")]
    more = [a for a in apps if a.get("long_tail")]
    outputs = {"README.md": render_readme(main_list, len(more)), "more-clients.md": render_more(more),
               "PLATFORMS.md": render_platforms(apps)}
    outputs.update({f"platforms/{p}.md": render_platform_page(p, items)
                    for p, items in by_platform(apps).items()})
    stale = []
    for fname, text in outputs.items():
        path = ROOT / fname
        if "--check" in argv:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(fname)
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(text, encoding="utf-8")
    # A platform that lost its last app must not keep an old page.
    for path in (ROOT / "platforms").glob("*.md"):
        fname = f"platforms/{path.name}"
        if fname not in outputs:
            if "--check" in argv:
                stale.append(fname)
            else:
                path.unlink()
    if stale:
        print("Out of date: " + ", ".join(stale) + ". Run python3 scripts/generate.py and commit the result.",
              file=sys.stderr)
        return 1
    pages = sum(1 for f in outputs if f.startswith("platforms/"))
    sizes = ", ".join(f"{f} {len(t.encode()) // 1024} KB" for f, t in outputs.items() if "/" not in f)
    print(f"{len(apps)} apps ({len(main_list)} in README, {len(more)} in more-clients.md); {sizes}; "
          f"{pages} platform pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
