# Vero Pricing Model: Considerations, Cost Factors & Architecture

*Datum Labs · Internal pricing framework · Last updated 2026-06-30*

This document defines **how Vero should be priced**. It does two things:

1. Lays out every cost factor and strategic consideration that the price has to absorb.
2. Turns those factors into a **bottom-up cost model** (formulas + a worked example) that you can plug real numbers into.

The numbers in the worked examples are **illustrative placeholders**, flagged as `«assumption»`. Replace them with your real internal rates before quoting.

---

## 1. The one decision that drives everything: split build from run

Vero's offer on the landing page is two products bolted together:

- **"Live in 5–7 days"**, a one-time *build*.
- **"We stay on as your data team"**, an ongoing *managed retainer*.

These have completely different cost structures and must be priced as **two separate line items**:

| | One-time **Build** | Recurring **Run / Retainer** |
|---|---|---|
| What it is | Designing & deploying the stack | Keeping it alive + new work |
| Cost driver | **Engineering hours** | **Tool licenses + infra + maintenance labor** |
| Bills as | Fixed setup fee | Monthly (or annual) subscription |
| Risk owner | Vero (fixed scope → Vero eats overruns) | Shared (volume/usage can drift) |

> **Why this matters:** If you fold everything into one number you will either lose money on maintenance or look expensive on day one. The build fee anchors against *"hiring a data engineer takes 3–6 months and costs $120k–160k/yr"*; the retainer anchors against *"$120k+ saved annually."* Keep them distinct.

---

## 2. Cost factors, layer by layer

Each layer of the stack contributes to **build hours**, **recurring license**, **recurring infra**, or some combination. The table below is the master factor list.

| Layer | Build cost driver | Recurring cost driver | Build vs Buy decision |
|---|---|---|---|
| **Ingestion** | Hours per pipeline × eng rate | dlt = $0 license; Fivetran = MAR-based $ | dlt (eng-hour heavy, $0 run) vs Fivetran (fast build, $$$ run) |
| **Warehouse** | Setup hours | Compute + storage (usage-based) | BigQuery / Snowflake / ClickHouse; usually billed in **client's own cloud** |
| **Transformation** | Modeling hours × eng rate | dbt Core = $0; dbt Cloud = seats/jobs | dbt Core self-hosted vs dbt Cloud |
| **Orchestration** | Setup hours | Dagster self-host on K8s/GCP infra | Self-host (infra only) vs managed |
| **BI / Analytics** | Setup + per-dashboard hours | Metabase = $0 + VM; Hex/Looker/PowerBI = per-seat license | Open-source self-host vs SaaS license |
| **Monitoring / Alerting** | Setup hours | Tooling + on-call labor | Bundled into retainer |

### 2.1 Ingestion: the primary scaling unit

This is your most important pricing lever, because **price should scale per source**. Not all sources cost the same, tier them:

| Source tier | Examples | Build hours `«assumption»` |
|---|---|---|
| **T1, Simple** | Stripe, HubSpot, Google Ads (verified dlt source exists) | 4–8 hrs |
| **T2, Moderate** | Custom REST API, pagination, incremental loads | 8–16 hrs |
| **T3, Complex** | No connector, hard auth, large historical backfill, custom schema | 16–40 hrs |

**Ingestion cost (one-time)** = `Σ over sources ( hours_i × eng_rate )`

Your inputs map here exactly: *"total hours to build a single DLT pipeline × the hourly DLT rate."* The refinement is that "hours per pipeline" is **not a constant**. It's a function of source tier. Quote per-source, tiered.

> **dlt vs Fivetran trade-off (decide per engagement):**
> - **dlt** (open source): $0 recurring license, but build hours are higher and *you* own breakages. Best margin on the retainer, higher build labor.
> - **Fivetran**: minimal build hours, but recurring cost scales with **Monthly Active Rows (MAR)** and can balloon. Either pass through to the client's cloud bill or build a markup into the retainer, never absorb silently.

### 2.2 Transformation: dbt

Your input: *"if we use dbt in the cloud, include the basic package cost and the transformation time."*

- **Build**: `modeling_hours × eng_rate`. Modeling hours scale with **number of sources × business-logic complexity** (a clean staging model per source + a handful of marts). Rule of thumb `«assumption»`: ~5–8 modeling hours per source plus a fixed mart-building block.
- **Recurring**: dbt Cloud "basic/team" subscription (per developer seat + job runs) **or** $0 if you run dbt Core on the orchestration layer. Default to **dbt Core** unless the client wants the dbt Cloud IDE/scheduler.

### 2.3 Analytics / BI platform

Your input: *"Hex, Metabase or another tool, VM or cloud service, add licensing cost + setup hours."*

- **Build**: `BI_setup_hours + Σ(dashboard_hours)`. Each board-ready dashboard is a discrete unit, price per dashboard.
- **Recurring**:
  - **Metabase / self-host** → $0 license + a small VM (`«$30–80/mo»`, usually in the client's cloud).
  - **Hex / Looker / Power BI** → per-seat SaaS license. Pass through or mark up.
- This is also where **"Ask Vero anything"** (the NL query layer on the landing page) lives, if you ship that, it adds an LLM/API recurring cost (token usage) that must be metered and capped.

### 2.4 Warehouse, Orchestration & Infra: "in your own cloud"

The landing page promises *"on your own cloud account."* This is a **pricing advantage**, not just an architecture choice:

- Warehouse compute/storage, the Dagster K8s cluster, and BI VMs are billed **directly to the client's cloud account** → they don't sit on Vero's COGS, and they're transparent to the client.
- Vero still spends **setup hours** (warehouse provisioning, Dagster on K8s/GCP, networking, IAM), those are build hours.
- **Security/access onboarding** (credentials, IAM, a possible client security review) is real build time, budget for it; the landing page FAQ explicitly raises *"Is my data secure, and who owns it?"*

---

## 3. The cost model (formulas)

### 3.1 One-time build

```
Build_cost =  Discovery_&_onboarding_hours          × eng_rate
            + Σ_sources ( ingestion_hours_tier_i )    × eng_rate
            + modeling_hours (dbt)                    × eng_rate
            + warehouse_setup_hours                   × eng_rate
            + orchestration_setup_hours               × eng_rate
            + BI_setup_hours + Σ(dashboard_hours)      × eng_rate
            ─────────────────────────────────────────
            = base_labor_cost

Build_cost_loaded = base_labor_cost × (1 + PM_QA_overhead) × (1 + contingency)

Build_price       = Build_cost_loaded × (1 + build_margin)
```

- `PM_QA_overhead` `«15%»`, project management, code review, QA.
- `contingency` `«10–20%»`, **critical** because fixed scope means Vero absorbs overruns.
- `build_margin` `«100–150%»` (i.e. price = 2.0–2.5× loaded cost), or override with value-based pricing (§4).

### 3.2 Recurring monthly run cost (your COGS)

```
Run_cost_monthly =  ingestion_license      (Fivetran MAR, or $0 for dlt)
                  + dbt_subscription        (dbt Cloud, or $0 for dbt Core)
                  + BI_license              (Hex/Looker seats, or $0 Metabase)
                  + warehouse_compute_storage   ← usually CLIENT cloud (pass-through)
                  + orchestration_infra         ← usually CLIENT cloud (pass-through)
                  + monitoring_tooling
                  + maintenance_labor_hours × eng_rate

Retainer_price   =  Vero-borne_run_cost × (1 + run_margin)   [floor]
                   , set as a flat tiered fee, validated against this floor
```

- `maintenance_labor_hours` scales with **#sources + #models** (schema drift, pipeline breaks, new requests). Rule of thumb `«assumption»`: ~1–2 hrs/source/month.
- Pass-through cloud costs land on the **client's** bill, keep them out of your COGS but show them in the proposal so the client sees the true total.

---

## 4. Three ways to set the price (use all three as guardrails)

1. **Cost-plus (the floor)**. The model in §3. Never price below this.
2. **Value-based (the ceiling)**, anchor to the alternatives the landing page already names:
   - vs. hiring: $120k–160k/yr salary + 3–6 mo to hire.
   - "$120k+ saved annually."
   - A build fee of $15k–40k and a retainer of $2k–5k/mo is trivially justified against a $120k+ salary. **Value-based pricing leaves far more margin than cost-plus** here, lead with it.
3. **Competitive**, what comparable productized data-stack / fractional-data-team offers charge. Use to sanity-check, not to set.

**Recommendation:** Price the **build** value-based by tier (cost-plus is only the floor), and price the **retainer** as a flat tiered fee with the §3.2 cost as the floor.

---

## 5. Recommended packaging: productized tiers

Scale the tier by the things that actually drive cost: **# sources, # dashboards, # models, support SLA.**

| | **Starter** | **Growth** | **Scale** |
|---|---|---|---|
| Sources | up to 4 | up to 10 | 10+ |
| Dashboards | 3 | 6–8 | custom |
| Ingestion | dlt | dlt (Fivetran optional) | dlt + Fivetran |
| Transformation | dbt Core | dbt Core | dbt Core / Cloud |
| BI | Metabase | Metabase / Hex | Hex / Looker |
| Build timeline | 5 days | 5–7 days | scoped |
| **Build fee** `«»` | `~$12–18k` | `~$25–40k` | custom |
| **Retainer/mo** `«»` | `~$1.5–2.5k` | `~$3–5k` | custom |
| Support SLA | best-effort | business-hours | priority |

> Package tiers in [`pricing_calculator.html`](pricing_calculator.html) mirror this table. Pick a tier, then adjust any field for a scoped quote.

> Keep a clean **per-source** and **per-dashboard** add-on price so anything outside a tier is quotable without a re-scope.

---

## 6. Considerations checklist (don't ship a quote without these)

- [ ] **Build and retainer priced separately.**
- [ ] **Sources tiered** (T1/T2/T3), not flat-rated.
- [ ] **Build-vs-buy chosen per layer** (dlt vs Fivetran; dbt Core vs Cloud; Metabase vs Hex) and recurring cost of each path is reflected.
- [ ] **Cloud/infra costs identified as client-borne pass-through** and shown in the proposal.
- [ ] **Contingency buffer** added (fixed scope = Vero's risk).
- [ ] **Maintenance labor** scaled to #sources/#models, not guessed.
- [ ] **Security/onboarding hours** budgeted.
- [ ] **NL "Ask Vero" / LLM token cost** metered and capped if shipped.
- [ ] **Scope boundary defined**, what triggers a new SOW vs. what's covered by retainer.
- [ ] **Annual prepay discount** considered for retainer cash-flow.

---

## 7. Worked example: "Growth" tier (illustrative)

`«All rates and hours are placeholders.»` Assume blended **eng cost rate = $50/hr**, **build margin = 2.2×**.

**Build (one-time):**

| Item | Hours |
|---|---:|
| Discovery + onboarding/IAM | 12 |
| Ingestion, 8 sources (avg 10 hrs: mix of T1/T2) | 80 |
| dbt modeling | 60 |
| Warehouse (BigQuery) setup | 16 |
| Orchestration (Dagster on K8s/GCP) | 24 |
| BI (Metabase) + 6 dashboards (6 hrs ea.) | 52 |
| **Subtotal** | **244** |
| + 15% PM/QA | 281 |
| + 15% contingency | **323** |

- Loaded cost = 323 × $50 = **$16,150**
- Build price @ 2.2× = **~$35,500** → round to a tier price of **$35k**.
- (Sanity vs timeline: ~280–320 hrs across a 4–5 person team ≈ the promised 5–7 days.)

**Retainer (monthly):**

| Item | Cost |
|---|---:|
| dlt license | $0 |
| dbt Core | $0 |
| Metabase license | $0 (VM in client cloud) |
| Warehouse / Dagster infra | client cloud (pass-through) |
| Monitoring tooling | `«$50»` |
| Maintenance labor, ~12 hrs/mo × $50 | $600 |
| **Vero-borne COGS** | **~$650** |

- Retainer price floor = $650 × `«run_margin»`. Flat tier price **$3,500/mo** → healthy margin, still a fraction of a $120k+ DE salary.

**Contrast, same build on Fivetran:** ingestion build hours drop (~30 hrs saved) but recurring Fivetran MAR (`«$500–2,000+/mo»` depending on volume) must be passed through or marked into the retainer. Faster to ship, thinner long-run margin unless billed to the client.

---

## 8. Architecture ↔ cost map (for the cost-model spreadsheet / diagram)

Every box in the stack is a cost node. Build the calculator/diagram around these nodes:

```
                          ┌─────────── BUILD (one-time, hours) ───────────┐
 Sources (T1/T2/T3) ─dlt─▶ Warehouse ─dbt─▶ Models ──▶ BI ──▶ Dashboards
   │ Σ hrs×rate          │ setup hrs   │ modeling hrs │ setup+dash hrs
   │                     │             │              │
   └──────────── RUN (monthly) ────────┴──────────────┘
     Fivetran MAR │ WH compute/storage │ dbt Cloud │ BI seats │ maint. labor
        (license)    (client cloud)      (license)  (license)   (Vero COGS)
```

- **Build calculator inputs:** per-source tier & count, modeling hours, warehouse/orchestration/BI setup hours, dashboard count, eng rate, overhead %, contingency %, build margin.
- **Run calculator inputs:** chosen tool per layer (toggles license $), maintenance hrs/source, run margin.
- **Outputs:** build price, monthly retainer, client-borne cloud pass-through estimate, and gross margin on each.

---

### Open questions to lock before finalizing

1. Real blended **eng cost rate** and target **margins** (build vs run)?
2. Default ingestion: **dlt** everywhere, or Fivetran for some sources?
3. Is the **"Ask Vero" NL layer** in scope of the standard build (adds LLM token cost)?
4. Retainer billed **monthly or annual prepay**?
5. Do you want this turned into an **interactive cost calculator** (spreadsheet or web tool)? → See [`pricing_calculator.html`](pricing_calculator.html).
