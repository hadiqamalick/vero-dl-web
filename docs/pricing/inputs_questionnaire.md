# Vero Pricing — Team Input Questionnaire

*Datum Labs · Fill this in to populate the [pricing model](model.md) · Last updated 2026-06-30*

Ask your team these questions. Every answer is an **input** the cost model needs. Fill in the blanks — once these are locked, the build fee and retainer fall out of the formulas automatically.

> Legend: **[one-time]** feeds the build fee · **[monthly]** feeds the retainer · **[%]** feeds margin/overhead.

---

## A. Rates & margins (ask once, reuse for every quote)

1. What is our **blended engineering cost rate** (loaded, internal) per hour? → `$____ /hr`
2. What hourly **bill rate** do we quote externally, if any? → `$____ /hr`
3. Target **build margin** (multiple on loaded cost)? → `____×` (e.g. 2.0–2.5×)
4. Target **retainer margin** (multiple on monthly COGS)? → `____×`
5. **PM / QA / code-review overhead** as % of build labor? → `____%`
6. **Contingency buffer** for fixed-scope overruns? → `____%`

---

## B. Ingestion (per source)

7. For a **simple (T1)** source (verified dlt connector — Stripe, HubSpot, Google Ads), how many hours to build one pipeline? **[one-time]** → `____ hrs`
8. For a **moderate (T2)** source (custom REST API, pagination, incremental)? **[one-time]** → `____ hrs`
9. For a **complex (T3)** source (no connector, hard auth, big historical backfill)? **[one-time]** → `____ hrs`
10. Default ingestion tool — **dlt everywhere**, or **Fivetran** for some? → `________`
11. If Fivetran: what's the **monthly cost** at our typical volume (MAR tier)? **[monthly]** → `$____ /mo` — and do we **pass it through** to the client or absorb it? → `________`
12. Average **maintenance hours per source per month** (schema drift, breakages)? **[monthly]** → `____ hrs/source`

---

## C. Transformation (dbt)

13. **dbt Core (self-hosted)** or **dbt Cloud** by default? → `________`
14. If dbt Cloud: **monthly subscription** cost (basic/team tier, per seat)? **[monthly]** → `$____ /mo`
15. **Modeling hours per source** (staging model + contribution to marts)? **[one-time]** → `____ hrs/source`
16. Fixed **mart-building block** hours regardless of source count? **[one-time]** → `____ hrs`

---

## D. Warehouse

17. Default warehouse — **BigQuery / Snowflake / ClickHouse**? → `________`
18. **Setup hours** (provisioning, datasets, IAM, networking)? **[one-time]** → `____ hrs`
19. Who pays warehouse **compute + storage** — client's own cloud (pass-through) or us? → `________`
20. Rough **monthly compute/storage** estimate for a typical client (to show in proposal)? → `$____ /mo`

---

## E. Orchestration

21. Default — **Dagster self-hosted on K8s/GCP** or managed? → `________`
22. **Setup hours**? **[one-time]** → `____ hrs`
23. Monthly **infra cost** for the orchestration layer (client cloud / ours)? **[monthly]** → `$____ /mo`

---

## F. Analytics / BI

24. Default BI tool — **Metabase / Hex / Looker / Power BI**? → `________`
25. **License cost** of that tool (per seat or flat, monthly)? **[monthly]** → `$____ /mo`
26. If self-hosted (Metabase): **VM cost** per month? **[monthly]** → `$____ /mo`
27. **BI setup hours** (install, connect, auth, base config)? **[one-time]** → `____ hrs`
28. **Hours per board-ready dashboard**? **[one-time]** → `____ hrs/dashboard`

---

## G. Onboarding, monitoring & "Ask Vero"

29. **Discovery + onboarding/IAM/security-review** hours per engagement? **[one-time]** → `____ hrs`
30. **Monitoring/alerting** setup hours? **[one-time]** → `____ hrs`
31. Monthly **monitoring tooling** cost? **[monthly]** → `$____ /mo`
32. Are we shipping the **"Ask Vero" NL query layer** by default? → `Yes / No`
33. If yes: estimated **LLM/API token cost** per month, and is it **capped**? **[monthly]** → `$____ /mo`, cap: `________`

---

## H. Packaging & commercial terms

34. What defines our **standard tiers** — max sources / dashboards / models per tier? → `________`
35. **Per-source add-on** price (outside a tier)? → `$____`
36. **Per-dashboard add-on** price? → `$____`
37. Retainer billed **monthly or annual prepay**? Any **prepay discount**? → `________`
38. What's **in** the retainer vs. what triggers a **new SOW**? → `________`
39. **Payment terms** for the build fee (upfront / 50-50 / on milestones)? → `________`

---

### Quick-fill summary (paste the key numbers here once gathered)

| Input | Value |
|---|---|
| Eng cost rate | `$____ /hr` |
| Build margin | `____×` |
| Retainer margin | `____×` |
| Overhead % / Contingency % | `____% / ____%` |
| Ingestion hrs T1 / T2 / T3 | `__ / __ / __` |
| Modeling hrs per source | `____` |
| Warehouse setup hrs | `____` |
| Orchestration setup hrs | `____` |
| BI setup hrs / per dashboard | `__ / __` |
| Maintenance hrs / source / mo | `____` |
| Default tools (ingest / transform / WH / BI) | `____ / ____ / ____ / ____` |

Once this table is filled, the build fee and retainer drop straight out of §3 of the pricing model.
