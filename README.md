# Vero — Documentation Hub

Internal workspace for all Vero context: copy drafts, pricing, case study notes, HTML prototypes, and sales/video assets. Use this repo to discuss ongoing changes before they ship to the live site.

**Live site:** [datumlabs.io/vero](https://www.datumlabs.io/vero)

## Case studies (live)

| Client | URL |
|--------|-----|
| AI Voice Agent SaaS | [datumlabs.io/vero/ai-voice-agent-saas](https://www.datumlabs.io/vero/ai-voice-agent-saas) |
| AI Voice SaaS | [datumlabs.io/vero/ai-voice-saas](https://www.datumlabs.io/vero/ai-voice-saas) |
| Filed | [datumlabs.io/vero/filed](https://www.datumlabs.io/vero/filed) |
| GovPlus | [datumlabs.io/vero/govplus](https://www.datumlabs.io/vero/govplus) |
| Voltera | [datumlabs.io/vero/voltera](https://www.datumlabs.io/vero/voltera) |

## Repo map

### `docs/`

- [`pricing/`](docs/pricing/) — pricing model, questionnaire, simple version
- [`case_studies/impact_metrics.md`](docs/case_studies/impact_metrics.md) — internal impact numbers per client
- [`video_plan.md`](docs/video_plan.md) — index to Upwork/Vero video assets

### `html/`

Working HTML prototypes (may differ from the production Webflow site).

| File | Description |
|------|-------------|
| [`vero_landing.html`](html/vero_landing.html) | Landing page draft |
| [`vero_wireframe.html`](html/vero_wireframe.html) | Wireframe layout |
| [`core_offering.html`](html/core_offering.html) | Core offering deck |
| [`case_studies/`](html/case_studies/) | Case study HTML drafts |

### `upwork/`

Loom/video scripts and slide decks — see [`upwork/README.md`](upwork/README.md).

### `assets/`

Brand and roadmap images used in docs and decks.

### Local-only (not in git)

These folders stay on disk for context but are excluded in `.gitignore`:

- **`Vero/`** — source `.docx` files, pitch deck, landing copy, competitor notes, PDF exports
- **`Dashboards/`** — client dashboard PDFs and screenshots (may contain client-specific data)

To track either folder, remove its entry from `.gitignore` and commit deliberately.

## Naming

File and folder names use `_` (not `-`). **datumlabs** is one word in paths. See [`.cursor/rules/file_naming.mdc`](.cursor/rules/file_naming.mdc).

## External references

- [Vero Core Offering (Google Doc)](https://docs.google.com/document/d/1V6bYGZ9Pwuc6zcqoBsTEaEgIgR4ejyO0zxmeUOKyLh0/edit?tab=t.0)
