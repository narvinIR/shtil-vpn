<div align="center">

<img src="assets/icon.png" width="96" alt="Shtil VPN">

# Shtil VPN · Штиль

[Русский](README.md) · **English** · [Deutsch](README.de.md) · [Español](README.es.md) · [فارسی](README.fa.md)

Product site: **[shtil.ndvsdom54.ru](https://shtil.ndvsdom54.ru/en/)**

**VPN apps built on the [sing-box](https://github.com/SagerNet/sing-box) core (VLESS + Reality)
for Android phones, Android TV, Windows and macOS.**

Russian sites — banks, government services, marketplaces — stay on the direct route
while the VPN is on, so they keep full speed and do not treat you as a foreign visitor.

![Android](https://img.shields.io/badge/Android-6.0%2B-3ddc84)
![Android TV](https://img.shields.io/badge/Android%20TV-remote%20friendly-3ddc84)
![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078d4)
![macOS](https://img.shields.io/badge/macOS-12%2B-000000)
![Core](https://img.shields.io/badge/core-sing--box-blue)
![Protocol](https://img.shields.io/badge/protocol-VLESS%20%2B%20Reality-blue)

</div>

---

## At a glance

| Question | Answer |
|---|---|
| What it is | A VPN client for Android phones and TV boxes, Windows and macOS |
| Core and protocol | sing-box, VLESS + Reality over TCP |
| Russian sites | routed directly; the rule lists ship inside the app, nothing is fetched at runtime |
| Key | a subscription link from our Telegram bot — any other provider's VLESS link works too |
| App stores | not needed: we host the files ourselves and updates arrive over the air |
| Interface languages | Russian, English, German, Spanish, Persian |
| Subscription | 30 days free, then 499 ₽ per month or 600 Telegram Stars (about $6 in conversion); 2 hours can be tried with no Telegram at all |
| Accounts inside the app | none. No ads, no in-app purchases |

---

## Downloads

| Device | File | How to install |
|---|---|---|
| **Android phone or tablet** | [sub.ndvsdom54.ru/get](https://sub.ndvsdom54.ru/get) — the page picks the file for you | Open the address in the phone browser, tap “Download” |
| **Android TV** | [sub.ndvsdom54.ru/tv.apk](https://sub.ndvsdom54.ru/tv.apk) — the file starts right away | Type the address into a downloader app (Downloader, for example) with the remote |
| **Windows** | [ShtilVPN-windows.exe](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-windows.exe) | Download and run |
| **Mac, Apple silicon** | [ShtilVPN-mac-apple.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-apple.dmg) | Drag into Applications |
| **Mac, Intel** (2020 and older) | [ShtilVPN-mac-intel.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-intel.dmg) | Drag into Applications |

Not sure which Android build you need — take the
[universal one](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-android-universal.apk):
it is the heaviest file (about 76 MB) but installs on any device.

Every file in one list: [“Shtil — installation
files”](https://github.com/narvinIR/shtil-vpn/releases/tag/apps). The addresses there are
permanent — the file is replaced, the link stays the same.

The subscription key comes from [@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot):
30 days free, then 499 ₽ per month, or 600 Telegram Stars if you have no Russian card. You can also start without Telegram — the app has a
“Try now” button that opens a 2-hour guest session.

---

## Three steps to a connection

1. Download the file for your device from the table above and install it.
2. Tap “Try now” (2 hours, no Telegram) **or** get a subscription link from the bot and add it
   in the app — by hand, from the clipboard, or with the short code from a QR image.
3. Tap “Connect”. Russian sites keep opening directly; that is by design, not a fault.

A TV never has to type the key: the short code is shown as a QR image, the phone scans it,
and the subscription arrives on the TV by itself.

---

## How it looks

| Phone: connected | Phone: split routing | TV | Desktop |
|---|---|---|---|
| <img src="assets/phone-connected.png" width="180"> | <img src="assets/phone-split-routing.png" width="180"> | <img src="assets/tv-connected.png" width="260"> | <img src="assets/desktop-main.png" width="260"> |

---

## What each app can do

| Capability | Phone | TV | Windows | macOS |
|---|:---:|:---:|:---:|:---:|
| VLESS + Reality on the sing-box core | yes | yes | yes | yes |
| Russian sites routed directly (lists inside the app) | yes | yes | yes | yes |
| Subscription link instead of a long key | yes | yes | yes | yes |
| Short pairing code from the bot | yes | yes | yes | yes |
| Code delivered as a QR image from the phone | yes | yes | — | — |
| 2-hour guest access without Telegram | yes | yes | yes | yes |
| Over-the-air updates, no store involved | yes | yes | yes | yes |
| Per-app routing | yes | yes | — | — |
| Remote-friendly layout | — | yes | — | — |
| Log and live connection table | in progress | in progress | yes | yes |
| Five interface languages | yes | yes | yes | yes |

---

## Under the hood

- **Core** — [sing-box](https://github.com/SagerNet/sing-box), VLESS + Reality over TCP.
- **Split routing.** The lists of Russian domains and address ranges live inside the app and
  are never downloaded: a remote rule-set server can be unreachable from Russia, and then the
  VPN would simply refuse to start. For domains on the direct route only IPv4 answers are
  returned — otherwise the device would follow an AAAA record straight past the route.
- **One key for every device.** The subscription link works on the phone, the TV and the
  computer at once; when the key changes on the server, every device picks the new one up.
- **Over-the-air updates.** The app checks for a new version itself; on desktop an update is
  installed only if it carries our signature.
- **Nothing extra.** No accounts inside the app, no ads, no in-app purchases.

---

## What the system will say during installation

The apps are distributed outside Google Play and the App Store, so each system asks once.
That happens with any app installed from outside a store.

**Android (phone).** “Installing from this source is not allowed” → allow the browser to
install apps. Google may then show a red “app may be harmful” screen → “Install anyway”.

**Android TV.** The same red Google screen; the confirm button is at the bottom — reach it
with the remote.

**Windows.** A blue “Windows protected your PC” box → **“More info” → “Run anyway”**. We have
no publisher certificate: since 2024 Microsoft no longer sells instant trust at any price —
reputation is earned through install count.

**macOS.** The first launch is refused → **System Settings → Privacy & Security → “Open
Anyway”** → administrator password. After that the app opens with a normal double click.

---

## FAQ

**Do I need Google Play or the App Store?**
No. The file is downloaded from here or from the [install page](https://sub.ndvsdom54.ru/get),
and the app finds new versions on its own.

**How do I install it on a TV that has no browser?**
Use a downloader app such as Downloader: type `sub.ndvsdom54.ru/tv.apk` with the remote and the
file starts immediately. The address is deliberately short and has no “https://”.

**Why do banking and government sites break under other VPNs?**
Because their traffic goes through the tunnel and the site sees a foreign address. Here those
sites stay on the direct route, and the rule list travels inside the app.

**Can I use a key from another provider?**
Yes, if it is a subscription link or a key in VLESS format. The app is the entrance to a
tunnel; the server itself is not included.

**How many devices per key?**
Two at the same time. One subscription link covers the phone, the TV and the computer.

**Is there an iOS or Linux build?**
Not of our own. The subscription link works in third-party clients — v2RayTun on iOS, or any
sing-box based client.

**What about logs and accounts?**
There are no accounts inside the app, no ads and no in-app purchases. The subscription and the
payment live in the Telegram bot.

---

## Apps and sources

| App | System | Source | Licence |
|---|---|---|---|
| Shtil (Android) | Android 6.0+, phones and TV boxes | fork of [vpn4tv-native](https://github.com/VPN4TV/vpn4tv-native) | GPL-3.0 |
| Shtil for desktop | Windows 10/11, macOS 12+ | [shtil-vpn-desktop](https://github.com/narvinIR/shtil-vpn-desktop) | MIT |
| Core | inside both apps | [sing-box](https://github.com/SagerNet/sing-box) | GPL-3.0 |

This repository is the storefront: descriptions and permanent links to the files. Each file is
distributed under the licence of its own app from the table above.

Questions, bug reports and suggestions — [issues](https://github.com/narvinIR/shtil-vpn/issues)
or the bot [@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot).
