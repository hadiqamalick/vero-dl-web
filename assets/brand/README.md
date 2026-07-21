# Datum Labs media kit assets

Pulled from [datumlabs.io/media-kit](https://www.datumlabs.io/media-kit) for decks, slides, and landing pages.

## Layout

```
assets/brand/
  brand_colors.md          # Official palette + CSS tokens
  README.md                # This file
  fonts/
    lexend_variable.ttf    # Lexend variable (all weights)
    OFL.txt                # Font license
  icons/
    favicon.png
    webclip.png
    datumlabs_icon.png
    slack/                 # Slack emoji / icon packs
  logos/
    png/                   # Logo PNGs (bg variants + transparent)
    png_alt/               # Alternate PNG renders from pack 2
    svg/                   # SVG variants (prefer these in HTML)
  social/
    linkedin_cover.png
    linkedin_mockup_example.png
  source_zips/             # Original downloads from the media kit
```

## Logos: which file to use

| Use case | Path |
|----------|------|
| Dark slides / dark UI | `logos/svg/all_white_transparent.svg` or `text_white_logo_bg_transparent.svg` |
| Light slides / light UI | `logos/svg/all_black_transparent.svg` or `text_black_logo_bg_transparent.svg` |
| Colored mark on dark | `logos/svg/logo_black_bg_white.svg` / related variants |
| Website header style | `logos/svg/datumlabs_logo_web.svg` |
| Favicon / small mark | `icons/favicon.png` or `icons/datumlabs_icon.png` |

## Source note

The media kit lists two zips:

1. **Logos.zip** → PNG + SVG logo set (`source_zips/logos_pack_1_png_svg.zip`)
2. **"Font.zip" link** → mislabeled on the site; it is a second logo pack with PNG/SVG + Slack icons (`source_zips/logos_pack_2_png_svg_slack.zip`)

Lexend was not a real font archive on the kit page (only Google Fonts embedding). We downloaded the official variable TTF from the [google/fonts](https://github.com/google/fonts/tree/main/ofl/lexend) OFL package.
