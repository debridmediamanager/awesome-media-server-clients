# Awesome Media Server Clients [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Every app that plays from a [Plex](https://www.plex.tv/) or [Jellyfin](https://jellyfin.org/) or [Emby](https://emby.media/) server. Phones and TVs and desktops. Browsers and consoles and headsets. Cars and watches and terminals. The list has the official apps and 1,810 third-party ones. Some are polished store apps. Others are small open-source projects.

> **Want these apps to play straight from debrid or Usenet?** [rex](https://rex.debridmediamanager.com/) and [zurg](https://zurg.debridmediamanager.com/) are made by the team that keeps this list. [See what they do.](#from-the-maintainers)

Looking for a platform? [PLATFORMS.md](PLATFORMS.md) lists every app by device and links a full page for each one such as [Roku](platforms/roku.md) or [Apple TV](platforms/tvos.md) or [Android TV](platforms/android-tv.md). Smaller projects have a page of their own under More clients below.

Official downloads come only from [plex.tv](https://www.plex.tv/media-server-downloads/?cat=plex+desktop) and [jellyfin.org](https://jellyfin.org/downloads/) and [emby.media](https://emby.media/download.html). A repository that offers a "full version" or an "unlocked" build or an "installer" for these apps is a scam.

## Contents

- [From the maintainers](#from-the-maintainers)
- [Legend](#legend)
- [Official apps](#official-apps)
  - [Plex](#plex)
  - [Jellyfin](#jellyfin)
  - [Emby](#emby)
- [Multi-server players](#multi-server-players)
  - [Cross-platform](#cross-platform)
  - [Android, Android TV and HarmonyOS](#android-android-tv-and-harmonyos)
  - [Apple platforms](#apple-platforms)
  - [Desktop](#desktop)
  - [Web](#web)
- [Jellyfin video clients](#jellyfin-video-clients)
  - [Cross-platform](#cross-platform-1)
  - [Android, Android TV and HarmonyOS](#android-android-tv-and-harmonyos-1)
  - [Apple platforms](#apple-platforms-1)
  - [Desktop](#desktop-1)
  - [Web](#web-1)
- [Plex video clients](#plex-video-clients)
  - [Cross-platform](#cross-platform-2)
  - [Android, Android TV and HarmonyOS](#android-android-tv-and-harmonyos-2)
  - [Apple platforms](#apple-platforms-2)
  - [Desktop](#desktop-2)
  - [Web](#web-2)
- [Emby video clients](#emby-video-clients)
  - [Cross-platform](#cross-platform-3)
  - [Android, Android TV and HarmonyOS](#android-android-tv-and-harmonyos-3)
  - [Apple platforms](#apple-platforms-3)
  - [Desktop](#desktop-3)
  - [Web](#web-3)
- [Music](#music)
  - [Multi-server music](#multi-server-music)
  - [Plex music](#plex-music)
  - [Jellyfin music](#jellyfin-music)
  - [Emby music](#emby-music)
- [Audiobooks, books and photos](#audiobooks-books-and-photos)
  - [Audiobooks](#audiobooks)
  - [Books, comics and manga](#books-comics-and-manga)
  - [Photos](#photos)
- [Live TV and channel apps](#live-tv-and-channel-apps)
- [Niche platforms](#niche-platforms)
  - [Consoles and homebrew](#consoles-and-homebrew)
  - [VR and XR](#vr-and-xr)
  - [TV operating systems](#tv-operating-systems)
  - [Car](#car)
  - [Watches](#watches)
  - [Voice assistants and speakers](#voice-assistants-and-speakers)
  - [Kodi add-ons](#kodi-add-ons)
  - [Terminal](#terminal)
  - [Desktop shims and external players](#desktop-shims-and-external-players)
  - [Other devices and legacy systems](#other-devices-and-legacy-systems)
- [Companion and remote apps](#companion-and-remote-apps)
  - [Remotes and controllers](#remotes-and-controllers)
  - [Admin, stats and requests](#admin-stats-and-requests)
  - [Bridges and integrations](#bridges-and-integrations)
- [Discontinued](#discontinued)
- [More clients](#more-clients)
- [Contribution Guidelines](#contribution-guidelines)

## From the maintainers

This list is kept by the team behind Debrid Media Manager. We also make the projects below. They give the apps on this page a library to play.

- **[rex](https://rex.debridmediamanager.com/)** · Any source. Every Plex app. Your films and shows stay on a debrid service or a Usenet provider or any web server. rex shows them to the Plex apps as a normal server. When you press play it streams the file straight from where it lives. Nothing is downloaded first. [Docs](https://notes.debridmediamanager.com/rex/)
- **[zurg](https://zurg.debridmediamanager.com/)** · Every debrid account and Usenet in one folder. Plex and Jellyfin and Emby read the folder through rclone like a normal drive. Infuse reads it directly. The public release covers Real-Debrid. [Sponsors](https://gatekeeper.debridmediamanager.com/) also get TorBox and AllDebrid and Premiumize and Debrid-Link and Offcloud and Usenet in the same folder. [Docs](https://notes.debridmediamanager.com/zurg/)
- **[Debrid Media Manager](https://debridmediamanager.com/)** · Curate an infinite media library. A free and open source web app that adds films and shows to your debrid library. [Docs](https://notes.debridmediamanager.com/dmm/)

Questions? Ask in the rex-support or zurg-support or dmm-support forum on [Discord](https://discord.com/invite/7u4YjMThXP).

## Legend

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

## Official apps

Apps made by Plex Inc. and the Jellyfin project and Emby LLC.

### Plex

- [Plex](https://www.plex.tv/apps-devices/) - Plex's main app for films, shows, music, photos and Live TV/DVR, plus its free streaming channels. `Plex` · `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` `Vega OS` `Roku` `webOS` `Tizen` `VIDAA` `Vizio` `Other TV` `Chromecast` `Xbox` `PS4` `PS5` `Quest` `Android Auto` · `Freemium` · [App Store](https://apps.apple.com/app/id383457673) · [Google Play](https://play.google.com/store/apps/details?id=com.plexapp.android) · [Meta Store](https://www.meta.com/experiences/plex-find-movies-tv-shows/1136900442841511/)
- [Plexamp](https://plexamp.com/) - Plex's music player, with a headless mode for Raspberry Pi; the new desktop app is in beta. `Plex` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `Freemium` · [App Store](https://apps.apple.com/app/id1500797510) · [Google Play](https://play.google.com/store/apps/details?id=tv.plex.labs.plexamp)
- [Plex Dash](https://apps.apple.com/app/id1500797677) - Server monitoring and management app for Plex Pass owners. `Plex` · `Android` `iOS` `iPadOS` · `Subscription` `Stale 2024`
- [Plex Desktop](https://apps.microsoft.com/detail/XP9CDQW6ML4NQN) - Desktop app for Windows, macOS and Linux. `Plex` · `Windows` `macOS` `Linux` · `Freemium` · [Flathub](https://flathub.org/apps/tv.plex.PlexDesktop) · [Snap](https://snapcraft.io/plex-desktop)
- [Plex for LG NetCast](https://support.plex.tv/articles/204080173-which-smart-tv-models-are-supported/) - Plex's older app for LG NetCast and webOS 1-2 TVs. Plex no longer supports it, but it still runs. `Plex` · `webOS` `Other TV` · `Stale 2024`
- [Plex HTPC](https://flathub.org/apps/tv.plex.PlexHTPC) - Full-screen 10-foot interface for home-theatre PCs; not updated since July 2025. `Plex` · `Windows` `macOS` `Linux` · `Freemium` `Stale 2025` · [Microsoft Store](https://apps.microsoft.com/detail/XPFFFF6NN1LZDQ) · [Snap](https://snapcraft.io/plex-htpc)
- [Plex on Sonos](https://support.sonos.com/services/plex) - Plex music service inside the Sonos app and on Sonos speakers. `Plex` · `Sonos` · `Free`
- [Plex Photos](https://apps.apple.com/app/id6504519803) - Photo app for Plex libraries; Plex says it will be retired once photos return to the main app. `Plex` · `Android` `iOS` `iPadOS` · `Free` `Stale 2025`
- [Plex Web](https://app.plex.tv/) - Browser app at app.plex.tv; the only place Watch Together still works. `Plex` · `Web` · `Freemium`

### Jellyfin

- [JellyCon](https://github.com/jellyfin/jellycon) - Kodi add-on that browses and plays the server library without syncing it. `Jellyfin` · `Kodi` · `GPL-2.0` `Free`
- [Jellyfin Desktop](https://github.com/jellyfin/jellyfin-desktop) - Desktop app with mpv playback; the stable release is still Jellyfin Media Player 1.12, 2.x is pre-release. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-2.0` `Free` · [Flathub](https://flathub.org/apps/org.jellyfin.JellyfinDesktop)
- [Jellyfin for Android](https://github.com/jellyfin/jellyfin-android) - Android phone and tablet app; Android Auto support returned in version 2.7. `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=org.jellyfin.mobile) · [F-Droid](https://f-droid.org/packages/org.jellyfin.mobile/)
- [Jellyfin for Android TV](https://github.com/jellyfin/jellyfin-androidtv) - Android TV, Google TV and Fire TV app. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=org.jellyfin.androidtv) · [F-Droid](https://f-droid.org/packages/org.jellyfin.androidtv/)
- [Jellyfin for Chromecast](https://github.com/jellyfin/jellyfin-chromecast) - Google Cast receiver used when you cast from Jellyfin apps. `Jellyfin` · `Chromecast` · `GPL-2.0` `Free`
- [Jellyfin for iOS](https://github.com/jellyfin/jellyfin-ios) - iPhone and iPad app that wraps the web client. `Jellyfin` · `iOS` `iPadOS` · `MPL-2.0` `Free` · [App Store](https://apps.apple.com/app/id1480192618)
- [Jellyfin for Kodi](https://github.com/jellyfin/jellyfin-kodi) - Kodi add-on that syncs the server library into Kodi's own database. `Jellyfin` · `Kodi` · `GPL-3.0` `Free`
- [Jellyfin for Roku](https://github.com/jellyfin/jellyfin-roku) - Roku channel; a frozen "Jellyfin Legacy" channel remains for servers 10.10 and older. `Jellyfin` · `Roku` · `GPL-2.0` `Free` · [Roku](https://channelstore.roku.com/details/4d9e526a7d972d4decf98ea6a84000f7:c617f4902629cc0bd1e1411db1775cf3/jellyfin)
- [Jellyfin for Titan OS](https://github.com/jellyfin/jellyfin-titanos) - App for Philips TVs on Titan OS, in development with no release yet. `Jellyfin` · `Titan OS` · `GPL-2.0` `Free` `Beta`
- [Jellyfin for Tizen](https://github.com/jellyfin/jellyfin-tizen) - Samsung TV app, in the Samsung store since 2026 for Tizen 6 (2021+) sets; older TVs can sideload it. `Jellyfin` · `Tizen` · `MPL-2.0` `Free`
- [Jellyfin for Vega](https://github.com/jellyfin/jellyfin-vega) - Prototype for Fire TV sticks running Vega OS. `Jellyfin` · `Vega OS` · `GPL-3.0` `Free` `Beta`
- [Jellyfin for webOS](https://github.com/jellyfin/jellyfin-webos) - LG TV app in the LG Content Store, a thin wrapper around the web client. `Jellyfin` · `webOS` · `MPL-2.0` `Free` · [LG Store](https://us.lgappstv.com/main/tvapp/detail?appId=1030579)
- [Jellyfin for Xbox](https://github.com/jellyfin/jellyfin-xbox) - Xbox One and Series app, revived in 2025 under a new maintainer. `Jellyfin` · `Xbox` · `GPL-2.0` `Free` · [Microsoft Store](https://apps.microsoft.com/detail/9P2DRTG62QF8)
- [Jellyfin MPV Shim](https://github.com/jellyfin/jellyfin-mpv-shim) - Cast target that plays items sent from other Jellyfin apps in mpv on a desktop. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free` · [Flathub](https://flathub.org/apps/com.github.iwalton3.jellyfin-mpv-shim)
- [Jellyfin OPDS plugin](https://github.com/jellyfin/jellyfin-plugin-opds) - Server plugin that serves book libraries to any OPDS reader app. `Jellyfin` · `Web` · `GPL-3.0` `Free`
- [Jellyfin Vue](https://github.com/jellyfin/jellyfin-vue) - Alternative web client written in Vue, badged Official Beta; no release since 2023. `Jellyfin` · `Web` · `GPL-3.0` `Free` `Beta` · [Website](https://jf-vue.pages.dev/)
- [Jellyfin Web](https://github.com/jellyfin/jellyfin-web) - Browser client that ships with every Jellyfin server. `Jellyfin` · `Web` · `GPL-2.0` `Free`
- [Mopidy-Jellyfin](https://github.com/jellyfin/mopidy-jellyfin) - Mopidy extension that plays Jellyfin music through Mopidy and any MPD client. `Jellyfin` · `Linux` · `Apache-2.0` `Free`
- [Swiftfin](https://github.com/jellyfin/Swiftfin) - Native Swift client and the only official Apple TV app, badged Official Beta. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `MPL-2.0` `Free` `Beta` · [App Store](https://apps.apple.com/app/id1604098728) · [TestFlight](https://testflight.apple.com/join/SqNPfdxq)

### Emby

- [Emby for Alexa and Google Home](https://emby.media/community/topic/60501-live-emby-with-alexa-skill/) - Voice control of Emby players through Alexa and Google Home. `Emby` · `Alexa` `Google Assistant` · `Subscription`
- [Emby for Android](https://emby.media/emby-for-android.html) - Android phone and tablet app; Android Auto, offline media and Live TV need Premiere. `Emby` · `Android` `Android Auto` · `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=com.mb.android) · [Amazon](https://www.amazon.com/dp/B00GVH9O0I)
- [Emby for Android TV](https://emby.media/emby-for-android-tv.html) - Android TV and Google TV app. `Emby` · `Android TV` · `Free` · [Google Play](https://play.google.com/store/apps/details?id=tv.emby.embyatv)
- [Emby for Apple TV](https://emby.media/emby-for-appletv.html) - Apple TV app with full playback for free users. `Emby` · `tvOS` · `Free`
- [Emby for Chromecast](https://emby.media/emby-for-chromecast.html) - Google Cast receiver used when you cast from Emby apps. `Emby` · `Chromecast` · `Free`
- [Emby for Fire TV](https://emby.media/emby-for-fire-tv.html) - Fire TV app. `Emby` · `Fire TV` · `Free` · [Amazon](https://www.amazon.com/dp/B00VVJKTW8)
- [Emby for iOS](https://apps.apple.com/app/id992180193) - iPhone and iPad app with Apple Watch and CarPlay support for Premiere users. `Emby` · `macOS` `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [Emby for Kodi](https://github.com/MediaBrowser/plugin.video.emby) - Kodi add-on that syncs the server library into Kodi's own database. `Emby` · `Kodi` · `GPL-3.0` `Free` · [Website](https://emby.media/emby-for-kodi.html)
- [Emby for LG](https://emby.media/emby-for-lg-smart-tv.html) - LG webOS TV app in the LG Content Store. `Emby` · `webOS` · `Free`
- [Emby for macOS](https://emby.media/emby-theater-macos.html) - Mac app, a Mac App Store build of the iOS app or a manual download. `Emby` · `macOS` · `Subscription`
- [Emby for PS4](https://emby.media/emby-ps4.html) - Web app for the PlayStation 4 browser at tv.emby.media, driven by the controller. `Emby` · `PS4` · `Subscription`
- [Emby for Roku](https://emby.media/emby-for-roku.html) - Roku channel with full playback for free users. `Emby` · `Roku` · `Free`
- [Emby for Samsung](https://emby.media/emby-for-samsung-smart-tv.html) - Samsung Tizen TV app, from the Samsung store or by USB install. `Emby` · `Tizen` · `Free`
- [Emby for Windows and Xbox](https://emby.media/emby-for-windows.html) - One Microsoft Store app for Windows 10/11 and Xbox One and Series, replacing Emby Theater in 2024. `Emby` · `Windows` `Xbox` · `Subscription` · [Website](https://emby.media/emby-for-xbox.html) · [Microsoft Store](https://apps.microsoft.com/detail/9NBLGGH4T70L)
- [Emby Theater](https://github.com/MediaBrowser/emby-theater-electron) - Electron app for Linux, a Raspberry Pi boot image and QNAP NAS HDMI output. `Emby` · `Linux` `Other device` · `GPL-2.0` `Subscription` `Stale 2024` · [Website](https://emby.media/emby-theater-linux.html) · [Snap](https://snapcraft.io/emby-theater)
- [Emby Web](https://emby.media/emby-web-client.html) - Browser client that ships with the server, also hosted at app.emby.media. `Emby` · `Web` · `Free`

## Multi-server players

Video and general clients that play from two or all three servers.

### Cross-platform

- [Aerial TV](https://aerialtv.app) - Video player that combines media servers with IPTV and Stremio addons. `Plex` `Jellyfin` `Emby` `+Stremio addons` `+IPTV` · `macOS` `Android` `iOS` `iPadOS` `Android TV` `tvOS` · `Freemium` · [App Store](https://apps.apple.com/app/id6756782948) · [Google Play](https://play.google.com/store/apps/details?id=com.jet27labs.aerialtv)
- [AfuseKt](https://apps.apple.com/app/id6760249287) - Android, Android TV and iPhone player. `Plex` `Jellyfin` `Emby` · `Android` `iOS` `iPadOS` `Android TV` `tvOS` · `Freemium` · [Source](https://github.com/AttemptD/AfuseKt-release) · [Source 2](https://github.com/AttemptD/AfuseKtV-release) · [Google Play](https://play.google.com/store/apps/details?id=com.attempt.afusekt)
- [AGCPlayer](https://agcplayer.com/) - Video player with custom widgets, AirPlay and subtitle support, plus SMB and cloud sources. `Plex` `Jellyfin` `Emby` · `macOS` `Android` `iOS` `iPadOS` `Android TV` `tvOS` · `Free` · [App Store](https://apps.apple.com/us/app/agc-video-player/id6670426427) · [Google Play](https://play.google.com/store/apps/details?id=com.agc.player)
- [Arnage](https://apps.apple.com/app/id6764849011) - Video client that auto-downloads followed shows and includes Live TV with an EPG. `Plex` `Jellyfin` · `Android` `iOS` `iPadOS` `Android TV` · `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=app.arnage.arnage)
- [ARVIO](https://github.com/ProdigyV21/ARVIO) - Android TV media hub with IPTV, Trakt/Simkl tracking, addons and a self-hostable web version. `Plex` `Jellyfin` `Emby` `+IPTV` · `Web` `Android` `Android TV` `Fire TV` · `Apache-2.0` `Freemium` · [Website](https://arvio.tv) · [Google Play](https://play.google.com/store/apps/details?id=com.arvio.tv)
- [CapyPlayer](https://apps.apple.com/app/id6755650660) - Paid video player for Android, iPhone and iPad. `Plex` `Jellyfin` `Emby` · `Android` `iOS` `iPadOS` · `Paid` · [Google Play](https://play.google.com/store/apps/details?id=com.feifeiduck.capyplayer)
- [Cinetry](https://github.com/gstory0404/Cinetry) - Multi-source player that also reads CMS video sites, IPTV, WebDAV, Alist, Subsonic and Audiobookshelf. `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` `+IPTV` · `Windows` `macOS` `Linux` `Android` `iOS` `Android TV` · `Open source`
- [Cmby](https://github.com/CeRu-007/Cmby) - Flutter client for phones, TV boxes and desktops, distributed as release builds only. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `Android TV`
- [Dengying Player](https://github.com/hanshengcc/dengying-player) - Flutter and mpv player for Emby and Jellyfin. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `Android TV` · `MIT` `Free`
- [DreamPlayer](https://apps.apple.com/us/app/dreamplayer-video-player/id6813066889) - Video player for MKV, MP4, TS and AVI files with hardware decoding and DTS/TrueHD audio. `Jellyfin` `Emby` · `Android` `iOS` `iPadOS` `Android TV` `Fire TV` · `Freemium` · [Source](https://github.com/mangeshghodke/DreamPlayer)
- [EmbyTok](https://github.com/migumigu/EmbyTok) - Vertical TikTok-style video browser. `Plex` `Emby` · `Web` `Android` `Android TV` · `Open source` · [Source (Gitee)](https://gitee.com/miguyomi/embytok)
- [EmbyX](https://github.com/juneix/EmbyX) - Web app that browses a library as a TikTok-style vertical short-video feed. `Jellyfin` `Emby` · `Web` `Android` · `MIT` `Free`
- [flutter_danmaku_player](https://github.com/huangshi10492/flutter_danmaku_player) - Flutter player with danmaku comments for server, WebDAV and SMB media. `Jellyfin` `Emby` · `Windows` `Linux` `Android` `Android TV` · `GPL-3.0` `Free`
- [GMCA](https://github.com/thcolin/gamepad-media-center-aggregator) - Gamepad-driven media centre for Switch, PS Vita and PS4 homebrew, Raspberry Pi and desktops. `Plex` `Jellyfin` `Emby` `+Stremio addons` · `Windows` `macOS` `Linux` `Android` `PS4` `PS Vita` `Switch` · `Apache-2.0` `Free` · [Info](https://forums.plex.tv/t/gmca-an-open-source-third-party-native-plex-client-for-the-nintendo-switch/939571)
- [halcyon-video](https://github.com/halcyon-video/halcyon-video) - Self-hosted web UI that shows your library as a walkable 1990s video-rental store. `Plex` `Jellyfin` `Emby` · `Web` `Android TV` `Fire TV` · `GPL-3.0` · [Website](https://halcyon-video.github.io/halcyon-video/)
- [Hills](https://play.google.com/store/apps/details?id=com.mountains.hills) - Android player with cross-server search and a choice of mpv or ExoPlayer. `Jellyfin` `Emby` · `Windows` `Android` · `Freemium` · [Microsoft Store](https://apps.microsoft.com/detail/9NXNZFRLLWZX)
- [iPlay](https://github.com/saltpi/iPlay) - Cross-platform player for phones, Apple TV, Windows and Xbox. `Jellyfin` `Emby` · `Windows` `macOS` `Android` `iOS` `iPadOS` `HarmonyOS` `tvOS` `Xbox` · `GPL-3.0` · [App Store](https://apps.apple.com/app/id6480576133) · [Google Play](https://play.google.com/store/apps/details?id=top.ourfor.app.iplay) · [AppGallery](https://appgallery.huawei.com/app/detail?id=top.ourfor.app.iPlay) · [Microsoft Store (Xbox)](https://apps.microsoft.com/detail/9PD0SG0LZTNL)
- [JellyPilot](https://github.com/hewel/jellypilot) - Native Rust desktop client with embedded mpv playback that also works as a cast receiver. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` · `MIT`
- [Kinby](https://github.com/kinby-official/kinby-release) - Cross-platform client for mobile, desktop and TV. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `Android TV` · [Info](https://www.v2ex.com/t/1140115)
- [Litefin](https://github.com/MoazSalem/litefin) - Lightweight client built for smart TVs, with desktop and web builds. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Web` `Android TV` `Fire TV` `webOS` `Tizen` · `MPL-2.0` `Free`
- [Lumovio](https://github.com/MOJI6416/lumovio-web) - Web and Android TV app with watch history and a built-in player. `Plex` `Jellyfin` · `Web` `Android TV` · `Apache-2.0`
- [Maku](https://github.com/yanutros/maku) - Tauri client for PCs, phones and Android TV. `Plex` `Jellyfin` · `Windows` `macOS` `Linux` `Android` `Android TV` `Android Auto` · `GPL-3.0`
- [marchen-player](https://github.com/marchen-dev/marchen-player) - Anime player with danmaku comments for local files, direct links and server libraries. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Web` · `AGPL-3.0` `Free`
- [Medio](https://github.com/blueone-6/medio) - Flutter library browsing client. `Jellyfin` `Emby` · `Windows` `Android` `Android TV` · `GPL-3.0` `Free`
- [Moonfin](https://github.com/Moonfin-Client/Moonfin-Core) - Cross-platform client with music, Live TV and DVR, built for TVs as well as phones and desktops. `Plex` `Jellyfin` `Emby` `+Silo` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` `Vega OS` `Roku` `webOS` `Tizen` `Xbox` `Android Auto` · `GPL-2.0` `Free` · [Source (Smart TV)](https://github.com/Moonfin-Client/Smart-TV) · [Source (Roku)](https://github.com/Moonfin-Client/Roku) · [App Store](https://apps.apple.com/app/id6761283970) · [Google Play](https://play.google.com/store/apps/details?id=org.moonfin.androidtv) · [Microsoft Store](https://apps.microsoft.com/detail/9plb327dd51d) · [Amazon](https://www.amazon.com/dp/B0H76BG3DW) · [AUR](https://aur.archlinux.org/packages/moonfin-bin) · [Roku](https://channelstore.roku.com/details/92a83c9f4112b76a7bcee3dc076254ca:3251a91bf7af7339652d5409ccfdcb39/moonfin)
- [Nekofin](https://github.com/lonzzi/nekofin) - Expo-based mobile player for Jellyfin and Emby libraries. `Jellyfin` `Emby` · `Android` `iOS` · `MPL-2.0` `Free`
- [NetEase Popcorn](https://bmh.163.com/) - Player for cloud drives, NAS, WebDAV, SMB, Emby and Jellyfin that matches posters into a personal library. `Jellyfin` `Emby` `+fnOS` · `Windows` `macOS` `Android` `iOS` `iPadOS` `Android TV` · `Free` · [App Store](https://apps.apple.com/us/app/%E7%BD%91%E6%98%93%E7%88%86%E7%B1%B3%E8%8A%B1-%E6%99%BA%E8%83%BD%E5%AA%92%E4%BD%93%E5%BA%93-%E5%85%A8%E8%83%BD%E4%BA%91%E7%9B%98-%E7%BD%91%E7%9B%98%E6%92%AD%E6%94%BE%E5%99%A8/id6553989480) · [App Store 2](https://apps.apple.com/app/id6480252695)
- [Nex](https://github.com/mattGUK97/nex-releases) - Windows and Android TV client, with a self-hosted web client for Plex. `Plex` `Jellyfin` · `Windows` `Web` `Android TV`
- [NexHub](https://github.com/nexhub-app/NexHub) - Flutter app that aggregates anime, manga, novels and video sources, with Emby and Jellyfin as library sources. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `HarmonyOS` · `Apache-2.0` `Free`
- [NipaPlay-Reload](https://github.com/AimesSoft/NipaPlay-Reload) - Anime-friendly video player with danmaku comments and Bangumi sync for media server libraries. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `HarmonyOS` `Android TV` `tvOS` · `MIT` `Free` · [App Store](https://apps.apple.com/app/id6751284970) · [Microsoft Store](https://apps.microsoft.com/detail/9NMR8CLQ0GCR) · [AUR](https://aur.archlinux.org/packages/nipaplay-reload)
- [OmniPlay](https://github.com/nandieling/OmniPlay) - Native poster-wall player on libmpv for local, WebDAV, SMB and server libraries. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Android` `Android TV` · `AGPL-3.0`
- [Plezy](https://github.com/edde746/plezy) - Multi-server client with cross-server search, mpv playback and HDR; free from GitHub, paid in app stores. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` `Android Automotive` · `GPL-3.0` `Paid` · [Website](https://plezy.app) · [App Store](https://apps.apple.com/us/app/id6754315964) · [Google Play](https://play.google.com/store/apps/details?id=com.edde746.plezy) · [Microsoft Store](https://apps.microsoft.com/detail/9n5r1s1t68h7) · [Amazon](https://www.amazon.com/edde746-Plezy-for-Plex-Jellyfin/dp/B0GK65CVS1) · [Info](https://archlinux.org/packages/extra/x86_64/plezy/)
- [Plix](https://github.com/Jman100/plix) - Flutter client for Plex and Jellyfin. `Plex` `Jellyfin` · `Windows` `Linux` `Android` `Android TV` · `Open source` `Free`
- [RelayTV](https://github.com/mcgeezy/relaytv) - Browser TV front end for a Linux box on the television, with live channels and request integration. `Plex` `Jellyfin` `Emby` `+IPTV` · `Linux` `Web` · `GPL-3.0` `Free`
- [Swiftly Player](https://github.com/paulherter/swiftly-player) - Cross-platform video client. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` · `MPL-2.0` `Free` · [App Store](https://apps.apple.com/app/id6806824067) · [Google Play](https://play.google.com/store/apps/details?id=de.paulherter.swiftly) · [TestFlight](https://testflight.apple.com/join/BKtrBmbz)
- [Tigerest Theater](https://github.com/Tigerest/Tigerest-Theater) - Client with embedded mpv playback and danmaku comments for desktop, Android, iPad and Apple TV. `Jellyfin` `Emby` · `Windows` `macOS` `Android` `iOS` `iPadOS` `tvOS` · `GPL-2.0` `Free`
- [TinyPlay](https://github.com/YangHanqing/tinyplay) - Turns an idle Windows or macOS mini-PC into a phone-controlled TV box with IPTV, casting and Bilibili. `Plex` `Jellyfin` `Emby` `+IPTV` · `Windows` `macOS` `tvOS` · `Open source` · [App Store](https://apps.apple.com/app/id6788041703)
- [Tuvora](https://tuvora.co/jellyfin-player) - Player for TV boxes, phones and desktops with Quick Connect and IPTV support. `Jellyfin` `Emby` `+IPTV` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` · `Free` · [Source](https://github.com/paradox-kush/tuvora) · [Google Play](https://play.google.com/store/apps/details?id=com.tuvora.mobile) · [TestFlight](https://testflight.apple.com/join/XDc6gVXc)
- [Ultimate Media Player](https://apps.apple.com/us/app/ultimate-media-player/id6799982687) - Library player for servers and network shares with artwork, subtitles and resume across devices. `Plex` `Jellyfin` · `Android` `iOS` `iPadOS` `Android TV` `tvOS` · `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.unikie1.ultimateplayer)
- [UnU-Player](https://github.com/weiyongzenqi/UnU-Player) - Anime player for Android and Windows with danmaku comments. `Jellyfin` `Emby` · `Windows` `Android` · `GPL-3.0`
- [VesperTV](https://github.com/NoXqc/VesperTV) - Android TV, Fire TV and phone player that mixes add-on catalogs with your own libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `Windows` `Android` `Android TV` `Fire TV` · `GPL-3.0` `Free`
- [VidHub](https://apps.apple.com/app/id1659622164) - Video player and media library app with an Apple TV build. `Plex` `Jellyfin` `Emby` · `macOS` `Android` `iOS` `iPadOS` `Android TV` `tvOS` · `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=com.oumi.utility.media.hub)
- [Vidzer](https://vidzer.app/) - Video player on mpv and FFmpeg with a language-learning subtitle mode. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Android` · `Freemium` · [Source](https://github.com/vidzer-app/vidzer-releases) · [Website](https://zeroflx.com) · [Info](https://hk.v2ex.com/t/1209996)
- [Vupl](https://vupl.stream/) - Video client with Watch Together sessions. `Plex` `Jellyfin` · `Windows` `macOS` `Android` `iOS` `iPadOS` `Android TV` `tvOS` `Xbox` `visionOS` · `Free` · [App Store](https://apps.apple.com/app/id6811736454) · [Microsoft Store](https://apps.microsoft.com/detail/9ns56d9hqn2w)
- [Wicaby](https://github.com/WicaebethTheo/wicaby) - Windows-first client with Linux, Android and Android TV builds. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `Linux` `Android` `Android TV` `Fire TV` `Android Auto` · `GPL-3.0`
- [YarmiplayTV](https://tv.yarmiplay.com/) - mpv-based watch-together player that finds a Syncplay room's file on your media server. `Plex` `Jellyfin` · `Windows` `macOS` `Linux` `Web` · `Free` · [Snap](https://snapcraft.io/yarmiplaytv)
- [Zelefin](https://github.com/rndllb/Zelefin) - Mac, iPhone and Android client with its own push-notification plugin. `Jellyfin` `Emby` `+Silo` · `macOS` `Android` `iOS` `iPadOS` · `GPL-3.0` `Free` · [Website](https://zelefin.app) · [TestFlight](https://testflight.apple.com/join/hHBVNKTj)
- [Zerk Play](https://github.com/florinp93/Zerk-Play-2.0) - Emby-first desktop and Android TV player using mpv with HDR switching on Windows. `Jellyfin` `Emby` · `Windows` `Linux` `Android TV` · `GPL-3.0` `Free` `Beta`
- [浩视播放器](https://wuhaohan.icu/apps/video.html) - Video player with NAS, network share, cloud-drive and IPTV sources and no ads. `Plex` `Jellyfin` `Emby` `+IPTV` · `Windows` `Android`

### Android, Android TV and HarmonyOS

- [Ambient TV](https://github.com/seinist/ambient-tv) - Android TV and phone client that also reaches TVHeadend and DLNA sources. `Plex` `Jellyfin` `Emby` · `Android` `Android TV` `Android Auto` · `CC0-1.0` `Free` `Beta`
- [EmPlayer](https://play.google.com/store/apps/details?id=com.emplayer.app) - Android video player. `Plex` `Jellyfin` `Emby` · `Android` `Android Auto`
- [Entryway](https://github.com/YuSheng-Jack/Entryway_Release) - Closed-source player that combines media servers, IPTV and cloud drives in one app. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` `+IPTV` · `Android` `Android TV`
- [Finmony](https://appgallery.huawei.com/app/detail?id=com.hontt.finmony) - HarmonyOS video player for media servers on phones, tablets and PCs. `Jellyfin` `Emby` · `HarmonyOS`
- [FinVideo](https://github.com/OHPG/FinVideo) - HarmonyOS video client. `Plex` `Jellyfin` `Emby` · `HarmonyOS` · `GPL-3.0`
- [FirstTV](https://github.com/brucelee135/FirstTV) - Android client for Emby and Jellyfin. `Jellyfin` `Emby` · `Android` · `Open source` `Free`
- [Flow](https://github.com/Flow-Media-Client/Flow-release) - Chinese Android TV client. `Jellyfin` `Emby` · `Android TV` · `Paid`
- [Flymby](https://www.flymby.top/) - MPV-based player with HDR/Dolby Vision, AI subtitles and Anime4K for servers, cloud drives and IPTV. `Jellyfin` `Emby` `+fnOS` `+IPTV` · `Android` `HarmonyOS` `Android TV` · [Source](https://github.com/fbinba3955/Flymby)
- [Ghosten-Player](https://github.com/GhostenEditor/Ghosten-Player) - Android and Android TV player that also plays cloud drives and IPTV. `Jellyfin` `Emby` `+IPTV` · `Android` `Android TV` · `AGPL-3.0` `Free`
- [Harrik Player](https://github.com/harriks/harrik-player) - Android TV player built with Compose for TV and Media3/FFmpeg. `Jellyfin` `Emby` · `Android TV`
- [HosPlayer](https://appgallery.huawei.com/app/detail?id=com.colorlifee.hosplayer) - HarmonyOS phone, tablet and PC player that also opens fnOS, WebDAV and IPTV. `Plex` `Jellyfin` `Emby` `+fnOS` `+IPTV` · `HarmonyOS`
- [JellyCine](https://github.com/sureshfizzy/JellyCine) - Android video client. `Jellyfin` `Emby` · `Android` `Android TV` · `GPL-3.0` · [Google Play](https://play.google.com/store/apps/details?id=com.jellycine.app)
- [JellyWatch](https://jellywatch.app/player) - Android TV and Fire TV client with Live TV and server admin. `Jellyfin` `Emby` · `Android` `Android TV` `Fire TV` `Android Auto` · [Google Play](https://play.google.com/store/apps/details?id=com.jellywatch.tv)
- [KDTIVI](https://play.google.com/store/apps/details?id=com.kdtvandroid) - All-in-one media app combining servers, Stremio addons and M3U playlists. `Plex` `Jellyfin` `Emby` `+Stremio addons` `+IPTV` · `Android` `Android TV`
- [Lumora](https://github.com/LumoraPlayer/Lumora) - Kotlin IPTV and media client for TV remotes, merging IPTV portals and media server libraries. `Plex` `Jellyfin` `Emby` `+Stremio addons` `+Silo` `+IPTV` · `Android` `Android TV` `Fire TV` `Android Auto` · `Open source` `Free`
- [Lumy Player](https://github.com/hesier/lumy-player) - Android TV and Fire TV player that also connects to fnOS. `Plex` `Jellyfin` `Emby` `+fnOS` · `Android TV` · `GPL-3.0`
- [mediatree-app](https://github.com/ZASENJC/mediatree-app) - Android media library app with SMB and WebDAV sources. `Jellyfin` `Emby` · `Android` · `MIT`
- [MoonPlay](https://www.isaced.com/post/moonplay/) - HarmonyOS video player pitched as an Infuse alternative, with cloud drives and network shares. `Plex` `Jellyfin` `Emby` · `HarmonyOS` · `Free`
- [Mumbo](https://play.google.com/store/apps/details?id=com.mellao.melliplayer) - Android video client. `Plex` `Jellyfin` · `Android`
- [NeoPlayer](https://play.google.com/store/apps/details?id=live.alist.mpv.gp) - Android player for NAS shares, WebDAV and media servers, with AI live subtitles. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` · `Android` · `Freemium`
- [Nook](https://gitee.com/ksd678/nook) - Android TV client that merges several servers into one library, with libVLC for ISO, BDMV and ASS. `Jellyfin` `Emby` · `Android TV`
- [Nuvio Arc](https://github.com/ysosrs123/NuvioTV-Fork) - Stremio-style Android TV app extended with personal-server libraries and Silo. `Jellyfin` `Emby` `+Stremio addons` `+Silo` · `Android TV` `Fire TV` · `GPL-3.0` `Free`
- [Playable](https://gitee.com/leeczli/playable-apk) - Android and Android TV player with a poster wall, direct play and progress write-back. `Plex` `Jellyfin` `Emby` · `Android` `Android TV`
- [PlezyFold](https://github.com/emersonCase/plezyFold) - Plezy fork adapted for foldable phones. `Plex` `Jellyfin` `Emby` · `Android` · `GPL-3.0` `Free`
- [PureVibe](https://poka.cc/) - HarmonyOS video and music player with NAS, network share and Chinese cloud-drive sources. `Plex` `Jellyfin` `Emby` `+fnOS` · `HarmonyOS` · `Freemium`
- [Spole](https://github.com/oyvhov/spole-android) - Android TV and phone client. `Jellyfin` `Emby` · `Android` `Android TV` · `Open source` `Free` `Beta`
- [Vela Player](https://vela.app.mahui.me/) - HarmonyOS video player that also runs on Huawei Vision TVs, with network shares and Chinese cloud drives. `Plex` `Jellyfin` `Emby` · `HarmonyOS` · `Free`
- [VlcJellyfin](https://github.com/sifacaii/VlcJellyfin) - VLC-based Android TV client for old Android 4.2+ devices; replaced by VlcXWJellyfin. `Jellyfin` `Emby` · `Android TV` · `Open source` `Free` `Stale 2025`
- [VlcXWJellyfin](https://github.com/sifacaii/VlcXWJellyfin) - VLC-based Android client, the successor to VlcJellyfin. `Jellyfin` `Emby` · `Android` · `Open source` `Free` `Stale 2025`
- [Yamby](https://play.google.com/store/apps/details?id=com.hush.yamby) - Android and Android TV client with DanDanPlay danmaku comments. `Jellyfin` `Emby` · `Android` `Android TV` · `Freemium` · [Info](https://v2ex.com/t/1107970)

### Apple platforms

- [Aether Player](https://apps.apple.com/us/app/aether-player/id6775229911) - Media player that merges several servers into one deduplicated library and flags the better copy of a title. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Free`
- [AirTV](https://apps.apple.com/app/id6759542580) - iPhone and Apple TV player for media servers and IPTV. `Plex` `Jellyfin` `+IPTV` · `iOS` `iPadOS` `tvOS`
- [Alexandria](https://apps.apple.com/tw/app/alexandria-the-media-library/id6756271770) - Multi-server library app for music, video, audiobooks, ebooks, comics and manga. `Plex` `Jellyfin` `+Audiobookshelf` `+Kavita` · `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Freemium`
- [AllPlayer Pro](https://apps.apple.com/us/app/allplayer-pro/id6761591864) - Media player and manager with a movie wall, iCloud sync and playback from local, NAS and cloud sources. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `watchOS` · `Free`
- [ApexPlayer](https://apps.apple.com/us/app/apexplayer-own-your-feed/id6802367377) - Player for Jellyfin, Plex, Emby and ApexFeeder libraries with a one-time Pro purchase for the full library. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium`
- [AshPlayer](https://apps.apple.com/us/app/ashplayer/id6797693539) - Library player with resume and subtitle and audio-track choice for personal media servers. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Atrium](https://apps.apple.com/app/atrium-media-player/id6777638751) - Apple TV player for home media servers. `Jellyfin` `Emby` · `tvOS` · `Free`
- [Avelio](https://apps.apple.com/us/app/avelio/id6811089789) - Native iPhone and iPad client for several server types, with Picture in Picture and Continue Watching. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [AvoPlayer](https://apps.apple.com/tw/app/avoplayer/id6818531981) - Video player with its own decoding and display pipeline for local files, shares and media servers. `Plex` `Jellyfin` `Emby` `+fnOS` · `macOS` `iOS` `iPadOS` · `Free`
- [Bandit Media Player](https://apps.apple.com/us/app/bandit-media-player/id6792535052) - Media player for servers, IPTV playlists and file shares, with Stremio-compatible add-on catalogs. `Plex` `Jellyfin` `Emby` `+Stremio addons` `+IPTV` · `iOS` `iPadOS` · `Freemium`
- [BeamOS](https://testflight.apple.com/join/h7VmeSqz) - Apple TV player that plays files untouched, including 4K HDR, Dolby Vision and MKV with DTS or TrueHD. `Plex` `Jellyfin` `Emby` `+IPTV` · `tvOS` · `Beta`
- [Beebox](https://apps.apple.com/us/app/beebox-smart-player/id6747574244) - Media manager and player for movies, shows, music and M3U IPTV from NAS, cloud drives and servers. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free` `Stale 2025`
- [BeeJoy](https://apps.apple.com/us/app/beejoy/id6670792086) - Video player for Blu-ray ISO and BDMV folders, network shares and server libraries, with HDR and Atmos. `Plex` `Jellyfin` `Emby` `+fnOS` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Free`
- [BoxPlayer](https://apps.apple.com/us/app/boxplayer-4k-video-player/id6739804060) - Video player that gathers cloud drives, NAS, IPTV and media servers into one poster-wall library. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Bref Player](https://www.bref.cn/) - Video, music and book player linking local files, NAS, cloud drives and media servers on every screen. `Plex` `Jellyfin` `Emby` `+fnOS` `+IPTV` `+OPDS` · `macOS` `iOS` `iPadOS` `tvOS` · `Free` · [App Store](https://apps.apple.com/us/app/bref-player/id6788695019)
- [CarCast Player](https://apps.apple.com/us/app/carcast-player/id6824499197) - Player and cast receiver for your own videos, playlists and media server, with CarPlay audio in the car. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [Car Cinema](https://apps.apple.com/us/app/car-cinema-tv-iptv-cast/id6819820648) - Car-screen player for playlists, live channels, web videos and your own clips, with casting. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [Car Play TV](https://apps.apple.com/tw/app/car-play-tv-%E8%BB%8A%E6%A9%9F%E6%8A%95%E5%BD%B1%E8%88%87%E9%9B%BB%E8%A6%96%E7%9B%B4%E6%92%AD/id6778658196) - Car-screen video player and casting app for playlists, media servers and WebDAV, with a driver-friendly Drive Mode. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [CarPlus](https://apps.apple.com/us/app/carplus/id6814469773) - Car-ready media library that combines M3U playlists, media servers, imported videos and YouTube links. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [CarScreen](https://apps.apple.com/us/app/carscreen-video-in-your-car/id6819269005) - Plays video from your library on CarPlay screens. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Car TV](https://apps.apple.com/us/app/car-tv-media-player-cast/id6818264613) - Car-screen player that gathers your video files, stream playlists and media server libraries on one home screen. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free`
- [CastFlow](https://apps.apple.com/us/app/castflow/id6448221325) - Home media hub that casts from the phone, plays IPTV and browses a server library or NAS files. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Paid`
- [Cathode](https://testflight.apple.com/join/hWgS5AZB) - iOS app that combines IPTV with media-server playback. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Beta`
- [Ceau Player](https://apps.apple.com/us/app/ceau-player/id6811592403) - Private-first player for live TV, media servers and local files with multi-view of up to four streams. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `CarPlay` `watchOS` · `Freemium`
- [Celo](https://apps.apple.com/cn/app/celo/id6802992811) - Library player with subtitle translation, downloads, offline viewing and local file playback. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Chroma](https://apps.apple.com/us/app/chroma-spatial-cinema/id6478800800) - Cinema-style video player with direct play of MKV, Dolby Vision and HDR across several servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` `visionOS` `CarPlay` · `Freemium`
- [Cinemarr](https://apps.apple.com/us/app/cinemarr-private-cinema/id6799851978) - Player for Plex, Jellyfin and Emby libraries with Seerr requests, watchlists and request status. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Subscription`
- [Cinereel Media Server Player](https://apps.apple.com/us/app/cinereel-media-server-player/id6792861697) - Plex and Jellyfin player with natural-language search such as funny movies from the 30s. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium`
- [Conflux](https://apps.apple.com/us/app/conflux-video-player/id6450330892) - Apple-platform video player for home media servers. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium`
- [DashCast](https://apps.apple.com/us/app/dashcast-cast-video-to-car/id6805296534) - Cast target for parked cars that shows phone videos, network media and casts from other apps on the car screen. `Plex` `Jellyfin` `Emby` · `iOS` `CarPlay` · `Free`
- [ddPlayer](https://apps.apple.com/us/app/ddplayer/id6810930763) - Video player for local files, Baidu Netdisk, OneDrive, NAS shares and media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [DeePlayer](https://deeplayer.feifeiduck.com) - Home-theater video player for cloud drives and media servers, with automatic poster scraping. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free` `Stale 2025` · [App Store](https://apps.apple.com/us/app/deeplayer-create-home-theater/id6744684471)
- [DocumentHub](https://apps.apple.com/fr/app/documenthub-gestionnaire/id6761395846) - File manager and document viewer that also streams video and music from media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [DS One](https://apps.apple.com/cn/app/ds-one-%E5%8E%9Fds-cloud-%E9%AB%98%E6%B8%85%E5%BD%B1%E7%89%87-%E6%97%A0%E6%8D%9F%E9%9F%B3%E4%B9%90%E8%BD%BB%E6%9D%BE%E6%92%AD/id6476057278) - Player for Synology NAS and media servers, with music playback. `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [EMTV](https://apps.apple.com/us/app/emtv/id1671608662) - Apple TV client activated through yybx. `Jellyfin` `Emby` · `tvOS` · `Free`
- [EplayerX](https://apps.apple.com/cn/app/eplayerx-%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE%E5%99%A8/id6747369377) - Video player for media servers, Chinese cloud drives and network shares. `Plex` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium` · [TestFlight](https://testflight.apple.com/join/k5dVQwHK)
- [Filebar](https://fileball.app/) - Apple-platform media player for servers and file shares. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium` · [App Store](https://apps.apple.com/us/app/filebar-media-player/id1558391784)
- [Flicktote](https://apps.apple.com/de/app/flicktote/id6822864981) - Offline-first player that downloads movies and shows and searches across several servers at once. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [Freya Player](https://apps.apple.com/us/app/freya-player/id6761883699) - Client for Plex and Jellyfin servers built around a native Apple TV interface. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Gen Player](https://apps.apple.com/us/app/gen-player/id6760933333) - Media manager and player for SMB, WebDAV, FTP, Alist, NFS and IPTV sources plus media servers. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Paid` · [Source](https://github.com/fugary/gen-player-pages)
- [Gravity](https://apps.apple.com/us/app/gravity-your-cloud-media-hub/id6813851230) - Cloud-first media library that builds posters and metadata from OpenList and cloud folders, plus media servers. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [GreenPlayer](https://apps.apple.com/us/app/greenplayer-media-player/id6803910858) - Video player for local, iCloud Drive and NAS files plus Jellyfin and Emby libraries, with one-tap enhancement. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` · `Free`
- [HamHub](https://apps.apple.com/app/id6458691598) - Apple-platform player for media servers and cloud drives. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`
- [HANAplay](https://apps.apple.com/us/app/hanaplay/id6782382601) - Media server player with a cinematic home, continue watching and a choice of media versions. `Plex` `Jellyfin` `Emby` `+Silo` · `iOS` `iPadOS` `tvOS` · `Free`
- [iCar for Tesla](https://apps.apple.com/de/app/icar-for-tesla/id6801842057) - Tesla companion app for charging, trips and navigation, with in-car video from your Plex or Jellyfin library. `Plex` `Jellyfin` · `iOS` `iPadOS` `Tesla` · `Free`
- [iCouldPlay](https://apps.apple.com/us/app/icouldplay/id6755653178) - Video player for most formats and codecs that also opens network shares and media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Paid`
- [Illumi Player](https://apps.apple.com/us/app/illumi-player/id6748852290) - Player with discovery, watchlists and library playback from Emby or Plex. `Plex` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [iNAS Player](https://apps.apple.com/us/app/inas-player-nas-video-music/id6787336253) - NAS video and music player that streams directly from shares and media servers without uploading. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [Infuse](https://firecore.com/infuse) - Video player for Apple devices with library browsing and an optional Pro tier. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium` · [App Store](https://apps.apple.com/us/app/infuse/id1136220934)
- [Infuse: Enterprise](https://apps.apple.com/app/id6755395866) - Enterprise edition of Infuse sold as its own App Store listing. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Paid`
- [Interlace Player](https://apps.apple.com/us/app/interlace-player/id6789244498) - Player that puts your media server and IPTV channels in one interface with a programme guide. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Subscription`
- [Kanata](https://apps.apple.com/us/app/kanata/id6806893112) - Media player with danmaku comments and subtitle tools that reads media servers and WebDAV. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [KenjaPlayer](https://apps.apple.com/us/app/kenjaplayer-ai-video-player/id6792728329) - Video player that generates and translates subtitles on-device, with media server sources. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Kosmos](https://apps.apple.com/us/app/kosmos-emby-client/id6758503137) - Client for Emby and Jellyfin servers and WebDAV storage with multiple accounts and dual playback engines. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [LASTROW](https://apps.apple.com/br/app/lastrow/id6782303804) - Cover-art video library for collections on a NAS, media server or WebDAV, with no cloud or subscription. `Plex` `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Lenna](https://apps.apple.com/us/app/lenna-video-library-player/id6502967807) - iPhone, iPad and Apple TV video library player. `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [LeyTV](https://apps.apple.com/us/app/leytv-iptv-media-player/id6815275073) - iPhone video app that plays on CarPlay screens. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `CarPlay` · `Freemium` `Beta` · [TestFlight](https://testflight.apple.com/join/tGMEk552) · [Info](https://www.reddit.com/r/CarPlay/comments/1xmeapt/works_with_272_i_made_a_carplay_video_app_that/)
- [Livedio](https://apps.apple.com/us/app/livedio-m3u-video-player/id6788334969) - Video player that gathers M3U playlists, drives, media servers and cloud folders in one library. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [Lura CarMode](https://apps.apple.com/us/app/lura-carmode/id6779367108) - File manager and media player with a car mode for local files, IPTV and Jellyfin or Emby libraries. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [LUX Video Player](https://apps.apple.com/us/app/lux-video-player-hd-media/id6762520464) - Video player for HD and 4K files with offline storage and network streaming on iPhone, iPad and Apple TV. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [MediaOne Player](https://apps.apple.com/us/app/mediaone-player/id6755380271) - All-in-one video player for local files, cloud storage, network shares and media servers. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [MoodBX](https://apps.apple.com/br/app/moodbx-series-pelis-y-juegos/id6769435122) - Tracker for series, films and games that also plays from a NAS, Jellyfin or Plex. `Plex` `Jellyfin` · `iOS` · `Free`
- [MovoHub](https://apps.apple.com/us/app/movohub/id6814582086) - Library and player for media servers, WebDAV folders and channel sources, with posters and favourites. `Plex` `Jellyfin` `Emby` `+fnOS` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Mulux](https://apps.apple.com/us/app/mulux/id6808890915) - Film player with a story-understanding feature for titles without subtitles, plus resume across devices. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` `visionOS` · `Free`
- [Muxivo](https://apps.apple.com/us/app/muxivo-mkv-player-cast/id6796830155) - MKV, AVI and TS player that converts on-device so casts to a TV keep picture and sound. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` · `Freemium`
- [MyCarPlay](https://apps.apple.com/us/app/mycarplay/id6822954118) - Car-screen player for Plex and Emby libraries, M3U and Xtream channels and phone videos while parked. `Plex` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [MyFiles](https://apps.apple.com/br/app/myfiles-gerencie-arquivos/id6478056702) - File manager and media player with a compressor and PDF scanner that also streams from media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [NanoShelf](https://apps.apple.com/us/app/nanoshelf/id6800173831) - Video and music player for media servers, NAS shares and local folders with continue watching and listening. `Plex` `Jellyfin` `Emby` `+Subsonic` · `macOS` `iOS` `iPadOS` `tvOS` · `Paid`
- [NAS Media Viewer](https://apps.apple.com/us/app/nas-media-viewer/id6759468790) - Vision Pro, iPhone and Mac player that also opens SMB shares. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `visionOS` · `Subscription`
- [Nest](https://apps.apple.com/us/app/nest-video-player/id6787344988) - Native Swift video player for server libraries with no monthly fee. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Nestrr](https://apps.apple.com/us/app/nestrr/id6759966207) - Discovery, requests and playback app for Seerr, Plex and Jellyfin libraries with synced progress. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free`
- [NextSee](https://apps.apple.com/us/app/nextsee/id6813748066) - Multi-source player for media servers, WebDAV and SMB with Dolby Vision, Blu-ray ISO and AI subtitles. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`
- [Noctra](https://apps.apple.com/us/app/noctra/id6811375568) - Media library player with a watchlist, calendar reminders, track selection and encrypted settings backup. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [OCPlayer](https://github.com/1824239290/OcPlayer) - Player with Bangumi tracking and dandanplay danmaku comments. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` · `GPL-3.0` `Free`
- [ONEX](https://apps.apple.com/tw/app/onex-video-library-player/id6781184071) - Library video player that joins servers, WebDAV, NAS and device files in one browsable view. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [OopsPlayer](https://apps.apple.com/us/app/oopsplayer/id6758075545) - iPhone and Apple TV player for servers, SMB/WebDAV shares, cloud drives and IPTV. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`
- [Panvox Player](https://apps.apple.com/us/app/panvox-player/id6819539073) - Video player for phone, NAS and server libraries that keeps ASS and PGS subtitle styling and 4K HDR. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` · `Freemium`
- [PearCinema](https://apps.apple.com/us/app/pearcinema-self-hosted-video/id6805989746) - Video app that streams a Jellyfin or Emby library over a direct encrypted link with no port forwarding. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Photon Player](https://apps.apple.com/us/app/photon-player/id6804291311) - Native player joining media servers, cloud and network storage and live TV; extra servers need Pro. `Plex` `Jellyfin` `Emby` `+Silo` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium`
- [Pippin](https://apps.apple.com/us/app/pippin/id6783976415) - Customisable Plex and Jellyfin client with hardware-accelerated playback, custom shelves and filters. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Pleya](https://apps.apple.com/de/app/pleya/id6787464031) - Plex and Jellyfin client with a cinematic home, continue-watching rows and detail pages. `Plex` `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Paid` · [Source](https://github.com/michelknoop21/pleya)
- [Plio](https://apps.apple.com/jp/app/plio-universal-media-player/id6786546470) - Universal media player for media servers and WebDAV. `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [Plozz](https://github.com/brandomoore/Plozz) - Native Apple TV, iPhone and iPad client that also plays network shares. `Plex` `Jellyfin` `Emby` `+Silo` · `iOS` `iPadOS` `tvOS` · `GPL-3.0` `Free` · [Website](https://plozz.app) · [App Store](https://apps.apple.com/app/plozz-player/id6782668147) · [TestFlight](https://testflight.apple.com/join/EKfReNMu)
- [Plynic](https://apps.apple.com/us/app/plynic/id6757113719) - Video player that combines NAS, Emby, Jellyfin, local files and IPTV playlists in one library. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free`
- [Portage](https://apps.apple.com/us/app/portage-media-server-player/id6816252844) - Player and downloader for media servers and folders, with background downloads for offline viewing. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` · `Free`
- [Projector](https://apps.apple.com/us/app/projector-cinema-player/id6817923186) - iPad cinema player that opens Files, shares, WebDAV, servers and URLs without recompressing video. `Plex` `Jellyfin` `Emby` · `iPadOS` `tvOS` · `Paid`
- [Railux](https://apps.apple.com/cn/app/id6773220930) - iPhone video player that connects to home media servers. `Plex` `Emby` · `iOS` `iPadOS`
- [Rex](https://apps.apple.com/us/app/rex-all-your-media/id6801583759) - Show tracker and video player with an episode calendar, air-time reminders and viewing history. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [Riveo](https://riveo.io/apple-tv) - Player for media servers, network shares, cloud drives and live TV in one app. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Free` · [App Store](https://apps.apple.com/us/app/riveo-media-player/id6782365180)
- [Rivulet Player](https://github.com/l984-451/Rivulet) - Apple TV video player. `Plex` `Jellyfin` `+IPTV` · `tvOS` · `Open source` `Free` `Beta` · [TestFlight](https://testflight.apple.com/join/TcCsF5As) · [App Store](https://apps.apple.com/app/id6756892857)
- [Saisei Player](https://apps.apple.com/us/app/saisei-player/id6764529684) - Multi-source video player with offline saving, in-frame text translation and Telegram video access. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Satellite](https://apps.apple.com/us/app/satellite-media-server-player/id6787551103) - Plex, Jellyfin and Emby client with offline viewing and Seerr search. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [Scorpio Player](https://apps.apple.com/gb/app/scorpio-player-2025/id1617922279) - Native video, audio and image player with playback-speed control and resume playback. `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free` `Stale 2024`
- [Screen2Car](https://apps.apple.com/us/app/screen2car-video-cast/id6814131451) - Car-screen app that mirrors the iPhone, takes DLNA casts and plays playlists and media server libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Freemium`
- [ScreenSpot](https://apps.apple.com/us/app/screenspot-%E6%9A%AE%E8%89%B2/id6792606268) - Player for movies, shows, music and podcasts from media servers, with CarPlay video support. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`
- [SenPlayer](https://apps.apple.com/app/id6443975850) - Apple-platform player for media servers, SMB/WebDAV/FTP shares, Chinese cloud drives and IPTV. `Plex` `Jellyfin` `Emby` `+fnOS` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Sleek](https://apps.apple.com/ru/app/sleek/id6763681786) - Video player and personal library fed from Files, Wi-Fi upload or a connected media server. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Spectati](https://apps.apple.com/app/id6767241047) - Apple-platform player for media servers and IPTV. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [SquareRoot Media](https://apps.apple.com/us/app/squareroot-media-poster-wall/id6813732902) - Poster-wall browser that shows a library as a zoomable wall of artwork and album covers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [StreamPocket](https://apps.apple.com/us/app/streampocket-offline-player/id6760236575) - Downloader and offline player that saves movies and episodes from a home server at full speed. `Plex` `Emby` · `iOS` `iPadOS` · `Free`
- [Strimr](https://github.com/wunax/strimr) - Native Apple video client. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `GPL-3.0` `Free` · [App Store](https://apps.apple.com/app/id6757491271) · [TestFlight](https://testflight.apple.com/join/nayaffkP)
- [SubFlow](https://apps.apple.com/cn/app/subflow-ai-%E5%AD%97%E5%B9%95%E6%92%AD%E6%94%BE%E5%99%A8/id6818683677) - Video player that generates on-device AI subtitles for shares and servers; Pro adds subtitle export. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [SubPlayer](https://apps.apple.com/us/app/subplayer-smart-video-player/id6759992867) - Video player with one-tap AI subtitle generation for local files, network sources and media servers. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` · `Free`
- [SVPlayer](https://apps.apple.com/ru/app/svplayer-%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B8-%D0%B2%D1%81%D1%91-%D0%B2-60-fps/id6446900981) - mpv-based video player that interpolates films to 60 fps and browses server libraries. `Plex` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [TechDad Player](https://apps.apple.com/app/id6756520836) - Apple-platform player that also plays local files. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Tekstream](https://apps.apple.com/jp/app/tekstream/id6786884911) - Video client with downloads. `Plex` `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [The Media Center](https://apps.apple.com/us/app/the-media-center/id6806915078) - Household client for a family-run server; ships with no content of its own. `Plex` `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [Tifo](https://apps.apple.com/app/id6782486035) - IPTV player for M3U, Xtream and Stalker that also plays from media servers. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · [TestFlight](https://testflight.apple.com/join/U66gTb2V)
- [Tilus](https://apps.apple.com/us/app/tilus-media-player/id6761753229) - Video player with its own engine for Dolby Vision and Atmos from USB, NAS, servers and the cloud. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Trovu](https://apps.apple.com/us/app/trovu-jellyfin-plex-player/id6760936018) - Touch-first player for Jellyfin and Plex libraries that direct-plays common formats to reduce transcoding. `Plex` `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Ultimate Media Player (Toby Jones)](https://apps.apple.com/us/app/ultimate-media-player/id6803723173) - Player for Jellyfin, Plex and IPTV sources with a 3D conversion mode. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Vanto](https://apps.apple.com/us/app/vanto-nas-media-player/id6794951510) - Media player for media servers and NAS shares that lets the phone control playback on Apple TV. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Velum](https://testflight.apple.com/join/vBfBu1PE) - Local video library with TMDB matching that also connects to media servers, no account needed. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Beta`
- [Vesper](https://testflight.apple.com/join/mcCk473Y) - Video player with Library Sync for media servers and WebDAV shares. `Plex` `Jellyfin` `Emby` `+Silo` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Beta`
- [Video +](https://apps.apple.com/us/app/video-player-for-cloud/id564484459) - iPhone video player for media servers, Subsonic and cloud storage. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS`
- [VideoBox](https://apps.apple.com/us/app/videobox-cloud-video-player/id1003166435) - Video downloader, player and file manager for cloud drives, DLNA, SMB and FTP that also browses media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [VideoHub](https://apps.apple.com/us/app/videohub-media-player-iptv/id6761449396) - Media player for cloud storage, local files, IPTV and home servers in one library. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free`
- [Video Player - All in One](https://apps.apple.com/us/app/video-player-all-in-one/id1538120666) - Video and music player with background playback, Cast, PiP and network share access. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Video Player - PIP and more](https://apps.apple.com/us/app/video-player-pip-and-more/id1610938825) - Video player with Picture in Picture, 4K HDR and support for SMB and server sources. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [Vidora](https://apps.apple.com/us/app/vidora/id6756205248) - Series tracker and player that syncs watch progress, upcoming episodes and discovery across devices with Trakt. `Plex` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [Vina](https://apps.apple.com/us/app/vina-nas-video-player/id6826125568) - NAS and media server player for video, music and photos over SMB, WebDAV, FTP, SFTP and NFS. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [Viondo](https://apps.apple.com/us/app/viondo-cartv-player-cast/id6820984228) - Car-screen video player for CarPlay that plays your own videos, M3U playlists and media server libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [Visorium](https://apps.apple.com/us/app/visorium/id6763748963) - Video player for NAS and media servers over WebDAV, SMB, FTP, NFS and DLNA with no downloads needed. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Vivid](https://apps.apple.com/us/app/vivid-video-player-for-nas/id6763759019) - NAS video player that streams directly over SMB, WebDAV and Dropbox without copying files. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Vuko Player](https://apps.apple.com/us/app/vuko-player/id6746368707) - HDR video player for Plex and Jellyfin with offline downloads and multiple server profiles. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free`
- [Watcher](https://apps.apple.com/us/app/watcher-video-player/id6826374333) - Plex and Jellyfin player with a My List for saving movies and shows. `Plex` `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Paid`
- [Watchy](https://apps.apple.com/app/id6822633437) - iPhone video player that connects to home media servers. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [XFiles](https://apps.apple.com/us/app/xfiles-sftp-ftp-nas-files/id6796674895) - File manager for FTP, SFTP, WebDAV, SMB and cloud storage that can also use media servers as sources. `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [YingBox](https://apps.apple.com/us/app/yingbox/id6761600855) - Media player that loads M3U playlists, JSON site configurations and private media servers. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [YingKu](https://apps.apple.com/us/app/yingku-video-player/id6816915245) - Video player for SMB shares, WebDAV, Aliyun Drive, media servers and local files. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [zFuse](https://apps.apple.com/cn/app/id1054505347) - iPhone client. `Jellyfin` `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium` · [App Store](https://apps.apple.com/app/id1009747025)
- [Zplayer Private Cinema](https://apps.apple.com/us/app/zplayer-private-cinema/id6814412951) - Player for Emby, Jellyfin, Feiniu (via its Jellyfin-compatible service), SMB shares and local files. `Jellyfin` `Emby` `+fnOS` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Zuno](https://apps.apple.com/us/app/id6759619793) - Apple-platform player with a 'Zuno Live' guide view. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [映盒TV](https://testflight.apple.com/join/cGrUnMAP) - Personal video aggregator with custom site configs, M3U IPTV and private media servers. `Jellyfin` `Emby` `+IPTV` · `tvOS` · `Beta`

### Desktop

- [AI Player](https://aiplayer.arkhamimp.qzz.io/) - Windows desktop player with a Fluent 2 interface and libmpv playback. `Jellyfin` `Emby` · `Windows` · `Free`
- [Catfyn](https://github.com/coderastic/Catfyn) - Couch-friendly client with a TV-style interface, written in Rust. `Plex` `Jellyfin` · `Linux` · `MIT` `Free`
- [CineTray](https://github.com/p3rception/CineTray) - Menu-bar app for browsing movies, shows and music from media servers and local folders. `Plex` `Jellyfin` `+Subsonic` · `macOS` · `Open source` `Free`
- [DeckVideoPlayer](https://github.com/nicocarbone/DeckVideoPlayer) - Controller-driven video player for Steam Deck Game Mode. `Plex` `Jellyfin` · `Linux` `Steam Deck` · `GPL-2.0`
- [Evervideo](https://apps.apple.com/us/app/evervideo/id6743504109) - Mac video player for local files, cloud storage, NAS and media servers, with offline playback and an equalizer. `Plex` `Jellyfin` `Emby` `+Subsonic` · `macOS` · `Free`
- [Flick](https://github.com/seoloon/flick_desktop) - Customisable Rust desktop client for media servers. `Plex` `Jellyfin` · `Windows` `macOS` · `GPL-3.0` `Free`
- [FloePlayer](https://apps.apple.com/us/app/floeplayer-video-player/id6817234839) - mpv-based video player for local files, media servers and network storage on Mac. `Jellyfin` `Emby` · `macOS` · `Free`
- [IPTV Fluent](https://apps.microsoft.com/detail/9pkmdlwbc8zj) - IPTV and media hub player for Xbox and Windows. `Jellyfin` `Emby` `+IPTV` · `Windows` `Xbox` · [Info](https://emby.media/community/topic/139659-fluent-player-media-hub-iptv-for-windows-and-xbox/)
- [Jeva](https://github.com/tearerry/Jeva) - Windows client with a streaming-service style interface. `Plex` `Jellyfin` `Emby` · `Windows` · `Open source` `Free`
- [loemby](https://github.com/NPCDW/loemby) - Simple desktop media-server client. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `MIT`
- [MediaLib](https://github.com/Again0521/MediaLib) - Native macOS home media library and player. `Plex` `Jellyfin` `Emby` · `macOS` · `Apache-2.0` `Free`
- [Momoka](https://github.com/cudamin/Momoka) - WinUI media library client for Windows. `Plex` `Jellyfin` `Emby` `+fnOS` · `Windows` · `MIT` `Free` · [Microsoft Store](https://apps.microsoft.com/detail/9NQJL7K0H8X0)
- [MyJellyfinClient](https://github.com/eater-altria/MyJellyfinClient) - Windows and macOS client built with Tauri, React and a native mpv player. `Jellyfin` `Emby` · `Windows` `macOS` · `Open source` `Free`
- [NekoPlayer](https://github.com/L51xyz12138/nekoplayer) - Electron and mpv desktop player for Emby, Jellyfin and Plex. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [Nimbus Player](https://github.com/JushiZen/Nimbus.Player) - Windows desktop media player. `Plex` `Jellyfin` `Emby` `+fnOS` · `Windows` · [Microsoft Store](https://apps.microsoft.com/detail/9NZGD27NW89W)
- [nyx-theater](https://github.com/design-nexus/nyx-theater) - GTK 4 desktop app that browses and plays Plex and Jellyfin in one window. `Plex` `Jellyfin` · `Linux` · `MIT`
- [Popvee](https://apps.apple.com/us/app/popvee-ai-media-player/id6784186034) - Mac media library for local folders, NAS, cloud drives and servers, with Dolby Vision and AI subtitles. `Jellyfin` `Emby` · `macOS` · `Free`
- [qEmby](https://github.com/AlanHJ/qEmby) - Qt6 and C++20 desktop client for Emby libraries with Jellyfin support. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [QiTV](https://github.com/ozankaraali/QiTV) - Desktop player for IPTV portals (STB, Xtream) and media server libraries. `Jellyfin` `Emby` `+IPTV` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [QP](https://github.com/KuDoZ007/QP) - macOS menu bar app for quickly finding and playing library items. `Plex` `Jellyfin` · `macOS` · `Open source` `Free` `Beta`
- [Reel](https://github.com/arsfeld/reel) - GTK4 desktop frontend for Linux. `Plex` `Jellyfin` · `Linux` · `Open source` `Free`
- [reEmby](https://github.com/suhiymof/ReEmby) - Qt 6 and libmpv desktop client for Emby and Jellyfin. `Jellyfin` `Emby` · `Windows` · `MIT` `Free`
- [Rodel Player](https://player.richasy.net) - Windows desktop player with a Fluent UI. `Plex` `Jellyfin` `Emby` · `Windows` · `Freemium` · [Source](https://github.com/Richasy/Rodel.Player.Public) · [Microsoft Store](https://apps.microsoft.com/detail/9nb0h051m4v4)
- [Vela](https://github.com/roethlar/vela) - Desktop front end that plays through mpv for HDR output. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [Vivid Player](https://apps.microsoft.com/detail/9pf8wt09d2nt) - Windows player that also opens fnOS, SMB, WebDAV, OpenList/Alist and rclone sources. `Plex` `Jellyfin` `Emby` `+fnOS` · `Windows` `Xbox` · `Paid`
- [WWPlayer](https://github.com/Carrottor/WWPlayer) - Desktop libmpv player for server libraries, cloud drives, NAS and local files, with HDR and Dolby Vision. `Jellyfin` `Emby` `+fnOS` · `Windows` · `Freemium`
- [xPlayer](https://github.com/xtq94kws7z-droid/Xplayer) - Windows desktop client for Emby and Jellyfin. `Jellyfin` `Emby` · `Windows` · `MIT` `Free`

### Web

- [BackseatFin](https://github.com/jiaton/backseatfin) - Client that runs in a car's web browser, even while the car is moving. `Jellyfin` `Emby` · `Web` `Tesla` · `MIT` `Free`
- [Glimpse Media Viewer](https://github.com/jeremehancock/Glimpse) - Self-hosted web viewer for browsing and playing media-server libraries. `Plex` `Jellyfin` `Emby` · `Web` · `MIT`

## Jellyfin video clients

Third-party video and general clients for Jellyfin only.

### Cross-platform

- [acedgold/jellyclient](https://github.com/acedgold/jellyclient) - Flutter Jellyfin client with a dark cinema-style design. `Jellyfin` · `Windows` `macOS` `Linux` `iOS` · `MIT` `Free`
- [Altcast](https://github.com/filipefilardi/altcast) - Movies and TV client for Jellyfin. `Jellyfin` · `macOS` `Android` `iOS` · `Apache-2.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.silent_summit.altcast)
- [Aurita](https://github.com/gnmyt/Aurita) - TV-oriented frontend for browsing and playing your library. `Jellyfin` · `Web` `Android TV` · `MIT` `Free`
- [Aurora for Jellyfin](https://github.com/Get-Coral/aurora) - Self-hosted browser frontend, run in Docker, that syncs playback back to the server. `Jellyfin` · `Web` `Android` · `MIT` · [Website](https://www.getcoral.dev/apps/aurora) · [Google Play](https://play.google.com/store/apps/details?id=dev.getcoral.aurora)
- [Bloom's Jellyfin Client](https://github.com/BloomPhobic/Bloom-s-Jellyfin-Client-iOS) - iPhone client that direct-plays through mpv. `Jellyfin` · `Linux` `iOS` · `MPL-2.0` `Free` · [Source](https://github.com/BloomPhobic/Bloom-s-Jellyfin-Client)
- [Cascade](https://github.com/Cha0s1nc/Cascade-Project) - Music, movies and TV app for Jellyfin. `Jellyfin` · `Windows` `macOS` `Linux` `iOS` `tvOS` · `Open source` `Free`
- [C-Film](https://apps.apple.com/hk/app/c-film/id6789828713) - Jellyfin client with direct play, offline downloads, seek previews and multi-server support. `Jellyfin` · `Android` `iOS` `iPadOS` · `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.cfilm.app)
- [Chameleon](https://github.com/jumpingfox-dev/chameleon) - Customisable Flutter client for Jellyfin. `Jellyfin` · `Android` `iOS` `Android TV` · `Open source` `Free`
- [Chudder](https://github.com/JenteJan/Chudder) - Opinionated fork of the Fladder Flutter client. `Jellyfin` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `Android TV` · `GPL-3.0` `Free`
- [Fathom](https://github.com/TraceApps/fathom) - Desktop client with a built-in YouTube player and Seerr requests. `Jellyfin` · `Windows` `Linux` `Android` `Android TV` `Android Auto` · `AGPL-3.0`
- [Finar](https://gitlab.com/Openlyst/finar) - Flutter client for video and music with downloads, multiple accounts and game controller support. `Jellyfin` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` · `AGPL-3.0` · [Website](https://openlyst.ink) · [AUR](https://aur.archlinux.org/packages/finar-bin)
- [Fladder](https://github.com/DonutWare/Fladder) - Cross-platform video client, including a web build that runs in Docker. `Jellyfin` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `iPadOS` `Android TV` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=nl.jknaapen.fladder) · [Flathub](https://flathub.org/apps/nl.jknaapen.fladder)
- [Flutterfin](https://github.com/stainlesteel/Flutterfin) - Flutter client for Jellyfin. `Jellyfin` · `Linux` `Web` `Android` · `Apache-2.0` `Free`
- [Gelatin](https://github.com/ManiProjs/gelatin) - Jellyfin client app. `Jellyfin` · `Windows` `macOS` `Linux` `Android` · `MIT` `Free`
- [Glassfin](https://github.com/doombadroid/glassfin) - Fork of Streamyfin. `Jellyfin` · `Android` `iOS` · `MPL-2.0` `Free`
- [Hestia](https://github.com/bybrooklyn/Hestia) - Web client built on Jellyfin Vue. `Jellyfin` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free`
- [Hevyfin](https://github.com/NickHemeryckeHevan/Hevyfin) - Jellyfin client aimed at most devices. `Jellyfin` · `Linux` `Web` `Android` `Android TV` · `GPL-3.0` `Free`
- [Homeflix](https://github.com/dahl-jar/homeflix-native) - Sideloaded iPhone client with an Android TV build. `Jellyfin` · `iOS` `Android TV` · `MPL-2.0` `Free`
- [HotpotPlayer](https://github.com/WangyuHello/HotPotPlayer) - Desktop player for Jellyfin music and video plus Bilibili; HotPotPlayer2 is its Avalonia and libmpv port. `Jellyfin` · `Windows` `Linux` `Android` · `Open source` `Free` `Stale 2025` · [Source 2](https://github.com/WangyuHello/HotPotPlayer2)
- [Iridium](https://github.com/bizzanteen/iridium) - Native Jellyfin client. `Jellyfin` · `macOS` `Linux` `Android` · `Open source` `Free`
- [Jellybeam](https://github.com/packetinspector/jellybeam-macos) - Native macOS client written in Rust with GPUI and libmpv. `Jellyfin` · `macOS` `Android TV` · `GPL-3.0` `Free` · [Source](https://github.com/packetinspector/jellybeam)
- [jellyfin-client-avalonia](https://github.com/crobibero/jellyfin-client-avalonia) - Avalonia desktop Jellyfin client written by a Jellyfin core developer. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `Android TV` `Fire TV` · `GPL-3.0` `Free`
- [Jellyfish](https://github.com/Jellyfish-Client/Mobile-Desktop) - Flutter Jellyfin client with built-in Jellyseerr requests. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` · `Open source` `Free`
- [Jellyflix](https://github.com/jellyflix-app/jellyflix) - Cross-platform client for phones and desktops. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.ambark.jellyflix) · [App Store](https://apps.apple.com/us/app/jellyflix/id6476043683)
- [jellyflut](https://github.com/Thomas-Sohier/jellyflut) - Flutter Jellyfin client started as a side project. `Jellyfin` · `Windows` `Linux` `Android` `iOS` · `MIT` `Free` `Stale 2025`
- [JellyMax](https://github.com/Doulvis/JellyMax) - Jellyfin client styled after HBO Max. `Jellyfin` · `Windows` `Android` `Tizen` · `MIT` `Free`
- [Jellyplay](https://github.com/raulshma/jellyplay) - Client for Android phones, Android TV and Fire TV. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `Android TV` `Fire TV` `Android Auto` · `GPL-3.0`
- [LumaFin](https://github.com/bagodees/LumaFin-AndroidTV) - Client for Android TV, Google TV and Fire TV. Its Tizen build ended in September 2026. `Jellyfin` · `Web` `Android` `Android TV` `Fire TV` `Tizen` · `GPL-2.0` `Free` · [Source](https://github.com/bagodees/LumaFin-Android) · [Source 2](https://github.com/bagodees/lumafin-web) · [Source 3](https://github.com/bagodees/LumaFin-Tizen)
- [Lumen (Raulpergon310)](https://github.com/Raulpergon310/lumen) - Jellyfin client for Windows, Android TV and the browser. `Jellyfin` · `Windows` `Web` `Android TV` · `MIT` `Free`
- [Lumen Streaming](https://github.com/Zafery-Cosmos/lumen-streaming) - Native desktop client, with an Android build. `Jellyfin` · `Windows` `macOS` `Linux` `Android` · `GPL-3.0` `Free`
- [Mira](https://github.com/sasou-web/Mira) - Native Windows and Mac client with mpv playback; phones use its built-in web app or a sideloaded iOS build. `Jellyfin` · `Windows` `macOS` `iOS` · `MIT` `Free`
- [mitch-jelly](https://github.com/mitchelljfranklin/mitch-jelly) - Browser-based client built with Next.js. `Jellyfin` · `Windows` `macOS` `Linux` `Web` · `AGPL-3.0` `Free`
- [Pelagica](https://github.com/PelagicaApp/pelagica) - Self-hosted web client that is also packaged for TVs. `Jellyfin` · `Windows` `macOS` `Linux` `Web` `tvOS` `webOS` `Tizen` · `GPL-3.0` `Free` · [App Store](https://apps.apple.com/app/id6811079730) · [Source (Apple TV)](https://github.com/PelagicaApp/pelagica-atv) · [TestFlight](https://testflight.apple.com/join/CUsEZtDK)
- [Phyn](https://apps.apple.com/app/id6457674815) - Player for Mac, iPhone, Android and Quest. `Jellyfin` · `macOS` `Android` `iOS` `iPadOS` `Android TV` `tvOS` `Quest` · `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=com.appsynergyts.phyn) · [Meta Store](https://www.meta.com/experiences/phyn-jellyfin-media-player/8075426475891543/)
- [Premflix](https://github.com/IamThejus/PremFlix) - Flutter client for Jellyfin. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `Android TV` · `Open source` `Free`
- [Streamyfin](https://github.com/streamyfin/streamyfin) - Phone and Apple TV client with mpv playback, offline downloads and Seerr requests. `Jellyfin` · `Android` `iOS` `iPadOS` `tvOS` · `MPL-2.0` `Free` · [App Store](https://apps.apple.com/app/id6593660679) · [Google Play](https://play.google.com/store/apps/details?id=com.fredrikburmester.streamyfin)
- [Sunfin](https://github.com/sunfin-dev/sunfin) - Jellyfin client for Android TV, mobile and desktop. `Jellyfin` · `Windows` `Android` `Android TV` `Android Auto` · `GPL-2.0` `Free`
- [Switchfin](https://github.com/dragonflylee/switchfin) - Homebrew client for Switch, PS Vita and PS4. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `PS4` `PS Vita` `Switch` · `Apache-2.0` `Free` · [Flathub](https://flathub.org/apps/fun.dragonfly.switchfin)
- [Turtlefin](https://github.com/Xelopteryx/Turtlefin) - Rust thin client meant to replace Jellyfin Desktop. `Jellyfin` · `Windows` `Linux` `Android` `Android TV` · `GPL-3.0` `Free`
- [Zoggyfin](https://github.com/zog-tech/zoggyfin) - Client for iPhone, iPad, the web and Mac; Android is coming soon. `Jellyfin` · `macOS` `Web` `iOS` `iPadOS` · `MPL-2.0` `Free` · [TestFlight](https://testflight.apple.com/join/qRFABNBJ)

### Android, Android TV and HarmonyOS

- [213366/Jellyfin-Android-TV-Danmaku-](https://github.com/213366/Jellyfin-Android-TV-Danmaku-) - Android TV client fork with danmaku comments and a larger playback buffer. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [AeonTV](https://github.com/aeon01100101/aeontv) - Rebranded build of the Android client (based on 2.6.2). `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free`
- [AFinity](https://github.com/MakD/AFinity) - Android client, in beta. `Jellyfin` `+Audiobookshelf` · `Android` · `GPL-3.0` `Beta`
- [Allerix](https://github.com/AlleriaLabs/Allerix) - Branded fork built for the Alleria Filmotheque. `Jellyfin` · `Android` · `Open source` `Free`
- [Android TV Plus](https://github.com/maybe-maeb/jellyfin-androidtv-plus) - Android TV client forked from the official Jellyfin Android TV app. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [Aurorama](https://github.com/zhangwenkang-github/Aurorama) - Findroid-based client for Android phones and tablets, with an EPUB, PDF and CBZ reader. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [Blade](https://github.com/Torresmi9294/blade) - Android TV frontend styled like the Xbox 360 dashboard, also browsing a RomM game library. `Jellyfin` · `Android TV` · `Open source` `Free`
- [CinefinTV](https://github.com/rpeters1430/CinefinTV) - Android TV client for Jellyfin. `Jellyfin` · `Android TV` · `MIT` `Free` `Beta`
- [CineIsle](https://gitee.com/angeladoudou/cineisle) - HarmonyOS NEXT client with picture-in-picture, background audio, offline downloads and a PIN lock. `Jellyfin` · `HarmonyOS` · `GPL-3.0`
- [CookeInCode/jellyfin-androidtv](https://github.com/CookeInCode/jellyfin-androidtv) - Android TV client fork. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free` `Stale 2024`
- [Driftfin](https://github.com/dhrandy/Driftfin) - Google TV and Android TV client that also runs on older Fire TVs. `Jellyfin` · `Android` `Android TV` `Fire TV` · `Open source` `Free`
- [Dune Web](https://github.com/Sam42a/DUNE-WEB) - Web-based client for Android TV, from the Dune project. `Jellyfin` · `Android TV` · `GPL-2.0` `Free` `Stale 2025`
- [Elefin](https://github.com/flex36ty/elefin) - Android TV client. `Jellyfin` · `Android` `Android TV` · `Open source`
- [Ellefin](https://github.com/flex36ty/Ellefin-Jellyfin-Client-ATV) - Early alpha Android TV client. `Jellyfin` · `Android` `Android TV` · `Open source` `Free` `Beta`
- [Ephyra](https://github.com/midasvo/ephyra) - Client for Android phones, tablets and Android TV. `Jellyfin` · `Android` `Android TV` · `GPL-3.0`
- [FamilyFlix](https://github.com/sjdigitall-maker/FamilyFlix) - Customised Android TV client for a private Jellyfin server. `Jellyfin` · `Android TV` · `Open source` `Free`
- [fengymi/jellyfin-androidtv](https://github.com/fengymi/jellyfin-androidtv) - Android TV client fork. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [Findroid](https://github.com/jarnedemeulemeester/findroid) - Native Android phone and tablet client with offline downloads. `Jellyfin` · `Android` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=dev.jdtech.jellyfin) · [F-Droid](https://f-droid.org/packages/dev.jdtech.jellyfin/)
- [Finora](https://github.com/MEHDImp4/FINORA) - Android client with offline support, built with Expo. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [Firefin](https://github.com/ZepiGit/Firefin) - Native 32-bit Kotlin client for older Fire TV devices. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [firetv-jellyfin-client](https://github.com/RT993/firetv-jellyfin-client) - Lightweight client for old Fire Stick devices. `Jellyfin` · `Android TV` `Fire TV` · `Open source` `Free`
- [Fjora](https://github.com/chrisox1/Fjora) - Third-party native Android app. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [Glacier](https://github.com/Glacier-Jellyfin/glacier-androidtv) - Client for Android TV, Google TV and Fire TV. `Jellyfin` · `Android TV` `Fire TV` · `GPL-3.0` `Free` · [Amazon](https://www.amazon.com/dp/B0HPL2YVVQ)
- [GtV](https://github.com/gil81/GtV) - Android TV frontend with Live TV support. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [Jcuhfehl/findroid](https://github.com/Jcuhfehl/findroid) - Fork of the Findroid Android client. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [JE AndroidTV](https://github.com/4eh5xitv6787h645ebv/je-androidtv) - Modified Android TV client with a new interface. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [Jellow](https://github.com/sadgen/jellow) - Findroid fork. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [JellyCast-Dev](https://github.com/Jordigb44/JellyCast-Dev) - Android client forked from Findroid. `Jellyfin` · `Android` `Android TV` · `GPL-3.0` `Free` `Stale 2025`
- [JellyDroid](https://github.com/Torahlzy/JellyDroid) - Android client tuned for foldables and large screens, with metadata scraping and a Chinese translation. `Jellyfin` · `Android` · `GPL-3.0`
- [JellyDV](https://github.com/skipydg/jellydv-androidtv) - Android TV client adapted for Dolby Vision playback. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [jellyfin-android-av1-transcode](https://github.com/en6ads/jellyfin-android-av1-transcode) - Android client fork with AV1 transcoding. `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free`
- [jellyfin-android-ip4p](https://github.com/firexbox/jellyfin-android-ip4p) - Android client with built-in IP4P NAT traversal. `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free`
- [jellyfin-androidtv-danmaku](https://github.com/sp960817/jellyfin-androidtv-danmaku) - Android TV client that overlays scrolling danmaku comments on video. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [jellyfin-androidtv-ip4p](https://github.com/firexbox/jellyfin-androidtv-ip4p) - Android TV client with built-in IP4P NAT traversal. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [jellyfin-android-with-mpv](https://github.com/sukerxi/jellyfin-android-with-mpv) - Android client with mpv playback. `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free`
- [Jellyfin-Broadcast](https://github.com/NeoRed-domo/Jellyfin-Broadcast) - Lightweight Android client for TV streaming. `Jellyfin` · `Android` `Android TV` · `GPL-3.0` `Free`
- [jellyfin-cyborg](https://gitlab.com/cromefire/jellyfin-cyborg) - Work-in-progress Kotlin Android client. `Jellyfin` · `Android` · `Open source` `Stale 2020`
- [jellyfin-fire](https://github.com/Snedik/jellyfin-fire) - Fire TV build of the Jellyfin Android app with SyncPlay in the built-in player. `Jellyfin` · `Fire TV` · `GPL-2.0` `Free`
- [Jellyfin for HarmonyOS](https://gitee.com/jellyfin-new/jellyfin-harmonyos) - HarmonyOS port of the Android app: web-view based, with a native AVPlayer and downloads. `Jellyfin` · `HarmonyOS` · `GPL-2.0`
- [JellyFin_HarmonyOS](https://github.com/chashaochang/JellyFin_HarmonyOS) - HarmonyOS client. `Jellyfin` · `HarmonyOS` · `GPL-2.0` `Free` `Stale 2025`
- [JellyfinHM](https://gitee.com/yaohx/jellyfin-hm) - HarmonyOS client for films and series with picture-in-picture and tap-to-share. `Jellyfin` · `HarmonyOS` · `GPL-2.0`
- [Jellyfin KitKat](https://gitee.com/moto1717/jellyfin-kitkat) - Lightweight client for Android 4.4 boxes that direct-plays and falls back to server HLS transcoding. `Jellyfin` · `Android` · `MulanPSL-2.0`
- [jellyfin-tvbox](https://github.com/zdl1982/jellyfin-tvbox) - Client for old Android 4 TV boxes. `Jellyfin` · `Android TV` · `Open source` `Free`
- [JellyFlow](https://github.com/boberic12321/JellyFlow) - Android client. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [JellyStack](https://github.com/Darkatek7/jellystack) - Android client with built-in Seerr requests, built with Kotlin Multiplatform. `Jellyfin` · `Android` `Android TV` `Fire TV` · `GPL-3.0` `Free` · [Website](https://jellystack.org) · [Google Play](https://play.google.com/store/apps/details?id=app.jellystack.mobile)
- [jellystone-video](https://github.com/DerAustistYT/jellystone-video) - Video client for very old Android versions (1.5 and up). `Jellyfin` · `Android` · `Open source` `Free`
- [JellyTiger](https://github.com/TigerBeanst/JellyTiger) - Android client. `Jellyfin` · `Android` · `GPL-3.0` `Free` `Stale 2024`
- [Jellytip](https://github.com/ricki2828/jellytip) - TV client forked from Wholphin. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [jellyvideo-legacy](https://github.com/DerAustistYT/jellyvideo-legacy) - Video client for legacy Android 4.0.3 and later. `Jellyfin` · `Android` · `Open source` `Free`
- [K3ntas/vlc-jellyfin](https://github.com/K3ntas/vlc-jellyfin) - Android TV client with a streaming-app style interface and libVLC playback. `Jellyfin` · `Android TV` · `GPL-2.0` `Free`
- [KoalaPaw](https://www.amazon.com/Koala-Software-Ltd-KoalaPaw-JellyFin/dp/B0GZ8MSSNB) - Paid Fire TV client sold on the Amazon Appstore. `Jellyfin` · `Fire TV` · `Paid`
- [Krispy](https://github.com/crunchy-in-milk/krispy) - Independent Android TV client. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [Lowfin](https://github.com/303inmyheart/Lowfin) - Lightweight Android TV client for low-end devices. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [Lumen TV](https://github.com/nbsimmons/lumen-tv) - Fire TV and Android TV client with an Apple TV-like look and built-in Seerr requests. `Jellyfin` · `Android TV` `Fire TV` · `Open source` `Free`
- [MediaCenter-Jellyfin](https://github.com/Madmaxx636/MediaCenter-Jellyfin) - Android TV client styled after Windows 7 Media Center. `Jellyfin` · `Android TV` `Fire TV` · `GPL-3.0` `Free`
- [Mellow](https://github.com/Malinskiy/mellow) - Android client. `Jellyfin` · `Android` `Android Auto` · `Apache-2.0`
- [Mirufin](https://github.com/wjmcspirit/mirufin) - Living-room Android TV client. `Jellyfin` · `Android TV` · `Open source` `Free`
- [MPV Infinity](https://github.com/ZHINFINITY/Mpv-infinity) - Android video player with mpv and Media3 engines that plays from a Jellyfin library. `Jellyfin` · `Android` · `Open source` `Free`
- [MuseVu](https://musevu.com) - TV-first video client with phone and tablet builds. `Jellyfin` · `Android` `Android TV` `Fire TV` · `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=com.thefuturecoderx.musevu) · [Amazon](https://www.amazon.com/dp/B0HG8GPR6Z)
- [nahcon](https://github.com/Nandanrmenon/nahcon) - Android client built with Flutter. `Jellyfin` · `Android` · `MIT` `Stale 2025` · [Google Play](https://play.google.com/store/apps/details?id=com.nahnah.nahcon)
- [Nextfin](https://github.com/realcgcristi/nextfin) - Jellyfin client app. `Jellyfin` · `Android` · `Apache-2.0` `Free`
- [nightfin](https://nightfin.app) - Fire TV client with built-in Seerr requests and Dialogue Boost. `Jellyfin` · `Android` `Android TV` `Fire TV` · `Free` · [Amazon](https://www.amazon.com/dp/B0HP8B7Q3Z)
- [Novafin](https://github.com/rene-roid/novafin) - Android phone and tablet video client. `Jellyfin` · `Android` · `MIT` `Free`
- [NovaX Player](https://github.com/liuyouwu1999/NovaX-Player) - Android player for SMB, SFTP, WebDAV and Jellyfin sources. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [Orca X](https://github.com/jkrishna289/OrcaX) - TV-first Android client built on Wholphin. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [Pakflix](https://github.com/sudoaanish/pakflix) - Android TV and Fire TV client. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [Pathfin](https://github.com/li88iioo/Pathfin) - Android client with MediaFlux STRM support. `Jellyfin` · `Android` · `Open source` `Free`
- [Picnic Player](https://github.com/YogiBear12/Picnic-Player) - Native Android TV client. `Jellyfin` · `Android TV` · `GPL-3.0` `Free`
- [Quallenkino](https://github.com/DrdotHouse2106/Jellyfin-TV-Client) - Android TV and Fire TV app. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free`
- [Reefin](https://play.google.com/store/apps/details?id=com.shady.reefin) - Client for Android phones and Android TV. `Jellyfin` · `Android` `Android TV`
- [Sanctumd](https://github.com/Phioster/sanctum_daemon) - Android app that runs a self-hosted media and *arr stack on the device, with a client. `Jellyfin` · `Android` `Android TV` · `GPL-3.0`
- [ShivPatel123/jellyfin-androidtv](https://github.com/ShivPatel123/jellyfin-androidtv) - Android TV client with an overhauled interface. `Jellyfin` · `Android TV` · `GPL-2.0` `Free` `Stale 2025`
- [SloppaTV](https://github.com/brandonp2412/sloppaTV) - Android TV client written in native C++. `Jellyfin` · `Android TV` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=app.sloppatv)
- [Spice](https://github.com/everettpenne/Spice) - Android client with a translucent liquid-glass interface. `Jellyfin` · `Android` · `MIT` `Free`
- [Streamix](https://github.com/nischalsir/Streamix) - Google TV and Android TV client. `Jellyfin` · `Android` `Android TV` `Android Auto` · `GPL-2.0` `Free`
- [Tally](https://github.com/Scdouglas1999/Tally) - Android TV app with live sports and watch parties, forked from Wholphin. `Jellyfin` · `Android` `Android TV` `Fire TV` `webOS` `Tizen` · `GPL-2.0` `Free`
- [VdC TV](https://github.com/Tvdc1998/vdc-tv) - Android client based on Findroid. `Jellyfin` · `Android` `Android TV` · `GPL-3.0` `Free`
- [Void](https://github.com/hritwikjohri/Void-for-jellyfin) - Client for Android phones and Android TV. `Jellyfin` · `Android` `Android TV` · `GPL-3.0`
- [VoidTV for Jellyfin](https://github.com/hritwikjohri/VoidTV-for-jellyfin) - Android TV client with ExoPlayer and mpv playback engines. `Jellyfin` · `Android TV` `Fire TV` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.hritwik.avoid)
- [Wholphin](https://github.com/damontecres/Wholphin) - Android TV client with a Plex-style interface and a choice of playback engines. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.github.damontecres.wholphin) · [Amazon](https://www.amazon.com/dp/B0G8RQQR9T)
- [Wholphin-webOS](https://github.com/JoeKer1/Wholphin-webOS) - Ember: LG webOS, Samsung Tizen and Fire TV client inspired by the Wholphin Android TV app. `Jellyfin` · `Fire TV` `webOS` `Tizen` · `GPL-2.0` `Free`
- [Xfin](https://github.com/JustDr00py/xFIN) - Android TV and phone client with Live TV. `Jellyfin` · `Android` `Android TV` `Fire TV` · `Open source` `Free`
- [Zerifin](https://github.com/sommepo/zerifin) - Android client fork with Japanese subtitle lookup and Anki card mining. `Jellyfin` · `Android` `Android Auto` · `GPL-2.0` `Free`

### Apple platforms

- [AQ13R 7V](https://apps.apple.com/us/app/aq13r-7v/id6776027539) - Social TV app with channels of posts plus playback of a connected server library. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Aquarium Media](https://apps.apple.com/us/app/aquarium-media/id6799581721) - Jellyfin app for films, shows, music, audiobooks and Live TV with Quick Connect and server discovery. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Free`
- [Arcfin](https://arcfin.psmattas.com) - Native client with direct play, AirPlay, Chromecast, PiP, downloads and Face ID/PIN profiles. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Free` `Beta` · [TestFlight](https://testflight.apple.com/join/kkC58n2w)
- [Bearfin](https://apps.apple.com/us/app/bearfin/id6817142267) - Client for a self-hosted library that plays your own pre-roll intro clips before movies. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Bloom Cinema](https://apps.apple.com/hk/app/bloom-cinema/id6820236256) - Streaming-style home screen with Continue Watching and live TV for a self-hosted library. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [Caviar Media Client](https://apps.apple.com/us/app/caviar-media-client/id6805609607) - Jellyfin client for browsing libraries and resuming playback, with Seerr request management. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Free`
- [Cinefin](https://apps.apple.com/hk/app/cinefin/id6824275546) - iPhone Jellyfin player with Continue Watching, Next Up and intro and recap skipping. `Jellyfin` · `iOS` · `Free`
- [Convolution](https://github.com/illixion/Convolution) - Spatial media app for Vision Pro, iPhone, iPad, Apple TV and Mac. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Open source` `Free`
- [Cue](https://craigosborne.com/cue/) - Media player for a personal library with resume and offline favourites. `Jellyfin` · `iOS` `iPadOS` · `Freemium` · [App Store](https://apps.apple.com/de/app/cue-media-player/id6798327106) · [TestFlight](https://testflight.apple.com/join/et6EFShU)
- [Dee Jellie](https://www.deejellie.com) - Jellyfin app for movies, shows and lossless music with synced lyrics, 4K HDR and offline downloads. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Paid` · [App Store](https://apps.apple.com/us/app/dee-jellie-jellyfin-media/id6755585736)
- [Ensō](https://testflight.apple.com/join/6GZBrj1t) - Native client with an Apple Watch companion app. `Jellyfin` · `iOS` `iPadOS` `tvOS` `watchOS` · `Beta`
- [FinFlix](https://apps.apple.com/de/app/finflix/id6756268520) - Native client to browse, stream and download a personal movie and TV library. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [FinPlus](https://apps.apple.com/gb/app/finplus/id6757364763) - Companion app for browsing, streaming and watching live TV from a personal library, built for iOS and tvOS. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Paid`
- [FinStream](https://github.com/SilverMarcs/SwiftJelly) - SwiftUI client for Apple devices. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `MIT` `Free` · [App Store](https://apps.apple.com/app/id6761840798)
- [Jelly](https://apps.apple.com/de/app/jelly/id6826379119) - Player that direct-plays files at original quality with no server transcoding, plus PiP and AirPlay. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Subscription`
- [Jellyboxd](https://github.com/matthewhalf/jellyboxd) - iPhone client. `Jellyfin` · `iOS` · `GPL-3.0` `Free` · [App Store](https://apps.apple.com/app/id6816114676)
- [jellyboy](https://apps.apple.com/us/app/jellyboy/id6802162329) - Small independent Jellyfin client for movies, shows, music and Live TV that tries on-device playback first. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free` · [Source](https://github.com/therealparmesh/jellyboy)
- [JellyCinema](https://apps.apple.com/de/app/jellycinema/id6809860686) - iPad client with artwork and resume positions; one purchase also covers the Apple TV app. `Jellyfin` · `iPadOS` `tvOS` · `Paid`
- [Jellyfin & SMB Video Player](https://apps.apple.com/us/app/jellyfin-smb-video-player/id6784719986) - Apple TV video player for Jellyfin servers and SMB shares with native HDR10 playback. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Paid`
- [JellyGlass for Jellyfin](https://apps.apple.com/us/app/jellyglass-for-jellyfin/id6769321512) - Jellyfin client with a dark, glass-style interface and editorial layouts. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free` · [App Store (tvOS)](https://apps.apple.com/us/app/jellyglass-tv-for-jellyfin/id6769321723)
- [JellyGo](https://apps.apple.com/us/app/jellygo-jellyfin-client/id6760751654) - iOS Jellyfin client with Continue Watching and Next Up and a choice of two playback engines. `Jellyfin` · `iOS` · `Free`
- [JellyGoose](https://apps.apple.com/us/app/jellygoose/id6814667375) - Jellyfin player that finds servers on the network and leads with a resume-first, poster-driven home. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Paid`
- [JellyKids](https://apps.apple.com/us/app/jellykids/id6756038036) - Kid-friendly Jellyfin client with a playful interface and content controls for parents. `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [JellyMold](https://jellymold.app/) - Client with its own playback engine so files play directly and are never transcoded. `Jellyfin` · `iOS` `iPadOS` · `Subscription` · [App Store](https://apps.apple.com/us/app/jellymold/id6813179451)
- [JellySee](https://apps.apple.com/app/id6748783768) - Paid Apple TV client. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Paid`
- [Jelly Shark](https://github.com/axeslasher/Jelly-Shark) - Apple TV and Vision Pro client. `Jellyfin` · `tvOS` `visionOS` · `MIT` `Free`
- [JellyStreamz](https://apps.apple.com/tr/app/jellystreamz-jellyfin-client/id6795484066) - Native Apple TV video client. `Jellyfin` · `tvOS` · `Free`
- [JellyTV](https://apps.apple.com/app/id6752357290) - Video client for Apple devices. `Jellyfin` · `iOS` `iPadOS` `tvOS` `watchOS` · `Freemium`
- [Jelly TV (Logan Janssen)](https://apps.apple.com/hk/app/jelly-tv/id6795124030) - Private client to browse, resume and download movies and episodes for offline viewing. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [JellyZaping](https://apps.apple.com/us/app/jellyzaping/id6757639322) - iOS client with a TikTok-style Zapping Timeline for finding what to watch next. `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [JustPlay Media](https://apps.apple.com/us/app/justplay-media/id6761976412) - Lightweight iPhone client for browsing and direct-playing a library through a VLC engine, with 360 VR. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Kid Player](https://apps.apple.com/de/app/kid-player-videos-games/id6761115557) - Kid-friendly iPad player for a home library, bundled with 27 educational mini-games. `Jellyfin` · `iPadOS` · `Free`
- [Kinema](https://github.com/evropiani/Kinema) - iOS client. `Jellyfin` · `iOS` `iPadOS` · `Apache-2.0` `Free`
- [Kotatsu for Jellyfin](https://apps.apple.com/us/app/kotatsu-for-jellyfin/id6794677229) - Jellyfin client with Continue Watching, Next Up and profile switching, laid out per screen. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [Leaf Player](https://apps.apple.com/us/app/leaf-player/id6779445510) - Ad-free audio and video player with offline playback and access to several sources. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [LiquidFin](https://apps.apple.com/app/id6755673532) - Apple-platform client covering video, music, audiobooks, Live TV and server admin. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` `watchOS` · `Freemium`
- [Lunafin](https://apps.apple.com/us/app/lunafin-movie-tv-player/id6824120703) - Jellyfin player for films, shows, music and audiobooks with a Watchlist, 4K HDR and Dolby Vision. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Manta](https://apps.apple.com/hk/app/manta-made-for-your-media/id6762310760) - Streaming-service-style client for a personal library with a clean interface. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [MediaRoam](https://apps.apple.com/tw/app/mediaroam/id6804534300) - Video player for NAS and cloud files that also previews documents and 3D models, with an Apple TV edition. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [Mediora](https://github.com/ghobs91/mediora) - Apple TV client with Sonarr and Radarr requests built in. `Jellyfin` · `tvOS` · `Open source` `Free` · [App Store](https://apps.apple.com/app/id6757345487)
- [Medusa](https://apps.apple.com/us/app/medusa-jellyfin-client/id6808727618) - Client whose home opens on Continue Watching, with shelves for series and favourites. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Mercury Player](https://apps.apple.com/hk/app/mercury-player/id6811932858) - Client for browsing and playing a whole movie and TV library in a minimal interface. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [NaviFin](https://apps.apple.com/us/app/navifin-jellyfin-player/id6778781788) - Video-first Jellyfin client with a hybrid AVPlayer and VLC engine, built separately for each Apple device. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Paid`
- [Neptune](https://neptuneplayer.com/) - Swift client designed only for Apple devices, with TestFlight codes handed out on Discord. `Jellyfin` · `tvOS` · `Free` `Beta` · [App Store](https://apps.apple.com/app/id6756797773) · [Info](https://discord.com/invite/6mm7YqvjW)
- [NGXSP Vidéo](https://apps.apple.com/fr/app/ngxsp-vid%C3%A9o/id6814944036) - Video player for local files, the photo library and Jellyfin, WebDAV and DLNA servers, with no account needed. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Ninefin](https://github.com/LukeLeFox/NineFin) - Client for devices running iOS 9. `Jellyfin` · `iOS` · `MIT` `Free`
- [Parallax](https://apps.apple.com/br/app/parallax-media-player/id6796474963) - Jellyfin player for multiple servers and SMB shares, written in Swift and SwiftUI. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Paid` · [Source](https://github.com/eutialia/Parallax)
- [Plankton](https://github.com/schembora/plankton) - Native Swift iPhone client using libmpv. `Jellyfin` · `iOS` `iPadOS` · `Apache-2.0` `Free`
- [Playfyn](https://apps.apple.com/hk/app/playfyn/id6790173778) - Client for a self-hosted library with 4K HDR10 and Dolby Vision passthrough on iPhone, iPad and Apple TV. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Plinthio](https://apps.apple.com/us/app/plinthio-media-viewer/id6821776680) - Media viewer for movies, shows, anime, manga, comics, books and audiobooks from a self-hosted server. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free`
- [Pocket Cinema](https://apps.apple.com/us/app/pocket-cinema-jellyfin-webdav/id6768525682) - libmpv-based video player for a library and WebDAV folders, tuned for phone playback. `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [Prowlogue](https://github.com/prowlogue/prowlogue) - Native Apple TV client with plugin support. `Jellyfin` · `tvOS` · `MPL-2.0` `Beta`
- [ReclineTV](https://apps.apple.com/us/app/reclinetv/id6820317648) - Video player that combines a Jellyfin library, M3U playlists, IPTV subscriptions and free public channels. `Jellyfin` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [Reefy](https://github.com/jmhunter83/reefy) - Paid Apple TV client using the VLC playback engine. `Jellyfin` · `tvOS` · `MPL-2.0` `Paid`
- [ReelFin](https://apps.apple.com/app/id6762079357) - Client for iPhone and Apple TV. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Rigel](https://github.com/hikaps/Rigel) - iOS player for HTTP streams, local files, Jellyfin and DLNA casting. `Jellyfin` · `iOS` · `GPL-3.0` `Free`
- [Serafin for Jellyfin](https://apps.apple.com/hk/app/serafin-for-jellyfin/id6818960899) - Native iPhone and iPad client with Continue Watching and Next Up for a personal library. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Sleeve Player](https://testflight.apple.com/join/k9MpTM4t) - iPhone, iPad and Mac app that mixes a personal media server with addons you choose. `Jellyfin` `+Stremio addons` · `macOS` `iOS` `iPadOS` · `Beta`
- [Sodalite](https://apps.apple.com/us/app/sodalite/id6764418563) - Jellyfin player with Live TV and Seerr requests, direct play for wide codec support and HDR. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free` · [Source](https://github.com/superuser404notfound/Sodalite) · [TestFlight](https://testflight.apple.com/join/nWeQzmBX)
- [Sparklux Go](https://apps.apple.com/tw/app/sparklux-go/id6815096233) - Video player that upscales and adds HDR brightness to SDR video from NAS shares, Jellyfin and DLNA. `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [StarPlay](https://apps.apple.com/br/app/starplay/id6806145078) - Plays video and music in place from chosen folders, the photo library, SMB, WebDAV and Jellyfin without importing. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Stingray](https://github.com/benjaminRoberts01375/Stingray) - Apple TV client for tvOS 18 and later. `Jellyfin` · `tvOS` · `MIT` `Freemium` · [App Store](https://apps.apple.com/app/id6756280505) · [TestFlight](https://testflight.apple.com/join/GSgjYB22)
- [Sunkfin](https://apps.apple.com/app/id6743207349) - iPhone client that saves content for offline viewing. `Jellyfin` · `iOS` `iPadOS`
- [swiftfin-home](https://github.com/Zelanh/swiftfin-home) - Swiftfin fork that adds Chromecast casting. `Jellyfin` · `iOS` · `MPL-2.0` `Free`
- [SwiftTube](https://testflight.apple.com/join/NQ9N7KbA) - iOS client for YouTube archives from Jellyfin and Tube Archivist, with PiP and background audio. `Jellyfin` · `iOS` · `Beta`
- [Tomo TV](https://github.com/keiver/tomotv) - Client for Apple TV, iPad, iPhone and Mac. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `MIT` · [App Store](https://apps.apple.com/app/id6755077888)
- [TVApp](https://apps.apple.com/us/app/tvapp-home-media-player/id6788813078) - VLC-powered Jellyfin and direct-file player that direct-plays most formats without transcoding. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Velo](https://apps.apple.com/us/app/velo-media-hub/id6749046147) - Apple TV media hub that plays Jellyfin and Stremio libraries and suggests what to watch next. `Jellyfin` `+Stremio addons` · `tvOS` · `Free`
- [xfinn](https://apps.apple.com/us/app/xfinn/id6757672232) - Native client for movies, shows and music with Apple's player, Picture in Picture and AirPlay. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [xPlay (Diamantina Saada)](https://apps.apple.com/us/app/xplay/id6757906889) - iPhone Jellyfin client with Quick Connect and resume that syncs progress with the server. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`
- [Zoeyflix](https://apps.apple.com/us/app/zoeyflix/id6757206770) - Client for streaming and downloading shows and movies for offline viewing, with MKV and Opus support. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [家映](https://apps.apple.com/tw/app/%E5%AE%B6%E6%98%A0/id6808049912) - Home NAS photo and video browser with a year-and-month timeline and playback of a Jellyfin library. `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Free`

### Desktop

- [Arc](https://github.com/Fareszaghloul/arc-player) - Desktop Jellyfin client with a minimal interface, forked from Jellyfin Desktop. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-2.0` `Free`
- [Blink](https://github.com/prayag17/Blink) - Desktop client built with Tauri, in alpha. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Beta`
- [Bloom](https://github.com/crowquillx/Bloom) - Couch-friendly HTPC client built with Qt 6 and mpv. `Jellyfin` · `Windows` `Linux` · `MIT` `Free`
- [bloom (dantech2000)](https://github.com/dantech2000/bloom) - Native macOS client written in Rust with GPUI and libmpv. `Jellyfin` · `macOS` · `AGPL-3.0` `Free`
- [Bobine](https://github.com/KristenJestin/bobine) - Native Linux film and series client written in Rust. `Jellyfin` · `Linux` · `AGPL-3.0` `Free`
- [Butter and Jelly](https://github.com/MrMilenko/ButterAndJelly) - App for classic game consoles. `Jellyfin` · `macOS` `Xbox 360` `Original Xbox` `Wii U` · `GPL-2.0` `Free`
- [Callephiin](https://github.com/callephi/callephiin) - Rust desktop client for Jellyfin. `Jellyfin` · `Windows` `macOS` · `GPL-3.0` `Free`
- [ctismer/jellyfin-desktop-qt](https://github.com/ctismer/jellyfin-desktop-qt) - Fork of the Qt desktop client, rebuilt for Intel Macs on macOS 12. `Jellyfin` · `macOS` · `GPL-2.0` `Free`
- [Delfin](https://codeberg.org/avery42/delfin) - Native Linux desktop client. `Jellyfin` · `Linux` · `Open source` · [Flathub](https://flathub.org/apps/cafe.avery.Delfin)
- [ExoCinema](https://github.com/UhhErix/ExoCinema) - Windows 11 client with a native mpv player. `Jellyfin` · `Windows` · `Open source` `Free`
- [Finplay](https://github.com/kings431/finplay) - Desktop Jellyfin client that plays through mpv. `Jellyfin` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [Fjord](https://github.com/KalasKonrad/Fjord) - Rust and Slint front end for Jellyfin. `Jellyfin` · `Linux` · `GPL-3.0` `Free`
- [FluentFin](https://github.com/insomniachi/FluentFin) - Native Windows desktop client. `Jellyfin` · `Windows` · `GPL-3.0`
- [Gelata](https://gitlab.com/bscubed/gelata) - GTK4/libadwaita desktop client written in Rust. `Jellyfin` · `Linux` · `GPL-3.0` `Stale 2025` · [AUR](https://aur.archlinux.org/packages/gelata-git)
- [Jellium Desktop](https://github.com/andrewrabert/jellium-desktop) - Desktop client built on CEF and mpv by the author of the Jellyfin Desktop rewrite. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-2.0` `Beta` · [AUR](https://aur.archlinux.org/packages/jellium-desktop-git)
- [JellyClient](https://github.com/LordLoras/JellyClient) - Hisense VIDAA TV app with a Windows build. `Jellyfin` · `Windows` `VIDAA` · `GPL-3.0` `Free`
- [jellyfin-client-uwp](https://github.com/ujvarigergo1/jellyfin-client-uwp) - UWP client for Windows and Xbox. `Jellyfin` · `Windows` `Xbox` · `Open source` `Free` `Stale 2024`
- [Jellyfin Connect](https://github.com/feddyplays/Jellyfin-Connect) - Electron desktop app for Jellyfin. `Jellyfin` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [jellyfin-desktop-pip](https://github.com/aemarzouk/jellyfin-desktop-pip) - Desktop client fork with picture-in-picture. `Jellyfin` · `Windows` `macOS` · `GPL-2.0` `Free`
- [jellyfin-desktop-qt](https://codeberg.org/achill/jellyfin-desktop-qt) - Continued fork of the Qt WebEngine and libmpv Jellyfin Desktop, focused on maintainability. `Jellyfin` · `Windows` `macOS` `Linux` · `Open source`
- [jellyfin-kattri](https://github.com/Archerkattri/jellyfin-kattri) - Rust egui desktop client that plays through libmpv. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [jellyfin-random-macos-screensaver](https://github.com/ndom91/jellyfin-random-macos-screensaver) - macOS screensaver that plays a random item from your library. `Jellyfin` · `macOS` · `MIT`
- [Jellyfin.UWP](https://github.com/senbeiwabaka/Jellyfin.UWP) - UWP app for Windows and Xbox. `Jellyfin` · `Windows` `Xbox` · `GPL-2.0` `Free`
- [Jellyflex](https://github.com/RED0XI/Jellyflex) - Windows and macOS client built with Flutter and mpv. `Jellyfin` · `Windows` `macOS` · `GPL-3.0` `Free`
- [JellyJelly](https://github.com/MatzeKitt/jellyjelly-app) - macOS client built around a library of YouTube videos. `Jellyfin` · `macOS` · `Open source` `Free`
- [JellyOne](https://github.com/mgautam07/jellyone) - Standalone desktop app for streaming media from a Jellyfin server. `Jellyfin` · `Windows` `macOS` `Linux` · `BSD-4-Clause` `Free` `Stale 2025`
- [JellyPot](https://github.com/Dongz9870/jellypot) - Windows 11 client that plays through PotPlayer. `Jellyfin` · `Windows` · `Open source` `Free`
- [JellyStation](https://github.com/dconair/jellystation) - Desktop media hub styled after the PS3 XrossMediaBar, built with Tauri. `Jellyfin` · `Windows` `macOS` · `Apache-2.0` `Free`
- [JellyTauri](https://github.com/dan-online/jellytauri) - Tauri-based desktop client for Jellyfin. `Jellyfin` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [JellyUI](https://github.com/iamd3vil/jellyui) - Native desktop client built with GPUI and libmpv. `Jellyfin` · `macOS` `Linux` · `AGPL-3.0` `Free`
- [Jelly Video App](https://github.com/Stannnnn/jelly-video-app) - Lightweight video interface for Jellyfin. `Jellyfin` · `Windows` · `MIT` `Free`
- [JellyWin32](https://github.com/Aspenini/jellywin32) - Very slim native Win32 client. `Jellyfin` · `Windows` · `Open source` `Free`
- [jlfine](https://github.com/prietus/jlfine) - Native Rust/Slint desktop client on libmpv, aimed at bit-perfect audio and HDR/Dolby Vision video. `Jellyfin` · `macOS` `Linux` · `MIT` `Beta` · [AUR](https://aur.archlinux.org/packages/jlfine-bin)
- [Lightweaver](https://github.com/oss96/LightWeaver-Windows) - WPF shell around an embedded mpv player. `Jellyfin` · `Windows` · `Open source` `Free`
- [LogVar Media Player](https://github.com/1140936435/logvar-player) - Desktop player for Jellyfin and local files with a danmaku comment overlay. `Jellyfin` · `Windows` · `Open source` `Free`
- [Lumen](https://github.com/Zupermini09/Lumen) - Native Jellyfin desktop client. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Luminary](https://github.com/portwhy/Luminary) - Native desktop Jellyfin player. `Jellyfin` · `macOS` · `GPL-3.0` `Free`
- [Matinee (kernastra)](https://github.com/kernastra/matinee) - Tauri and React desktop client for Jellyfin. `Jellyfin` · `Linux` · `MIT` `Free`
- [Minimal Fin](https://github.com/CodingFries/minimal_fin) - Minimal desktop Jellyfin client laid out for wide OLED monitors. `Jellyfin` · `Windows` · `GPL-3.0` `Free` `Stale 2025`
- [Noktus](https://github.com/jessielw/Noktus) - Thin desktop client that offers both web-based and mpv playback. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Nova Player](https://github.com/Bryson-he/nova-player) - Player for Windows. `Jellyfin` · `Windows` · `MIT` `Free`
- [OwnJelly](https://github.com/gustavomgama/ownjelly) - Desktop Jellyfin client. `Jellyfin` · `Windows` `Linux` · `GPL-3.0` `Free`
- [Sukiflix](https://github.com/sukrasuki/Sukiflix) - Personal desktop Jellyfin client. `Jellyfin` · `Windows` · `Open source` `Free`
- [Tabbyfin](https://github.com/lgpy/tabbyfin) - Rust egui desktop client that plays through mpv. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [tbis](https://github.com/mahi160/tbis) - Native macOS Jellyfin client built with GPUI and embedded mpv. `Jellyfin` · `macOS` · `GPL-3.0` `Free`
- [Tellyfin](https://github.com/ILikeTeaALot/Tellyfin) - Big-screen mpv-based player with gamepad and keyboard navigation in a console-style menu. `Jellyfin` · `Windows` · `Open source` `Free` `Stale 2025`
- [Terminus Player](https://github.com/Terminus-Media/jellyfin-media-player) - Desktop player forked from Jellyfin Media Player. `Jellyfin` · `Windows` `macOS` · `GPL-2.0` `Stale 2024`
- [tsukimi](https://github.com/tsukinaha/tsukimi) - Native GTK4 Linux client. `Jellyfin` · `Linux` · `GPL-3.0` · [Flathub](https://flathub.org/apps/moe.tsuna.tsukimi) · [AUR](https://aur.archlinux.org/packages/tsukimi-bin)
- [Tubefin](https://github.com/doromiert/tubefin) - GTK 4 client that combines YouTube and Jellyfin. `Jellyfin` · `Linux` · `Open source` `Free`
- [WonderFlix](https://github.com/davidesidoti/wonderflix) - Windows client. `Jellyfin` · `Windows` · `GPL-3.0` `Free`

### Web

- [Aperture](https://github.com/akhilmulpurii/aperture) - Alternative self-hosted web client. `Jellyfin` · `Web` · `MIT`
- [Apollo](https://github.com/DPilat-Dev/Apollo) - Netflix-style Jellyfin web client. `Jellyfin` · `Web` · `MIT` `Free`
- [Finetic](https://github.com/AyaanZaveri/finetic) - Web client. `Jellyfin` · `Web` · `GPL-3.0`
- [Jellix](https://github.com/doihaveto/jellix) - Netflix-style web client with daily picks. `Jellyfin` · `Web` · `Open source`
- [JellyDinosaur](https://github.com/Olsro/jellydinosaur) - Tiny Jellyfin front end under 100 kB. `Jellyfin` · `Web` · `MIT` `Free`
- [Jellyfied](https://github.com/CharlieGolfX/jellyfied) - Jellyfin web front end. `Jellyfin` · `Web` · `GPL-3.0` `Free`
- [Jellyfin-360VR-Player](https://github.com/Mix1C/Jellyfin-360VR-Player) - 360-degree VR video player. `Jellyfin` · `Web` · `GPL-2.0` `Free`
- [jellyfin-vr-player](https://github.com/biliksir95-blip/jellyfin-vr-player) - WebXR player for watching the library in a VR headset browser. `Jellyfin` · `Web` · `GPL-3.0`
- [Jellyfin-vr-plugin](https://github.com/Lqlsoftware/Jellyfin-vr-plugin) - VR playback plugin. `Jellyfin` · `Web` · `Open source`
- [jellyfin-web-client](https://github.com/ubarman262/jellyfin-web-client) - Alternative Jellyfin web client. `Jellyfin` · `Web` · `Open source` `Free` `Beta`
- [jellyfin-web-unstable](https://github.com/soultaco83/jellyfin-web-unstable) - Fork of the web client tracking the unstable branch. `Jellyfin` · `Web` · `GPL-2.0` `Free`
- [jellykids (philips)](https://github.com/philips/jellykids) - Text-only Jellyfin front end for kids. `Jellyfin` · `Web` · `Open source` `Free` `Stale 2025`
- [JellyTube](https://github.com/nilesjarvis/jellytube) - YouTube-style Jellyfin web client built with Svelte. `Jellyfin` · `Web` · `Open source` `Free`
- [JellyWatchParty](https://github.com/TIGamingTV/JellyWatchParty) - Watch-party tool for synchronised Jellyfin playback. `Jellyfin` · `Web` · `MIT` `Free`
- [Lalea](https://lalea.app) - Browser player for language learning with dual subtitles (original plus translation). `Jellyfin` · `Web`
- [OpenWatchParty](https://github.com/mhbxyz/OpenWatchParty) - Watch-party tool for synchronised Jellyfin playback. `Jellyfin` · `Web` · `MIT` `Free`
- [P-fin](https://github.com/varunaditya-plus/P-Fin) - Jellyfin web client in the P-Stream interface style. `Jellyfin` · `Web` · `MIT` `Free`
- [Reiverr](https://github.com/aleksilassila/reiverr) - Web and TV interface combining TMDB discovery, Sonarr/Radarr management and playback via a server plugin. `Jellyfin` · `Web` `Tizen` · `AGPL-3.0`
- [ScreenHarbour](https://github.com/jampez77/ScreenHarbour) - Cinematic Jellyfin web interface. `Jellyfin` · `Web` · `MIT` `Free`
- [Vanta](https://github.com/SlowlyTz/Vanta) - Self-hosted web client with its own player, watch parties and a TV mode. `Jellyfin` · `Web` · `Open source` `Free`

## Plex video clients

Third-party video and general clients for Plex only.

### Cross-platform

- [bufferzone](https://github.com/dkrb56/bufferzone) - Plain Plex player originally made for a friend's server. `Plex` · `Windows` `Android TV` `webOS` · `MIT` `Free`
- [comPlex](https://github.com/Orochimarufan/comPlex) - Experimental desktop Plex client from 2015. `Plex` · `Linux` `Fire TV` · `Open source` `Free` `Stale 2015` · [Amazon](https://www.amazon.com/hz/mas/detail?ie=UTF8&ASIN=B0CY43YY8K&asin=B0CY43YY8K)
- [Flixor](https://github.com/Flixorui/flixor) - Client for the web, Mac, iPhone and Android. `Plex` · `macOS` `Web` `Android` `iOS` `tvOS` · `Open source` `Free`
- [home-cinema](https://github.com/imrasalghul/home-cinema) - Self-hosted web front end for Plex films and shows, with music, YouTube and live TV. `Plex` `+Subsonic` `+IPTV` · `Web` `Android TV` · `MIT` `Free`
- [MooVie](https://github.com/JibayMcs/MooVie) - Android TV and desktop app that combines Plex, Stremio and streaming sites. `Plex` `+Stremio addons` · `Windows` `macOS` `Linux` `Android` `iOS` `Android TV` · `Open source` `Free`
- [Nevu](https://github.com/Ipmake/NevuForPlex) - Redesigned web interface for Plex built on the Plex Media Server API. `Plex` · `Web` `Android` `Android TV` · `GPL-3.0` `Free`
- [Poptonium for Plex](https://apps.apple.com/us/app/poptonium-for-plex/id6779742766) - Lightweight Plex client with Google Cast, broad codec support and owner-customised layouts and ratings. `Plex` · `Android` `iOS` `iPadOS` · `Free` · [Google Play](https://play.google.com/store/apps/details?id=games.benja.poptonium)

### Android, Android TV and HarmonyOS

- [Amplify](https://github.com/brdunn/Amplify) - Android frontend for Plex Media Server. `Plex` · `Android` · `GPL-3.0` `Free` `Stale 2024`
- [Android-TV-VHS-Video-Player](https://github.com/tonypeters/Android-TV-VHS-Video-Player) - Android TV Plex player with a VHS-style look. `Plex` · `Android TV` · `Apache-2.0` `Free`
- [Dooplex](https://github.com/jackra1n/Dooplex) - Client for Zidoo players that hands playback to the native player. `Plex` · `Android TV` · `GPL-3.0`
- [FreePlexity](https://github.com/crucifix86/freeplexity) - Android TV client. `Plex` · `Android TV` · `Open source`
- [MyPlexPlayer](https://github.com/biskyt/MyPlexPlayer) - Client for Android TV, Fire TV and phones. `Plex` · `Android` `Android TV` `Fire TV` · `GPL-3.0`
- [PlexiPlay](https://github.com/Kahenis/plexiplay) - Closed-source Android TV Plex player distributed as an APK. `Plex` · `Android` `Android TV` · `Free` · [Source](https://github.com/Kahenis/plexiplay-android)
- [PowerPlay](https://github.com/The-Power-0/PowerPlay) - Plezy-derived Plex player for Fire TV sticks, with Home Assistant deep links. `Plex` · `Fire TV` · `GPL-3.0` `Free`
- [Reelay](https://github.com/Midge-dev/reelay) - Android TV client. `Plex` · `Android TV` · `Open source`
- [UniPlex](https://github.com/altera11y/UniPlex) - Android TV Plex client that merges libraries from several servers. `Plex` · `Android TV` · `Open source` `Free`

### Apple platforms

- [2ButtonPlex](https://apps.apple.com/us/app/2buttonplex/id6824610997) - Accessibility-minded player for downloaded Plex videos, with a tap grid and two-button scanning. `Plex` · `iOS` `iPadOS` · `Free`
- [AnalogTV for TV](https://apps.apple.com/app/id6792310052) - Apple TV app that plays your library through a simulated analog TV with a Teletext interface. `Plex` · `tvOS` · `Paid`
- [Arth Media Center](https://forums.plex.tv/t/looking-for-testers-building-a-native-ios-client-for-plex/942705) - Native iOS video client. `Plex` · `iOS` · `Beta`
- [Canopy for Plex](https://canopykids.app/) - Family-friendly client with big controls that limits what each viewer can browse. `Plex` · `iOS` `iPadOS` `tvOS` · `Paid` · [App Store](https://apps.apple.com/us/app/canopy-for-plex/id6759919978)
- [Crucible for Plex](https://apps.apple.com/us/app/crucible-for-plex/id6822066419) - Plex client with a resume-first home, the system player and native menus. `Plex` · `iOS` `iPadOS` `tvOS` · `Freemium` · [Source](https://github.com/guitaripod/Crucible)
- [Cue for Plex](https://apps.apple.com/us/app/cue-for-plex/id6822878172) - iPhone and iPad client. `Plex` · `iOS` `iPadOS`
- [Dusk for Plex](https://github.com/marvinvr/dusk-player) - Native Apple video client. `Plex` · `macOS` `iOS` `iPadOS` `tvOS` · `MIT` `Free` · [App Store](https://apps.apple.com/us/app/dusk-for-plex/id6760492635)
- [FluxPlay](https://apps.apple.com/br/app/fluxplay/id6759933301) - mpv-based client with detailed subtitle controls and spatial audio on AirPods. `Plex` · `iOS` `iPadOS` · `Free`
- [Home Video Club](https://apps.apple.com/us/app/home-video-club/id6755478406) - Front end that turns a personal library into a household video store with shelves, staff picks and profiles. `Plex` · `iOS` `iPadOS` · `Free`
- [Interteno](https://apps.apple.com/us/app/interteno/id6787506017) - Plex client that pairs video playback with the Plexamp music engine, a Watch app and widgets. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Paid` · [Source](https://github.com/Sproglet/Interteno) · [TestFlight](https://testflight.apple.com/join/4dQa8bMH)
- [Lumen (kdorsey0718)](https://testflight.apple.com/join/1jQWwJQk) - Apple TV client with pre-rolls, theme music, profiles, PiP and remux playback. `Plex` · `tvOS` · `Beta` · [Info](https://www.reddit.com/r/appletv/comments/1xbc5i3/lumen_a_new_marquee_plex_client_for_tvos_is_now/)
- [Marquee](https://apps.apple.com/de/app/marquee-by-reneos/id6818315662) - Player with big artwork shelves, its own video engine for MKV and HDR, Top Shelf and Home profiles. `Plex` · `iOS` `iPadOS` `tvOS` · `Free`
- [Marquee (chadMueller)](https://testflight.apple.com/join/ETZgmCka) - Apple TV app for movies and shows only, with no Live TV or Discover. `Plex` · `tvOS` · `Beta`
- [My EvoPlayer](https://apps.apple.com/hk/app/my-evoplayer/id6762497614) - Player for a media server or playlist with live TV, an EPG, movies, shows and home videos. `Plex` `+IPTV` · `iOS` `iPadOS` · `Free`
- [Nyx](https://apps.apple.com/de/app/nyx-m%C3%A9diath%C3%A8que/id6819014501) - Library player that direct-plays films and shows without transcoding; needs a server of its own. `Plex` · `iOS` `tvOS` · `Free`
- [Orbit](https://brandonewade-debug.github.io/asterline-labs/apps/orbit/) - Video client with Quad View, Live TV and Invidious (YouTube) playback. `Plex` · `iOS` `iPadOS` `tvOS` · `Beta`
- [PlexATV3](https://github.com/huguesdelamure/PlexATV3) - Client for the third-generation Apple TV. `Plex` · `tvOS` · `Open source`
- [PlexConnect](https://github.com/iBaa/PlexConnect) - PC-side server that takes over the Trailers app on Apple TV 2 and 3 to browse and play Plex. `Plex` · `tvOS` · `Open source`
- [PlexConnectApp](https://github.com/iBaa/PlexConnectApp) - Apple TV 4 client modelled on PlexConnect. `Plex` · `tvOS` · `Open source` `Free` `Stale 2016`
- [plexplus](https://github.com/chasecheney/plexplus) - Simple Plex app for Mac and iPad. `Plex` · `macOS` `iPadOS` · `Open source` `Free`
- [Plinx](https://github.com/bballdavis/Plinx) - Parent-managed family Plex client with content-rating ceilings and offline access. `Plex` · `iOS` `iPadOS` · `GPL-3.0` `Free`
- [Radar Player](https://apps.apple.com/br/app/radar-player/id6804476203) - Media player for Files, linked folders and network URLs, with library streaming and subtitle import. `Plex` · `iOS` `iPadOS` · `Free`
- [RexyView](https://apps.apple.com/de/app/rexyview/id6761977975) - Native client built for every Apple device, with a Watch app to monitor the server. `Plex` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `watchOS` · `Free`
- [Simple Theater](https://apps.apple.com/us/app/simple-theater/id6812149057) - Plain player for personal video libraries, with no ads, subscriptions or extra channels. `Plex` · `iOS` `iPadOS` `tvOS` · `Free`
- [Subnext Player](https://apps.apple.com/de/app/subnext-player/id6815342410) - Player that merges connected servers, including shared ones, and other sources into one library. `Plex` · `iOS` `iPadOS` · `Free`
- [Surf for Plex](https://surfforplex.com) - Vertical short-form browser for your library, in the style of TikTok. `Plex` · `iOS` · `Beta`
- [UmaMedia](https://apps.apple.com/br/app/umamedia/id6811944771) - Media player for iOS and iPadOS connecting personal servers and NAS, with playlists and offline downloads. `Plex` · `iOS` `iPadOS` · `Free`
- [Video Explorer II](https://apps.apple.com/us/app/video-explorer-ii-player-for-chromecast-plex-nas/id1044421698) - Video browser and player with a built-in web browser that casts to Chromecast and searches subtitles. `Plex` · `iOS` `iPadOS` `tvOS` · `Paid` `Stale 2016`
- [Vipe](https://apps.apple.com/us/app/vipe-all-in-one-video-player/id6760535813) - All-in-one player for video, audio and subtitles from SMB, FTP, NFS, cloud and local files. `Plex` · `iOS` · `Free`
- [Vortexo](https://forums.plex.tv/t/introducing-vortexo-a-new-plex-client-for-apple-tv/938897) - Apple TV client that merges local and shared servers. `Plex` · `tvOS`

### Desktop

- [champ](https://github.com/dz0ny/champ) - Raspberry Pi Plex player from 2016. `Plex` · `Linux` · `MIT` `Free` `Stale 2016`
- [Girens for Plex](https://gitlab.gnome.org/tijder/girens) - GTK desktop client for Linux. `Plex` · `Linux` · `Open source` · [Flathub](https://flathub.org/apps/nl.g4d.Girens)
- [LunaVideo](https://apps.microsoft.com/detail/9n2csfcpn3j8) - WinUI 3 video player for Windows 11 that also plays local files. `Plex` · `Windows`
- [NevuDesktop](https://github.com/Ipmake/NevuDesktop) - Desktop wrapper around the Nevu Plex web interface. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free` `Stale 2025`
- [OmenPlayer](https://github.com/SemHiel2003/OmenPlayer) - Windows IPTV player written with Qt6 and libVLC that also plays from Plex. `Plex` `+IPTV` · `Windows` · `GPL-3.0` `Free`
- [OpenPHT](https://github.com/RasPlex/OpenPHT) - Community fork of Plex Home Theater, the old ten-foot desktop player. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Stale 2022`
- [Patina](https://github.com/madrazaldi/patina) - Desktop client with a Rust terminal interface. `Plex` · `Windows` `macOS` `Linux` `CLI` · `Apache-2.0`
- [Plauri](https://github.com/FortNbreak/Plauri) - Rust and Tauri desktop wrapper for the Plex web interface, aimed at low-end PCs. `Plex` · `Windows` · `Open source` `Free` `Stale 2024`
- [PlexClient](https://github.com/RuurdBijlsma/PlexClient) - Electron and Vue desktop Plex player that uses VLC. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free` `Stale 2022`
- [PlexDeck](https://github.com/Farathim89/plexdeck) - Windows client with a controller-driven TV mode. `Plex` · `Windows` · `GPL-3.0`
- [plex-desktop-client](https://github.com/austinkregel/plex-desktop-client) - Personal Tauri-based Plex desktop client. `Plex` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [Plexible](https://github.com/serrebidev/Plexible) - Plex client designed for screen readers, with Windows, macOS and Linux builds. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [recalplex](https://gitlab.com/recalplex/recalplex) - Raspberry Pi NOOBS image that combines the Recalbox retro-gaming system with RasPlex. `Plex` · `Linux` · `Open source` `Stale 2020`
- [Scanline](https://github.com/0SkillAllLuck/Scanline) - Unofficial native GTK4 and libadwaita Plex client for Linux. `Plex` · `Linux` · `GPL-3.0` `Free`
- [tma02/plex-app](https://github.com/tma02/plex-app) - Mac wrapper app for the Plex web player, from 2015. `Plex` · `macOS` · `MIT` `Free` `Stale 2015`
- [Tuxflix](https://github.com/codingncaffeine/Tuxflix) - Avalonia desktop client laid out like a game library, with hardware-decoded playback and resume. `Plex` · `Linux` · `GPL-3.0` `Beta` · [AUR](https://aur.archlinux.org/packages/tuxflix-bin)
- [VidyeoFE](https://github.com/han-sz/VidyeoFE) - Native macOS front end for Plex. `Plex` · `macOS` · `Open source` `Free`

### Web

- [FrayWatch](https://github.com/Dejniel/FrayWatch-Plex-WebUI) - Self-hosted alternative web interface. `Plex` · `Web` · `GPL-3.0`
- [plexy](https://github.com/ricoloic/plexy) - Alternative Plex web interface built with Next.js. `Plex` · `Web` · `MIT` `Free`
- [SyncLounge](https://github.com/synclounge/synclounge) - Watch-together web client that keeps playback in sync for a group. `Plex` · `Web` · `MIT` · [AUR](https://aur.archlinux.org/packages/synclounge)

## Emby video clients

Third-party video and general clients for Emby only. Many come from the large Chinese-language scene.

### Cross-platform

- [Aether](https://emby.media/community/topic/146174-new-android-tv-app-aether-a-direct-play-first-emby-client-for-windows-android-tv/) - Direct-play-first client for Windows and Android TV built with Tauri and Rust. `Emby` · `Windows` `Android TV` · `MIT` `Free` `Beta`
- [AltEmby](https://github.com/kyrollosnageh/AltEmby) - Flutter streaming client. `Emby` · `Android` `iOS` · `Open source` `Free`
- [EmbyFlutter](https://github.com/liyongliao/EmbyFlutter) - Flutter player for phones and desktops. `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` · `Open source` `Free`
- [emby_my_client](https://github.com/jsdfhasuh/emby_my_client) - Android and iOS client with a focused feature set. `Emby` · `Android` `iOS` `iPadOS` · `Open source` `Free`
- [emby-shorts-player](https://github.com/zym20192019/emby-shorts-player) - Player that browses videos in a TikTok-style short-video feed. `Emby` · `Windows` `Android` · `Open source` `Free`
- [EmbyTok-Flutter](https://github.com/1525745393/EmbyTok-Flutter) - TikTok-style vertical feed for browsing an Emby library. `Emby` · `Web` `Android` · `MIT`
- [Emby Watch Party Client](https://codeberg.org/Hazing6995/emby-watchparty-client) - Kotlin Multiplatform client with a Continue Watching row and watch-party playback sync. `Emby` · `Windows` `macOS` `Linux` `Android` · `Open source`
- [Himi SyncWatch](https://github.com/JzeroM/himi-syncwatch) - Flutter client with group watching. `Emby` · `Windows` `Android` `iOS` `HarmonyOS` `Android TV` · `Open source` `Free`
- [Media-Player](https://github.com/SakuraLoveSmile/Media-Player) - Flutter Emby player that also connects to MoviePilot. `Emby` · `Windows` `macOS` `Android` · `Open source`
- [Optic Player](https://optic-player.github.io/?lang=en) - Cross-platform video player distributed through the Microsoft Store and GitHub releases. `Emby` · `Windows` `macOS` `Linux` `Android` `iOS` · `Free` · [Source](https://github.com/optic-player/optic-player.github.io) · [Microsoft Store](https://apps.microsoft.com/detail/9pmt50svspl0)
- [Syncwe](https://github.com/SyncweApp/syncwe) - Watch-together player that syncs playback between viewers. `Emby` · `Windows` `macOS` `Android` `iOS` · `Open source` `Free`
- [Themby](https://apps.apple.com/us/app/themby/id6757106291) - Third-party Flutter player. `Emby` · `macOS` `Android` `iOS` `iPadOS` · `Free` · [Source](https://github.com/chicring/Themby)
- [XEmby](https://github.com/fxstd/xemby) - Multi-platform Emby client. `Emby` · `Windows` `Android` · `Open source`
- [xikkcn/myemby](https://github.com/xikkcn/myemby) - Client for Windows, Linux, Android phones and TV, and the web. `Emby` · `Windows` `Linux` `Web` `Android` `Android TV` · `Open source`
- [Yingyu](https://github.com/kai489646859-netizen/Yingyu) - Android and Windows client with mpv playback. `Emby` · `Windows` `Android` · `GPL-3.0` `Free`

### Android, Android TV and HarmonyOS

- [Angelplayer](https://github.com/Sanbuge777/Angelplayer-Releases) - Emby client for Android TV with its own playback core; release builds only. `Emby` · `Android TV`
- [Arloes](https://emby.media/community/topic/150320-arloes-a-true-modern-android-tv-client-for-emby/) - Android TV client based on the official app. `Emby` · `Android TV` · `Beta`
- [AureP](https://github.com/2982136527/AureP-app) - Mobile player app. `Emby` · `Android` · `Open source` `Free`
- [BEMPlayer](https://github.com/liveinaus/bemplayer) - Player app for Android TV. `Emby` · `Android TV` · `Open source` `Free`
- [camby](https://github.com/run456/camby) - Android Emby client with a glass-style interface and ExoPlayer or MPV playback. `Emby` · `Android` · `Open source`
- [ChaiChaiEmbyTV](https://github.com/dh374374/ChaiChaiEmbyTV) - Chinese Android TV client. `Emby` · `Android TV` · `Free`
- [CineFlow](https://github.com/bsfcxz/CineFlow) - Material Design player built with Flutter. `Emby` · `Android` · `Apache-2.0` `Free`
- [Ember](https://github.com/xmfx11/Ember) - Android Emby client with a hybrid player engine. `Emby` · `Android` · `Open source`
- [Embrr](https://emby.media/community/topic/149916-embrr-%E2%80%94-a-premium-android-tv-client-for-emby/) - Android TV client built with Compose for TV. `Emby` · `Android TV` · `Beta`
- [EmbyPlayerNext](https://github.com/hspmanbu/EmbyPlayerNext) - Native Android client built on Media3 for phones, tablets and TV. `Emby` · `Android` `Android TV` · `Open source` `Free`
- [emby-short-video-client](https://github.com/kylindebug/emby-short-video-client) - Android client that browses a library as a short-video feed. `Emby` · `Android` · `MIT` `Free`
- [EmbyStream](https://github.com/xmfx11/EmbyStream) - Lightweight Emby client for Android using ExoPlayer. `Emby` · `Android` · `Open source`
- [EmbyTV客户端](https://www.bilibili.com/video/BV1tcraBTEwU/) - Free Android TV client with danmaku comments and multi-server support. `Emby` · `Android TV` · `Free` · [Info](https://www.bilibili.com/video/BV1ZjcMzqEwQ/)
- [Emdy](https://github.com/zzh407/EMDY) - Douyin-style short-video client. `Emby` · `Android` `HarmonyOS` · `MIT` `Free`
- [Emfin](https://github.com/NextPlayerCloud/Emfin) - Third-party Android TV client. `Emby` · `Android TV` · `Open source` `Free`
- [Gemby](https://github.com/AmbitiousJun/gemby) - Android TV client with a choice of MPV, Media3 or VLC playback engines. `Emby` · `Android TV` · `Open source` `Free`
- [Glowplayer](https://www.bilibili.com/video/BV1wmuc6YEdL/) - Independently developed HarmonyOS video player. `Emby` · `HarmonyOS`
- [Harflix](https://github.com/Actrlq/Harflix) - HarmonyOS video player; a phone-first project that is still adding features. `Emby` · `HarmonyOS` · `GPL-3.0` `Free`
- [MediaHub](https://github.com/fwzm/MediaHub) - Compose-based Android player for Emby and local files; Jellyfin, Plex and WebDAV sources are planned. `Emby` · `Android` · `Open source` `Beta`
- [nasplayer](https://gitee.com/shruihu/nasplayer) - Flutter video player for local files and Emby streaming. `Emby` · `Android` · `Apache-2.0`
- [nasvideoplayer](https://gitee.com/shruihu/nasvideoplayer) - Kotlin NAS video player for Android phones and TVs that browses and plays an Emby library. `Emby` · `Android` `Android TV` · `Open source`
- [OpenEmby TV](https://github.com/shareven/openemby_tv) - Open-source client for Android TV boxes. `Emby` · `Android TV` · `Open source` `Free`
- [OpenPlayer](https://github.com/xmfx11/OpenPlayer) - Android player styled after the 极影视 app. `Emby` · `Android` · `Open source` `Free`
- [Serenity for Android](https://github.com/NineWorlds/serenity-android) - Android client optimised for television displays. `Emby` · `Android` `Android TV` `Fire TV` · `MIT` · [Amazon](https://www.amazon.com/NineWorlds-Serenity-for-Android/dp/B00H3UBS2O)
- [SkyPlayer](https://www.bilibili.com/video/BV1UKh36dEX2/) - Native HarmonyOS video player with a poster wall and cloud-drive sources. `Emby` · `HarmonyOS`
- [SwiftPlayer](https://github.com/cptbt22/SwiftPlayer-Android) - Android NAS video player for local files, SMB shares and a media server. `Emby` · `Android` · `GPL-3.0` `Free`
- [TvxEmby](https://t.me/s/tvxemby) - Android TV client with danmaku (bullet comments). `Emby` · `Android TV` · `Free` `Beta`
- [Unified Media](https://emby.media/community/topic/149993-unified-media-an-emby-client/) - Android TV client distributed as a free beta APK. `Emby` · `Android TV` · `Free` `Beta`
- [Vellora](https://play.google.com/store/apps/details?id=app.vellora.client) - Android client. `Emby` · `Android`
- [Visink](https://github.com/skymei/VisInkAndroidTVRelease) - Free Android TV client distributed as ready-made releases only. `Emby` · `Android TV` · `Free`
- [WBEmby](https://github.com/WhiteBearWB/WBEmby) - Android TV client. `Emby` · `Android TV` · `Open source` `Free`
- [WJPlayer](https://github.com/Maple-Ling/WJPlayer) - Android client for arm64 devices. `Emby` · `Android` · `Open source` `Free`
- [Yonto Player](https://player.yonto.app/) - Android TV client set up by scanning a QR code with a phone. `Emby` · `Android` `Android TV` · `Freemium`
- [zmby](https://github.com/zhenyuefu/zmby) - Multi-server Emby client for Android TV and Zidoo players. `Emby` · `Android TV` · `GPL-3.0`
- [影屿 CineIsle](https://github.com/nu1lkali/CineIsle) - Android player built on mpvEx that plays local files and Emby libraries. `Emby` · `Android` · `Apache-2.0`
- [钢筋浏览器 TV](https://www.bilibili.com/video/BV16M4qzdEUW/) - Android TV browser that opens Emby, IPTV, web pages and SMB shares without Kodi. `Emby` `+IPTV` · `Android TV`

### Apple platforms

- [APTVMAN](https://apps.apple.com/us/app/aptvman-your-nas-player/id6808655545) - NAS player for movies, shows and music over SMB, WebDAV or a media server, on iPhone and Apple TV. `Emby` · `iOS` `tvOS` · `Free`
- [CATV](https://apps.apple.com/us/app/catv/id6783948214) - Native media-server client with layouts tuned to each device; ships with no content. `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [Cylux](https://apps.apple.com/us/app/cylux/id6789887867) - Simple third-party Emby video player with no ads. `Emby` · `iOS` `iPadOS` `tvOS` · `Free`
- [Den](https://apps.apple.com/us/app/den/id6807652177) - Self-hosted media hub for music, films, shows, audiobooks, comics and novels, with iCloud-synced settings. `Emby` `+Audiobookshelf` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [DreamBy](https://testflight.apple.com/join/Vet98X4r) - Aggregator player for several servers, with Dolby Vision support. `Emby` · `iOS` `iPadOS` · `Beta`
- [EmbyFlow](https://github.com/cui327524840/embyflow) - iPhone Emby client built around H.264 hardware decoding for older devices. `Emby` · `iOS` · `Open source`
- [Filo](https://apps.apple.com/us/app/filo/id6802485025) - MPV-based media browser for NAS, cloud drives and servers, with a poster wall and transfer queue. `Emby` `+fnOS` · `iOS` `iPadOS` · `Freemium`
- [iemc](https://apps.apple.com/cn/app/iemc/id1467462861) - iPhone client with search across several servers. `Emby` · `iOS` `iPadOS` · `Paid`
- [IIVA](https://apps.apple.com/us/app/iiva/id1614231457) - iPhone client. `Emby` · `iOS` `iPadOS` `tvOS` · `Free` `Stale 2023`
- [Kinode](https://apps.apple.com/us/app/kinode/id6796324720) - Personal media library for local files, NAS, WebDAV and Emby with posters, subtitles and resume. `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Klusto](https://apps.apple.com/us/app/klusto/id6782746622) - Private client for self-hosted services, combining music, video, memos and finance tools in one app. `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`
- [KSPlayer Tracy](https://apps.apple.com/us/app/ksplayer%E6%92%AD%E6%94%BE%E5%99%A8-tracy/id6450770064) - Video player that plays nearly any format from network shares and a server library without conversion. `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Paid`
- [Prismo](https://apps.apple.com/cn/app/prismo/id6748607260) - iPhone player for the server, Aliyun Drive and WebDAV. `Emby` · `iOS`
- [Reel Player](https://apps.apple.com/us/app/reel-player-video-player/id6471356040) - Video player for a server library with broad MP4, MKV, M4V and MOV support. `Emby` · `macOS` `iOS` `iPadOS` · `Freemium` `Stale 2024`
- [Reflix](https://apps.apple.com/us/app/reflix-emby-video-player/id6621243955) - iPhone video player. `Emby` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Temby](https://apps.apple.com/cn/app/id6449966958) - Paid iPhone client that also plays music in the background. `Emby` · `iOS` `iPadOS` · `Paid`
- [Wakk Player](https://apps.apple.com/us/app/wakk-player/id6804757527) - Emby player with multi-server support, danmaku, AI subtitle translation and casting. `Emby` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Wizju](https://apps.apple.com/cn/app/id6749068740) - iPhone player for the server and IPTV. `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` · `Free`
- [X Play](https://apps.apple.com/us/app/x-play/id6806874973) - Emby player and library that can also import HTTPS JSON media lists and CMS endpoints. `Emby` · `iOS` `iPadOS` `tvOS` `visionOS` · `Paid`
- [XPTV](https://apps.apple.com/us/app/xptv/id6459409368) - Multi-protocol video player for cloud drives, Emby, VOD sources, M3U and IPTV. `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Paid`
- [yybx](https://apps.apple.com/cn/app/yybx/id1519723194) - Paid client for iPhone and Apple TV. `Emby` · `iOS` `iPadOS` `tvOS` · `Paid`

### Desktop

- [CodeCrafter-bit/emby-player](https://github.com/CodeCrafter-bit/emby-player) - Desktop video player built with Electron and React. `Emby` · `Windows` `macOS` `Linux` · `MIT` `Free` `Stale 2025`
- [EasyHub](https://github.com/sanqianxingluo/easyhub) - Windows desktop client playing through libmpv. `Emby` · `Windows` · `Open source` `Free`
- [EmberFlux](https://github.com/moyuand/EmberFluxAPP) - Mac player app. `Emby` · `macOS` · `Open source` `Free`
- [EmbyClientPlus](https://github.com/krakerz/EmbyClientPlus) - Rust desktop client focused on SmoothVideo Project (SVP) frame interpolation. `Emby` · `Windows` `macOS` `Linux` `Steam Deck` · `GPL-3.0` `Free`
- [EmbyDesk](https://github.com/SideFx/EmbyDesk) - Qt desktop Emby client and successor to EmbyExplorerQt. `Emby` · `Windows` `macOS` · `MPL-2.0`
- [EmbyFlix](https://github.com/J0n4e/Embyfix) - Netflix-style native macOS client written in SwiftUI. `Emby` · `macOS` · `GPL-3.0`
- [EmbyMini](https://github.com/stqfdyr/embymini) - Rust desktop client modelled on SenPlayer, playing through mpv. `Emby` · `Windows` · `Open source` `Free`
- [EmbyPlayer](https://github.com/desire668/embyplayer) - Windows desktop client on WinUI 3 with mpv playback and search across several servers. `Emby` · `Windows` · `Open source` `Free`
- [Jinx](https://github.com/SeriousQY/JINX-EmbyClient) - Simple Windows client using mpv with Anime4K upscaling; release builds only. `Emby` · `Windows`
- [Kude](https://apps.apple.com/us/app/kude/id6757255785) - Mac video player and library manager for WebDAV, Emby and SMB with a cinema-style view. `Emby` · `macOS` · `Paid`
- [Mambo](https://github.com/Aaleo73/Mambo) - WinUI 3 Emby client using libmpv. `Emby` · `Windows` · `GPL-3.0`
- [media-server-connect](https://aur.archlinux.org/packages/media-server-connect-git) - Linux desktop app that opens an Emby server's web interface. `Emby` · `Linux` · `Open source` `Stale 2021`
- [MFPlayer](https://github.com/abcming/MfPlayer) - Desktop player built with Qt 6 QML and libmpv. `Emby` · `Windows` · `Open source` `Free`
- [Miry](https://github.com/Lomiry/Miry) - Windows desktop client powered by mpv. `Emby` · `Windows` · `MIT` `Free`
- [MyEmby](https://github.com/tnt19886/MyEmby) - Tauri desktop client for Emby that plays through mpv. `Emby` · `Windows` · `Open source`
- [Penrose](https://github.com/zzzyang03/penrose) - Windows video player with HDR output and a built-in client. `Emby` · `Windows` · `GPL-3.0` `Free`
- [PillVideo](https://emby.media/community/topic/148983-pillvideo-%E2%80%94-a-modern-emby-client-for-windows/) - Windows 10 and 11 client built on mpv. `Emby` · `Windows`
- [Raven RD Media Player](https://github.com/raven2892/Raven-rd-media-player-for-Emby) - Native Windows player. `Emby` · `Windows` · `Open source` `Free`
- [ShenhePlayer](https://github.com/L51xyz12138/ShenhePlayer) - Small Windows client built with Tauri, Vue and mpv. `Emby` · `Windows` · `Open source` `Free`
- [Taluxa](https://github.com/trans76544/Taluxa) - Emby browser and player that runs in the browser or as a desktop app. `Emby` · `Windows` · `Open source`
- [Tiny Player](https://github.com/Clwury/tiny-player) - Desktop client written in Rust. `Emby` · `Windows` `Linux` `Steam Deck` · `GPL-3.0` `Free`
- [xikkcn/wemby](https://github.com/xikkcn/wemby) - Lightweight desktop player built on Electron. `Emby` · `Windows` · `Open source` `Free`
- [YppHub](https://apps.apple.com/us/app/ypphub/id6779518602) - Mac media library and player for local folders, NAS, WebDAV, SMB and Emby. `Emby` · `macOS` · `Freemium`

### Web

- [fast-emby](https://gitee.com/chenshaogui/fast-emby) - Vue short-video style front end for Emby. `Emby` · `Web` · `Open source`
- [MiceYaa](https://www.nodeseek.com/post-547061-1) - Web client for a single server. `Emby` · `Web`

## Music

Music players and music-first clients.

### Multi-server music

- [52XN Music King](https://apps.apple.com/us/app/52xn-music-king/id6783871006) - Music player for local audio, stream links and self-hosted server profiles. `Plex` `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` · `Free`
- [AJ Audio](https://aj-studio-com.itch.io/aj-audio-player) - Windows music player for media servers and local files, distributed on itch.io. `Jellyfin` `Emby` · `Windows`
- [Amcfy Music](https://apps.apple.com/us/app/amcfy-music-navidrome-client/id6758010612) - Subsonic-compatible music player for Navidrome, Jellyfin, Emby and other servers with offline caching. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` · `Free` · [Source](https://github.com/amcfy-music/amcfy-music)
- [ampcast](https://github.com/rekkyrosso/ampcast) - Browser music player that combines several media servers in one library. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free`
- [Amplayer](https://apps.apple.com/ru/app/amplayer/id6826611277) - Retro desktop-style music player with a three-window layout, skins and a 10-band equalizer. `Jellyfin` `Emby` `+Subsonic` · `iOS` · `Free`
- [Artic Audio](https://apps.apple.com/us/app/artic-audio/id6748662036) - Audiophile music player with bit-perfect, gapless playback for Plex and Jellyfin libraries. `Plex` `Jellyfin` · `iOS` `iPadOS` · `Free`
- [Audara](https://apps.apple.com/gb/app/audara/id6780220192) - Music player for a home server with no third-party cloud; also on Mac, Apple TV and CarPlay. `Plex` `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `CarPlay` · `Freemium`
- [Aurora](https://github.com/nessli420/aurora) - Music player for Android, Windows and Linux, plus local files. `Plex` `Jellyfin` `+Subsonic` · `Windows` `Linux` `Android` `Android Auto` · `Apache-2.0` `Free` · [Website](https://auroraplayer.lol)
- [Beacon](https://github.com/mihaitom/beacon) - Self-hosted web and desktop music client with casting. `Plex` `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free`
- [BlueMusic](https://apps.apple.com/us/app/bluemusic-music-player-radio/id6775983788) - Music player combining phone files, cloud storage and home servers, with internet radio. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [B-Side](https://apps.apple.com/kr/app/b-side-cd-%ED%94%8C%EB%A0%88%EC%9D%B4%EC%96%B4-%EB%AF%B9%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%94%84/id6826441635) - Music player styled as a CD player, turntable, cassette deck and FM tuner, driven by the phone hinge. `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` · `Free`
- [Cadence](https://github.com/MDaV05/cadence) - Lightweight Android music and media player. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Android` `Android Auto` · `GPL-3.0` `Free`
- [Chromatix](https://chromatix.app) - Desktop music player for Plex and Jellyfin libraries. `Plex` `Jellyfin` · `Windows` `macOS` `Linux`
- [Cloudflow Music](https://apps.apple.com/us/app/cloudflow-music-nas-player/id6761190341) - Music manager for cloud drives, NAS and personal servers, with offline download and a Watch app. `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` `+fnOS` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [Cotton Music](https://apps.apple.com/us/app/cottonmusic/id6752617064) - Music player with lyrics and cover art that mounts cloud drives and server libraries. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` · `Free` · [Source](https://github.com/pure-music/PureMusic) · [Google Play](https://play.google.com/store/apps/details?id=com.caij.puremusic)
- [CTZZG/feishin](https://github.com/CTZZG/feishin) - Feishin fork that adds Emby support. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Dino's Jukebox](https://apps.apple.com/fr/app/dinos-jukebox/id6825466032) - Jukebox-style music player with crossfades, a most-played chart and DJ intros for NAS, server and Dropbox music. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `CarPlay` · `Freemium`
- [Doudou](https://gitlab.com/Openlyst/doudou) - Flutter music player that also streams YouTube Music; Subsonic is its most-tested source. `Plex` `Jellyfin` `+Subsonic` · `Android` `Android TV` `Android Auto` · `Open source`
- [Drift](https://apps.apple.com/us/app/offline-music-player-drift/id6789325283) - Offline music player with a button-free playing screen; free for seven days, then one purchase. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [DYSC](https://apps.apple.com/us/app/dysc/id6803165063) - Album-first music player that presents a collection as a tactile stack, like owned physical media. `Plex` `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`
- [EchoVault](https://apps.apple.com/tw/app/%E5%90%AC%E5%B1%BF%E9%9F%B3%E4%B9%90/id6772057208) - Private music library player for local folders, WebDAV, SMB, NAS and music servers. `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` · `Free`
- [Embeat](https://apps.apple.com/app/embeat/id6788410988) - Music player for iPhone, iPad and Android with gapless playback, DLNA and offline mode. `Jellyfin` `Emby` · `Android` `iOS` `iPadOS` `CarPlay` · `Subscription`
- [Evermusic](https://apps.apple.com/hk/app/evermusic-%E9%9B%A2%E7%B7%9A%E9%9F%B3%E6%A8%82%E6%92%AD%E6%94%BE%E5%99%A8%E5%92%8C%E5%9D%87%E8%A1%A1%E5%99%A8-%E9%9B%B2%E6%B5%81%E5%AA%92%E9%AB%94/id885367198) - Cloud and offline music player with equalizer, playlists and file management. `Plex` `Jellyfin` `Emby` `+Subsonic` · `macOS` `iOS` `iPadOS` `CarPlay` · `Free` · [App Store](https://apps.apple.com/us/app/evermusic/id1564384601)
- [Feishin Plex fork](https://github.com/lux032/feishin) - Fork of the Feishin desktop music player that adds Plex. `Plex` `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) - Hi-res lossless music player with an equalizer, streaming from NAS or cloud and offline saving. `Plex` `Jellyfin` `Emby` `+Subsonic` · `macOS` `iOS` `iPadOS` `CarPlay` · `Free` · [App Store](https://apps.apple.com/ru/app/flacbox/id1594027432)
- [Glimpse Music](https://launchpad.net/glimpse-music) - GNOME music player for local, USB, Samba and WebDAV music, media servers and internet radio. `Plex` `Jellyfin` · `Linux` · `GPL-3.0`
- [GridPlayer](https://apps.apple.com/us/app/gridplayer-music-player/id6771136647) - Music player for local folders, WebDAV, NAS and self-hosted servers in one organized library. `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` · `Free`
- [Headroom](https://headroommusic.app/) - Music, audiobook and podcast player with a 32-band EQ and casting. `Plex` `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` · `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `Beta`
- [HiFier](https://apps.apple.com/us/app/hifier-hifi-music-player/id6740998246) - Hi-fi music player for Jellyfin and Emby libraries, with ads that extend free usage time. `Jellyfin` `Emby` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [JellyBox Player](https://github.com/avdept/JellyBoxPlayer) - Music player for desktop, phone and car. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `AGPL-3.0` `Free` · [Website](https://jellybox.app/) · [App Store](https://apps.apple.com/us/app/jellybox-player/id6469732117) · [Google Play](https://play.google.com/store/apps/details?id=com.prodigytech.jellybox)
- [JTplayer](https://apps.apple.com/tw/app/jtplayer/id6826739916) - Retro desktop-style music player with synced karaoke lyrics, skins and a mini mode. `Jellyfin` `Emby` `+Subsonic` · `iOS` · `Free`
- [Ling Ran](https://apps.apple.com/us/app/ling-ran/id6755538782) - Native music player where folders are playlists, with animated lyrics and lossless local files. `Jellyfin` `Emby` `+Subsonic` · `macOS` `iOS` `iPadOS` `CarPlay` · `Free`
- [Linthra](https://github.com/TheZupZup/Linthra) - Local-first music player that can also connect to your own server. `Plex` `Jellyfin` `+Subsonic` · `Linux` `Android` `Android Auto` · `AGPL-3.0` `Free` · [F-Droid](https://f-droid.org/packages/io.github.thezupzup.linthra/)
- [LMP Music Hub](https://apps.apple.com/us/app/lmp-music-hub/id6451009326) - Paid iPhone music player. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Paid`
- [L-MUSIC](https://gitee.com/lxsol/l-music) - Android music player for media servers, Navidrome/Subsonic, Synology Audio Station and WebDAV. `Plex` `Emby` `+Subsonic` · `Android`
- [LuSound](https://github.com/ion-lgb/lusound) - Android music player for local files and private-cloud libraries. `Plex` `Jellyfin` `+Subsonic` · `Android` · `GPL-3.0` `Free`
- [LynMusic](https://apps.apple.com/us/app/lynmusic/id6797922509) - Music player for local files, Navidrome, Subsonic, Emby, Jellyfin, SMB and WebDAV libraries. `Jellyfin` `Emby` `+Subsonic` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Matcha Music](https://github.com/c12n/matcha-music) - Music player that connects to several servers at once. `Plex` `Jellyfin` `+Subsonic` · `iOS` · `MIT` `Free`
- [Maxzero](https://apps.apple.com/us/app/maxzero-offline-music-player/id6787266767) - Offline music player for your own files and iTunes purchases, with themes and server libraries. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Paid`
- [Morph Audiophile](https://emby.media/community/topic/150555-morph-audiophile-%E2%80%93-android-music-player-for-emby-bit-perfect-usb-dac-driver-free-beta-testers-wan/) - Android music player with a bit-perfect USB DAC driver. `Jellyfin` `Emby` `+Subsonic` · `Android` · `Free` `Beta`
- [MOSAIC](https://apps.apple.com/us/app/%E9%A9%AC%E8%B5%9B%E5%85%8B%E9%9F%B3%E4%B9%90/id6808726785) - Music player for Navidrome, Subsonic, Emby and Jellyfin servers with synced lyrics, CarPlay and widgets. `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Mossca](https://apps.apple.com/us/app/mossca-lossless-music-player/id6756006362) - Mac music player for local libraries and servers with a high-quality audio engine and DAC support. `Plex` `Jellyfin` `Emby` `+Subsonic` · `macOS` · `Paid`
- [Mozz](https://github.com/brandomoore/Mozz) - Music app that builds queues with sonic analysis. `Plex` `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `Open source` `Free` · [TestFlight](https://testflight.apple.com/join/dmeawSSM)
- [Mu3ic](https://mu3ic.xyz) - Android music player for Navidrome/Subsonic and media servers. `Jellyfin` `Emby` `+Subsonic` · `Android` `Android Auto` · `Freemium`
- [MusicXX](https://github.com/coolight7/musicxx) - Flutter player for local files, cloud drives and NAS shares. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS`
- [Musiver](https://apps.apple.com/cn/app/%E9%9F%B3%E6%B5%81-%E8%BF%9E%E6%8E%A5%E4%BD%A0%E7%9A%84%E9%9F%B3%E4%B9%90/id6449966496) - Music player for Navidrome, Subsonic, Synology Audio Station, Emby and Jellyfin, on iPhone and Android. `Jellyfin` `Emby` `+Subsonic` · `Android` `iOS` `iPadOS` `CarPlay` · `Free` `Stale 2025` · [Info](https://4pda.to/forum/index.php?showtopic=1123147)
- [N1ko Music](https://github.com/baogutang/N1KO-MUSIC) - Music streaming app for phones, tablets and desktops. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `iPadOS` · `MIT` `Free`
- [Narjo](https://apps.apple.com/us/app/narjo/id6748359006) - iPhone music player. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [Niche](https://apps.apple.com/app/niche-audio-player/id6755544716) - Folder-based audio player for Apple TV. `Plex` `Emby` · `tvOS` · `Freemium`
- [NostalgicPod](https://apps.apple.com/app/id6781631808) - Music player styled after the iPod Classic, with local files too. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Android` `iOS` `iPadOS` · `Paid` · [Google Play](https://play.google.com/store/apps/details?id=com.nostalgicpod.app)
- [NSMusicS](https://github.com/Super-Badmen-Viper/NSMusicS) - Music player and server pair with clients for desktop and web. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `AGPL-3.0` `Free` · [Microsoft Store](https://apps.microsoft.com/detail/9n0rws2tjxg1)
- [PearTune](https://apps.apple.com/us/app/peartune-self-hosted-music/id6796709523) - Music app that streams your library from a machine you own over a direct encrypted link. `Jellyfin` `Emby` · `iOS` · `Free`
- [Phoebe](https://github.com/j-roskopf/Phoebe) - Compose Multiplatform music player that also reaches Music Assistant. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` `CarPlay` `Android Auto` · `MIT` `Free`
- [Platter](https://github.com/Silvercyclops999/platter) - Desktop music player for Windows and macOS. `Plex` `Jellyfin` `+Subsonic` · `Windows` `macOS` · `GPL-3.0`
- [Plinth Player](https://apps.apple.com/us/app/plinth-player/id6772366960) - iPhone player for music and podcasts. `Jellyfin` `Emby` · `iOS`
- [Primuse](https://apps.apple.com/us/app/primuse-self-hosted-music/id6761675450) - Self-hosted music player that also handles podcasts, audiobooks and internet radio, with synced lyrics. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Free`
- [Qingyuan Player](https://apps.apple.com/us/app/%E9%9D%92%E5%85%83-player/id6761592311) - Local music player with metadata and lyric tools that also streams from Jellyfin, Emby, WebDAV and Alist. `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [Radiccio](https://apps.apple.com/us/app/radiccio/id6751426653) - Mac music player and personal music server with local files, Apple Music, Navidrome, Plex and Jellyfin. `Plex` `Jellyfin` `+Subsonic` · `macOS` · `Freemium`
- [RoadSonic](https://www.roadsonic.com/) - iPhone music player built for CarPlay. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Freemium` · [App Store](https://apps.apple.com/app/id6811639958)
- [Rufin](https://github.com/screwys/Rufin) - Multi-platform music player with a headless web UI, plus WebDAV and SMB. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free` · [Flathub](https://flathub.org/apps/io.github.screwys.Rufin) · [AUR](https://aur.archlinux.org/packages/rufin-bin)
- [Shuttle Music](https://github.com/timusus/Shuttle2) - Music player for local files and server streaming. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Android` `Android Auto` · `Apache-2.0` `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=com.simplecityapps.shuttle)
- [Sillon (Wifsimster)](https://github.com/Wifsimster/sillon) - Android music player for Plex and Jellyfin with Android Auto, offline downloads and ratings. `Plex` `Jellyfin` · `Android` `Android Auto` · `Open source` `Free`
- [SirenX](https://apps.apple.com/tw/app/sirenx-hi-res-music-player/id6757968535) - Free Hi-res lossless player for FLAC, ALAC and DSD, with EQ and headphone tuning profiles. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`
- [SonaWave](https://github.com/Tlntin/SonaWave-Release) - Multi-source music player for desktop and mobile. `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` `+fnOS` · `Windows` `macOS` `Linux` `Android` `HarmonyOS` `Android TV` · [AppGallery](https://appgallery.huawei.com/app/detail?id=com.tlntin.sonawave)
- [Sonzra](https://github.com/sonzra/sonzra) - Player for music, podcasts and audiobooks, currently in alpha. `Plex` `Jellyfin` · `Web` · `AGPL-3.0` `Free` `Beta`
- [Striae](https://apps.apple.com/kr/app/striae/id6779471339) - Music player with a Cover Flow view that switches between servers, on iPhone, iPad and Apple Watch. `Plex` `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [SuperMusicHub](https://apps.apple.com/us/app/supermusichub-stream-music/id6760216257) - Mac music player that unifies streaming services, local libraries and media servers. `Plex` `Jellyfin` `Emby` · `macOS` · `Paid`
- [Symfonium](https://symfonium.app/) - Android music player that casts to Chromecast and Sonos groups. `Plex` `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` `+Kodi` · `Android` `Android TV` `Android Auto` `Wear OS` · `Paid` · [Google Play](https://play.google.com/store/apps/details?id=app.symfonik.music.player)
- [SynoMusic](https://apps.apple.com/us/app/synomusic/id6784094020) - Music client for self-hosted libraries with smart mixes, lyrics, downloads, podcasts and radio. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Free`
- [Tape Deck](https://apps.apple.com/us/app/tape-deck/id6822531305) - Plays an album as a cassette in a deck with turning reels, a counter and tape sides. `Plex` `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [Tauon Music Box](https://github.com/Taiko2k/Tauon) - Desktop music player for Windows and Linux. `Plex` `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free` · [Flathub](https://flathub.org/apps/com.github.taiko2k.tauonmb)
- [Tonar](https://apps.apple.com/us/app/tonar-flac-hi-res-player/id6791282669) - Hi-res lossless player on an AVAudioEngine chain, streaming from NAS shares, servers and S3 storage. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [Tonarr](https://apps.apple.com/us/app/tonarr-private-music-player/id6796856828) - Music player for Plex, Jellyfin and Navidrome or OpenSubsonic libraries. `Plex` `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` `CarPlay` `watchOS` · `Subscription`
- [TuneSync](https://apps.apple.com/us/app/tunesync-nas-music-player/id6783845149) - Music player for NAS and media servers, plus WebDAV, SMB, FTP, NFS and local folders. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` · `Freemium`
- [UTUVO Player Go](https://apps.apple.com/tw/app/utuvo-player-go/id6803722484) - Music and video player; local files and Apple Music are free, servers and drives need a one-time unlock. `Plex` `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` `watchOS` · `Freemium`
- [VutronMusic](https://github.com/stark81/VutronMusic) - NetEase-style desktop player that also streams from your servers. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [walkman-server](https://github.com/djmanri3/walkman-server-android-app) - Walkman-style music player for Android, iOS, Mac and the web. `Plex` `Jellyfin` `Emby` · `macOS` `Web` `Android` `iOS` `iPadOS` `Android Auto` · `GPL-3.0` `Free` · [Source](https://github.com/djmanri3/walkman-server-apple-app) · [Source 2](https://github.com/djmanri3/walkman-server)
- [WatchAmp](https://apps.apple.com/us/app/watchamp-for-plex-jellyfin/id6761737569) - Apple Watch music player that streams, transcodes and downloads from your server for phone-free use. `Plex` `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `watchOS` · `Freemium` · [Source](https://github.com/fkick/WatchAmp) · [TestFlight](https://testflight.apple.com/join/vrehhvsY)
- [XYMusic](https://github.com/xianyvbang/XyMusic) - NAS music player for Android and Windows. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Windows` `Android` · `Apache-2.0` `Free`
- [Yinhu Music](https://apps.apple.com/us/app/yinhu-music/id6738853540) - Music player for NAS libraries with Jellyfin integration and CarPlay. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Paid` · [Source](https://github.com/jxweb/YinHuMusic)
- [Yueyin TV](https://github.com/Traceci/yueyin-tv) - Android TV and phone music player for self-hosted libraries. `Plex` `Jellyfin` `Emby` `+Subsonic` `+fnOS` · `Android` `Android TV` · `GPL-3.0` `Free`
- [Yuzic](https://apps.apple.com/us/app/yuzic-navidrome-jellyfin/id6740042497) - Music player for Navidrome and Jellyfin libraries with offline downloads and a recently-played home. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `Free` · [Source](https://github.com/yuzicapp/yuzic) · [Google Play](https://play.google.com/store/apps/details?id=com.arinora.rawarr)
- [ZMusic](https://meta.appinn.net/t/topic/94903) - Music player under 3 MB with no ads or tracking. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Android` · `Free`
- [对音](https://apps.apple.com/us/app/%E5%AF%B9%E9%9F%B3/id6770529688) - Music player for personal servers, WebDAV, OpenList and device music, with several saved servers. `Jellyfin` `Emby` `+Subsonic` · `iOS` `iPadOS` · `Paid`

### Plex music

- [apistat-music-player](https://github.com/visageeee/apistat-music-player) - Native GTK music player for Plex. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [Audionest (Cameron Howard)](https://apps.apple.com/us/app/audionest/id6761437515) - Music player for local and cloud libraries with CarPlay, Apple Watch and Home Screen support. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [AudioServe](https://apps.apple.com/us/app/audioserve/id6769726072) - Music player focused on finding and playing tracks quickly from a personal server. `Plex` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Bionic Tape](https://apps.apple.com/fr/app/bionic-tape/id6819212863) - Cassette-style music player for a folding iPhone, with playlists and albums shelved as tapes. `Plex` · `iOS` · `Paid`
- [BitaBit](https://apps.apple.com/fr/app/bitabit-hi-fi-audio-player/id6763935151) - Hi-fi lossless player combining files, server libraries, internet radio and podcasts. `Plex` `+Subsonic` · `iOS` `iPadOS` · `Free`
- [BOBMUSIC](https://github.com/BOB-MUSIC/BOBMUSIC) - Free desktop Plex music player with lossless playback and listening stats. `Plex` · `Windows` `macOS` · `Open source` `Free`
- [Caldera Music](https://caldera.homes/music/) - Music player for Apple TV, Android TV, desktop and headless setups. `Plex` · `Android TV` `tvOS`
- [Codafy](https://apps.apple.com/us/app/codafy/id6782122345) - Music player with CarPlay. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [Crate for Plex](https://apps.apple.com/us/app/crate-for-plex/id6767005738) - Native unofficial music player with Watch and CarPlay apps, paid once with no subscription. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Paid`
- [Eclipse Music](https://eclipsemusic.app) - Music player with apps for phones, TVs, Windows and Mac, plus a web player. `Plex` · `Windows` `macOS` `Web` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `CarPlay` `Android Auto` · [TestFlight](https://testflight.apple.com/join/GQvWjTWT)
- [Ensemble](https://apps.apple.com/us/app/ensemble-music-player/id6759577769) - Native iOS music player with hubs and mood playlists. `Plex` · `macOS` `iOS` `iPadOS` `watchOS` · [TestFlight](https://testflight.apple.com/join/HQTUPmE8)
- [Flex Music](https://apps.apple.com/us/app/flex-music-player/id6795259400) - Plex music player and playlist manager with offline downloads, ratings sync and synced lyrics. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [Fluida Player](https://apps.apple.com/us/app/fluida-player/id6820142292) - Music player that picks the next song for you, with gapless albums and loudness matching. `Plex` · `iOS` · `Free`
- [Hathor Player](https://apps.apple.com/us/app/hathor-player/id6821212497) - iPhone music player with CarPlay. `Plex` · `iOS` `CarPlay` · `Freemium` `Beta` · [Info](https://www.reddit.com/r/plexamp/comments/1x4knyv/not_just_another_plexamp_alternative_hathor_turns/)
- [headless-plexamp](https://github.com/dustinrue/headless-plexamp) - Build for running headless Plexamp on a Raspberry Pi. `Plex` · `Linux` · `Open source` `Stale 2022`
- [Hex Music Player](https://github.com/andrew-meis/hex-music-player) - Desktop music player. `Plex` · `Windows` · `MIT` `Stale 2024`
- [Hex Music Player 2.0](https://github.com/andrew-meis/hex-music-player-2.0) - Electron desktop music player for Plex. `Plex` · `Windows` · `Open source` `Free` `Stale 2025`
- [hibiki](https://github.com/karbowiak/hibiki) - Desktop music player built with Tauri. `Plex` · `Windows` `macOS` `Linux` · `MIT`
- [HomeBarr Tunes](https://github.com/gilligan5000/plexTunes) - TouchTunes-style jukebox web app for Plex music, built for touch screens. `Plex` · `Web` · `Open source` `Free` `Beta`
- [Interlude Music](https://apps.apple.com/us/app/interlude-music/id1545773677) - Cover-led music player for a self-hosted library, without rebuilding the library elsewhere. `Plex` · `iOS` `CarPlay` · `Free`
- [JLTamp](https://apps.apple.com/fr/app/jltamp/id6807401608) - Ad-free music player for a self-hosted JLTamp server or a media server, with per-user likes and playlists. `Plex` · `iOS` `iPadOS` · `Free`
- [klingar](https://github.com/simonnorberg/klingar) - Android music player for Plex with Google Cast support. `Plex` · `Android` · `Apache-2.0` `Free` `Stale 2020`
- [Lagu](https://lagu.fm) - Music player for Android, Apple TV, CarPlay and Windows. `Plex` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` `Fire TV` `tvOS` `CarPlay` `Android Auto` `watchOS` · `Beta`
- [Lirro](https://apps.apple.com/us/app/lirro/id6785751140) - Native music player that brings self-hosted servers and Apple Music into one library. `Plex` `+Subsonic` `+Audiobookshelf` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Lull Player](https://apps.apple.com/ru/app/lull-player-podcasts-books/id6775313582) - Podcast and audiobook player whose sleep timer fades into sleep sounds; a paid tier adds more. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [mopidy_plex](https://github.com/havardgulldahl/mopidy_plex) - Mopidy extension that plays Plex audio libraries. `Plex` · `Linux` · `Apache-2.0` `Stale 2016` · [Info](https://pypi.org/project/Mopidy-Plex/)
- [MusicBridge](https://github.com/lux032/MusicBridge) - Android music client with Plex compatibility and Sonos push. `Plex` · `Android` · `MIT` `Free`
- [MusicCovered Mobile](https://apps.apple.com/fr/app/musiccovered-mobile/id6757678404) - Album-focused music player with offline listening, library connection and transfer from a Mac. `Plex` · `iOS` `iPadOS` `watchOS` · `Paid`
- [NonSpecific44/platter](https://github.com/NonSpecific44/platter) - Plex music player for Linux and Android. `Plex` · `Linux` `Android` · `MIT` `Free`
- [Obscurify](https://github.com/j-convey/Obscurify) - Spotify-style desktop app for Plex music. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [Offbeat Player](https://offbeat-player.com) - Paid music player for iPhone and Android. `Plex` · `Android` `iOS` · `Paid` · [App Store](https://apps.apple.com/us/app/offbeat-player/id6786753099)
- [OmaAmp](https://github.com/iainlennox/OmaAmp) - Music plugin for the Omarchy desktop bar. `Plex` · `Linux` · `MIT`
- [OpAmp](https://opamp.app) - Desktop music player for Plex on Mac and Windows. `Plex` · `Windows` `macOS` `iOS` · `Free`
- [phonodeck](https://github.com/dragoshont/phonodeck) - Native macOS music app that plays from Plex, YouTube Music and Spotify. `Plex` · `macOS` · `MIT` `Free`
- [Playris](https://apps.apple.com/app/id6762232046) - Apple TV music player with a bit-perfect mode. `Plex` · `tvOS` · `Free`
- [plexamp-pi](https://github.com/ardenpm/plexamp-pi) - Raspberry Pi setup for headless Plexamp. `Plex` · `Linux` · `GPL-2.0` `Stale 2023`
- [plexfreq](https://github.com/nappa85/plexfreq) - Native Rust music player for Sailfish OS phones and the Linux desktop. `Plex` · `Linux` `Sailfish OS` · `Open source` `Free`
- [PlexMusicPlayer](https://github.com/mrartanis/PlexMusicPlayer) - Simple Python desktop music app for Plex. `Plex` · `Windows` `macOS` `Linux` · `Open source` `Free`
- [Prism Music](https://apps.apple.com/us/app/prism-music/id1335007451) - iPhone and iPad music player with unlimited CarPlay downloads. `Plex` · `iOS` `iPadOS` `CarPlay` · `Freemium` `Stale 2022`
- [ramus](https://github.com/1337raspberry/ramus) - Tauri music client for Plex that browses by genre first. `Plex` · `Windows` `macOS` `Linux` `Android` `iOS` · `MIT` `Free`
- [Rayna](https://github.com/ibb2/Rayna) - Music player. `Plex` · `Windows` `macOS` · `Zlib`
- [SStream](https://play.google.com/store/apps/details?id=io.github.sstream) - Android music player. `Plex` · `Android`
- [Synthesis](https://testflight.apple.com/join/SBfEYGSd) - Music player with Apple Music alongside, credits, related music and playback to AirPlay and Plex players. `Plex` · `iOS` `iPadOS` · `Beta`
- [Tromme](https://tromme.app) - Music player with CarPlay. `Plex` · `iOS` `iPadOS` `CarPlay` · `Free` · [App Store](https://apps.apple.com/us/app/tromme/id6762415193)
- [Truffle](https://apps.apple.com/us/app/truffle-music-player-for-plex/id6829085593) - Music player made for the car, with Shuffle All that plays every song once. `Plex` · `iOS` `iPadOS` `CarPlay` · `Free` · [Source](https://github.com/vanities/truffle) · [TestFlight](https://testflight.apple.com/join/ZXeFFhZM)
- [TuneFalls](https://apps.apple.com/fr/app/tunefalls/id6793672766) - Turns a music library into radio stations by genre, mood, decade and activity, with thumbs up and down. `Plex` · `macOS` `iOS` · `Free`
- [Umbrex](https://apps.apple.com/us/app/umbrex-music-player-for-plex/id6792601467) - Music player with 35 reactive visualizers and on-device key and BPM analysis, for a server and imported files. `Plex` · `iOS` `iPadOS` `CarPlay` · `Paid`
- [Verbara](https://apps.apple.com/br/app/verbara-podcast-player/id6782371836) - Podcast player that merges server, Audiobookshelf and RSS feeds, with ad-free archiving. `Plex` `+Audiobookshelf` · `iOS` `CarPlay` · `Freemium`
- [Wavelength](https://github.com/Spacegoose02/wavelength) - Music player that combines several self-hosted audio sources, with 62 skins. `Plex` `+Subsonic` `+Audiobookshelf` · `Windows` `macOS` `Linux` `Android` `iOS` `Android TV` `Android Auto` · `MIT` `Free`
- [Wristrax](https://apps.apple.com/us/app/wristrax/id6758014508) - Apple Watch music player. `Plex` · `iOS` `watchOS`

### Jellyfin music

- [Aduoer Music](https://apps.apple.com/us/app/aduoer-music/id6794036425) - Music player that merges local folders, WebDAV, SMB, Jellyfin, Navidrome and cloud storage. `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` · `Free`
- [Aetherfin](https://github.com/Aetherfin/mobile-app) - Native Android music player. `Jellyfin` `+Subsonic` · `Android` · `MIT` `Free`
- [Altsound](https://github.com/filipefilardi/altsound) - Music player for a Jellyfin library. `Jellyfin` · `macOS` `Android` `iOS` · `Apache-2.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.silent_summit.altsound)
- [Ammuz](https://apps.apple.com/tw/app/ammuz-jellyfin-navidrome/id6789731991) - Native music player for personal servers, with no subscription or cloud lock-in. `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` · `Paid`
- [Aoide](https://github.com/Virel0/Aoide) - Native Jellyfin music player: SwiftUI on iPhone with CarPlay, and a Rust build for Linux. `Jellyfin` · `Linux` `iOS` `CarPlay` · `GPL-3.0` `Free` · [Source (Linux)](https://github.com/Virel0/Aoide-Linux)
- [Atolla](https://github.com/tx3stn/atolla) - Music player. `Jellyfin` · `Android` `iOS` · `GPL-3.0`
- [Aurelia](https://github.com/j4ckxyz/Aurelia) - Native desktop music player. `Jellyfin` · `Windows` `macOS` `Linux` · `MIT` `Free`
- [Aurelia (xorwyrm)](https://github.com/xorwyrm/aurelia) - Music player. `Jellyfin` · `Android` `iOS` `Android Auto` · `Open source`
- [Backplane](https://testflight.apple.com/join/Q44NnaEX) - Music player that keeps what you play offline within a storage budget, evicting the least recent. `Jellyfin` · `iOS` · `Beta`
- [Bloodin](https://github.com/pathetic/bloodin) - Self-hosted music player written in Rust. `Jellyfin` · `Windows` · `MIT` `Free` `Stale 2025`
- [Bolera](https://apps.apple.com/us/app/bolera/id6774174898) - SwiftUI music client for Jellyfin with CarPlay browsing of artists, albums, playlists and mixes. `Jellyfin` · `macOS` `iOS` `iPadOS` `CarPlay` · `Freemium`
- [boum](https://github.com/henniaufmrenni/boum) - Android music player. `Jellyfin` · `Android` · `MPL-2.0` `Stale 2023` · [F-Droid](https://apt.izzysoft.de/fdroid/index/apk/de.eindm.boum)
- [CassetteCat](https://github.com/samyyy2311/CassetteCat) - Android music player for local files and servers. `Jellyfin` `+Subsonic` · `Windows` `Linux` `Android` `Android Auto` · `GPL-3.0` `Free` · [Source](https://github.com/samyyy2311/CassetteCat-Desktop) · [Google Play](https://play.google.com/store/apps/details?id=in.caffeinelabs.cassettecat)
- [ChordCut](https://github.com/Futyn-Maker/ChordCut) - Screen-reader-friendly Windows music client. `Jellyfin` · `Windows` · `MIT` `Free`
- [Citron Music](https://apps.apple.com/tw/app/citron-music/id6778586935) - Music and audiobook player for a personal server. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Coppelia](https://github.com/j6k4m8/coppelia) - Music player for Mac, iPhone, Android and Linux. `Jellyfin` · `macOS` `Linux` `Android` `iOS` · `Apache-2.0` `Free` `Beta` · [F-Droid](https://f-droid.org/packages/com.matelsky.coppelia/)
- [Diapason](https://github.com/indiependente/diapason) - Native macOS music client. `Jellyfin` · `macOS` · `Open source` `Free`
- [Discophile](https://github.com/debba/discophile) - Record-collection style music player for desktop and web. `Jellyfin` `+Subsonic` `+Audiobookshelf` · `Windows` `macOS` `Linux` `Web` `Android` `iOS` · `MIT` `Free` · [Website](https://www.discophile.app/) · [AUR](https://aur.archlinux.org/packages/discophile-bin)
- [Discrete](https://discrete.app/) - Music player for Jellyfin with cached library views, progressive loading and background downloads. `Jellyfin` · `macOS` `iOS` `iPadOS` `CarPlay` · `Freemium` · [App Store](https://apps.apple.com/us/app/discrete/id6746067740)
- [Dorsal](https://apps.apple.com/hk/app/dorsal-music/id6762251157) - Album-focused Jellyfin music player that caches or downloads tracks for offline use, with CarPlay and Siri. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Paid` · [Source](https://github.com/jaredreich/dorsal) · [TestFlight](https://testflight.apple.com/join/p3cMepSH)
- [Drac's Jukebox](https://apps.apple.com/us/app/dracs-jukebox-subsonic-music/id6761393228) - Music player for OpenSubsonic servers with lossless gapless playback; adds movies and shows from a media server. `Jellyfin` `+Subsonic` · `macOS` `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Paid`
- [Extify](https://github.com/Expuz66/extify) - Customised build of the Finamp music player. `Jellyfin` · `Android` `iOS` `CarPlay` `Android Auto` · `MIT` `Free`
- [Feishin](https://github.com/jeffvli/feishin) - Desktop and web music player. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free` · [Website](https://feishin.vercel.app) · [Flathub](https://flathub.org/apps/org.jeffvli.feishin)
- [feishin-offline](https://github.com/jimhooker/feishin-offline) - Desktop music player forked from Feishin, with an added offline mode. `Jellyfin` `+Subsonic` · `Linux` · `GPL-3.0` `Free`
- [Finale](https://gitlab.com/pschuegr/finale) - Minimal music player built for Jellyfin 12 only; 10.x servers do not work. `Jellyfin` · `macOS` `Linux` `Web` `Android` `iOS` · `MIT`
- [Finamp](https://github.com/finamp-app/finamp) - Music player with offline downloads. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `MPL-2.0` `Free` · [App Store](https://apps.apple.com/us/app/finamp/id1574922594) · [Google Play](https://play.google.com/store/apps/details?id=com.unicornsonlsd.finamp) · [F-Droid](https://f-droid.org/packages/com.unicornsonlsd.finamp/) · [Flathub](https://flathub.org/apps/com.unicornsonlsd.finamp) · [AUR](https://aur.archlinux.org/packages/finamp)
- [Finer Player](https://apps.apple.com/app/id6738301953) - Music player for iPhone and Mac with CarPlay. `Jellyfin` · `macOS` `iOS` `iPadOS` `CarPlay` · `Freemium`
- [FinMusic](https://github.com/OHPG/FinMusic) - HarmonyOS music client. `Jellyfin` · `HarmonyOS` · `GPL-3.0`
- [FinTune](https://github.com/henryHe5638/fintune) - Music player for Huawei HarmonyOS watches. `Jellyfin` · `HarmonyOS` · `Unlicense` `Free`
- [Fintunes](https://apps.apple.com/us/app/fintunes/id1527732194) - Jellyfin music player that streams at the highest quality and plays your Jellyfin playlists. `Jellyfin` · `Android` `iOS` · `Free` `Stale 2025` · [Source](https://github.com/leinelissen/jellyfin-audio-player) · [F-Droid](https://f-droid.org/packages/nl.moeilijkedingen.jellyfinaudioplayer/) · [Google Play](https://play.google.com/store/apps/details?id=nl.moeilijkedingen.jellyfinaudioplayer)
- [Flione](https://github.com/rocavence/Flione-app) - macOS player for a Jellyfin library and YouTube Music. `Jellyfin` · `macOS` · `Open source` `Free`
- [fn-music](https://github.com/pany4321/fn-music) - Music player for fnOS Music and Jellyfin libraries. `Jellyfin` `+fnOS` · `Android` `Android TV` · `GPL-3.0` `Free`
- [Foxy Desktop](https://github.com/Devioxic/Foxy-Desktop) - Desktop music player. `Jellyfin` · `Windows` `macOS` `Linux` · `AGPL-3.0`
- [Gelly](https://github.com/Fingel/gelly) - Linux music player. `Jellyfin` `+Subsonic` · `Linux` · `GPL-3.0` `Free` · [Flathub](https://flathub.org/apps/io.m51.Gelly) · [AUR](https://aur.archlinux.org/packages/gelly)
- [Hakuro](https://apps.apple.com/us/app/hakuro/id6756937091) - Lightweight music player with lyrics, lyric translation and AirPlay. `Jellyfin` · `iOS` · `Free`
- [Heddohon](https://github.com/zorcerer/heddohon) - Server-rendered web music player. `Jellyfin` `+Subsonic` · `Windows` `Linux` `Web` `Android` · `MIT` `Free`
- [Horizon CloudBeats](https://gitlab.com/myluxy/fh6-cloudbeats-custom-radio) - Forza Horizon 6 mod that streams your music library, Spotify or YouTube through the in-game radio. `Jellyfin` · `Windows` · `GPL-3.0`
- [Ikigai Music](https://github.com/Garvittt-API/Ikigai-music) - Rust/Dioxus music player. `Jellyfin` `+Subsonic` · `Windows` · `MIT` `Free`
- [Jamfin](https://apps.apple.com/us/app/jamfin/id6814805439) - Focused music player with song suggestions, genre mixes and an automatic queue. `Jellyfin` · `iOS` `CarPlay` `watchOS` · `Free`
- [Jamfish](https://f-droid.org/packages/org.adrianvictor.geleia/) - Android music player built on the archived Gelli. `Jellyfin` · `Android` · `Open source`
- [Jamjar](https://github.com/rob-land/jamjar) - GTK4 music client for mobile Linux phones. `Jellyfin` · `Linux` · `GPL-3.0` `Free`
- [JammyMusic](https://apps.apple.com/us/app/jammymusic/id6752684680) - Minimal music player for a library, with offline music and Apple Watch support. `Jellyfin` · `iOS` `CarPlay` `watchOS` · `Free`
- [Jellamp](https://github.com/cmdrflyr/Jellamp) - Music player for a Jellyfin library. `Jellyfin` · `Android` `Android Auto` `Android Automotive` · `MIT` `Free`
- [Jeller](https://apps.apple.com/us/app/jeller/id6806754165) - Jellyfin music client with an equalizer, synced lyrics and a full-resolution now playing screen. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free`
- [Jellia](https://github.com/cjbars/jellia) - Native SwiftUI music client for the Mac. `Jellyfin` · `macOS` · `MIT` `Free`
- [Jellibozia](https://apps.apple.com/hk/app/jellibozia/id6798027478) - Music player with CarPlay that streams albums, artists and playlists, with no subscription. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Jellify](https://github.com/Jellify-Music/App) - Free music player for Jellyfin with offline downloads, transcoding options, playlists and instant mixes. `Jellyfin` · `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `MIT` `Free` · [App Store](https://apps.apple.com/us/app/jellify/id6736884612) · [Google Play](https://play.google.com/store/apps/details?id=com.cosmonautical.jellify) · [TestFlight](https://testflight.apple.com/join/etVSc7ZQ)
- [JellyAmp](https://apps.apple.com/us/app/jellyamp-listen-everywhere/id6762120337) - Music and audiobook player for Jellyfin and Audiobookshelf with offline downloads. `Jellyfin` `+Audiobookshelf` · `macOS` `iOS` `iPadOS` `CarPlay` `watchOS` · `Subscription`
- [Jellybee Music](https://apps.apple.com/tw/app/jellybee-music/id6782260879) - Mobile music player with background playback, queue control and recommendations. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [JellyBurn](https://github.com/pixels-more/jellyburn) - GTK3 music player that can burn CDs. `Jellyfin` · `Linux` · `MIT` `Free`
- [JellyCat](https://github.com/Marisalreadytaken/JellyCat-Web-Player) - Static browser client for playing a Jellyfin music library. `Jellyfin` · `Web` · `AGPL-3.0` `Free`
- [JellyCat for AltStore](https://github.com/Marisalreadytaken/Jellycat-altstore) - AltStore source for sideloading the JellyCat music app on iOS. `Jellyfin` · `iOS` · `Open source` `Free`
- [jellyfin-music](https://github.com/endoflineservice/jellyfin-music) - Free, open-source native Android music player. `Jellyfin` · `Android` `Android Auto` `Android Automotive` · `MIT` `Free`
- [Jelly Jams](https://github.com/PatrickTCB/JellyJams) - Open-source music app for Jellyfin with favourites, downloads and no tracking or fees. `Jellyfin` · `macOS` `iOS` `iPadOS` `CarPlay` · `MPL-2.0` `Free` · [App Store](https://apps.apple.com/us/app/jelly-jams-music/id6804514014)
- [JellyMix](https://github.com/BadBagger/jellymix) - Android music client. `Jellyfin` · `Android` `Android Auto` · `Open source` `Free`
- [Jelly Music App](https://github.com/Stannnnn/jelly-app) - Web music player with desktop builds. `Jellyfin` · `Windows` `macOS` `Linux` `Web` · `MIT` `Free`
- [jellymusic-legacy](https://github.com/DerAustistYT/jellymusic-legacy) - Music player for Android 4.0.3 and later. `Jellyfin` · `Android` · `Open source`
- [JellyPlayer](https://apps.apple.com/us/app/jellyplayer/id6761337129) - Music player with downloads, streaming and CarPlay. `Jellyfin` · `iOS` `CarPlay` · `Free`
- [JellyPod](https://apps.apple.com/us/app/jellypod-retro-style-music/id6788034358) - Click-wheel style music player for Jellyfin with album-art flipping, playlists and ratings. `Jellyfin` · `iOS` `CarPlay` · `Paid`
- [jellyPod (nickwilde77555)](https://github.com/nickwilde77555/jellyPod) - iPod-style Jellyfin music player for Android, made in Processing. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [JellySpot](https://github.com/AadiSPrabs/JellySpot_React) - Music client for a Jellyfin library, built with React. `Jellyfin` · `Web` `Android` · `MIT` `Free` · [Source](https://github.com/AadiSPrabs/JellySpot-Web)
- [jellystone-music](https://github.com/DerAustistYT/jellystone-music) - Android music player that runs on very old Android versions. `Jellyfin` · `Android` · `Open source` `Free`
- [JellyStream](https://apps.apple.com/us/app/jellystream/id6759179966) - Jellyfin music player with liked songs, composers, classical browsing and unified search. `Jellyfin` · `iOS` `CarPlay` · `Free`
- [JellyToast](https://github.com/wolfgangwarehaus/jellytoast) - Desktop music player with bit-perfect mpv playback, casting and offline downloads. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-2.0` `Free` · [Website](https://wolfgangwarehaus.com/jellytoast/) · [App Store](https://apps.apple.com/app/id6784370624) · [Microsoft Store](https://apps.microsoft.com/detail/9pnltpxghn79) · [AUR](https://aur.archlinux.org/packages/jellytoast)
- [JellyTune](https://github.com/bacmanni/jellytune) - GNOME audio player for browsing and streaming a Jellyfin library. `Jellyfin` · `Linux` · `GPL-3.0` `Free`
- [JellyTV Music](https://www.amazon.com/993apps-JellyTV-Music/dp/B0G5HW48PF) - Fire TV music player. `Jellyfin` · `Fire TV`
- [JellyWave Mobile](https://apps.apple.com/de/app/jellywave-mobile/id6763198840) - Distraction-free music player for browsing artists, albums and songs. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Paid`
- [Jellywing](https://github.com/birdrock00/jellywing) - Native Android music player. `Jellyfin` · `Android` · `GPL-3.0` `Free`
- [JellyWisp](https://github.com/SofStartsFires/JellyWisp) - Customisable music client. `Jellyfin` · `Windows` · `Open source` `Free`
- [jel-music-app](https://github.com/obiwanconobi/jel-music-app) - Flutter music app. `Jellyfin` · `Windows` `Android` `Android Auto` · `MIT` `Free`
- [Jerry's Simple MP3](https://apps.apple.com/tw/app/jerrys-simple-mp3/id6797705211) - Local music player with playlists and Liked Songs, aimed at in-car listening. `Jellyfin` · `iOS` `iPadOS` · `Free`
- [jfMusic](https://github.com/esmondmissen/jfMusic) - iOS music client. `Jellyfin` · `iOS` · `GPL-3.0` `Free` `Stale 2020`
- [Jojk](https://github.com/BusterLandstrom/Jojk) - Cross-platform desktop music player built with Avalonia. `Jellyfin` · `Windows` · `MIT` `Free`
- [Jukebox](https://apps.apple.com/us/app/jukebox-offline-music-player/id6775927655) - Offline music player for iPhone, iCloud, WebDAV, NAS and server music, with vocal-removal karaoke. `Jellyfin` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [kiiaud](https://github.com/kii-notes/kiiaud) - Rust bit-perfect music player that also talks to LMS and MPD. `Jellyfin` · `Windows` `Linux` `Android` · `Apache-2.0` `Free`
- [Kikidame](https://github.com/t-seki/kikidame) - Offline-first player for recorded radio shows. `Jellyfin` · `Android` `Android Auto` · `MPL-2.0` `Free`
- [Kopuz](https://kopuz.moe) - Linux music player that also plays local files and YouTube Music. `Jellyfin` · `Linux` · `Open source` · [Flathub](https://flathub.org/apps/moe.kopuz.kopuz)
- [Lidifin](https://github.com/jamzercise/lidifin) - Jellyfin music client derived from the Lidify music app. `Jellyfin` `+Audiobookshelf` · `Web` `Android TV` `Fire TV` · `GPL-3.0` `Free`
- [LudyAmp](https://apps.apple.com/us/app/ludyamp-offline-music-player/id6759071307) - Offline-first music player for FLAC, ALAC, DSD and Opus with a 10-band equalizer and server streaming. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [Lyris](https://apps.apple.com/us/app/lyris-navidrome-player/id6764873657) - Native music player for self-hosted servers with no account or tracking; trial, then a one-time unlock. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Manet Music](https://apps.apple.com/us/app/manet-music/id6470928235) - iPhone music player with CarPlay and Siri. `Jellyfin` · `macOS` `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Meringo](https://meringo.app) - Paid Android music player. `Jellyfin` · `Android` `Android Auto` · `Paid`
- [Modshin](https://github.com/pbhLBOLBvZSH/Modshin) - Modified Feishin music player. `Jellyfin` `+Subsonic` · `Windows` `Linux` · `GPL-3.0` `Free`
- [Moonjelly](https://apps.apple.com/us/app/moonjelly-jellyfin-player/id6792574140) - Ad-free Jellyfin music player that streams straight from your own server. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Musicfin](https://apps.apple.com/tw/app/musicfin/id6810962920) - Jellyfin music player with lyrics, a play queue and Quick Connect sign-in. `Jellyfin` · `iOS` `iPadOS` · `Free` · [Source](https://github.com/qtmleap/Musicfin)
- [Musify](https://github.com/Bulma1337/musify) - Music player for Subsonic-style and Jellyfin servers. `Jellyfin` `+Subsonic` · `Windows` · `Open source` `Free`
- [Musifyn](https://github.com/0x80070006/Musifyn) - Flutter music client for Android. `Jellyfin` · `Android` · `MIT` `Free`
- [Namida](https://github.com/namidaco/namida) - Flutter music and video player with multiple libraries and offline caching for server sources. `Jellyfin` `+Subsonic` · `Windows` `Android` `Android Auto` · `Open source`
- [NAS Music Mobile](https://github.com/lahuolou/NAS-Music-mobile) - Android music player for a NAS music library. `Jellyfin` `+Subsonic` · `Android` `Android Auto` · `Open source` `Free`
- [NAS Music TV](https://gitee.com/liang_SL/NASMusicTV) - Android TV music player with lyrics, an equalizer and FFT visualisers. `Jellyfin` `+Subsonic` · `Android TV`
- [Nautica](https://github.com/truthadam01/Nautica-Web-Music-Player-for-Jellyfin) - Browser-based music player. `Jellyfin` · `Web` · `Open source` `Free`
- [Nautune](https://apps.apple.com/us/app/nautune/id6754812208) - Flutter-based Jellyfin music player with a deep-sea theme. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [NimiBeats](https://github.com/gitevanh/nimibeats) - Simple music player for a Jellyfin library. `Jellyfin` · `Web` · `GPL-3.0` `Free`
- [NoisePort](https://github.com/raxmou/noiseport) - Feishin-based music player. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free`
- [OceanWaves](https://play.google.com/store/apps/details?id=com.zfredesign.myapplicationdump) - Android music player with offline files (transcoded or original) and synced lyrics. `Jellyfin` · `Android` · `Free`
- [Omagawd](https://github.com/davidjpramsay/OmaGAWD) - Winamp-style music player for Omarchy Linux and macOS. `Jellyfin` · `macOS` `Linux` · `MIT` `Free`
- [PixelPlayerOSS](https://f-droid.org/packages/com.lostf1sh.pixelplayeross/) - Android music player. `Jellyfin` `+Subsonic` · `Android` · `Open source`
- [PulseFin](https://github.com/AryanKingSir/PulseFin) - Music player. `Jellyfin` · `Android` · `GPL-3.0`
- [Qcm](https://github.com/hypengw/Qcm) - Linux music player that also streams NetEase Cloud Music. `Jellyfin` `+Subsonic` · `Linux` · `GPL-2.0` · [Flathub](https://flathub.org/apps/io.github.hypengw.Qcm)
- [Rakki](https://github.com/LuckiRakki/rakki) - Music client for iPhone and desktop with word-by-word synced lyrics. `Jellyfin` · `Windows` `Linux` `iOS` · `AGPL-3.0` `Free`
- [redfin](https://github.com/kodydeda4/redfin) - Music player. `Jellyfin` · `macOS` `iOS` · `Open source`
- [Reeltone](https://apps.apple.com/us/app/reeltone-music-for-jellyfin/id6792892065) - Jellyfin music player with background playback, offline downloads, AirPlay and synced lyrics. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free`
- [RePlay](https://github.com/Utsavrajputt/Replay) - Android media player fork that adds music sources. `Jellyfin` `+Subsonic` · `Android` · `AGPL-3.0` `Free`
- [Resonus](https://github.com/juananzzz/resonus) - Music player for Jellyfin, Navidrome and OpenSubsonic servers and local files. `Jellyfin` `+Subsonic` · `Android` `iOS` `Android Auto` · `GPL-3.0`
- [RewindAmp](https://github.com/rknell/rewindamp) - Winamp-style Android music player. `Jellyfin` · `Android` `Android Auto` · `MIT` `Free`
- [Rhythm](https://github.com/cromaguy/Rhythm) - Android music player. `Jellyfin` `+Subsonic` · `Android` · `GPL-3.0` · [F-Droid](https://f-droid.org/packages/chromahub.rhythm.app/) · [Google Play](https://play.google.com/store/apps/details?id=chromahub.rhythm.play)
- [Rivelo](https://apps.apple.com/us/app/rivelo/id6807153144) - Music player that merges a private library with Apple Music and imports Apple Music playlists. `Jellyfin` · `macOS` `iOS` `CarPlay` · `Free`
- [RockyStereo](https://apps.apple.com/us/app/rockystereo/id6747009914) - Mac audio player with dynamic range compression and other audio processing; imports a server music library. `Jellyfin` · `macOS` · `Paid` `Stale 2025`
- [Segue](https://github.com/segue-music/segue-app) - Music player for several self-hosted servers. `Jellyfin` `+Subsonic` · `Windows` `Linux` `Android` `iOS` `Android TV` `Android Auto` · `MIT` `Free`
- [Shrimphony](https://apps.apple.com/us/app/shrimphony/id6809664949) - Focused Jellyfin music player with albums, artists, genres, playlists and grouped search. `Jellyfin` · `Android` `iOS` `iPadOS` `CarPlay` `Android Auto` · `Free` · [Source](https://github.com/HucksleyNash/shrimphony)
- [Sillon Musique](https://apps.apple.com/us/app/sillon-musique/id6822914803) - Jellyfin music player with lossless playback, synced lyrics and a Cover Flow album browser. `Jellyfin` · `macOS` `iOS` `CarPlay` `watchOS` · `Free`
- [Sonarune](https://github.com/Ariazonaa/sonarune) - Desktop music client built with Tauri and Svelte. `Jellyfin` · `Windows` · `GPL-3.0` `Free`
- [Sonethyst](https://github.com/sqwiziiy/Sonethyst) - Customisable Android music player. `Jellyfin` `+Subsonic` · `Android` `Android Auto` · `GPL-3.0` `Free`
- [Songsta](https://github.com/steggi-bernd/Songsta) - Music player for your own collection on Windows, Linux and Android. `Jellyfin` `+Subsonic` · `Windows` `Linux` `Android` · `GPL-3.0` `Free`
- [Sonixd Redux](https://github.com/joffrey-b/Sonixd-Redux) - Desktop music client forked from Sonixd. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Subatomic](https://apps.apple.com/us/app/subatomic-navidrome-client/id6761458858) - iOS client for self-hosted music servers that streams audio in chunks. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` · `Paid`
- [SubSonify](https://apps.apple.com/us/app/navidrome-player-subsonify/id6483939229) - Music client for Subsonic-API servers with offline mode, CarPlay and an Apple Watch app. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [SunnySong](https://github.com/xsunnygal/SunnySong) - Music player for Android and Linux. `Jellyfin` · `Linux` `Android` `Android Auto` · `MIT` `Free`
- [Supersonic](https://github.com/supersonic-app/supersonic) - Desktop music player. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free` · [Flathub](https://flathub.org/apps/io.github.dweymouth.supersonic)
- [Triptych](https://github.com/greenythebeany/triptych) - Music app for a Jellyfin library. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` · `MIT` `Free`
- [Tune](https://gitee.com/pengtang1024/tune) - Flutter music player for local files and self-hosted music servers. `Jellyfin` `+Subsonic` · `Linux` · `MIT`
- [ViBE](https://apps.apple.com/us/app/vibe-personal-music-player/id6786501269) - Album-first Jellyfin music player with offline downloads and landscape mode. `Jellyfin` · `iOS` · `Free`
- [VoidCast](https://github.com/ronnyporsch/Voidcast) - Music client with YouTube integration. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Web` `Android` `Android Auto` · `Open source` `Free`
- [Vynody](https://github.com/axel10/vynody) - Flutter music player that streams from Navidrome or Jellyfin. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` · `GPL-3.0` · [App Store](https://apps.apple.com/app/id6799339894) · [Microsoft Store](https://apps.microsoft.com/detail/9NMZRZZ6RSD3)
- [xsMusic](https://apps.apple.com/us/app/xsmusic/id6743747005) - Jellyfin music player for streaming and downloading your library. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Free` · [App Store](https://apps.apple.com/us/app/xsmusic-player/id6743954138)
- [ZMT](https://github.com/Rezerox39/zmt) - Terminal-inspired Android music player. `Jellyfin` · `Android` `Android Auto` · `GPL-3.0` `Free`
- [掌音](https://apps.apple.com/tw/app/%E6%8E%8C%E9%9F%B3/id6779252636) - Music player for self-hosted libraries with local playback and customizable CarPlay buttons. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`
- [散帅播放器](https://apps.apple.com/cn/app/%E6%95%A3%E5%B8%85%E6%92%AD%E6%94%BE%E5%99%A8-nas%E9%9F%B3%E4%B9%90%E6%92%AD%E6%94%BE%E5%99%A8/id6784067140) - NAS music player with quality presets, SMB import and CarPlay browsing. `Jellyfin` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Free`

### Emby music

- [aurora-emby-music](https://github.com/ywhgh/aurora-emby-music) - Web music player. `Emby` · `Web` · `Open source`
- [EMU](https://emby.media/community/topic/139893-emu-emby-music-player/) - Android music player. `Emby` · `Android`
- [liquidWave](https://github.com/liquidguru/emby-sonic) - Android player for music and audiobooks with Android Auto. `Emby` · `Web` `Android` `Android Auto` · `Beta`
- [Mopidy-Emby](https://pypi.org/project/Mopidy-Emby/) - Mopidy extension that plays music from an Emby server. `Emby` · `Linux` · `Open source` `Stale 2017`
- [Navid Music](https://apps.apple.com/us/app/navid-music-clear-hifi-player/id6786164266) - Music player with lyrics and a Metro-inspired design for Navidrome, Subsonic, Emby and local libraries. `Emby` `+Subsonic` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`
- [Player](https://github.com/WXFY/Player) - Android music player app. `Emby` `+Subsonic` · `Android` · `Open source` `Free`
- [Siansa](https://emby.media/community/topic/150390-siansa/) - Android music player. `Emby` · `Android`
- [SylphyMusic](https://github.com/ymltsh/SylphyMusic) - Multi-source music player that also streams from WebDAV. `Emby` `+Subsonic` · `Windows` `Android` · `MIT` `Free`
- [Sylvakru](https://apps.apple.com/us/app/sylvakru/id6783824639) - Music player for local files and Navidrome, WebDAV, Emby and Feiniu Music with a 10-band equalizer. `Emby` `+Subsonic` · `Windows` `macOS` `Linux` `Android` `iOS` `iPadOS` `Android TV` · `Free` · [Source](https://github.com/AfalpHy/sylvakru)
- [Traxx](https://emby.media/community/topic/148035-introducing-traxx-an-android-music-app-built-for-emby-music-libraries/) - Android music player. `Emby` · `Android`
- [Waca](https://apps.apple.com/us/app/waca/id6748253402) - Local music player with 3D particle visualizations, supporting NAS and server sources. `Emby` `+Subsonic` `+fnOS` · `macOS` `iOS` `iPadOS` `watchOS` · `Free`
- [静听](https://apps.apple.com/us/app/%E9%9D%99%E5%90%AC-%E6%9C%AC%E5%9C%B0%E6%97%A0%E6%8D%9F%E9%9F%B3%E4%B9%90%E6%92%AD%E6%94%BE%E5%99%A8%E4%B8%8E%E7%A6%BB%E7%BA%BFmp3%E4%BC%A0%E6%AD%8C%E7%A5%9E%E5%99%A8/id6755151133) - Lossless local music player with Wi-Fi transfer, cloud-drive sources and CarPlay. `Emby` `+Subsonic` · `iOS` `iPadOS` `CarPlay` · `Freemium`

## Audiobooks, books and photos

Audiobook players and book or comic readers and photo viewers.

### Audiobooks

- [aBooks](https://apps.apple.com/br/app/abooks-app/id6812074500) - Self-hosted audiobook player with chapters, resumable playback and offline downloads. `Plex` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Paid`
- [AudioBooks](https://apps.apple.com/us/app/audiobooks-mp3-m4b-player/id6471399965) - Audiobook player for DRM-free M4B, MP3 and FLAC files with chapters; ad-free, no tracking. `Jellyfin` `+Audiobookshelf` · `iOS` `iPadOS` · `Freemium`
- [Audiofin](https://apps.apple.com/tw/app/audiofin/id6786714515) - Audiobook player for a server library organized by author, book and series, with CarPlay. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [AudioNest](https://apps.apple.com/us/app/audionest-audiobook-player/id6811492203) - Audiobook player with character guides, read-along text and thousands of free classics. `Plex` `Jellyfin` `Emby` `+Audiobookshelf` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Free`
- [Awdio](https://apps.apple.com/us/app/awdio-audiobook-player/id6768204729) - Audiobook player that keeps five minutes of audio buffered ahead; also reads Audiobookshelf libraries. `Plex` `+Audiobookshelf` · `iOS` · `Freemium`
- [Bardley](https://apps.apple.com/us/app/bardley/id6747647606) - Privacy-first audiobook player with LibriVox access; Pro adds Jellyfin, iCloud sync and unlimited books. `Jellyfin` · `macOS` `iOS` `iPadOS` · `Freemium`
- [Bookcamp](https://apps.apple.com/us/app/bookcamp/id1523540165) - Audiobook player for Plex libraries with offline downloads, speed control and voice boost. `Plex` · `Android` `iOS` `Android Auto` · `Freemium` `Stale 2025` · [Google Play](https://play.google.com/store/apps/details?id=app.bookcamp.android)
- [Book Hut](https://apps.apple.com/de/app/b%C3%BCcher-h%C3%B6rb%C3%BCcher-von-hutapp/id6805440627) - Reading and audiobook player that syncs books, progress and bookmarks across devices. `Jellyfin` `+Audiobookshelf` · `iOS` `watchOS` · `Free`
- [BookPlayer](https://github.com/TortugaPower/BookPlayer) - Audiobook player for M4B, M4A, MP3 and FLAC that imports from files, AirDrop, Audiobookshelf and Jellyfin. `Jellyfin` `+Audiobookshelf` · `iOS` `iPadOS` `CarPlay` `watchOS` · `GPL-3.0` `Freemium` · [App Store](https://apps.apple.com/us/app/bookplayer/id1138219998)
- [Chronicle](https://github.com/mattttvaughn/chronicle) - Android audiobook player. `Plex` · `Android` `Android Auto` · `GPL-3.0` `Freemium` · [Google Play](https://play.google.com/store/apps/details?id=io.github.mattpvaughn.chronicle)
- [Chronicle Epilogue](https://github.com/fabiogermann/chronicle) - Android audiobook player with Android Auto. `Plex` · `Android` `Android Auto` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=local.oss.chronicle) · [Info](https://forums.plex.tv/t/reviving-chronicle-audiobook-app-for-plex/935438)
- [CLAUDIO](https://apps.apple.com/us/app/claudio-audiobooks-music/id6760961153) - Audiobook player for M4B and MP3 with chapters and sleep timer; server connections need a paid tier. `Jellyfin` `+Subsonic` `+Audiobookshelf` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Codex](https://apps.apple.com/de/app/codex-audiobook-player/id6759009860) - Audiobook player with three interface skins, including a Braun-inspired dial design. `Jellyfin` `+Audiobookshelf` · `iOS` `CarPlay` · `Paid`
- [Jellyfin-Audiobook](https://github.com/adSORRYvance/Jellyfin-Audiobook) - Server plugin that replaces the web player with a chapter-aware audiobook player. `Jellyfin` · `Web` · `Open source`
- [Listen Audiobook Player](https://play.google.com/store/apps/details?id=com.acmeandroid.listen) - Audiobook player that downloads books from your own server. `Plex` `+Audiobookshelf` · `Android` `Android Auto` · `Paid`
- [Listening Library](https://apps.apple.com/us/app/listening-library/id6778243568) - Audiobook player for iCloud, Google Drive, servers and local files, with sleep timer and widgets. `Plex` `Jellyfin` `+Audiobookshelf` · `iOS` `iPadOS` `watchOS` · `Free`
- [Lysn](https://apps.apple.com/us/app/lysn-audiobook-player/id6756090240) - Audiobook player for imported books and self-hosted servers, with streaming or download. `Plex` `+Audiobookshelf` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium`
- [OnyxAudiobookPlayer](https://github.com/adamskoog/OnyxAudiobookPlayer) - Web audiobook player for Plex. `Plex` · `Web` · `Open source` `Free` `Stale 2025`
- [OperaLibre](https://apps.apple.com/cn/app/operalibre/id6792065037) - Audiobook player for a self-hosted server with background playback and saved positions. `Jellyfin` · `iOS` `iPadOS` `CarPlay` · `Free`
- [Plappa](https://github.com/LeoKlaus/plappa) - iPhone audiobook player. `Jellyfin` `Emby` `+Audiobookshelf` · `iOS` `iPadOS` `CarPlay` `watchOS` · `Open source` `Freemium` · [App Store](https://apps.apple.com/app/id6475201956)
- [PrivateShelf](https://apps.apple.com/us/app/privateshelf-shelf-for-plex/id6758427607) - Audiobook player that skips intros and outros, built for listening comfort. `Plex` · `iOS` · `Free`
- [Prologue](https://prologue.audio) - Audiobook player for Plex and Audiobookshelf libraries with offline downloads and CarPlay. `Plex` `+Audiobookshelf` · `Android` `iOS` `iPadOS` `CarPlay` `watchOS` · `Freemium` · [App Store](https://apps.apple.com/app/id1459223267) · [Google Play](https://play.google.com/store/apps/details?id=audio.prologue.android)
- [Recto](https://apps.apple.com/us/app/recto-audiobooks/id6763444940) - Native audiobook player with an Apple Music-inspired interface for a server library. `Plex` · `iOS` `iPadOS` `CarPlay` · `Free`
- [saga](https://github.com/gaut3/saga) - Native Android audiobook player for Plex. `Plex` · `Android` `Android Auto` · `MIT` `Free` · [Website](https://saga-app.no)
- [Sennachie](https://github.com/user256/Sennachie-Audiobooks-and-Music-Player-for-Plex) - Android audiobook and music player shipped as a signed APK. `Plex` · `Android` · `Open source`
- [TomeRoam](https://github.com/nzilberberg/TomeRoam) - Audiobook player. `Plex` · `Web` `Android` · `Open source`
- [Verbook](https://apps.apple.com/us/app/verbook/id6823258134) - Audiobook and music client with bookshelf browsing, series tracking and downloads. `Plex` · `iOS` `iPadOS` · `Paid`
- [Voca Player](https://apps.apple.com/us/app/voca-player/id6762044756) - Simple audiobook player for a self-hosted server or files on the device. `Plex` `+Audiobookshelf` · `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Freemium`
- [Volume](https://play.google.com/store/apps/details?id=com.hyperfixation.volume) - Android audiobook player. `Plex` `Jellyfin` `+Audiobookshelf` · `Android` `Android Auto`
- [Yarnplayer](https://apps.apple.com/br/app/yarnplayer/id6783205138) - Audiobook and podcast player with search by what was said and ad skipping. `Plex` `+Audiobookshelf` · `iOS` `iPadOS` `tvOS` `CarPlay` `watchOS` · `Free`
- [听见有声](https://apps.apple.com/us/app/%E5%90%AC%E8%A7%81%E6%9C%89%E5%A3%B0-%E5%85%A8%E8%83%BD%E6%9C%89%E5%A3%B0%E4%B9%A6%E6%92%AD%E6%94%BE%E5%99%A8/id6770381502) - Audiobook player with chapters, downloads and local import for NAS and fnOS libraries. `Emby` `+Audiobookshelf` `+fnOS` · `iOS` `iPadOS` `CarPlay` · `Paid`

### Books, comics and manga

- [Codex Reader](https://apps.apple.com/br/app/codex-reader-early-access/id6762022936) - Reader and listener that gathers EPUBs, M4Bs and MP3 audiobooks from several sources into one shelf. `Plex` `+Audiobookshelf` `+OPDS` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Cosmic Comics](https://github.com/Nytuo/CosmicComics) - Comic, manga and ebook reader that integrates with a Jellyfin library. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` · `GPL-3.0` `Free` · [Snap](https://snapcraft.io/cosmiccomics)
- [Fathom (Get-Coral)](https://github.com/Get-Coral/fathom) - Reading room for books, manga, comics and PDFs stored in Jellyfin. `Jellyfin` · `Web` · `Open source` `Free`
- [JellyBook](https://github.com/JellyBookOrg/JellyBook) - Reader for ebooks and comics that also plays audiobooks. `Jellyfin` · `Android` `iOS` · `MIT` `Free`
- [KiokuYomi](https://apps.apple.com/tw/app/kiokuyomi/id6795781367) - Manga and article reader with site rules and CBZ/PDF import that also opens Komga, Kavita, OPDS and Jellyfin sources. `Jellyfin` `+Komga` `+Kavita` `+OPDS` · `iOS` `iPadOS` · `Free`
- [Kurage](https://github.com/lkcv/Kurage) - Manga and comic reader. `Jellyfin` · `Android` · `MIT` `Free`
- [Mihon Jellyfin extension](https://github.com/keiyoushi/extensions-source) - Mihon source extension for reading manga from the server on Android. `Jellyfin` · `Android` · `Apache-2.0`
- [music-manga-linux](https://github.com/xHitech/music-manga-linux) - Linux desktop client for music, manga and audiobooks. `Jellyfin` · `Linux` · `Open source` `Free`
- [Nebula Reader](https://github.com/NotTimm/NebulaReader) - Comic, manga and ebook reader for Linux, Windows and macOS desktops. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free`
- [Stacks](https://github.com/rob-land/stacks) - GTK4 ebook reader for mobile Linux. `Jellyfin` · `Linux` · `GPL-3.0` `Free`

### Photos

- [MediaWall](https://github.com/nothing2obvi/mediawall) - Self-hosted display for Jellyfin and Subsonic libraries. `Jellyfin` `+Subsonic` · `Web` · `AGPL-3.0` `Free`
- [nFolio](https://play.google.com/store/apps/details?id=com.snapwood.nfolio) - Photo viewer for NAS, SMB and DLNA sources. `Plex` `Jellyfin` `Emby` · `Android` `Android TV`
- [Phlix Photos](https://apps.apple.com/us/app/phlix-photos/id6796820208) - Plex photo library viewer with folders, a date timeline, year scrubber, slideshows and search. `Plex` · `iOS` `iPadOS` · `Freemium`
- [PhotoFalls](https://apps.apple.com/us/app/photofalls/id6792492433) - Plex photo library app that builds a local index so large libraries scroll instantly. `Plex` · `iOS` `iPadOS` · `Free`
- [pix](https://github.com/betta-apps/pix) - Android TV screensaver that shows photos from a Plex library. `Plex` · `Android TV` · `MIT` `Free`
- [Plex-Pix](https://github.com/Kahenis/Plex-Pix) - Android TV app for browsing Plex photos and videos. `Plex` · `Android TV` · `Open source` `Free`
- [PlexPix-Player](https://github.com/Kahenis/PlexPix-Player) - Android viewer for Plex photos and videos. `Plex` · `Android` · `Open source` `Free`
- [Posterrama](https://github.com/Posterrama/posterrama) - Self-hosted screensaver that cycles posters from your library. `Plex` `Jellyfin` `Emby` · `Web` · `GPL-3.0`

## Live TV and channel apps

IPTV players that also read media servers. Apps that turn a library into scheduled channels.

- [90sTV](https://apps.apple.com/us/app/90stv-retro-tv-channels/id6800050490) - Turns a Jellyfin movie and show library into always-running retro TV channels you tune into. `Jellyfin` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Airwave](https://github.com/Quixomatic/Airwave) - Self-hosted service that turns the library into 24/7 channels, with its own TV, desktop and web players. `Plex` · `Windows` `macOS` `Linux` `Web` `iPadOS` `Android TV` `Fire TV` `tvOS` `Roku` `webOS` `Tizen` · `Open source` `Paid`
- [analoq](https://github.com/Robot-Duck-32/analoq) - Apple TV app that turns Plex collections into TV-style channels. `Plex` · `tvOS` · `GPL-3.0` `Free`
- [AnyTV](https://apps.apple.com/us/app/anytv-iptv-player-m3u-xtream/id6450650101) - IPTV and library player for M3U, Xtream and server sources with posters, episode guides and a TV guide. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Subscription`
- [AutoTV](https://apps.apple.com/us/app/autotv-iptv-player/id6819201356) - Ad-free IPTV player for M3U, Xtream Codes and media server sources with live channels, movies and series. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Free`
- [Bingr](https://apps.apple.com/us/app/bingr/id6821401598) - IPTV and media server player with profiles, a TV guide and sync across Apple devices. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Bunny Ears TV](https://testflight.apple.com/join/NdaJfb9n) - Apple TV app that turns your library into live TV with a cable-style guide and channel surfing. `Plex` · `tvOS` · `Beta`
- [BurgTV](https://apps.apple.com/br/app/burgtv-player-m3u-xtream/id6761636987) - IPTV player for M3U playlists, Xtream Codes and portals that also connects to a media server. `Jellyfin` `+IPTV` · `iOS` `iPadOS` · `Freemium`
- [Cable Stream](https://www.reddit.com/r/TestFlight/comments/1s8oyo6/cable_stream_beta_testflight_cable_tv_from_plex/) - Cable-TV-style app with auto-channels by genre, decade, series and mood, and an EPG grid. `Plex` · `tvOS` · `Beta`
- [Cablex](https://testflight.apple.com/join/6XjjJdSH) - Turns your library into themed 24/7 channels for TV-style channel surfing. `Plex` · `tvOS` · `Beta`
- [CarCast](https://apps.apple.com/us/app/carcast-m3u-iptv-player-m3u8/id6820999972) - M3U IPTV player and cast app that also reads a media server and shows on a parked car display. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Freemium`
- [CarTV (Avaniben Sardhara)](https://apps.apple.com/us/app/cartv-m3u-iptv-player-cast/id6818045286) - IPTV and M3U player for iPhone and CarPlay that also connects private media servers. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Freemium`
- [CarTV (Lyntra)](https://apps.apple.com/us/app/cartv-m3u-iptv-player-cast/id6800211040) - M3U playlist player with iPhone screen mirroring to the car display, for use when parked. `Jellyfin` `Emby` `+IPTV` · `iOS` · `Free`
- [CarTVPro](https://apps.apple.com/us/app/cartvpro-playlist-player/id6818544027) - Playlist player that mirrors the iPhone to CarPlay or plays your own channel lists on the car screen when parked. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Freemium`
- [cinefin/cinefin](https://github.com/cinefin/cinefin) - Home-theater playout app that runs a programme schedule from library media through mpv. `Plex` `Jellyfin` · `Windows` `Linux` · `AGPL-3.0`
- [Coax](https://apps.apple.com/app/id6752622762) - iPhone and Apple TV app that presents the library as a cable-style channel guide. `Plex` `Jellyfin` `Emby` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `CarPlay` · `Freemium`
- [Cordbox](https://apps.apple.com/us/app/cordbox-iptv-media-player/id6788759297) - IPTV and media player that brings playlists, portals, media servers and network shares into one app, with recordings. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free`
- [Crivid IPTV Player](https://apps.apple.com/us/app/crivid-iptv-player-m3u-xtream/id6783083716) - IPTV player for M3U playlists and Xtream logins that can also connect media servers and tuners. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Cuspart](https://apps.apple.com/us/app/cuspart-iptv/id6812349140) - IPTV player for M3U, Xtream Codes and Stalker portals, organised into a library with resume and favourites. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Freemium`
- [Dino IPTV Player](https://apps.apple.com/us/app/dino-iptv-player/id6799335873) - IPTV player for your own Xtream Codes login or M3U playlist, with media server libraries as extra sources. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Paid`
- [DriveTV](https://apps.apple.com/us/app/drivetv-car-iptv-m3u-player/id6824541941) - M3U and Xtream player with Jellyfin and Emby import that plays on iPhone and in CarPlay. `Jellyfin` `Emby` `+IPTV` · `iOS` `CarPlay` · `Freemium`
- [Hectic TV](https://apps.apple.com/us/app/hectic-tv-tv-player/id6820662503) - Live TV player for Xtream Codes, M3U and Jellyfin sources with an XMLTV guide, movies and series. `Jellyfin` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `watchOS` · `Freemium`
- [HOMEKING](https://apps.apple.com/br/app/homeking/id6796014292) - IPTV player for Xtream accounts and M3U playlists with XMLTV guides, plus Jellyfin libraries. `Jellyfin` `+IPTV` · `iOS` `iPadOS` · `Free`
- [IPTViX](https://apps.apple.com/ru/app/iptv-%D0%BF%D0%BB%D0%B5%D0%B5%D1%80-%D0%B8-%D1%82%D0%B2-%D0%B3%D0%B8%D0%B4-iptvix/id6762452941) - IPTV player with TV guide, catch-up and Xtream support that also reads Plex and SMB shares. `Plex` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [IPTVX](https://apps.apple.com/us/app/iptvx/id1451470024) - IPTV player for live TV, movies and shows that also reads server and SMB sources. `Plex` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [Kine](https://apps.apple.com/us/app/kine-iptv-m3u-xtream-player/id6778128277) - VLC-powered IPTV player with a programme guide and global search. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Free`
- [LillyPlayer](https://apps.apple.com/fr/app/lillyplayer-iptv-player/id1446967273) - IPTV and Xtream player with a live TV guide, replay and a movie and series catalog. `Plex` `Jellyfin` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [LiveFin](https://github.com/LiveFin/LiveFin) - Live TV-only client for iPhone, iPad and Apple Watch. `Jellyfin` · `iOS` `iPadOS` `watchOS` · `GPL-3.0` · [App Store](https://apps.apple.com/app/id6748318433)
- [Mediavyr Player](https://apps.apple.com/us/app/mediavyr-player/id6810717224) - IPTV and media library player with a programme guide, covering live TV, movies and series. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Melyro](https://apps.apple.com/us/app/melyro-iptv-player/id6812315758) - IPTV player for your own playlists and media server sources, with no built-in channels. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [nexStream](https://github.com/nexStream-app/nexStream) - IPTV player for TV boxes that can also open media-server libraries. `Plex` `Jellyfin` `+IPTV` · `Android` `Android TV` `Fire TV` · `Paid`
- [NostalgiaTV](https://play.google.com/store/apps/details?id=com.nostalgiatv) - Android and Android TV app that plays your library as a retro cable lineup. `Plex` `Jellyfin` `Emby` · `Android` `Android TV`
- [NowSeen](https://apps.apple.com/us/app/nowseen-iptv-media-player/id6780634050) - IPTV player for Apple TV and iPhone that also plays media-server libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [OneTV Connect](https://apps.apple.com/us/app/onetv-connect-iptv-player/id6756811791) - IPTV player for M3U playlists, Xtream Codes and media server sources, with a carousel home screen. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` `watchOS` · `Freemium`
- [OtusTV](https://apps.apple.com/br/app/otustv-liptv-bien-au-chaud/id6816083887) - IPTV and media player that adds M3U lists, subscriptions, media servers and your ISP box channel list. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [PlaylistTV](https://apps.apple.com/us/app/playlisttv/id6804035471) - Mac app that turns playlists and collections into TV channels that start playing when picked. `Plex` · `macOS` `tvOS` · `Freemium`
- [Popcorn](https://github.com/netpersona/Popcorn) - Self-hosted channel generator with a TV guide that plays in its web player or on Plex clients. `Plex` · `Web` · `GPL-3.0`
- [QuasiTV](https://www.quasitv.app/) - Builds linear TV-style channels from your own library, with a channel guide. `Plex` `Jellyfin` `Emby` · `Fire TV` · [Amazon](https://www.amazon.com/Quasi-TV-Unlimited-Custom-Channels/dp/B0921KRNMQ)
- [RetroGuide.TV](https://apps.apple.com/us/app/retroguide-tv/id6816213425) - Turns a media library into always-on TV channels with a schedule and program guide. `Plex` `Jellyfin` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Smart IPTV APP](https://apps.apple.com/us/app/smart-iptv-app/id6790420279) - IPTV player for your own M3U playlists and Xtream accounts, with media server and network sources. `Plex` `+IPTV` · `iOS` · `Free`
- [Sparkle TV](https://play.google.com/store/apps/details?id=se.hedekonsult.sparkle) - Live TV player with EPG that pulls channels from server live TV, HDHomeRun, Tvheadend, Enigma2 and Xtream. `Plex` `Jellyfin` `+IPTV` · `Android TV` `Fire TV` · `Freemium`
- [Squire](https://apps.apple.com/gb/app/xtream-iptv-player-squire/id951483331) - IPTV and media client for Xtream Codes, M3U, Put.io and home servers, organised in one place. `Plex` `Jellyfin` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [Stream Setu](https://apps.apple.com/br/app/stream-setu/id6821526110) - IPTV and media server player for M3U and Xtream lists, tuners and servers, covering live TV, movies and shows. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` · `Free`
- [StreamX](https://apps.apple.com/gb/app/streamx-iptv-player-m3u/id6755919340) - IPTV player for M3U and Xtream playlists that also browses movie and series libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [Syravo](https://apps.apple.com/us/app/syravo-iptv-m3u-player/id6797567023) - Xtream Codes and M3U player with live TV, movies and series, plus Jellyfin and Emby servers. `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` `visionOS` · `Freemium`
- [Telora Player](https://apps.apple.com/us/app/telora-player/id6821877987) - IPTV and media server player that puts channels, movies and shows in one interface. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Subscription`
- [Tivsy](https://apps.apple.com/br/app/tivsy-player-iptv-m3u/id6795955479) - IPTV player for M3U lists, Xtream panels and media servers with posters, synopses and a time-ordered guide. `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Tub IPTV](https://apps.apple.com/br/app/tub-iptv/id6795949531) - IPTV player for M3U links, Xtream panels, a Plex server or an SMB library. `Plex` `+IPTV` · `iOS` `iPadOS` `CarPlay` · `Freemium`
- [Tuneline](https://tuneline.app/) - Cross-platform M3U and Xtream player that can also play media from home servers. `Plex` `Jellyfin` `Emby` `+IPTV` · `Windows` `macOS` `Linux` `Android` `Android TV` `Fire TV` · `Freemium`
- [UHF](https://apps.apple.com/us/app/uhf-love-your-iptv/id6443751726) - IPTV player for Apple devices that also plays media-server libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Freemium`
- [Veoday](https://apps.apple.com/us/app/veoday/id6799393674) - Personal media player for playlists, provider accounts and media servers with live TV and favourites. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` `visionOS` · `Free`
- [Vireko](https://apps.apple.com/us/app/vireko-iptv-player/id6778041611) - IPTV player for playlists, portals and media servers with a real program guide; a paid tier unlocks libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `macOS` `iOS` `iPadOS` `tvOS` · `Freemium`
- [Zaply](https://apps.apple.com/us/app/zaply-iptv-player-live-tv/id6817406667) - IPTV player for M3U and Xtream lists that also plays media-server libraries. `Plex` `Jellyfin` `Emby` `+IPTV` · `iOS` `iPadOS` `tvOS` `CarPlay` · `Freemium`

## Niche platforms

Apps for consoles and headsets and cars and watches. Also TV systems and Kodi and terminals and other less common platforms.

### Consoles and homebrew

- [3d-jelly](https://github.com/8-bitStudio/3d-jelly) - Unofficial Nintendo 3DS homebrew app for playing your library. `Jellyfin` · `3DS` · `GPL-2.0` `Free`
- [3DSfin](https://github.com/arechawla/3DSfin) - Work-in-progress app for the New Nintendo 3DS. `Jellyfin` · `3DS` · `GPL-3.0` `Free` `Beta`
- [Couch PiP](https://github.com/CaraJean206/couch-pip) - Steam Deck Decky plugin that shows web apps such as Plex or Jellyfin in a picture-in-picture window. `Plex` `Jellyfin` · `Steam Deck` · `BSD-3-Clause`
- [decky-plex-audiobooks](https://github.com/indyjamesb/decky-plex-audiobooks) - Steam Deck Decky plugin for listening to audiobooks. `Plex` · `Steam Deck` · `MIT`
- [DualPlex](https://github.com/thoughts3rased/DualPlex) - Nintendo 3DS homebrew music player. `Plex` · `3DS` · `Open source`
- [Emby5](https://github.com/bornaradusin/Emby5) - Native app for jailbroken PS5 with hardware H.264/HEVC decoding and HDR. `Jellyfin` `Emby` · `PS5` · `GPL-3.0` `Free`
- [Gelatinarm](https://github.com/gitman-101111/gelatinarm) - Native Xbox media client. `Jellyfin` · `Xbox` · `MIT` `Free`
- [Jelly3DS](https://github.com/DarthTigerson/Jelly3DS) - Work-in-progress app for the 3DS and New 3DS. `Jellyfin` · `3DS` · `Open source` `Free` `Beta`
- [Jelly5](https://github.com/02dnot/Jelly5) - Native app for jailbroken PS5 with hardware-decoded 4K HDR. `Jellyfin` `Emby` · `PS5` · `GPL-3.0` `Free`
- [JellyBox](https://github.com/dfederm/JellyBox) - Native Xbox app. `Jellyfin` · `Xbox` · `MIT` `Free`
- [JellyCTR](https://github.com/colokoko1/JellyCTR) - Nintendo 3DS homebrew app for browsing and playing your music library. No video yet. `Jellyfin` · `3DS` · `GPL-2.0` `Free`
- [jellyfin-3ds](https://github.com/bogocat/jellyfin-3ds) - Nintendo 3DS homebrew client. `Jellyfin` · `3DS` · `GPL-3.0`
- [JellyFin \[PS\]](https://github.com/jw-notes/JellyFin-PS3) - Homebrew client for PS3 (HEN or CFW) and jailbroken PS4, with USB and offline playback; the PS4 build direct-plays up to 1080p. `Jellyfin` · `PS3` `PS4` · `GPL-3.0` `Free` · [Source (original PS3)](https://github.com/MontyMcK/JellyFin-PS3) · [Source (lossless audio)](https://github.com/vortigauntlet/JellyFin-PS3-LosslessAudio) · [Source (PS4)](https://github.com/jw-notes/JellyFin-PS4)
- [jellyfin-ps2](https://github.com/jimmyBizMobile/jellyfin-ps2) - Homebrew PlayStation 2 client. `Jellyfin` · `PS2` · `MIT`
- [jellyfin-rg35xxh](https://github.com/aG00Dtime/jellyfin-rg35xxh) - Controller-first app for the Anbernic RG35XX H. `Jellyfin` · `Retro handheld` · `MIT` `Free`
- [m7-jellyfin](https://github.com/LouisMarotta/m7-jellyfin) - Movian plugin for PS3. `Jellyfin` · `PS3` · `GPL-3.0`
- [Minifin](https://github.com/zakijss/MiniFin) - Movies and shows on the Miyoo Mini Plus. `Jellyfin` · `Retro handheld` · `MIT` `Free`
- [MiSTerEmby](https://github.com/freemchr/MiSTerEmby) - MiSTer FPGA video player. `Emby` · `MiSTer` · `Open source` `Free`
- [MiSTerFin](https://github.com/puddingstudio/MiSTerFin) - MiSTer FPGA player for server-transcoded video, suited to CRT output. `Jellyfin` · `MiSTer` · `Open source` `Free` · [Info](https://www.reddit.com/r/MiSTerFPGA/comments/1v4khri/misterfin_v09_mister_fpga_jellyfin_client_first/)
- [mister_plex](https://github.com/mrchrisster/mister_plex) - Script that plays Plex library videos on a MiSTer FPGA over SSH. `Plex` · `MiSTer` · `Open source`
- [mistervision](https://github.com/trentnix/mistervision) - MiSTer FPGA client for watching your library on CRT TVs. `Plex` `Jellyfin` · `MiSTer` · `Open source`
- [Miyoofin](https://github.com/S3ggie/MiyooFin) - App for the Miyoo Mini Plus running Onion OS. `Jellyfin` · `Retro handheld` · `GPL-3.0` `Free`
- [Mufin](https://github.com/escal8tor/MuFin) - App for handhelds running muOS. `Jellyfin` · `Retro handheld` · `AGPL-3.0` `Free`
- [multiplex360](https://github.com/HG-ERIK/multiplex360) - Homebrew client for modded Xbox 360 consoles. `Plex` · `Xbox 360` · `GPL-3.0`
- [Museck](https://github.com/Nezreka/Museck) - Steam Deck plugin for streaming a music library. `Plex` `Jellyfin` `Emby` `+Subsonic` · `Steam Deck` · `MIT`
- [Pelagia](https://github.com/steredbits/pelagia) - Unofficial app for jailbroken PS5 homebrew. `Jellyfin` · `PS5` · `GPL-3.0` `Free`
- [Playfin](https://github.com/LowganDev/PlayfinPS4) - PS4 homebrew app with direct play of H.264, HEVC, VP9 and AV1 to 1080p. `Jellyfin` · `PS4` · `GPL-3.0` `Free`
- [plex-3ds](https://github.com/herdlevar/plex-3ds) - Nintendo 3DS homebrew client. `Plex` · `3DS` · `Open source`
- [PlexMusic.pak](https://github.com/thwonp/PlexMusicPak) - Plex music player pak for TrimUI Brick and other MinUI handhelds. `Plex` · `Retro handheld` · `Open source`
- [PocketFin](https://github.com/CidVonHighwind/pocketfin) - PSP homebrew app for browsing and playing your library. `Jellyfin` · `PSP` · `GPL-3.0` `Free`
- [PocketFlex](https://github.com/jackharvest/PocketFlex) - Client for the Miyoo Mini Plus retro handheld. `Plex` · `Retro handheld` · `MIT`
- [PSPStreamer](https://github.com/dreimer1986/PSPStreamer) - Sony PSP player backed by a transcoding server, with watch-status sync and MilkDrop visualisers. `Plex` `Jellyfin` · `Original Xbox` `PSP` · `GPL-2.0`
- [Resonant-PS3](https://github.com/daedra000/Resonant-PS3) - Homebrew Plex music player for the PlayStation 3. `Plex` · `PS3` · `GPL-2.0`
- [Saffron](https://github.com/xlanor/saffron) - Nintendo Switch homebrew client. `Plex` · `Switch` · `Apache-2.0`
- [sammwyy/jellyfish](https://github.com/sammwyy/jellyfish) - PlayStation 2 homebrew music player. `Jellyfin` · `PS2` · `Open source`
- [Slopfin](https://github.com/BeLikeBrett/SlopFin) - Jailbroken PS5 app with direct playback up to 4K and HDR10. `Jellyfin` · `PS5` · `GPL-3.0` `Free`
- [SSSPlayer](https://github.com/SergioSSantiago/SSSPlayer) - PS Vita music and video player with SMB, SFTP and WebDAV network sources. `Jellyfin` · `PS Vita` · `GPL-3.0`
- [Streamfin](https://github.com/dammitjeff/streamfin-switch) - Switch overlay that streams music in the background through Ultrahand. `Jellyfin` · `Switch` · `GPL-2.0` `Free`
- [Ufin](https://github.com/antu2010/Ufin-A-Wii-U-Jellyfin-client) - Wii U homebrew app; music, video and Live TV work on real hardware. `Jellyfin` · `Wii U` · `Open source` `Free` `Beta`
- [WiiFin](https://github.com/fabienmillet/WiiFin) - Nintendo Wii homebrew client. `Jellyfin` · `Wii` · `GPL-3.0`
- [YubariPlay](https://github.com/marjoefinn-spec/YubariPlay) - Switch video player that also opens cloud drives and WebDAV shares. `Jellyfin` `Emby` · `Switch` · `AGPL-3.0` `Free`

### VR and XR

- [4XVR](https://www.altlabvr.com/4xvr-video-player) - VR video player for Meta Quest, PICO and Apple Vision Pro. `Plex` `Jellyfin` `Emby` · `Quest` `Pico` `visionOS` · `Paid` · [Meta Store](https://www.meta.com/experiences/4xvr-video-player/5936567899722707/) · [App Store](https://apps.apple.com/app/id6737879659)
- [Aurora for Plex](https://apps.apple.com/app/id6547867554) - Apple Vision Pro client. `Plex` · `visionOS`
- [B0BEmby VR](https://github.com/wangbob-0787/B0BEmby-VR) - Virtual-cinema Emby client for the PICO 4. `Emby` · `Pico` · `Open source` `Free`
- [CineDepth](https://www.reddit.com/r/VisionPro/comments/1vhjxm1/cinedepth_my_2dto3d_video_app_now_supports/) - Vision Pro player that converts 2D video to 3D. `Plex` `Jellyfin` `Emby` · `visionOS` · `Free`
- [CineVoid](https://www.meta.com/en-gb/experiences/cinevoid-vr-media-player/1199393973267430/) - Meta Quest VR media player. `Plex` `Jellyfin` `Emby` · `Quest` · `Paid`
- [Depthray](https://www.meta.com/experiences/depthray-3d-video-player/1343679048826072/) - Meta Quest player that converts 2D video to 3D. `Plex` `Jellyfin` `Emby` `+Stremio addons` · `Quest` · `Free`
- [JellyTheatre](https://github.com/valentinp72/JellyTheatre) - Godot-based VR theatre client. `Jellyfin` · `Quest` · `GPL-3.0` · [Meta Store](https://www.meta.com/experiences/jellytheatre/4688003738150435/)
- [JellyVR](https://github.com/VersaYT/JellyVR) - Godot-based VR client. `Jellyfin` · `Quest` `PC VR` · `Apache-2.0`
- [JellyXR](https://github.com/Cuteminded/JellyXR) - VR media client for Quest and Steam Frame. `Jellyfin` · `Quest` `PC VR` · `Apache-2.0` `Free`
- [koko](https://www.meta.com/experiences/koko-vr-theater/1124509337421248/) - Meta Quest player that converts video to 3D live through a desktop companion. `Plex` `Jellyfin` · `Quest` · [Info](https://www.reddit.com/r/OculusQuest/comments/1vxy7t0/i_made_a_quest_player_that_converts_your_whole/)
- [LsVRPlayer](https://github.com/bibibivlin/LsVRPlayer) - PICO 4 VR player for local files, SMB shares and Emby. `Emby` · `Pico` · `MIT` `Free`
- [Lumenoir](https://lumenoir.app/plex-meta-quest/) - Meta Quest movie theatre player. `Plex` `Jellyfin` `Emby` `+Silo` · `Quest` · `Freemium` · [Meta Store](https://www.meta.com/en-gb/experiences/lumenoir-movie-theater-video-player/1552281053325883/)
- [MetaPlexVR](https://github.com/IvanVojtko/meta-plex-vr) - Meta Quest client. `Plex` · `Quest` · `GPL-3.0`
- [Movie Deck for Plex](https://www.meta.com/experiences/movie-deck-for-plex/6664246617031653/) - Meta Quest player. `Plex` · `Quest` · `Paid` · [Info](https://sidequestvr.com/app/27537/movie-deck-for-plex)
- [Reel Room](https://store.steampowered.com/app/4762320) - Paid PC VR theatre on Steam, also usable via Quest Link. `Jellyfin` · `PC VR` · `Paid`
- [Screenlit](https://apps.apple.com/us/app/screenlit/id6499478407) - Vision Pro player for MV-HEVC, side-by-side 3D, VR180 and 360 video. `Plex` `Jellyfin` `Emby` · `visionOS` · `Paid`
- [Suite Browser](https://www.reddit.com/r/VisionPro/comments/1wnddw0/suite_7_brings_virtual_projection_and/) - Apple Vision Pro browser with virtual projection that plays from media servers. `Plex` `Jellyfin` `Emby` · `visionOS`
- [Tachi](https://github.com/buggzd/tachi) - Spatial media client for RayNeo Air glasses. `Jellyfin` · `Smart glasses` · `MIT` `Free`
- [Whirligig](https://www.meta.com/experiences/whirligig-media-player/3581543561949869/) - Paid VR video player for Meta Quest and PC VR headsets. `Plex` `Jellyfin` `Emby` · `Quest` `PC VR` · `Paid` · [Steam](https://store.steampowered.com/app/451650) · [Info](https://www.reddit.com/r/OculusQuest/comments/1v98kld/whirligig_major_update_goes_live_media_server/)

### TV operating systems

- [Astra](https://github.com/AmbientFlare/astra-tv) - Client for Fire TV sticks running Vega OS. `Jellyfin` · `Vega OS` · `source-available` `Free` · [Info](https://forum.jellyfin.org/t-astra-%E2%80%94-a-jellyfin-client-for-the-new-vega-os-fire-tv-sticks-free?pid=72988)
- [Breezyfin](https://github.com/botagas/Breezyfin) - LG webOS client installed through Homebrew. `Jellyfin` · `webOS` · `GPL-3.0`
- [Caravela](https://github.com/melojms/caravela) - Native app for Fire TV devices running Vega OS. `Jellyfin` · `Vega OS` · `GPL-2.0` `Free` · [Amazon](https://www.amazon.com/dp/B0HNR62RQ9)
- [Cinefin (Ashiroen)](https://github.com/Ashiroen/cinefin) - Minimal home-theater client for LG webOS TVs; an Android TV build is planned. `Jellyfin` · `webOS` · `Open source` `Free`
- [Dreamfin](https://github.com/jrodzar/DreamFin) - Enigma2 (OpenATV) plugin for browsing and playing libraries. `Jellyfin` `Emby` · `Enigma2` · `GPL-2.0` `Free`
- [DreamPlex](https://github.com/oe-alliance/DreamPlex) - Plex client plugin for Enigma2 Linux set-top boxes. `Plex` · `Enigma2` · `Open source` `Free` · [Source (original)](https://github.com/DonDavici/DreamPlex)
- [emplexer](https://github.com/newloran2/emplexer) - Plex client for Dune HD media players. `Plex` · `Other TV` · `Open source` `Stale 2015`
- [FinLightning](https://github.com/hjourdain-ryvr/finlightning) - TV app built on the Lightning 3 / Blits UI framework. `Jellyfin` · `Tizen` `Other TV` · `Apache-2.0` `Free`
- [Fin Native](https://github.com/tiper/fin-native) - Native LG webOS app built on the PlxNative framework. `Jellyfin` · `webOS` · `GPL-3.0` `Free`
- [Jellyfin Lite](https://github.com/Grumm3l/jellyfin-lite) - Samsung Tizen 2.3 TV app using AVPlay, for older sets. `Jellyfin` · `Tizen` · `MIT` `Free`
- [jellyfin-roku-with-delete](https://github.com/garberfc/jellyfin-roku-with-delete) - Roku client that adds a delete action to the stock Jellyfin Roku app. `Jellyfin` · `Roku` · `GPL-2.0` `Free`
- [JellyFin-SamsungTizenTV](https://github.com/ChessDragon136/JellyFin-SamsungTizenTV) - Samsung Tizen TV app for playing your library. `Jellyfin` · `Tizen` · `Open source` `Free` `Stale 2022`
- [jellyfin-vidaa](https://github.com/lourensdev/jellyfin-vidaa) - Hisense VIDAA app with its own interface on the Jellyfin API. HLS streaming was still a work in progress in 2024. `Jellyfin` · `VIDAA` · `Open source` `Stale 2024`
- [JellyRock](https://github.com/jellyrock/jellyrock) - Roku client forked from the official channel. `Jellyfin` · `Roku` · `GPL-2.0` `Free` · [Roku](https://channelstore.roku.com/details/232f9e82db11ce628e3fe7e01382a330:a85d6e9e520567806e8dae1c0cabadd5/jellyrock)
- [Local Photos Screensaver](https://forums.plex.tv/t/roku-screensaver-app-to-use-plex-photos/939633) - Roku screensaver that shows your photo libraries. `Plex` · `Roku`
- [Luma](https://github.com/jravolio/luma-roku) - Roku channel with an Apple TV-style interface. `Jellyfin` · `Roku` · `MIT` `Free`
- [Native Jelly](https://github.com/sostk/native-jelly) - TV-first native app adapted from the PLX Native client. `Jellyfin` · `webOS` · `GPL-3.0` `Free`
- [Neolume](https://github.com/itsab1989/neolume) - Client for 2014 Samsung Orsay TVs. `Plex` · `Other TV` · `Open source`
- [OcenFin](https://github.com/seluce/OcenFin) - Sideloaded LG TV client. `Jellyfin` · `webOS` · `MIT`
- [p2F](https://p2f-freebox.fr/) - Plex client for the Freebox Revolution, Delta and One set-top boxes. `Plex` · `Other TV` · `Stale 2022` · [Info](https://forums.plex.tv/t/p2f-is-still-alive-p2f-est-toujours-vivant/937932)
- [plezy-webos](https://github.com/GLNick/plezy-webos) - webOS port of the Plezy Flutter client. `Plex` `Jellyfin` `Emby` · `webOS` · `GPL-3.0` `Free`
- [ploff-webos](https://github.com/lucabravi/ploff-webos) - Client for legacy LG webOS TVs. `Plex` · `webOS` · `MIT`
- [PlxNative](https://github.com/GLinnik21/plx-native) - Native LG TV client with an interface written in Rust and OpenGL. `Plex` · `webOS` · `GPL-3.0` `Free` · [Website](http://plxnative.com/)
- [Redefin](https://github.com/laborantine/ReDeFin) - Freebox Player app for the Freebox Revolution and the Freebox Delta (Devialet). `Jellyfin` · `Other TV` · `GPL-3.0` `Free`
- [SamSUCKS](https://github.com/rfaile313/samsucks) - Sideloaded Samsung TV client. `Plex` · `Tizen` · `GPL-3.0` `Free`
- [ScreenPlay](https://github.com/sleuth255/screenplay) - LG webOS app for browsing and playing a media library; last updated in 2020. `Emby` · `webOS` · `MIT` `Free` `Stale 2020`
- [Starfin](https://github.com/thedavidhoffman/starfin-roku) - Roku channel for browsing and playing your library. `Jellyfin` · `Roku` · `GPL-3.0` `Free`
- [tacplayer](https://github.com/sfsdffesfsfg-cloud/tacplayer) - Custom Samsung Tizen TV app. `Jellyfin` · `Tizen` · `Open source` `Free`
- [Velox](https://github.com/SuperDOS/velox) - Sideloaded Samsung TV client. `Plex` · `Tizen` · `GPL-3.0`
- [WebOS-Jellyfin-Native](https://github.com/SchulzCode/WebOS-Jellyfin-Native) - Native LG webOS app for browsing and playing your library. `Jellyfin` · `webOS` · `0BSD` `Free`

### Car

- [canvas](https://github.com/bleichroeder/canvas) - In-car browser video player for Plex and YouTube using canvas and WebCodecs. `Plex` · `Tesla` · `MIT`
- [DashTune](https://github.com/chamika/DashTune) - Android Automotive music and audiobook player with offline downloads. `Jellyfin` · `Android Automotive` · `Open source` `Free` · [Google Play](https://play.google.com/store/apps/details?id=com.chamika.dashtune)
- [Momentum: Plex Music for Cars](https://play.google.com/store/apps/details?id=com.williammunn.aaos.momentum) - Native Android Automotive music player. `Plex` · `Android Automotive` · `Freemium` · [Info](https://forums.plex.tv/t/momentum-a-native-plex-music-client-for-android-automotive-os-closed-testing-open-now/940529)
- [Norrklang](https://github.com/koedastudio/norrklang) - Music client for Android Automotive cars. `Plex` `Jellyfin` `+Subsonic` · `Android Automotive` · `GPL-3.0` `Free` · [Google Play](https://play.google.com/store/apps/details?id=studio.koeda.norrklang)
- [Plex AAOS (Unofficial)](https://github.com/joeyberkovitz/plex-aaos) - Unofficial music player for cars running Android Automotive OS. `Plex` · `Android Automotive` · `MIT` · [Google Play](https://play.google.com/store/apps/details?id=us.berkovitz.plexaaos)
- [Shark Marmalade](https://github.com/bendardenne/sharkmarmalade) - Android Automotive music player. `Jellyfin` · `Android Automotive` · `GPL-2.0` · [Google Play](https://play.google.com/store/apps/details?id=be.bendardenne.jellyfin.aaos)

### Watches

- [JellyWear](https://github.com/AndrewEllen/JellyWear) - Smartwatch client. `Jellyfin` · `Wear OS` · `GPL-3.0` `Free`
- [Onban](https://onban.app) - Standalone Apple Watch player for music and audiobooks. `Plex` · `watchOS` · `Beta`
- [SubMusic](https://github.com/memen45/SubMusic) - Garmin watch app that syncs music for offline listening. `Plex` `+Subsonic` · `Garmin` · `GPL-3.0` `Stale 2024`
- [Time for Plex](https://apps.apple.com/us/app/time-for-plex/id6792536676) - Independent Apple Watch client for browsing and streaming video, live TV and music. `Plex` · `watchOS` · `Paid`
- [WearAmp](https://github.com/03c/WearAmp) - Standalone Wear OS music player. `Plex` · `Wear OS` · `GPL-3.0`
- [WearJelly](https://github.com/Nanakusa-Nazuna7/WearJelly) - Standalone Wear OS music player that works on the watch without a phone. `Jellyfin` · `Wear OS` · `Open source` `Free`
- [wristAmp](https://apps.apple.com/us/app/wristamp/id6760357303) - Standalone Apple Watch music app that streams or downloads from a home server, no phone needed. `Plex` · `watchOS` · `Paid`
- [WristStream for Plex](https://apps.apple.com/us/app/wriststream-for-plex/id6751917976) - Standalone Apple Watch music client that streams a server library independently of the iPhone. `Plex` · `watchOS` · `Paid`
- [Wristwatch Player](https://apps.apple.com/us/app/wristwatch-player/id6793179479) - Standalone Apple Watch client that browses libraries and plays movies and shows without the phone. `Plex` · `watchOS` · `Free`

### Voice assistants and speakers

- [alexa-plex-music-player-skill](https://github.com/erinlkolp/alexa-plex-music-player-skill) - Self-hosted Alexa skill for playing your music. `Plex` · `Alexa` · `MIT`
- [Ear Wax](https://ear-wax-config.marvinbrown9999.workers.dev/) - Alexa skill for playing your music library by voice. `Plex` `Emby` · `Alexa` · [Info](https://forums.plex.tv/t/ear-wax-is-now-live-in-the-amazon-skill-store/940414)
- [jellyfin_alexa_skill](https://github.com/infinityofspace/jellyfin_alexa_skill) - Self-hosted Alexa skill that plays music from the server. `Jellyfin` · `Alexa` · `GPL-3.0` `Stale 2023`
- [plexMusicPlayer (Tyzer34)](https://github.com/Tyzer34/plexMusicPlayer) - Self-hosted Alexa skill for playing your music. `Plex` · `Alexa` · `GPL-3.0` `Stale 2017`

### Kodi add-ons

- [Composite for Plex](https://github.com/anxdpanic/plugin.video.composite_for_plex) - Kodi add-on for browsing and playing the library. `Plex` · `Kodi` · `GPL-2.0` `Free` `Stale 2024`
- [drivemby-kodi](https://github.com/skLeo/drivemby-kodi) - Drivemby compatibility build of the Emby for Kodi Next Gen add-on. `Emby` · `Kodi` · `GPL-3.0`
- [EmbyCon](https://github.com/faush01/plugin.video.embycon) - Kodi add-on that browses an Emby server directly, without syncing. `Emby` · `Kodi` · `GPL-2.0` `Free`
- [jellyfin-kodi](https://github.com/dan-riley/jellyfin-kodi) - Fork of the Kodi add-on that syncs a Jellyfin library into Kodi. `Jellyfin` · `Kodi` · `GPL-3.0` `Free`
- [kodi-addon-emby](https://github.com/TheWorms/kodi-addon-emby) - Emby add-on for Kodi that descends from EmbyCon. `Emby` · `Kodi` · `GPL-2.0`
- [kodi-addons](https://github.com/zzzwannasleep/kodi-addons) - Kodi add-on for UHD Media Server accounts. `Emby` · `Kodi` · `GPL-3.0` `Free`
- [Kofin PVR](https://github.com/kontell/pvr.kofin) - Kodi PVR add-on for watching Live TV. `Jellyfin` · `Kodi` · `GPL-2.0`
- [mediaimporter.emby](https://github.com/Montellese/mediaimporter.emby) - Kodi add-on that imports Emby library items into Kodi's own library. `Emby` · `Kodi` · `GPL-2.0` `Free` `Stale 2023`
- [mediaimporter.plex](https://github.com/Montellese/mediaimporter.plex) - Kodi media importer that brings a Plex library into Kodi. `Plex` · `Kodi` · `GPL-2.0` `Stale 2022`
- [Oriel](https://github.com/GR3ee3N/Oriel) - Plex client for CoreELEC on Amlogic boxes. `Plex` · `Kodi` · `GPL-3.0`
- [PlexKodiConnect](https://github.com/croneter/PlexKodiConnect) - Kodi add-on that syncs a library into Kodi's native database. `Plex` · `Kodi` · `GPL-2.0` `Free`
- [plugin.video.emby.vfs](https://github.com/forbxy/plugin.video.emby.vfs) - Emby for Kodi Next Gen variant adapted to Kodi's VFS. `Emby` · `Kodi` · `GPL-3.0`
- [PM4K](https://github.com/pannal/plex-for-kodi) - Kodi add-on with the Plex-style interface, forked from the official add-on. `Plex` · `Kodi` · `GPL-2.0` `Free` · [Website](https://pm4k.eu) · [Info](https://forums.plex.tv/t/pm4k-plexmod-for-kodi-18-19-20-21-22/481208)
- [pm4kvertical](https://github.com/jpalenz77/pm4kvertical) - Mod of Plex for Kodi with a vertical home screen layout. `Plex` · `Kodi` · `Open source`

### Terminal

- [Amptui](https://github.com/tipii/amptui) - Terminal music client. `Plex` `Jellyfin` · `CLI` · `Open source` `Free`
- [Aquafin](https://github.com/Armando-ven/aquafin) - Terminal UI client. `Jellyfin` · `CLI` · `GPL-3.0` `Free` · [AUR](https://aur.archlinux.org/packages/aquafin)
- [cliamp](https://github.com/bjarneo/cliamp) - Terminal music player for several back ends. `Plex` `Jellyfin` `Emby` `+Subsonic` `+Audiobookshelf` · `CLI` · `MIT`
- [clifin](https://github.com/urlocalhemaduck/CLIfin) - Minimal terminal client. `Jellyfin` · `CLI` · `Open source` `Free`
- [CLIX](https://github.com/jeremehancock/CLIX) - Plex terminal media player written as a shell script. `Plex` · `CLI` · `MIT` `Free`
- [deglerj/fin](https://github.com/deglerj/fin) - Terminal UI client. `Jellyfin` · `CLI` · `MIT` `Free`
- [dotamp](https://github.com/brady1408/dotamp) - Winamp-style terminal music player drawn with braille characters. `Plex` `+Subsonic` · `CLI` · `MIT`
- [emby-cli](https://github.com/soukron/emby-cli) - Command-line client. `Emby` · `CLI` · `Open source`
- [jelly (AzureHound)](https://github.com/AzureHound/jelly) - Terminal client for browsing and streaming a Jellyfin library. `Jellyfin` · `CLI` · `Open source` `Free` · [AUR](https://aur.archlinux.org/packages/jelly)
- [jellycli](https://github.com/tryffel/jellycli) - Terminal music client written in Go. `Jellyfin` `Emby` `+Subsonic` · `CLI` · `GPL-3.0` `Free` `Stale 2023` · [AUR](https://aur.archlinux.org/packages/jellycli)
- [jellyfin-agent-cli](https://www.npmjs.com/package/jellyfin-agent-cli) - Command-line client for browsing, playback, administration and automation. `Jellyfin` · `CLI`
- [Jellyfin-CLI](https://github.com/marios8543/Jellyfin-CLI) - Python command-line client. `Jellyfin` · `CLI` · `MIT` `Stale 2024` · [Info](https://pypi.org/project/Jellyfin-CLI/)
- [jellyfin-client-lite](https://github.com/Epiklal/jellyfin-client-lite) - Small terminal music player. `Jellyfin` · `CLI` · `GPL-3.0` `Free`
- [jellyfin-cli (green)](https://git.gay/green/jellyfin-cli) - Python terminal picker built on fzf and mpv that can use several accounts at once. `Jellyfin` · `CLI` · `Open source`
- [jellyfin-emms-mpv.el](https://github.com/emacs-os/jellyfin-emms-mpv.el) - Emacs package for browsing the library and playing through EMMS and mpv. `Jellyfin` · `CLI` · `GPL-3.0` `Free`
- [jellyfin-tui](https://github.com/dhonus/jellyfin-tui) - Terminal music player. `Jellyfin` · `CLI` · `GPL-3.0` `Free` · [AUR](https://aur.archlinux.org/packages/jellyfin-tui)
- [jellyhaj](https://github.com/owo-uwu-nyaa/jellyhaj) - Terminal music player. `Jellyfin` · `CLI` · `MIT` · [AUR](https://aur.archlinux.org/packages/jellyhaj)
- [JellyTerm](https://github.com/tammo2701/jellyterm) - Terminal client. `Jellyfin` · `CLI` · `Open source` `Free`
- [jfcli](https://github.com/cumulus13/jfcli) - Command-line client written in Go. `Jellyfin` · `CLI` · `Open source` `Free`
- [jfsh](https://github.com/hacel/jfsh) - Terminal client that plays in mpv. `Jellyfin` · `CLI` · `Unlicense` · [AUR](https://aur.archlinux.org/packages/jfsh)
- [jftui](https://github.com/Aanok/jftui) - Terminal client that plays in mpv. `Jellyfin` · `CLI` · `Unlicense` `Free` · [AUR](https://aur.archlinux.org/packages/jftui)
- [jtui](https://github.com/Banh-Canh/jtui) - Terminal UI for searching and playing videos. `Jellyfin` · `CLI` · `MIT` `Free`
- [jukebox (gustarmartins)](https://github.com/gustarmartins/jukebox) - Terminal music player for local files and Jellyfin, with album art, queues and synced lyrics. `Jellyfin` · `CLI` · `MIT` `Free` · [AUR](https://aur.archlinux.org/packages/jukebox)
- [kino](https://github.com/mmcdole/kino) - Terminal client for browsing and playing media. `Plex` `Jellyfin` · `CLI` · `MIT` `Free` · [AUR](https://aur.archlinux.org/packages/kino-tui)
- [Luqman2003/jelly-tui](https://github.com/Luqman2003/jelly-tui) - Terminal UI client. `Jellyfin` · `CLI` · `Open source` `Free`
- [mbv](https://github.com/slatkin/mbv) - Terminal UI front-end that plays library media through mpv. `Emby` `+Audiobookshelf` · `CLI` · `MIT` · [AUR](https://aur.archlinux.org/packages/mbv)
- [minittupoyo/jellycli](https://github.com/minittupoyo/jellycli) - Command-line and terminal UI client that plays through mpv. `Jellyfin` · `CLI` · `Open source` `Free`
- [musica](https://github.com/codila125/musica) - Terminal music player with a cassette-deck interface. `Jellyfin` `+Subsonic` · `CLI` · `MIT` `Free`
- [Noah0504/plext](https://github.com/Noah0504/plext) - Bit-perfect terminal music player. `Plex` · `CLI` · `MIT`
- [plexbar](https://github.com/feoh/plexbar) - Plex music player with a text-mode interface. `Plex` · `CLI` · `MIT` · [Info](https://pypi.org/project/plexbar/)
- [plexi](https://github.com/brunoenten/plexi) - Terminal client. `Plex` · `CLI` · `MIT`
- [plexshell](https://pypi.org/project/plexshell/) - Old Python command-line Plex client. `Plex` · `CLI` · `Open source` `Stale 2011`
- [plex-tui](https://github.com/so1omon563/plex-tui) - Terminal client. `Plex` · `CLI` · `MIT` · [AUR](https://aur.archlinux.org/packages/plex-tui)
- [pseudo-channel](https://github.com/justinemter/pseudo-channel) - Self-hosted generator that plays the library as linear channels on existing players. `Plex` · `CLI` · `GPL-3.0` `Stale 2022`
- [Puddler-RS](https://github.com/Vernoxvernax/Puddler-RS) - Terminal client that plays media in mpv. `Plex` `Jellyfin` `Emby` · `CLI` · `MIT` · [Source (Python)](https://github.com/Vernoxvernax/Puddler)
- [Remby](https://github.com/qtxie/remby) - Terminal UI client that plays through mpv. `Emby` · `CLI` · `MIT` `Free`
- [rexamp](https://github.com/defaultdino/rexamp) - Terminal music player for Plex. `Plex` · `CLI` · `MIT`
- [Rustune](https://github.com/dzulfikar08/rustune) - Terminal music player with Winamp skin support. `Jellyfin` `Emby` `+Subsonic` · `CLI` · `MIT` `Free`
- [SuperCoolPencil/cue](https://github.com/SuperCoolPencil/cue) - Terminal client forked from kino for browsing and playing media. `Plex` `Jellyfin` · `CLI` · `MIT` `Free`
- [Tizonia](https://github.com/tizonia/tizonia-openmax-il) - Linux command-line music player for several sources. `Plex` · `CLI` · `LGPL-3.0` · [Snap](https://snapcraft.io/tizonia) · [AUR](https://aur.archlinux.org/packages/tizonia-all-git)
- [tsirysndr/fin](https://github.com/tsirysndr/fin) - Terminal music client that can cast to Chromecast and UPnP renderers. `Jellyfin` `+Subsonic` · `CLI` · `MPL-2.0` `Free` · [Info](https://www.npmjs.com/package/@tsiry/fin)
- [tsplay](https://github.com/28allday/tsplay) - Terminal player for Omarchy and Arch Linux. `Jellyfin` · `CLI` · `Open source` `Free`
- [Waddenn/plex-client](https://github.com/Waddenn/plex-client) - Minimal command-line Plex client that plays through mpv with an fzf picker. `Plex` · `CLI` · `Open source`
- [xHitech/jellytui](https://github.com/xHitech/jellytui) - Terminal music client that plays through mpv. `Jellyfin` · `CLI` · `MIT` `Free`

### Desktop shims and external players

- [AllCast](https://apps.apple.com/fr/app/allcast-recopie-d%C3%A9cran-tv/id474717827) - Screen-mirroring and casting app that also streams from servers and DLNA to smart TVs. `Plex` `+IPTV` · `iOS` `iPadOS` · `Free`
- [Aspecta Cinema Player](https://emby.media/community/topic/147512-aspecta-cinema-player/) - Android TV external player with automatic black-bar detection. `Emby` · `Android TV`
- [Caldera Amp](https://caldera.homes/music/amp/) - Headless menu-bar or tray player for Plex music, controlled from Plexamp. `Plex` · `Windows` `macOS` `Linux`
- [Cast Rocket for Plex](https://github.com/ledge74/Cast-Rocket-for-Plex) - Cast bridge for Plex. `Plex` · `Web` · `Open source` `Stale 2015`
- [dknz7/lumen](https://github.com/dknz7/lumen) - Web Plex client that opens playback in an external PotPlayer. `Plex` · `Windows` · `MIT` `Free`
- [EmbyExternalPlayerLauncher](https://github.com/red217/EmbyExternalPlayerLauncher) - Windows launcher that opens Emby videos in MPC-HC. `Emby` · `Windows` · `GPL-3.0` `Free` `Stale 2022`
- [embyToLocalPlayer](https://github.com/kjtsune/embyToLocalPlayer) - Sends items from the server's web client to a local mpv, VLC or PotPlayer and syncs progress back. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `Apache-2.0`
- [fjkfwz/iina-emby](https://github.com/fjkfwz/iina-emby) - IINA plugin that plays your library with MPV hardware decoding on macOS. `Emby` · `macOS` · `Open source` `Free`
- [Freebo](https://github.com/elonzh/freebo) - Electron app that browses the server web UI and hands playback to mpv or IINA, syncing progress back. `Plex` `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `Apache-2.0` `Free`
- [groovy-cli](https://github.com/SeeThruHead/groovy-cli) - Command-line tool that streams Plex media to a MiSTer for CRT output. `Plex` · `MiSTer` `CLI` · `Open source`
- [Home Cinema Control](https://github.com/tousled/home-cinema-control) - Sends library items to OPPO and Chinoppo disc players for playback. `Jellyfin` `Emby` · `Other device` · `Open source`
- [iina-emby](https://github.com/ghotriw/iina-emby) - IINA plugin that plays Emby library items in IINA. `Emby` · `macOS` · `Open source`
- [iina-jellyfin](https://github.com/mhajder/iina-jellyfin) - IINA plugin that browses the server and plays items in IINA on macOS. `Jellyfin` · `macOS` · `GPL-3.0`
- [jellyfin-iina](https://github.com/ada-bee/jellyfin-iina) - IINA plugin that browses the server and plays items in IINA on macOS. `Jellyfin` · `macOS` · `GPL-3.0`
- [Jellyfin MPC Shim](https://github.com/jonahstoermer/jellyfin-mpc-shim) - Cast target that plays Jellyfin items in MPC-HC, updated for Jellyfin 12.0. `Jellyfin` · `Windows` · `GPL-3.0` `Free`
- [Jellyfin MPC Shim (Trellmor)](https://github.com/Trellmor/jellyfin-mpc-shim) - Windows cast client that plays through Media Player Classic. `Jellyfin` · `Windows` · `GPL-3.0` `Stale 2024`
- [Jellyfin VLC Bridge](https://github.com/CrySer66/jellyfin-vlc-bridge) - Windows helper that hands Jellyfin Web playback to VLC, with resume and progress sync. `Jellyfin` · `Windows` · `MIT`
- [jellyfin-vlc-shim](https://github.com/tseho/jellyfin-vlc-shim) - Cast target that plays Jellyfin items in VLC. `Jellyfin` · `Linux` · `GPL-3.0` `Free`
- [LocalCast](https://apps.apple.com/us/app/localcast-cast-to-tv/id969804264) - Casting app that sends videos, music and photos from phone, NAS, cloud or a server to smart TVs and DLNA. `Plex` `+IPTV` · `iOS` `iPadOS` `tvOS` · `Free`
- [MediaFlick Desktop](https://github.com/phob/MediaFlick-Desktop) - Desktop wrapper that shows the Jellyfin web UI and plays through your own mpv. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-2.0` `Free`
- [MeowFlixEmby](https://github.com/EasyTidy/MeowFlixEmby) - External-player launcher for the Emby and Jellyfin web apps. `Jellyfin` `Emby` · `Windows` `macOS` `Linux` · `MIT`
- [mov-cli-jellyplex](https://github.com/mov-cli/mov-cli-jellyplex) - mov-cli plugin that plays server content through mov-cli's external player. `Plex` `Jellyfin` · `CLI` · `MIT` `Stale 2025`
- [mpv-handler (Kosette)](https://github.com/Kosette/mpv-handler) - Protocol handler that opens web-player links in mpv. `Emby` · `Windows` `macOS` `Linux` · `MIT`
- [mpv-jellyfin](https://github.com/EmperorPenguin18/mpv-jellyfin) - mpv Lua plugin that browses and plays the server's library inside mpv. `Jellyfin` · `Windows` `macOS` `Linux` · `Unlicense`
- [OliPlay](https://apps.apple.com/jp/app/oliplay/id6760545351) - Opens a server's web interface and plays the chosen video in a native VLC player. `Plex` `Jellyfin` · `iOS` `iPadOS` · `Freemium`
- [PlayBridge](https://github.com/Damocles-fr/PlayBridge) - Windows launcher that opens server items in PotPlayer, VLC or MPC-HC. `Jellyfin` · `Windows` · `MIT`
- [playlink](https://github.com/lulalulaluobo/playlink) - Chrome extension that opens Emby and Jellyfin web playback in IINA or PotPlayer. `Jellyfin` `Emby` · `Windows` `macOS` `Web` · `Open source`
- [plexdlnaplayer](https://github.com/songchenwen/plexdlnaplayer) - Exposes DLNA speakers as Plex players. `Plex` · `Linux` · `GPL-3.0`
- [PlexExternalPlayer](https://github.com/Kayomani/PlexExternalPlayer) - Opens Plex Web items in an external desktop player. `Plex` · `Windows` `Web` · `GPL-3.0` `Stale 2024`
- [Plex-MPV-Shim](https://github.com/iwalton3/plex-mpv-shim) - Desktop cast target that plays items sent from other apps in mpv. `Plex` · `Windows` `macOS` `Linux` · `MIT` `Free` `Stale 2025`
- [plex-to-vlc](https://github.com/soerenkampschroer/plex-to-vlc) - Sends Plex Web playback to VLC. `Plex` · `macOS` `Web` · `GPL-3.0` `Stale 2023`
- [PlexToZidoo](https://github.com/hpn789/PlexToZidoo) - Plays Plex items in the native player of Zidoo media players. `Plex` · `Android TV` · `Open source` `Stale 2023`
- [Rushy](https://github.com/brivera2005/Rushy) - Android TV media hub for Plex and Xtream sources. `Plex` `+IPTV` · `Android TV` · `Open source` `Free`
- [Xnoppo](https://github.com/siberian-git/Xnoppo) - Lets Emby act as the interface while an Oppo UDP-203 player does the playback. `Emby` · `Other device` · `Open source` `Free` `Stale 2025`

### Other devices and legacy systems

- [Bookshelf-jukebox](https://github.com/YosoraLife/Bookshelf-jukebox) - Bookshelf jukebox hardware build around headless Plexamp. `Plex` · `Other device` · `Open source`
- [emby-skill](https://github.com/rickyphewitt/emby-skill) - Mycroft voice-assistant skill that plays Emby audio. `Emby` · `Other device` · `Open source`
- [Emby (Unofficial) for Ubuntu Touch](https://gitlab.com/bhdouglass/emby-ubuntu-touch) - Ubuntu Touch web-app wrapper for an Emby server's web interface. `Emby` · `Ubuntu Touch` · `GPL-3.0` `Stale 2020` · [Info](https://open-store.io/app/emby.bhdouglass)
- [FlipFin](https://github.com/jackharvest/FlipFin) - Text-only app for the TCL 4058G flip phone. `Jellyfin` · `Other device` · `MIT` `Free`
- [FlipFlex](https://github.com/jackharvest/FlipFlex) - Client for a TCL flip phone. `Plex` · `Other device` · `MIT`
- [Jellychord](https://github.com/felix920506/jellychord) - Discord bot that plays music from the library in voice channels. `Jellyfin` · `Discord` · `MIT` `Free`
- [Jellyfin68K](https://github.com/pukikiko/Jellyfin68K) - Music player for classic 68K Macintosh computers. `Jellyfin` · `Classic Mac` · `Open source` `Free`
- [Jellyfin Discord Music Bot](https://github.com/manuel-rw/jellyfin-discord-music-bot) - Discord bot that plays music from the library in voice channels. `Jellyfin` · `Discord` · `MIT` `Free`
- [Jellyfin Media Center (Tafitson)](https://open-store.io/app/jellyfin.tafitson) - Ubuntu Touch wrapper for the Jellyfin web client. `Jellyfin` · `Ubuntu Touch` · `GPL-2.0` `Stale 2023`
- [jellyfin-s60v3](https://github.com/Hinduc0der/jellyfin-s60v3) - Symbian S60v3 phone app; a companion service transcodes for the phone. `Jellyfin` · `Symbian` · `GPL-3.0` `Free`
- [Jellyfin.W10M](https://github.com/Starkka15/Jellyfin.W10M) - Client for Windows 10 Mobile. `Jellyfin` · `Windows Phone` · `Open source` `Free`
- [JellyfUn](https://open-store.io/app/jellyfun.jellyfun) - Unofficial Ubuntu Touch app for using Jellyfin. `Jellyfin` · `Ubuntu Touch` · `GPL-3.0` `Stale 2021`
- [JF-BeamNG.drive-Audio-Player](https://github.com/Inevitabby/JF-BeamNG.drive-Audio-Player) - BeamNG.drive mod that plays your music in the game. `Jellyfin` · `Other device` · `Open source` `Free`
- [KOReader-Jellyfin-Plugin](https://github.com/DeclanChidlow/KOReader-Jellyfin-Plugin) - KOReader plugin that reads books from the server on e-readers. `Jellyfin` · `Other device` · `AGPL-3.0`
- [Light Amp](https://github.com/sublunarian/light-amp) - Music player for the Light Phone III. `Plex` `Jellyfin` `+Subsonic` · `Other device` · `Open source` `Free`
- [Matinee](https://github.com/adyoull/riscos-matinee) - RISC OS app that plays what the machine decodes; the server converts the rest. `Plex` `Jellyfin` · `RISC OS` · `GPL-2.0` `Free`
- [PixelReel](https://github.com/Samarth-programming/PixelReel) - Minecraft mod that plays your library on in-game TV and cinema screens. `Plex` `Jellyfin` `Emby` `+IPTV` · `Other device` · `CC0-1.0` `Free`
- [Portalfin](https://github.com/luke-hurd/portalfin) - Native Facebook Portal app for browsing and playing your library. `Jellyfin` · `Other device` · `GPL-2.0` `Free`
- [Sailfin](https://github.com/heartfin/harbour-sailfin) - Sailfish OS client. `Jellyfin` · `Sailfish OS` · `LGPL-2.1`
- [volumio-jellyfin](https://github.com/patrickkfkan/volumio-jellyfin) - Volumio plugin that plays the music library on Volumio players. `Jellyfin` · `Other device` · `Open source` `Free`

## Companion and remote apps

These do not play media themselves. They control or manage a server or connect it to other software.

### Remotes and controllers

- [alexa-plex](https://github.com/OverloadUT/alexa-plex) - Alexa skill for controlling Plex. `Plex` · `Alexa` · `MIT` `Stale 2016`
- [alfred-plex](https://github.com/BenjaminOddou/alfred-plex) - Alfred workflow for searching and controlling Plex on macOS. `Plex` · `macOS` · `MIT` `Stale 2025`
- [AmpBubble](https://github.com/DreadHeadHippy/AmpBubble) - Android overlay for rating Plexamp tracks. `Plex` · `Android` · `MIT`
- [Ampdeck](https://github.com/rackemrack/ampdeck) - Elgato Stream Deck plugin that controls Plexamp playback. `Plex` · `Other device` · `MIT`
- [AmpdeckPlus](https://github.com/DreadHeadHippy/AmpdeckPlus) - Stream Deck controller for Plexamp. `Plex` · `Other device` · `MIT`
- [Crestron-PlexHT](https://github.com/ecleese/Crestron-PlexHT) - Crestron control module for Plex Home Theater. `Plex` · `Other device` · `Open source` `Stale 2014`
- [hail-frequency](https://github.com/SpaceinvaderOne/hail-frequency) - Phone voice control for Emby and Jellyfin. `Jellyfin` `Emby` · `Web` · `GPL-3.0`
- [heldover](https://github.com/anthonyonazure/heldover) - Picks titles across servers and sends them to a TV. `Plex` · `Windows` `macOS` `Linux` `Web` · `MIT`
- [JellyRemote](https://github.com/TeeWare2026/JellyRemote) - Android remote that browses the library, picks what plays and controls playback on another client. `Jellyfin` · `Android` · `Open source`
- [Phlex](https://github.com/d8ahazard/FlexTV) - Voice interface for controlling Plex. `Plex` · `Web` `Alexa` `Google Assistant` · `Open source` `Stale 2023` · [Source](https://github.com/d8ahazard/Phlex)
- [plexamp-nfc-listener](https://github.com/aubrey-wodonga/plexamp-nfc-listener) - Starts Plexamp playback from NFC tags. `Plex` · `Other device` · `MIT` `Stale 2023`
- [plexamp-tui](https://github.com/spiercey/plexamp-tui) - Terminal remote that controls music players on the LAN. `Plex` · `CLI` · `MIT`
- [Plex & Kodi Remote](https://apps.apple.com/app/id403716879) - iPhone remote control. `Plex` `+Kodi` · `iOS` `iPadOS` `watchOS` · `Stale 2019`
- [Scyphomote](https://play.google.com/store/apps/details?id=com.eiffelbeef.scyphomote) - Android remote control for the server's players. `Jellyfin` · `Android`
- [whatsplaying](https://github.com/gloaysa/whatsplaying) - Now-playing display for Plex. `Plex` · `Web` · `MIT` `Stale 2024`
- [wym-tv](https://github.com/danmmr/wym-tv) - Fire TV remote and browser for WiiM streamers, with a Plex music library. `Plex` · `Fire TV` · `MIT` `Free`

### Admin, stats and requests

- [Accio for Plex](https://apps.apple.com/us/app/accio-for-plex/id6759935357) - iPhone app for making Seerr requests. `Plex` · `iOS` `iPadOS` `tvOS`
- [Emby Companion](https://github.com/ffinly/emby-companion) - Library discovery app that hands playback to an external player and syncs watch progress. `Emby` · `macOS` · `Open source` `Free`
- [EmbyUserHub](https://apps.apple.com/cn/app/embyuserhub/id6759602198) - iPhone server user admin and statistics app. `Emby` · `iOS` · `Free`
- [Flick for Plex](https://apps.apple.com/us/app/flick-for-plex/id6806605373) - iPhone app for swiping through the library to triage it. `Plex` · `iOS` `iPadOS` · `Freemium`
- [HifiMule](https://github.com/HifiMule/HifiMule) - Sync tool that copies music and playlists to MTP phones and watches, USB drives and Rockbox players. `Jellyfin` `+Subsonic` `+Audiobookshelf` · `Windows` `macOS` `Linux` · `GPL-2.0`
- [Homelab](https://f-droid.org/packages/com.homelab.app/) - Android dashboard for the server and *arr apps. `Plex` · `Android` · `Open source`
- [JellyTunes](https://orainlabs.dev/) - Linux tool that syncs music from the server to MP3 players for offline use. `Jellyfin` · `Linux` · [Snap](https://snapcraft.io/jellytunes)
- [Movie Tinder for Plex](https://play.google.com/store/apps/details?id=dev.hagios.movietinder) - Android app for picking a film as a group. `Plex` · `Android` · `Stale 2024`
- [MSM](https://github.com/prinzpiuz/MSM) - Android app for managing files on a media server. `Plex` `Jellyfin` `Emby` `+Kodi` · `Android` · `GPL-3.0` · [F-Droid](https://apt.izzysoft.de/fdroid/index/apk/com.prinzpiuz.msm)
- [NasScale](https://apps.apple.com/us/app/nasscale/id6796591787) - Synology NAS manager with built-in Tailscale for files, transfers and downloads, plus optional Jellyfin playback. `Jellyfin` · `iOS` · `Free`
- [Playlifin](https://flathub.org/apps/net.krafting.Playlifin) - Linux tool for converting playlists into the server. `Jellyfin` · `Linux`
- [Playlifin Voyager](https://flathub.org/apps/net.krafting.PlaylifinVoyager) - Moves playlists to and from a server. `Jellyfin` · `Linux`
- [Purger for Plex](https://play.google.com/store/apps/details?id=it.devcells.plexpurger) - Android app for swipe-to-delete library cleanup. `Plex` · `Android` · `Freemium`
- [Quartermaster](https://apps.apple.com/us/app/quartermaster-homelab-stack/id6779994284) - Homelab control app with media requests, download status, server controls and library playback. `Plex` `Jellyfin` `Emby` · `iOS` `iPadOS` · `Freemium`
- [Remote for Tautulli](https://apps.apple.com/us/app/remote-for-tautulli/id1343177312) - Statistics app for Tautulli on iPhone, iPad and Apple Watch. `Plex` · `iOS` `iPadOS` `watchOS` · `Freemium` `Stale 2024`
- [seerr-tv](https://github.com/Vermino/seerr-tv) - Android TV app for making Seerr requests. `Plex` `Jellyfin` `Emby` · `Android TV` `Fire TV` · `MIT`
- [Tautulli Remote](https://github.com/Tautulli/Tautulli-Remote) - Official Tautulli app for server statistics and activity. `Plex` · `Android` `iOS` `iPadOS` · `GPL-3.0` · [App Store](https://apps.apple.com/app/id1570909086) · [Google Play](https://play.google.com/store/apps/details?id=com.tautulli.tautulli_remote)
- [Twig](https://f-droid.org/packages/com.twig.app/) - Android file manager for the server. `Jellyfin` · `Android` · `Open source`
- [Varys for Plex](https://apps.apple.com/us/app/varys-for-plex/id1450380518) - iPhone server statistics app. `Plex` · `iOS` `iPadOS` `watchOS` · `Freemium`

### Bridges and integrations

- [Channel Connect for Plex](https://play.google.com/store/apps/details?id=com.spauldhaliwal.plexchannelconnect) - Adds library rows and Play Next items to the Android TV home screen. `Plex` · `Android TV` · `Stale 2022`
- [emby2podcasts](https://github.com/zhimiaoli/emby2podcasts) - Turns audiobooks on the server into podcast feeds. `Emby` · `Linux` · `Open source`
- [Gelato](https://github.com/lostb1t/Gelato) - Server plugin that shows Stremio addon results inside any client app. `Jellyfin` `+Stremio addons` · `Web` · `GPL-3.0`
- [Home Assistant Emby integration](https://www.home-assistant.io/integrations/emby/) - Home Assistant integration that exposes players as media player entities. `Emby` · `Home Assistant` · `Open source`
- [Home Assistant Jellyfin integration](https://www.home-assistant.io/integrations/jellyfin/) - Home Assistant integration that exposes the server as a media source. `Jellyfin` · `Home Assistant` · `Open source`
- [Home Assistant Plex integration](https://www.home-assistant.io/integrations/plex/) - Home Assistant integration that exposes players as media player entities. `Plex` · `Home Assistant` · `Open source`
- [jellyha](https://github.com/zupancicmarko/JellyHA) - Home Assistant integration for a Jellyfin server. `Jellyfin` · `Home Assistant` · `MIT`
- [JellyStreams](https://store.elfhosted.com/blog/2026/09/11/jellystreams-your-addons-in-any-jellyfin-app/) - Hosted service that shows Stremio addon results inside any client app. `Jellyfin` `+Stremio addons` · `Web`
- [plex-browser-card](https://github.com/stoffer123/plex-browser-card) - Home Assistant dashboard card for browsing the library. `Plex` · `Home Assistant` · `MIT`
- [ricercar-plex](https://github.com/ricercar-player/ricercar-plex) - Plex source plugin for the ricercar bit-perfect music player. `Plex` · `Linux` · `MIT`
- [squeeze-plex-hub](https://github.com/onmomo/squeeze-plex-hub) - Bridge that plays the music library on Lyrion (Logitech Media Server) players. `Plex` · `Other device` · `MIT`
- [stremio-jellyfin](https://github.com/akarazniewicz/stremio-jellyfin) - Stremio addon that puts your server's library into Stremio. `Jellyfin` `+Stremio addons` · `Web` · `Apache-2.0` `Stale 2024`
- [Subfin](https://github.com/williamkray/subfin-plugin) - Server plugin that exposes an OpenSubsonic API so Subsonic music apps can connect. `Jellyfin` `+Subsonic` · `Web` · `MIT`
- [XiaoEmby](https://github.com/backtracker/xiaoemby) - Self-hosted bridge that plays your Emby music on Xiaomi XiaoAi smart speakers by voice. `Emby` · `Other device` · `MIT`
- [Zwind](https://apps.apple.com/us/app/zwind-webdav-server-player/id6755239096) - Turns the phone into a WebDAV hub that maps local files, SMB, cloud drives, feeds and media libraries. `Emby` · `iOS` `iPadOS` · `Freemium`

## Discontinued

Apps that were withdrawn or archived or abandoned. Kept for reference.

- [ABJC-tvOS](https://github.com/ABJC/ABJC-tvOS) - Apple TV client. `Jellyfin` · `tvOS` · `Open source` `Ended 2022`
- [AmpFin](https://github.com/rasmuslos/AmpFin) - Music player. `Jellyfin` · `iOS` `iPadOS` · `Open source` `Ended 2025`
- [bruhdudeisdead/Jellyfin-Legacy-iOS](https://github.com/bruhdudeisdead/Jellyfin-Legacy-iOS) - Client for legacy iOS versions; the repository is archived. `Jellyfin` · `iOS` · `Open source` `Free` `Ended 2026`
- [carstream-android-auto](https://github.com/thekirankumar/carstream-android-auto) - Android Auto video player for Plex and YouTube. `Plex` · `Android Auto` · `Apache-2.0` `Ended 2021`
- [DUNE](https://github.com/Sam42a/DUNE) - Android TV client. `Jellyfin` · `Android TV` · `GPL-2.0` `Ended 2026`
- [electron-plex-menubar](https://github.com/jdrydn/electron-plex-menubar) - Archived macOS menu-bar player for Plex music. `Plex` · `macOS` · `MIT` `Free` `Ended 2023`
- [Ember for Emby](https://emby.media/community/topic/39191-ember-for-emby/) - Client for Windows 8/10, Windows 10 Mobile and Xbox One. `Emby` · `Windows` `Xbox` `Windows Phone` · `Paid` `Ended 2019`
- [Emby for Windows Phone](https://github.com/MediaBrowser/Emby.WindowsPhone) - Windows Phone app, archived. `Emby` · `Windows Phone` · `GPL-2.0` `Ended 2016`
- [Emby Theater for Windows](https://github.com/MediaBrowser/emby-theater-windows) - Former Windows desktop app; it and the old UWP app were replaced by the Store app in December 2024. `Emby` · `Windows` · `GPL-2.0` `Ended 2024`
- [EmbyWatch](https://play.google.com/store/apps/details?id=com.embywatch.app) - Android server admin and statistics app. `Emby` · `Android` · `Freemium` `Ended 2026`
- [feishin-connect](https://github.com/mihaitom/feishin-connect) - Feishin fork that adds Sonos, Chromecast, AirPlay and DLNA casting. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free` `Ended 2026`
- [Fincord](https://github.com/Bananz0/Fincord) - Android music player forked from Accord with Jellyfin streaming, shipped only as debug builds before it was deprecated. `Jellyfin` · `Android` · `GPL-3.0` `Free` `Ended 2026`
- [Finzy](https://github.com/dkmcgowan/finzy) - Jellyfin fork of Plezy for desktop and mobile; archived in 2026 and pulled from the stores. `Jellyfin` · `Windows` `macOS` `Linux` `Android` `iOS` · `GPL-3.0` `Free` `Ended 2026`
- Forward - iOS and Apple TV media player with cloud and Stremio-style modules; removed from the App Store (link dead as of 2026-11). `Jellyfin` `Emby` `+Stremio addons` · `macOS` `iOS` `iPadOS` `tvOS` · `Subscription` `Ended 2026`
- [Gelli](https://github.com/dkanada/gelli) - Music player. `Jellyfin` · `Android` `Android Auto` · `GPL-3.0` `Ended 2023`
- [intro-skipper/jellyfin-androidtv](https://github.com/intro-skipper/jellyfin-androidtv) - Android TV client with the Intro Skipper feature built in. `Jellyfin` · `Android TV` `Fire TV` · `GPL-2.0` `Free` `Ended 2025`
- [jellio](https://github.com/vanchaxy/jellio) - Stremio addon that puts your server's library into Stremio. `Jellyfin` `+Stremio addons` · `Web` · `GPL-3.0` `Ended 2025`
- [Jellyamp (jellyfin-archive)](https://github.com/jellyfin-archive/jellyamp) - Early Electron desktop music player for Jellyfin, now archived. `Jellyfin` · `Windows` `macOS` `Linux` · `MIT` `Free` `Ended 2020`
- [Jelly Desktop](https://github.com/imLinguin/jelly-desktop) - Community desktop client for Jellyfin, archived since 2022. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Free` `Ended 2022`
- [jellyfin-android-original](https://github.com/jellyfin-archive/jellyfin-android-original) - First Android app, replaced by Jellyfin for Android. `Jellyfin` · `Android` · `GPL-2.0` `Ended 2020`
- [jellyfin-androidtv-zidoo](https://github.com/Andy2244/jellyfin-androidtv-zidoo) - Android TV client tuned for Zidoo media players. `Jellyfin` · `Android TV` · `GPL-2.0` `Free` `Ended 2024` · [Source](https://github.com/fengfp/jellyfin-androidtv-zidoo)
- [jellyfin-client-ios](https://github.com/jellyfin-archive/jellyfin-client-ios) - First iOS app, replaced by Jellyfin for iOS and Swiftfin. `Jellyfin` · `iOS` · `MPL-2.0` `Ended 2020`
- [Jellyfin Legacy](https://github.com/jellyfin-archive/jellyfin-roku-legacy) - Former Roku app, archived in 2025 and frozen as the unsupported "Jellyfin Legacy" channel. `Jellyfin` · `Roku` · `GPL-2.0` `Ended 2025` · [Roku](https://channelstore.roku.com/details/cc5e559d08d9ec87c5f30dcebdeebc12/jellyfin)
- [jellyfin-mpv-player](https://github.com/wzyoct/jellyfin-mpv-player) - Unofficial Windows x64 desktop client with mpv playback. `Jellyfin` · `Windows` · `MIT` `Free` `Ended 2026`
- Jellyfin Music Player (06Games) - Archived work-in-progress macOS music player. `Jellyfin` · `macOS` · `Open source` `Ended`
- [jellyfin-samsungtv](https://github.com/jellyfin-archive/jellyfin-samsungtv) - Early app for Samsung Orsay TVs. `Jellyfin` · `Other TV` · `MIT` `Ended 2021`
- [jellyfin-svelte](https://gitlab.com/pSchwietzer/jellyfin-svelte) - Work-in-progress web client written in Svelte. `Jellyfin` · `Web` · `Open source` `Ended 2024`
- [Jellyfin Theater](https://github.com/jellyfin-archive/jellyfin-desktop-electron) - Early Electron desktop app, replaced by Jellyfin Media Player. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-2.0` `Ended 2020`
- [jellyfin-tui (austinwilcox)](https://github.com/austinwilcox/jellyfin-tui) - Rust terminal client; the repository became a Navidrome client in 2026, v0.5.1 is the last Jellyfin build. `Jellyfin` · `CLI` · `MIT` `Ended 2026`
- [Jellyfuse](https://github.com/OverGlass/jellyfuse-rn-legacy) - Legacy React Native Jellyfin client with Jellyseerr requests. `Jellyfin` · `iOS` · `GPL-3.0` `Free` `Ended 2026`
- [jfin](https://github.com/Sophia-Craw/jfin) - Music client for a Jellyfin library. `Jellyfin` · `Windows` `macOS` `Linux` · `Open source` `Free` `Ended 2026`
- [jfmp](https://github.com/n-peugnet/jfmp) - Music player. `Jellyfin` · `Windows` `macOS` `Linux` · `GPL-3.0` `Ended 2020`
- [jidoujisho](https://github.com/arianneorpilla/jidoujisho) - Japanese-learning immersion app that can stream video from a Jellyfin library. `Jellyfin` · `Android` · `GPL-3.0` `Free` `Ended 2025`
- Kolis Music - Apple-platform music player with CarPlay lyrics; removed from the App Store (link dead as of 2026-11). `Jellyfin` `Emby` `+Subsonic` · `iOS` `CarPlay` · `Ended 2026`
- [kyoku](https://github.com/httpjamesm/kyoku) - Music player. `Jellyfin` · `Windows` `macOS` `Linux` · `MPL-2.0` `Ended 2024`
- [LinPlayer](https://github.com/zzzwannasleep/LinPlayer) - Emby client with a Go core and a native interface per platform; archived. `Emby` · `Windows` `Linux` `Android` `Android TV` · `AGPL-3.0` `Ended 2026`
- [LunaSea](https://github.com/jagandeepbrar/lunasea) - Controller for the *arr stack and Tautulli, for phones and desktops. `Plex` · `Windows` `macOS` `Linux` `Android` `iOS` · `Open source` `Ended 2025`
- [Media Browser Classic](https://github.com/MediaBrowser/MediaBrowser.Classic) - Windows Media Center plug-in from Emby's Media Browser days. `Emby` · `Windows` · `Open source` `Ended 2019`
- MK Plex - Kodi add-on. `Plex` · `Kodi` · `Ended 2017`
- [MrMC](https://github.com/MrMC/mrmc) - Kodi fork for Apple TV and Android. `Plex` `Emby` `+Kodi` · `Android` `tvOS` · `Open source` `Ended 2020`
- [Muufin](https://github.com/rikkichy/Muufin) - Music player with a Material Expressive design. `Jellyfin` · `Android` · `GPL-3.0` `Free` `Ended 2026`
- [nettv-plex-client](https://github.com/hitolaus/nettv-plex-client) - Plex client for Philips NetTV smart TVs. `Plex` · `Other TV` · `Open source` `Ended 2014`
- [PLAYz Media for PLEX](https://github.com/simonjhogan/PLAYz-Media-for-PLEX) - Plex app for older LG NetCast smart TVs. `Plex` · `Other TV` · `Apache-2.0` `Ended 2015`
- Plex Alexa skill - Voice control for Plex players on Echo devices, disabled on 15 June 2026. `Plex` · `Alexa` · `Ended 2026`
- [plex_assistant](https://github.com/maykar/plex_assistant) - Home Assistant voice-casting component. `Plex` · `Google Assistant` `Home Assistant` · `MIT` `Ended 2021`
- [PleXBMC](https://github.com/hippojay/plugin.video.plexbmc) - Early Plex add-on for XBMC and Kodi; the repository is archived. `Plex` · `Kodi` · `GPL-2.0` `Ended 2020`
- [PlexFlux](https://github.com/brian9206/PlexFlux) - Music player. `Plex` · `Windows` · `MIT` `Ended 2018`
- [PlexForBoxee](https://github.com/grantmcwilliams/PlexForBoxee) - Plex client for Boxee boxes. `Plex` · `Other TV` · `Open source` `Ended 2017`
- [Plex for Kodi](https://github.com/plexinc/plex-for-kodi) - Plex's own Kodi add-on; abandoned since December 2023 and broken on Kodi 20 and later. `Plex` · `Kodi` · `GPL-2.0` `Ended 2023`
- Plex for PS3 - PlayStation 3 app, frozen in 2017 and removed from the store on 24 March 2023. `Plex` · `PS3` · `Ended 2023`
- [Plex for Ubuntu Touch](https://open-store.io/app/plex-local.luksus) - Unofficial Ubuntu Touch app for Plex. `Plex` · `Ubuntu Touch` · `GPL-3.0` `Ended 2018` · [Source](https://github.com/luksus42/plex-app)
- Plex for Xbox 360 - Xbox 360 app, no longer maintained. `Plex` · `Xbox 360` · `Ended`
- [Plex Home Theater](https://github.com/plexinc/plex-home-theater-public) - The original XBMC-based Plex media-centre app, replaced by Plex Media Player. `Plex` · `Windows` `macOS` `Linux` · `GPL-2.0` `Ended 2016`
- [plexio](https://github.com/vanchaxy/plexio) - Stremio addon that puts your server's library into Stremio. `Plex` `+Stremio addons` · `Web` · `MIT` `Ended 2025`
- [plexjs](https://github.com/jfremy/plexjs) - Archived 2013 Node.js web front end for Plex. `Plex` · `Web` · `Open source` `Free` `Ended 2013`
- plex-linux - Historical Plex Media Center client project for Linux. `Plex` · `Linux` · `Ended`
- [Plex Manager](https://github.com/sikelio/plexmanager) - Android server admin app. `Plex` · `Android` · `GPL-3.0` `Ended 2024` · [F-Droid](https://apt.izzysoft.de/fdroid/index/apk/wtf.plexmanager)
- [Plex Media Player](https://github.com/plexinc/plex-media-player) - Former desktop and TV-mode player; updates ended in January 2020 and the repository is archived. `Plex` · `Windows` `macOS` `Linux` · `GPL-2.0` `Ended 2022`
- [plex-music](https://github.com/knoopx/plex-music) - Archived web and desktop music player for Plex. `Plex` · `Windows` `macOS` `Linux` `Web` · `GPL-3.0` `Free` `Ended 2022`
- [plex-music-react-native-macosx](https://github.com/knoopx/plex-music-react-native-macosx) - React Native macOS music player for Plex. `Plex` · `macOS` · `GPL-3.0` `Free` `Ended 2022`
- [plexNMT](https://github.com/riplatt/plexNMT) - Plex client for Popcorn Hour and other Networked Media Tank players. `Plex` · `Other TV` · `Open source` `Ended 2013`
- Plex VR - Virtual theatre app for Daydream, Gear VR and Oculus Go, shut down in March 2024. `Plex` · `Other device` · `Ended 2024`
- [pmcli](https://github.com/Aanok/pmcli) - Command-line Plex video client written in Lua. `Plex` · `CLI` · `MIT` `Ended 2019` · [AUR](https://aur.archlinux.org/packages/pmcli-git)
- [RARflix](https://github.com/ljunkie/rarflix) - Community fork of the original Plex Roku channel; archived. `Plex` · `Roku` · `MIT` `Ended 2022`
- [RasPlex](https://github.com/RasPlex/RasPlex) - Raspberry Pi media-centre distribution built around a Plex client. `Plex` · `Linux` · `Open source` `Free` `Ended 2021`
- [Sonixd](https://github.com/jeffvli/sonixd) - Music player. `Jellyfin` `+Subsonic` · `Windows` `macOS` `Linux` · `GPL-3.0` `Ended 2024`
- [SPlayer](https://github.com/SPlayer-Dev/SPlayer) - Electron desktop music player with word-by-word lyrics. `Jellyfin` `Emby` `+Subsonic` · `Windows` `macOS` `Linux` · `AGPL-3.0` `Free` `Ended 2026`
- [Vantage](https://github.com/Jellyfin-PG/Vantage) - Flutter client for Android phones, Android TV and Windows. `Jellyfin` · `Windows` `Android` `Android TV` · `Open source` `Free` `Ended 2026`
- [VoiceControlForPlex](https://github.com/atomjack/VoiceControlForPlex) - Android voice control for players. `Plex` · `Android` · `Open source` `Ended 2019`

## More clients

[more-clients.md](more-clients.md) lists 439 smaller projects by platform. They live only on GitHub with no release and under 10 stars.

## Contribution Guidelines

Contributions are welcome. Read the [contributing guidelines](contributing.md) first. Entries live in [data/clients.yaml](data/clients.yaml) and the Markdown files are generated from it.

**More from DMM:** [Debrid Media Manager](https://debridmediamanager.com/) · [zurg](https://zurg.debridmediamanager.com/) · [rex](https://rex.debridmediamanager.com/) · [Docs](https://notes.debridmediamanager.com/) · [Sponsor](https://gatekeeper.debridmediamanager.com/) · [Discord](https://discord.com/invite/7u4YjMThXP) · [Reddit](https://www.reddit.com/r/debridmediamanager/)
