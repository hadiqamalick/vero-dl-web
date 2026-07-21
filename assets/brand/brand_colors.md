# Datum Labs brand colors

Source: [datumlabs.io/media-kit](https://www.datumlabs.io/media-kit)

| Name | Hex | RGB | Notes |
|------|-----|-----|-------|
| Obsidian Black | `#171717` | `23, 23, 23` | Primary dark |
| Ivory Silk | `#FFFCF7` | `255, 252, 247` | Warm off-white |
| Azure Radiance | `#237FDE` | `35, 127, 222` | Brand blue (official) |
| Jet Black | `#292929` | `41, 41, 41` | Secondary dark |
| Pure White | `#FFFFFF` | `255, 255, 255` | White |
| Midnight Abyss Gradient | `#041734` → `#020B18` | — | Dark gradient |
| Obsidian Night | `#0A0F14` | `10, 15, 20` | Near-black |

## CSS variables (suggested)

```css
:root {
  --dl-obsidian-black: #171717;
  --dl-ivory-silk: #FFFCF7;
  --dl-azure-radiance: #237FDE;
  --dl-jet-black: #292929;
  --dl-pure-white: #FFFFFF;
  --dl-obsidian-night: #0A0F14;
  --dl-midnight-abyss: linear-gradient(180deg, #041734 0%, #020B18 100%);
}
```

## Typography

- **Font:** Lexend (weights 300–700 on media kit; variable TTF includes Thin–Black)
- **File:** `fonts/lexend_variable.ttf`
- **License:** `fonts/OFL.txt`

## Note on deck blue

Some Vero decks historically used `#4a9eed`. Prefer **`#237FDE`** (Azure Radiance) for new work to match the media kit.
