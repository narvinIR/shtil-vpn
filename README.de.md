<div align="center">

<img src="assets/icon.png" width="96" alt="Shtil VPN">

# Shtil VPN · Штиль

[Русский](README.md) · [English](README.en.md) · **Deutsch** · [Español](README.es.md) · [فارسی](README.fa.md)

Produktseite: **[shtil.ndvsdom54.ru](https://shtil.ndvsdom54.ru/de/)**

**VPN-Apps auf Basis des [sing-box](https://github.com/SagerNet/sing-box)-Kerns (VLESS + Reality)
für Android-Telefone, Android TV, Windows und macOS.**

Russische Seiten — Banken, Behördenportale, Marktplätze — bleiben bei eingeschaltetem VPN auf
dem direkten Weg und laufen deshalb mit voller Geschwindigkeit weiter.

![Android](https://img.shields.io/badge/Android-6.0%2B-3ddc84)
![Android TV](https://img.shields.io/badge/Android%20TV-fernbedienbar-3ddc84)
![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078d4)
![macOS](https://img.shields.io/badge/macOS-12%2B-000000)
![Kern](https://img.shields.io/badge/Kern-sing--box-blue)
![Protokoll](https://img.shields.io/badge/Protokoll-VLESS%20%2B%20Reality-blue)

</div>

---

## Auf einen Blick

| Frage | Antwort |
|---|---|
| Was ist das | Ein VPN-Client für Android-Telefone und -Fernseher, Windows und macOS |
| Kern und Protokoll | sing-box, VLESS + Reality über TCP |
| Russische Seiten | laufen direkt; die Regellisten stecken in der App und werden nie nachgeladen |
| Schlüssel | ein Abo-Link aus unserem Telegram-Bot — jeder andere VLESS-Link funktioniert ebenfalls |
| App-Stores | nicht nötig: wir verteilen die Dateien selbst, Updates kommen über die Luft |
| Sprachen der Oberfläche | Russisch, Englisch, Deutsch, Spanisch, Persisch |
| Abo | 30 Tage kostenlos, danach 499 ₽ pro Monat oder 600 Telegram Stars (umgerechnet etwa 6 $); 2 Stunden sind ganz ohne Telegram möglich |
| Konten in der App | keine. Keine Werbung, keine In-App-Käufe |

---

## Downloads

| Gerät | Datei | Installation |
|---|---|---|
| **Android-Telefon oder -Tablet** | [sub.ndvsdom54.ru/get](https://sub.ndvsdom54.ru/get) — die Seite wählt die Datei selbst | Adresse im Browser des Telefons öffnen, „Herunterladen“ antippen |
| **Android TV** | [sub.ndvsdom54.ru/tv.apk](https://sub.ndvsdom54.ru/tv.apk) — die Datei startet sofort | Adresse mit der Fernbedienung in eine Downloader-App eingeben |
| **Windows** | [ShtilVPN-windows.exe](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-windows.exe) | Herunterladen und starten |
| **Mac, Apple-Chip** | [ShtilVPN-mac-apple.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-apple.dmg) | In „Programme“ ziehen |
| **Mac, Intel** (2020 und älter) | [ShtilVPN-mac-intel.dmg](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-mac-intel.dmg) | In „Programme“ ziehen |

Unklar, welche Android-Datei passt — dann die
[universelle](https://github.com/narvinIR/shtil-vpn/releases/download/apps/ShtilVPN-android-universal.apk)
nehmen: sie ist die schwerste (rund 76 MB), läuft aber auf jedem Gerät.

Alle Dateien in einer Liste: [„Shtil — Installationsdateien“](https://github.com/narvinIR/shtil-vpn/releases/tag/apps).
Die Adressen dort bleiben bestehen — die Datei wird ersetzt, der Link bleibt gleich.

Den Abo-Schlüssel gibt [@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot): 30 Tage kostenlos,
danach 499 ₽ im Monat oder 600 Telegram Stars, wenn es keine russische Karte gibt. Ohne Telegram geht es auch — in der App öffnet „Jetzt testen“ eine
Gastsitzung über 2 Stunden.

---

## Drei Schritte bis zur Verbindung

1. Die passende Datei aus der Tabelle herunterladen und installieren.
2. „Jetzt testen“ antippen (2 Stunden, ohne Telegram) **oder** den Abo-Link im Bot holen und in
   der App hinzufügen — von Hand, aus der Zwischenablage oder per Kurzcode vom QR-Bild.
3. „Verbinden“ antippen. Russische Seiten öffnen weiterhin direkt — das ist Absicht, kein Fehler.

Am Fernseher muss niemand tippen: Der Kurzcode erscheint als QR-Bild, das Telefon scannt ihn,
und das Abo landet von selbst auf dem Fernseher.

---

## So sieht es aus

| Telefon: verbunden | Telefon: getrennte Wege | Fernseher | Rechner |
|---|---|---|---|
| <img src="assets/phone-connected.png" width="180"> | <img src="assets/phone-split-routing.png" width="180"> | <img src="assets/tv-connected.png" width="260"> | <img src="assets/desktop-main.png" width="260"> |

---

## Was jede App kann

| Funktion | Telefon | Fernseher | Windows | macOS |
|---|:---:|:---:|:---:|:---:|
| VLESS + Reality auf dem sing-box-Kern | ja | ja | ja | ja |
| Russische Seiten direkt (Listen in der App) | ja | ja | ja | ja |
| Abo-Link statt langem Schlüssel | ja | ja | ja | ja |
| Kurzcode aus dem Bot | ja | ja | ja | ja |
| Code als QR-Bild vom Telefon | ja | ja | — | — |
| Gastzugang 2 Stunden ohne Telegram | ja | ja | ja | ja |
| Updates über die Luft, ohne Store | ja | ja | ja | ja |
| Auswahl der Apps im Tunnel | ja | ja | — | — |
| Layout für die Fernbedienung | — | ja | — | — |
| Protokoll und Verbindungsliste | in Arbeit | in Arbeit | ja | ja |
| Fünf Sprachen | ja | ja | ja | ja |

---

## Was drinsteckt

- **Kern** — [sing-box](https://github.com/SagerNet/sing-box), VLESS + Reality über TCP.
- **Getrennte Wege.** Die Listen russischer Domains und Adressbereiche liegen in der App und
  werden nie geladen: Ein entfernter Regel-Server kann aus Russland unerreichbar sein, und dann
  würde das VPN gar nicht erst starten. Für Domains auf dem direkten Weg gibt es nur IPv4-Antworten,
  sonst folgte das Gerät einem AAAA-Eintrag an der Route vorbei.
- **Ein Schlüssel für alle Geräte.** Der Abo-Link gilt gleichzeitig für Telefon, Fernseher und
  Rechner; ändert sich der Schlüssel auf dem Server, holen sich alle Geräte den neuen selbst.
- **Updates über die Luft.** Die App prüft selbst auf neue Versionen; am Rechner wird nur
  installiert, was unsere Signatur trägt.
- **Nichts Überflüssiges.** Keine Konten in der App, keine Werbung, keine In-App-Käufe.

---

## Was das System bei der Installation sagt

Die Apps werden außerhalb von Google Play und App Store verteilt, deshalb fragt jedes System
einmal nach — wie bei jeder App von außerhalb eines Stores.

**Android (Telefon).** „Installation aus dieser Quelle nicht erlaubt“ → dem Browser das
Installieren erlauben. Danach zeigt Google eventuell einen roten Hinweis → „Trotzdem installieren“.

**Android TV.** Derselbe rote Google-Hinweis; die Bestätigung steht unten und wird mit der
Fernbedienung erreicht.

**Windows.** Blaues Fenster „Der Computer wurde durch Windows geschützt“ → **„Weitere
Informationen“ → „Trotzdem ausführen“**. Ein Herausgeberzertifikat haben wir nicht: Microsoft
verkauft seit 2024 kein sofortiges Vertrauen mehr, es entsteht über die Zahl der Installationen.

**macOS.** Der erste Start wird abgelehnt → **Systemeinstellungen → Datenschutz & Sicherheit →
„Dennoch öffnen“** → Administratorkennwort. Danach startet die App per Doppelklick.

---

## Häufige Fragen

**Braucht es Google Play oder den App Store?**
Nein. Die Datei kommt von hier oder von der [Installationsseite](https://sub.ndvsdom54.ru/get),
neue Versionen findet die App selbst.

**Wie installiere ich auf einem Fernseher ohne Browser?**
Über eine Downloader-App: `sub.ndvsdom54.ru/tv.apk` mit der Fernbedienung eingeben, die Datei
startet sofort. Die Adresse ist absichtlich kurz und ohne „https://“.

**Warum brechen Bank- und Behördenseiten unter anderen VPNs ab?**
Weil ihr Verkehr durch den Tunnel läuft und die Seite eine ausländische Adresse sieht. Hier
bleiben diese Seiten auf dem direkten Weg, und die Liste reist in der App mit.

**Funktioniert ein Schlüssel eines anderen Anbieters?**
Ja, wenn es ein Abo-Link oder ein Schlüssel im VLESS-Format ist. Die App ist der Eingang zum
Tunnel; der Server gehört nicht dazu.

**Wie viele Geräte pro Schlüssel?**
Zwei gleichzeitig. Ein Abo-Link deckt Telefon, Fernseher und Rechner ab.

**Gibt es eine Version für iOS oder Linux?**
Keine eigene. Der Abo-Link funktioniert in fremden Clients — etwa v2RayTun unter iOS oder jedem
sing-box-Client.

---

## Apps und Quellcode

| App | System | Quellcode | Lizenz |
|---|---|---|---|
| Shtil (Android) | Android 6.0+, Telefone und Fernseher | Fork von [vpn4tv-native](https://github.com/VPN4TV/vpn4tv-native) | GPL-3.0 |
| Shtil für den Rechner | Windows 10/11, macOS 12+ | [shtil-vpn-desktop](https://github.com/narvinIR/shtil-vpn-desktop) | MIT |
| Kern | in beiden Apps | [sing-box](https://github.com/SagerNet/sing-box) | GPL-3.0 |

Dieses Repository ist die Auslage: Beschreibungen und dauerhafte Links zu den Dateien. Jede Datei
steht unter der Lizenz ihrer App aus der Tabelle oben.

Fragen, Fehlerberichte und Vorschläge — [Issues](https://github.com/narvinIR/shtil-vpn/issues)
oder der Bot [@RealityVPNBot_bot](https://t.me/RealityVPNBot_bot).
