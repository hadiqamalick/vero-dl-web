# Vero: Documentation Hub

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

### Root decks

Pitch decks stay at the repo root so `assets/` paths resolve when opened in a browser.

| File | Description |
|------|-------------|
| [`vero_v2.html`](vero_v2.html) + [`vero_v2_script.md`](vero_v2_script.md) | Head of Engineering intro deck and narration script |
| [`vero_v2_technical.html`](vero_v2_technical.html) + [`vero_v2_technical_script.md`](vero_v2_technical_script.md) | Technical deep dive deck and script |
| [`vero_v1.html`](vero_v1.html) | Prior pitch deck version (kept for reference) |
| [`streamlit_app.py`](streamlit_app.py) | Streamlit Cloud entry; loads the pricing calculator |

### `docs/`

- [`pricing/`](docs/pricing/), pricing model, questionnaire, [calculator](docs/pricing/pricing_calculator.html), simple version
- [`data_audit.html`](docs/data_audit.html), stakeholder discovery (Grain / email / Slack → Answer log → PRD)
- [`case_studies/impact_metrics.md`](docs/case_studies/impact_metrics.md), internal impact numbers per client
- [`case_study_context_brief.md`](docs/case_study_context_brief.md), raw verified context for marketing case studies
- [`hadiqa_linkedin_content_brief.md`](docs/hadiqa_linkedin_content_brief.md), LinkedIn profile content brief
- [`vero_icp_targeting_brief.md`](docs/vero_icp_targeting_brief.md), ICP and targeting brief

### `html/`

Working HTML prototypes (may differ from the production Webflow site).

| File | Description |
|------|-------------|
| [`vero_landing.html`](html/vero_landing.html) | Landing page draft |
| [`vero_wireframe.html`](html/vero_wireframe.html) | Wireframe layout |
| [`core_offering.html`](html/core_offering.html) | Core offering deck |
| [`case_studies/`](html/case_studies/) | Case study HTML drafts |

### `upwork/`

Loom/video scripts and slide decks, see [`upwork/README.md`](upwork/README.md).

### `assets/`

Brand images and stack logos used by `vero_v2.html` and decks.

### Local-only (not in git)

These folders stay on disk for context but are excluded in `.gitignore`:

- **`Vero/`**, source `.docx` files, pitch deck, landing copy, competitor notes, PDF exports
- **`Dashboards/`**, client dashboard PDFs and screenshots (may contain client-specific data)
- **`upwork/`**, Loom/video scripts and slide decks
- **`sources/`**, LinkedIn PDF exports and other one-off source dumps

To track a local-only folder, remove its entry from `.gitignore` and commit deliberately.

## Naming

File and folder names use `_` (not `-`). **datumlabs** is one word in paths. See [`.cursor/rules/project_conventions.mdc`](.cursor/rules/project_conventions.mdc).

## External references

- [Vero Core Offering (Google Doc)](https://docs.google.com/document/d/1V6bYGZ9Pwuc6zcqoBsTEaEgIgR4ejyO0zxmeUOKyLh0/edit?tab=t.0)
