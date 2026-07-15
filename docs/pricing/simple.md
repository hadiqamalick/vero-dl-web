# Vero Pricing: The Simple Version

*Datum Labs · 2026-06-30*

Two prices, always:
- **Build fee** (one-time) = the hours to set it up.
- **Retainer** (monthly) = tool costs + keeping it running.

---

## Questions to ask the team

**Rates**
1. Our cost per engineering hour? `$____`
2. How much do we mark it up? `____×`

**Build hours**
3. Hours to connect one **simple** source (Stripe, HubSpot)? `____`
4. Hours to connect one **hard** source (custom API, big backfill)? `____`
5. Hours to build the **dbt models**? `____`
6. Hours to set up the **warehouse + orchestration**? `____`
7. Hours per **dashboard**? `____`

**Monthly tool costs**
8. Ingestion, using free **dlt**, or paid **Fivetran**? If Fivetran, `$____/mo`
9. Transformation, free **dbt Core**, or **dbt Cloud**? If Cloud, `$____/mo`
10. BI, free **Metabase**, or paid **Hex/Looker**? If paid, `$____/mo`
11. Hours/month to **maintain** it (per source)? `____`

**Terms**
12. Who pays the **cloud bill**, client's own account? (usually yes)
13. Retainer billed **monthly or yearly**?

---

## How the price is built

```
Build fee  =  (all scoped build hours)  ×  bill rate / hr
Retainer   =  (maintenance hrs × bill rate)  +  tool costs ($/mo)
```

That's it. PM overhead, contingency, and retainer markup can be added back later if needed.

---

## Quick example

`$50/hr · 2× markup · 8 sources · 6 dashboards · all free tools`

- Build hours ≈ 250 → **~$25k build fee**
- Tools free, maintenance ~12 hrs/mo → **~$2–3.5k/mo retainer**
- Client pays their own cloud bill separately.

Anchor both against the alternative: *hiring a data engineer = $120k+/yr and 3–6 months.* You're a fraction of that.

> **Interactive calculator:** open [`pricing_calculator.html`](pricing_calculator.html) in a browser for live build + retainer estimates from scope inputs.

> Full breakdown (source tiers, formulas, the long questionnaire) lives in [model.md](model.md) if you need it.
