# Upwork Video Plan — Datum Labs (no Vero)

**Presenter:** Hadiqa  
**Company:** Datum Labs  
**Use for:** Upwork profile video, freelancer invites  
**Format:** Animated HTML slides + Loom (screen + small circular webcam)  
**Target length:** ~2.5–3 minutes (~90 seconds spoken)  
**Deck files:**
- `upwork/deck/datumlabs.html` — **8 slides** (includes case study slide 6)
- `upwork/deck/datumlabs_no_cases.html` — **7 slides** (skips case study — shorter recording)

**To preview:** Open in browser → press **F** for fullscreen → **→** or **Space** to advance. Dashed circle bottom-right = Loom camera safe zone.

**No “Vero” in speech or slides.** Datum Labs consulting pitch — like colleague script.

---

## Production notes

- Advance slides with **arrow keys** in Loom (Screen + Camera).
- Hide self-view if the bubble is distracting.
- Record **3 takes max**; pick the most natural.
- Do **not** name individual clients (Filed, GovPlus, etc.). Use *SaaS* and *service-based companies* only.
- **One dedicated stack slide (Slide 7)** — logos on screen; one short spoken line grouped by layer. Upwork buyers search for tools; don't bury them only in the CTA.

---

## Slide overview

| # | Title | Purpose |
|---|-------|---------|
| 1 | Scattered data. No single picture. | Hook |
| 2 | We unify it all | Solution |
| 3 | Days, not months | The work — pipelines, reports, speed |
| 4 | Toward analytics, fast | Payoff — analytics while setup lands |
| 5 | How it works | Data flow diagram (visual only — tools on slide 7) |
| 6 | What clients achieve | Anonymized proof |
| 7 | Where I've worked · My stack | Industry icons + tech by function |
| 8 | Hi, I'm Hadiqa · Let's talk | CTA |

---

## Slide 1 — Scattered data. No single picture.

### On screen

**Headline:** Scattered data. No single picture.

**Subtext:** CRM · Billing · Product DB · Ad platforms · Spreadsheets — data everywhere, but no one view of where the business is heading.

**Visual:** Icons scattered / disconnected (HubSpot, Stripe, Postgres, Google Ads, Meta, spreadsheet).

### Spoken script

> Hi, I'm Hadiqa — Senior Data Analyst at Datum Labs.
>
> Most teams I work with don't have a data problem — they have a **scattered data problem**.
>
> CRM in one place. Billing in another. Product data in a database. Ad spend across three platforms. But nobody can see one clear picture of where the business is actually heading.

---

## Slide 2 — We unify it all

### On screen

**Headline:** We unify it all.

**Subtext:**
- Scattered systems → one foundation
- One clear picture of your business
- Live dashboards · timely alerts
- Decisions driven by data

**Visual:** Scattered icons collapsing into one unified block.

### Spoken script

> That's what we do at **Datum Labs**. We help startups and growing companies pull scattered systems together into one foundation — so you get one clear picture, live dashboards you can trust, timely alerts when something shifts, and decisions driven by data.

---

## Slide 3 — Days, not months

### On screen

**Headline:** Days, not months.

**Subtext:** Connecting sources · Building pipelines · Reports in production — the work that usually slows teams down.

```
┌─────────────────────┐         ┌─────────────────────┐
│  BUILDING IN-HOUSE  │    →    │   WITH DATUM LABS   │
│     3 – 6 months    │         │       days          │
│  hire · pipelines   │         │  setup · reports live│
└─────────────────────┘         └─────────────────────┘
```

**Chips:** ✓ Data connected across sources · ✓ Pipelines built · ✓ Reports in production

### Spoken script

> All of this work — connecting your data from different sources, building the pipelines, getting your reports into production — is what slows teams down. Pipeline building alone takes months when you're hiring or pulling engineers off product. We get through it in days, so you can move toward analytics right from the start.

---

## Slide 4 — Toward analytics, fast

### On screen

**Headline:** Toward analytics, fast.

**Subtext:** We handle the heavy setup. You focus on insights.

**Visual:** Split — greyed ("Pipeline building · Source connections · Reports") vs active ("Analytics · Timely alerts · Decisions driven by data").

### Spoken script

> While we land the setup, you can already be moving toward **your analytics** — timely alerts, the metrics that matter, and decisions driven by data.

---

## Slide 5 — How it works (data flow diagram)

### On screen

**Headline:** How it works.

```
Scattered Sources  →  Pipelines  →  Warehouse  →  Models  →  Dashboards
 CRM · Billing         dlt /           BigQuery      dbt        MRR · CAC
 Ads · Product DB      Airbyte         Snowflake               Retention
                       Dagster                                 Pipeline
```

**Visual:** Animated arrows between stages.

### Spoken script

> This is how the pieces fit together — your sources connected, data flowing through pipelines, clean models in the middle, and dashboards and alerts on the other side.

---

## Slide 6 — What clients achieve (anonymized)

### On screen

**Headline:** What clients achieve.

#### SaaS companies

| Before | After |
|--------|-------|
| Product, billing, and ads in separate platforms | 12+ sources unified into one warehouse |
| No shared view of engagement or funnel | One engagement model across the full funnel |
| Manual exports after every release | Automated pipelines — zero manual pulls |

#### Service-based companies

| Before | After |
|--------|-------|
| 9 disconnected systems, no warehouse | 1 unified warehouse, all sources connected |
| 3 teams reporting 3 different numbers | 1 source of truth across ops, sales, and finance |
| Rising complaints, no visible root cause | Refund rate cut in half once the full picture was clear |

**Footer:** *SaaS clients · Service-based clients · Datum Labs engagements*

### Spoken script

> We've done this for both **SaaS companies** and **service-based companies**.
>
> For SaaS teams — product events, billing, and ad spend were scattered across a dozen systems with no shared identity. We unified them, and they went from manual exports to automated pipelines and one view of the full funnel.
>
> For a service-based client — nine disconnected systems, three teams with three different numbers, and rising refunds with no one able to see why. We unified everything into one warehouse. Refund rate cut in half once they could see the full picture.

---

## Slide 7 — Where I've worked · My stack

### On screen

**Headline:** Where I've worked · What I build with

**On screen — two columns (speak left → right, in sync with what's shown):**

#### Left — Industries *(icons or simple illustrations per sector)*
| | |
|--|--|
| **SaaS** | app / subscription icon |
| **Fintech** | payments / card icon |
| **Marketplaces** | two-sided / cart icon |
| **Service-based** | operations / team icon |

#### Right — My tech stack by function *(logos per row)*
| Function | Tools |
|----------|-------|
| **Ingestion** | Airbyte · dlt · Fivetran |
| **Warehousing** | BigQuery · Snowflake · ClickHouse |
| **Transform** | dbt |
| **Orchestration** | Dagster |
| **BI & dashboards** | Metabase · Hex · Looker · Power BI |

**Visual:** Left = four industry tiles with a small picture/icon each. Right = five function rows with tool logos. Script follows the slide — industries first, stack second.

### Spoken script

> I've worked across **these industries** — SaaS, fintech, marketplaces, and service-based companies.
>
> And **this is my stack** — Airbyte and dlt for ingestion, BigQuery and Snowflake for warehousing, dbt for modeling, Dagster for orchestration, and Metabase and Hex for dashboards.

---

## Slide 8 — Hi, I'm Hadiqa · Let's talk

### On screen

**Headline:** Let's map your stack.

**Presenter:** Hadiqa — Senior Data Analyst · Datum Labs  
**One line:** *I connect sources, build models, and ship dashboards your team actually uses.*

**CTA:** datumlabs.io · *Invite me to your project on Upwork*

### Spoken script

> I'm Hadiqa. I handle the hands-on build — and I stay on as your analyst as you grow.
>
> If your data is scattered and you can't see where your business is heading — invite me to your project. Happy to take a look.

---

## Full script (rehearsal)

```
Hi, I'm Hadiqa — Senior Data Analyst at Datum Labs.

Most teams I work with don't have a data problem — they have a scattered data problem.

CRM in one place. Billing in another. Product data in a database.
Ad spend across three platforms. But nobody can see one clear picture
of where the business is actually heading.

That's what we do at Datum Labs. We help startups and growing companies pull
scattered systems together into one foundation — so you get one clear picture,
live dashboards you can trust, timely alerts when something shifts,
and decisions driven by data.

All of this work — connecting your data from different sources, building the pipelines,
getting your reports into production — is what slows teams down. Pipeline building alone
takes months when you're hiring or pulling engineers off product. We get through it in days,
so you can move toward analytics right from the start.

While we land the setup, you can already be moving toward your analytics — timely alerts,
the metrics that matter, and decisions driven by data.

This is how the pieces fit together — your sources connected, data flowing through
pipelines, clean models in the middle, and dashboards and alerts on the other side.

We've done this for both SaaS companies and service-based companies.

For SaaS teams — product events, billing, and ad spend were scattered across
a dozen systems with no shared identity. We unified them, and they went from
manual exports to automated pipelines and one view of the full funnel.

For a service-based client — nine disconnected systems, three teams with
three different numbers, and rising refunds with no one able to see why.
We unified everything into one warehouse. Refund rate cut in half once
they could see the full picture.

I've worked across these industries — SaaS, fintech, marketplaces,
and service-based companies.

And this is my stack — Airbyte and dlt for ingestion, BigQuery and Snowflake
for warehousing, dbt for modeling, Dagster for orchestration, and Metabase
and Hex for dashboards.

I'm Hadiqa. I handle the hands-on build — and I stay on as your analyst as you grow.

If your data is scattered and you can't see where your business is heading —
invite me to your project. Happy to take a look.
```

---

## HTML deck — build checklist

### `upwork/deck/datumlabs.html` (with case studies)

- [x] 8 slides, 16:9, keyboard nav (← → spacebar · F fullscreen)
- [x] Datum Labs branding
- [x] Slide 5: data flow diagram
- [x] Slide 6: two-column anonymized outcomes
- [x] Slide 7: industry tiles + stack by function
- [x] Slide 8: CTA + avatar placeholder (Loom safe zone bottom-right)
- [x] Slide counter

### `upwork/deck/datumlabs_no_cases.html` (shorter)

- [x] Same as above but **skips slide 6** — 7 slides total

---

## Open questions / edits

_Add notes here before recording:_

- [x] Slide 2 locked — Datum Labs, no Vero
- [x] Slide 3 locked — speed contrast + chips
- [x] Slide 7 added — dedicated stacks slide (tools on screen, one spoken line)
- [ ] Confirm presenter photo for Slide 8
- [ ] "about a week" vs "5 to 7 days"
- [ ] Stats on Slide 6 — final?

---

## Changelog

| Date | Change |
|------|--------|
| 2026-07-02 | Slide 7 — first-person script; industry icons + "this is my stack" aligned to slide |
| 2026-07-03 | Consolidated to `upwork/script/` and `upwork/deck/` |
| 2026-07-02 | Renamed layout — `upwork/script/`, `upwork/deck/` |
| 2026-07-02 | Moved to `upwork/script/` and `upwork/deck/` |
