#!/usr/bin/env python3
"""Собирает страницу «Штиля» на пяти языках в docs/ (оттуда её отдаёт GitHub Pages).

Тексты — в site-src/i18n/*.json, вид — в site-src/style.css. Правится текст в одном
месте, страницы пересобираются целиком:

    python3 site-src/build.py
"""

import datetime
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "site-src"
OUT = ROOT / "docs"

SITE = "https://shtil.ndvsdom54.ru"
REPO = "https://github.com/narvinIR/shtil-vpn"
DL = REPO + "/releases/download/apps"
BOT = "https://t.me/RealityVPNBot_bot"
# ключ для IndexNow: Bing и Яндекс забирают страницу по уведомлению, без кабинета
INDEXNOW_KEY = "8c92923a9d5cb2cc4e8d403b5e7dc5d3"

LANGS = ["ru", "en", "de", "es", "fa"]
LANG_NAMES = {"ru": "Русский", "en": "English", "de": "Deutsch", "es": "Español", "fa": "فارسی"}
# справочник пишется на двух языках; с остальных страниц ссылка ведёт на английский
GUIDE_LANGS = ["ru", "en"]

FILES = {
    "android": f"{DL}/ShtilVPN-android-arm64.apk",
    "tv": f"{DL}/ShtilVPN-android-arm32.apk",
    "windows": f"{DL}/ShtilVPN-windows.exe",
    "mac": f"{DL}/ShtilVPN-mac-apple.dmg",
    "macintel": f"{DL}/ShtilVPN-mac-intel.dmg",
    "universal": f"{DL}/ShtilVPN-android-universal.apk",
    "ios": BOT,
}


def esc(s):
    return (
        s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    )


def url_for(lang, tail=""):
    return f"{SITE}/" if lang == "ru" and not tail else (
        f"{SITE}/{tail}" if lang == "ru" else f"{SITE}/{lang}/{tail}"
    )


def meta_head(lang, title, desc, canonical, alts, ld_list, root):
    """Шапка документа: одна на главную и на страницы справочника."""
    alt = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts)
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
        for x in ld_list
    )
    rtl = ' dir="rtl"' if lang == "fa" else ""
    return f"""<!doctype html>
<html lang="{lang}"{rtl}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{alt}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:locale" content="{lang}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#090e1a">
<link rel="icon" href="{root}assets/shtil-icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/icon-180.png">
<link rel="stylesheet" href="{root}assets/style.css">
{ld}
</head>
<body>
"""


def head(lang, d):
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q["q"],
                "acceptedAnswer": {"@type": "Answer", "text": q["a"]},
            }
            for q in d["faq"]["items"]
        ],
    }
    app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Shtil VPN",
        "alternateName": "Штиль VPN",
        "applicationCategory": "SecurityApplication",
        "operatingSystem": "Android 6.0+, Android TV, Windows 10/11, macOS 12+",
        "url": url_for(lang),
        "downloadUrl": FILES["android"],
        "installUrl": "https://sub.ndvsdom54.ru/get",
        "softwareHelp": BOT,
        "inLanguage": ["ru", "en", "de", "es", "fa"],
        "description": d["meta"]["description"],
        "offers": [
            {
                "@type": "Offer",
                "price": "499",
                "priceCurrency": "RUB",
                "category": "subscription",
                "url": BOT,
                "availability": "https://schema.org/InStock",
            },
            {
                "@type": "Offer",
                "price": "600",
                "priceCurrency": "XTR",
                "category": "subscription",
                "url": BOT,
                "availability": "https://schema.org/InStock",
            },
        ],
        "featureList": [f["title"] for f in d["inside"]["items"]],
        "screenshot": [f"{SITE}/assets/shots/{n}.png" for n in ("phone", "tv", "desktop")],
        "isBasedOn": "https://github.com/SagerNet/sing-box",
        "author": {"@type": "Organization", "name": "Shtil VPN", "url": SITE},
    }
    alts = [(l, url_for(l)) for l in LANGS] + [("x-default", url_for("en"))]
    return meta_head(
        lang,
        d["meta"]["title"],
        d["meta"]["description"],
        url_for(lang),
        alts,
        [app, faq],
        "" if lang == "ru" else "../",
    )


def langs_nav(lang):
    out = []
    for l in LANGS:
        cls = ' class="on"' if l == lang else ""
        out.append(f'<a href="{url_for(l)}"{cls} hreflang="{l}">{LANG_NAMES[l]}</a>')
    return "\n      ".join(out)


def guides_url(lang, slug=""):
    """Адрес справочника. Языки, которых в справочнике нет, ведут на английский."""
    base = lang if lang in GUIDE_LANGS else "en"
    return url_for(base, f"guides/{slug}/" if slug else "guides/")


def guide_body(blocks):
    out = []
    for b in blocks:
        parts = [f"<h2>{esc(b['h2'])}</h2>"]
        parts += [f"<p>{esc(p)}</p>" for p in b.get("p", [])]
        if b.get("list"):
            parts.append("<ul>" + "".join(f"<li>{esc(i)}</li>" for i in b["list"]) + "</ul>")
        if b.get("steps"):
            parts.append("<ol>" + "".join(f"<li>{esc(i)}</li>" for i in b["steps"]) + "</ol>")
        out.append('<section class="block">\n  ' + "\n  ".join(parts) + "\n</section>")
    return "\n".join(out)


def guide_chrome(lang, sec, root, inner):
    """Шапка, подвал и обёртка, общие для справочника и его страниц."""
    return f"""<header class="wrap top">
  <a class="brand" href="{url_for(lang)}">
    <img src="{root}assets/shtil-mark.svg" alt="" width="34" height="34">
    <b>Shtil VPN</b>
  </a>
  <nav class="langs" aria-label="{esc(sec["title"])}">
    <a href="{guides_url("ru")}"{' class="on"' if lang == "ru" else ""} hreflang="ru">Русский</a>
    <a href="{guides_url("en")}"{' class="on"' if lang == "en" else ""} hreflang="en">English</a>
  </nav>
</header>

<main class="wrap guide">
{inner}
</main>

<footer class="wrap">
  <p><a href="{guides_url(lang)}">{esc(sec["all"])}</a> · <a href="{url_for(lang)}">{esc(sec["back"])}</a> · <a href="{BOT}">@RealityVPNBot_bot</a></p>
</footer>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""


def render_guide(lang, art, sec, updated):
    root = "../../../" if lang != "ru" else "../../"
    canonical = guides_url(lang, art["slug"])
    alts = [(l, guides_url(l, art["slug"])) for l in GUIDE_LANGS]
    alts.append(("x-default", guides_url("en", art["slug"])))
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "TechArticle",
            "headline": art["title"],
            "description": art["description"],
            "inLanguage": lang,
            "url": canonical,
            "dateModified": updated,
            "author": {"@type": "Organization", "name": "Shtil VPN", "url": SITE},
            "isPartOf": {"@type": "WebSite", "name": "Shtil VPN", "url": SITE},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Shtil VPN", "item": url_for(lang)},
                {"@type": "ListItem", "position": 2, "name": sec["title"], "item": guides_url(lang)},
                {"@type": "ListItem", "position": 3, "name": art["title"], "item": canonical},
            ],
        },
    ]
    inner = f"""  <article>
    <p class="crumbs"><a href="{guides_url(lang)}">{esc(sec["title"])}</a></p>
    <h1>{esc(art["title"])}</h1>
    <p class="lead">{esc(art["lead"])}</p>
{guide_body(art["blocks"])}
    <p class="updated">{esc(sec["updated"])}: {updated}</p>
  </article>"""
    return meta_head(lang, art["title"], art["description"], canonical, alts, ld, root) + guide_chrome(
        lang, sec, root, inner
    )


def render_guides_index(lang, data, updated):
    root = "../" if lang == "ru" else "../../"
    sec = data["section"]
    canonical = guides_url(lang)
    alts = [(l, guides_url(l)) for l in GUIDE_LANGS] + [("x-default", guides_url("en"))]
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": sec["meta_title"],
            "description": sec["description"],
            "inLanguage": lang,
            "url": canonical,
            "dateModified": updated,
            "hasPart": [
                {
                    "@type": "TechArticle",
                    "headline": a["title"],
                    "description": a["description"],
                    "url": guides_url(lang, a["slug"]),
                }
                for a in data["articles"]
            ],
        }
    ]
    cards = "\n        ".join(
        f'<article class="card"><h3><a href="{guides_url(lang, a["slug"])}">{esc(a["title"])}</a></h3>'
        f'<p>{esc(a["description"])}</p></article>'
        for a in data["articles"]
    )
    inner = f"""  <div class="section-head">
    <h1>{esc(sec["title"])}</h1>
    <p>{esc(sec["lead"])}</p>
  </div>
  <div class="grid two">
        {cards}
  </div>"""
    return meta_head(lang, sec["meta_title"], sec["description"], canonical, alts, ld, root) + guide_chrome(
        lang, sec, root, inner
    )


def schema_svg(d):
    s = d["split"]["schema"]
    return f"""<svg viewBox="0 0 566 300" role="img" aria-label="{esc(s['alt'])}" class="routes">
  <defs>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#4F92FF"/><stop offset="1" stop-color="#7FB2FF"/>
    </linearGradient>
  </defs>

  <path d="M178 138 C 254 138, 272 76, 344 76" stroke="url(#line)" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <path d="M178 162 C 254 162, 272 224, 344 224" stroke="#46D189" stroke-width="3.5" fill="none" stroke-linecap="round"/>

  <rect x="6" y="114" width="172" height="72" rx="18" fill="rgba(79,146,255,.14)" stroke="#4F92FF" stroke-width="1.5"/>
  <text x="92" y="156" text-anchor="middle" fill="currentColor" font-size="17">{esc(s['device'])}</text>

  <rect x="344" y="36" width="216" height="80" rx="18" fill="rgba(79,146,255,.14)" stroke="#4F92FF" stroke-width="1.5"/>
  <text x="452" y="70" text-anchor="middle" fill="currentColor" font-size="17">{esc(s['server'])}</text>
  <text x="452" y="94" text-anchor="middle" fill="currentColor" opacity=".62" font-size="13">{esc(s['tunnel_label'])}</text>

  <rect x="344" y="184" width="216" height="80" rx="18" fill="rgba(70,209,137,.12)" stroke="#46D189" stroke-width="1.5"/>
  <text x="452" y="218" text-anchor="middle" fill="currentColor" font-size="17">{esc(s['direct'])}</text>
  <text x="452" y="242" text-anchor="middle" fill="currentColor" opacity=".62" font-size="13">{esc(s['direct_label'])}</text>
</svg>"""


def render(lang, d):
    root = "" if lang == "ru" else "../"
    labels = json.dumps(d["hero"]["download"], ensure_ascii=False)
    files = json.dumps(FILES, ensure_ascii=False)

    badges = "\n        ".join(f"<span>{esc(b)}</span>" for b in d["hero"]["badges"])
    split_list = "\n          ".join(f"<li>{esc(i)}</li>" for i in d["split"]["list"])
    shots = "\n        ".join(
        f'<figure class="shot"><img src="{root}assets/shots/{n}.png" alt="{esc(c)}" loading="lazy" '
        f'width="{w}" height="{h}"><span>{esc(c)}</span></figure>'
        for n, c, w, h in zip(
            ("phone", "tv", "desktop"),
            d["shots"]["captions"],
            (288, 1000, 1000),
            (640, 562, 700),
        )
    )
    steps = "\n        ".join(
        f'<article class="card"><span class="num">{n}</span><h3>{esc(s["title"])}</h3>'
        f"<p>{esc(s['text'])}</p></article>"
        for n, s in enumerate(d["steps"]["items"], 1)
    )
    prices = "\n        ".join(
        f'<article class="card price{" free" if p.get("free") else ""}">'
        f'<div class="amount">{esc(p["amount"])}</div><div class="per">{esc(p["per"])}</div>'
        f'<p class="note">{esc(p["note"])}</p></article>'
        for p in d["price"]["items"]
    )
    inside = "\n        ".join(
        f'<article class="card"><h3>{esc(i["title"])}</h3><p>{esc(i["text"])}</p></article>'
        for i in d["inside"]["items"]
    )
    install = "\n        ".join(
        f"<tr><th>{esc(i['system'])}</th><td>{esc(i['text'])}</td></tr>"
        for i in d["install"]["items"]
    )
    faq = "\n        ".join(
        f"<details><summary>{esc(q['q'])}</summary><p>{esc(q['a'])}</p></details>"
        for q in d["faq"]["items"]
    )

    return (
        head(lang, d)
        + f"""<header class="wrap top">
  <a class="brand" href="{url_for(lang)}">
    <img src="{root}assets/shtil-mark.svg" alt="" width="34" height="34">
    <b>{esc(d["brand"])}</b>
  </a>
  <a class="to-guides" href="{guides_url(lang)}">{esc(d["meta"]["guides"])}</a>
  <nav class="langs" aria-label="{esc(d["meta"]["langs"])}">
      {langs_nav(lang)}
  </nav>
</header>

<main>
  <section class="wrap hero">
    <img class="mark" src="{root}assets/shtil-icon.svg" alt="" width="124" height="124">
    <h1>{esc(d["hero"]["h1"])}</h1>
    <p class="lead">{esc(d["hero"]["lead"])}</p>
    <p class="cta">
      <a class="btn" data-download data-files='{files}' data-labels='{labels}'
         href="{FILES["android"]}">{esc(d["hero"]["download"]["android"])}</a>
      <span class="sub">{esc(d["hero"]["other"])} <a href="#platforms">{esc(d["hero"]["other_link"])}</a></span>
    </p>
    <p class="badges">
        {badges}
    </p>
  </section>

  <section class="wrap" id="routing">
    <div class="section-head">
      <h2>{esc(d["split"]["h2"])}</h2>
      <p>{esc(d["split"]["lead"])}</p>
    </div>
    <div class="split">
      {schema_svg(d)}
      <div>
        <ul>
          {split_list}
        </ul>
      </div>
    </div>
  </section>

  <section class="wrap" id="screens">
    <div class="section-head"><h2>{esc(d["shots"]["h2"])}</h2></div>
    <div class="shots">
        {shots}
    </div>
  </section>

  <section class="wrap" id="start">
    <div class="section-head">
      <h2>{esc(d["steps"]["h2"])}</h2>
      <p>{esc(d["steps"]["lead"])}</p>
    </div>
    <div class="grid three">
        {steps}
    </div>
  </section>

  <section class="wrap" id="price">
    <div class="section-head">
      <h2>{esc(d["price"]["h2"])}</h2>
      <p>{esc(d["price"]["lead"])}</p>
    </div>
    <div class="grid three">
        {prices}
    </div>
  </section>

  <section class="wrap" id="platforms">
    <div class="section-head">
      <h2>{esc(d["install"]["h2"])}</h2>
      <p>{esc(d["install"]["lead"])}</p>
    </div>
    <table>
      <tbody>
        {install}
      </tbody>
    </table>
  </section>

  <section class="wrap" id="inside">
    <div class="section-head"><h2>{esc(d["inside"]["h2"])}</h2></div>
    <div class="grid two">
        {inside}
    </div>
  </section>

  <section class="wrap" id="faq">
    <div class="section-head"><h2>{esc(d["faq"]["h2"])}</h2></div>
    <div>
        {faq}
    </div>
  </section>

  <section class="wrap last">
    <h2>{esc(d["last"]["h2"])}</h2>
    <p>{esc(d["last"]["lead"])}</p>
    <p class="cta">
      <a class="btn" data-download data-files='{files}' data-labels='{labels}'
         href="{FILES["android"]}">{esc(d["hero"]["download"]["android"])}</a>
      <span class="sub">{esc(d["hero"]["other"])} <a href="{REPO}/releases/tag/apps">{esc(d["hero"]["other_link"])}</a></span>
    </p>
  </section>
</main>

<footer class="wrap">
  <div class="grid three">
    <div>
      <h3>{esc(d["footer"]["apps_title"])}</h3>
      <p><a href="{REPO}/releases/tag/apps">{esc(d["footer"]["apps"])}</a></p>
    </div>
    <div>
      <h3>{esc(d["footer"]["source_title"])}</h3>
      <p><a href="https://github.com/narvinIR/shtil-vpn-desktop">shtil-vpn-desktop</a> · MIT<br>
      <a href="https://github.com/SagerNet/sing-box">sing-box</a> · GPL-3.0</p>
    </div>
    <div>
      <h3>{esc(d["footer"]["contact_title"])}</h3>
      <p><a href="{BOT}">@RealityVPNBot_bot</a></p>
    </div>
  </div>
  <p>{esc(d["footer"]["note"])}</p>
</footer>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""
    )


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)

    for name in ("style.css", "app.js", "shtil-mark.svg", "shtil-icon.svg"):
        src = SRC / name if (SRC / name).exists() else SRC / "assets" / name
        shutil.copy(src, OUT / "assets" / name)
    shutil.copytree(SRC / "assets" / "shots", OUT / "assets" / "shots")
    for extra in ("og.png", "icon-180.png"):
        shutil.copy(SRC / "assets" / extra, OUT / "assets" / extra)

    for lang in LANGS:
        d = json.loads((SRC / "i18n" / f"{lang}.json").read_text(encoding="utf-8"))
        page = render(lang, d)
        target = OUT / "index.html" if lang == "ru" else OUT / lang / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")
        print(f"{lang}: {len(page) // 1024} КБ → {target.relative_to(ROOT)}")

    guide_pages = [""]  # пустой хвост — сам индекс справочника
    for lang in GUIDE_LANGS:
        src = SRC / "i18n" / f"guides.{lang}.json"
        data = json.loads(src.read_text(encoding="utf-8"))
        updated = datetime.date.fromtimestamp(src.stat().st_mtime).isoformat()
        base = OUT / "guides" if lang == "ru" else OUT / lang / "guides"
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(render_guides_index(lang, data, updated), encoding="utf-8")
        for art in data["articles"]:
            page = base / art["slug"]
            page.mkdir(exist_ok=True)
            (page / "index.html").write_text(render_guide(lang, art, data["section"], updated), encoding="utf-8")
            if lang == GUIDE_LANGS[0]:
                guide_pages.append(art["slug"])
        print(f"{lang}: справочник — {len(data['articles'])} статей → {base.relative_to(ROOT)}")

    (OUT / "CNAME").write_text("shtil.ndvsdom54.ru\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )
    urls = "\n".join(
        "  <url>\n"
        f"    <loc>{url_for(l)}</loc>\n"
        + "".join(
            f'    <xhtml:link rel="alternate" hreflang="{a}" href="{url_for(a)}"/>\n'
            for a in LANGS
        )
        + "  </url>"
        for l in LANGS
    )
    urls += "\n" + "\n".join(
        "  <url>\n"
        f"    <loc>{guides_url(l, slug)}</loc>\n"
        + "".join(
            f'    <xhtml:link rel="alternate" hreflang="{a}" href="{guides_url(a, slug)}"/>\n'
            for a in GUIDE_LANGS
        )
        + "  </url>"
        for slug in guide_pages
        for l in GUIDE_LANGS
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    shutil.copy(ROOT / "llms.txt", OUT / "llms.txt")
    print("готово:", OUT)


if __name__ == "__main__":
    build()
