# Vero HoE script: Act 1 (market intro)

**Presenters:** Hadiqa & Nidal  
**Audience:** Head of Engineering (internal product intro)  
**Deck:** [`vero_v2.html`](./vero_v2.html)  
**Scope:** Slides 1–9 only (through How we sell it; before the dark Technical / How it works break)  
**Inspo:** [`upwork/script/datumlabs_w_vero.md`](./upwork/script/datumlabs_w_vero.md), Fix beats in [`upwork/script/datumlabs.md`](./upwork/script/datumlabs.md)  
**Target length:** ~4–5 minutes spoken

---

## Voice rules

- Do **not** read on-screen definition or sub lines word for word when they are already visible.
- On **The Fix**, Space advances steps 1→2→3, then Space for the next slide.
- Do **not** name GovPlus on camera. Use *a service-based SaaS client* or *one recent engagement*.
- Ownership and deep stack detail stay light. Architecture and vero-init come after this act.
- Voice is **we / Vero**, not the Upwork first-person freelancer track.

---

## Slide map (Act 1)

| # | Slide | Job |
|---|--------|-----|
| 1 | Title | Name Vero and the offer |
| 2 | Why teams come | Four pains |
| 3 | The Fix | 3-step journey (Space × 3) |
| 4 | What we build | Five forms, including NL answers |
| 5 | Delivery | Kickoff → retainer |
| 6 | Speed | Days, not months |
| 7 | ICPs | Who buys + sample clients |
| 8 | Proof | 9 to 1 systems · 3 dashboards · under 6 weeks |
| 9 | How we sell it | Channels · Land / Expand / Grow |

**Stop here.** Hand off on the dark Technical divider (slide 10).

---

## Slide 1: Title

### On screen

VERO · Data infrastructure for growing teams · Live in days, not months · definition · Hadiqa & Nidal

### Spoken (~15s)

> Hi, we're Hadiqa and Nidal. Today we're walking through **Vero**, the data foundation Datumlabs is taking to market.
>
> Short version: we build the warehouse, the pipelines, and the dashboards, so the whole team works from **one number everyone trusts**. Live in days, not months.

---

## Slide 2: Why teams come

### On screen

Four pain cards: different numbers · manual exports · no data team · AI and dashboards blocked

### Spoken (~25s)

> Most teams at this stage are not missing data. They are missing a foundation.
>
> Same four complaints every conversation: every team reports a **different number**; they live in **manual exports** nobody trusts; there is **no data team** free to build the stack; and **AI and dashboards stay blocked** because the data underneath is not ready. Every question still waits on a person.

---

## Slide 3: The Fix (3 Spaces)

### On screen

Interactive journey. Space advances 1 → 2 → 3, then Space to leave the slide.

### Spoken

> **Space 1:** This is what that looks like. Product, marketing, ecommerce, finance, CRM, support. Tools that don't talk to each other. Manual exports.
>
> **Space 2:** Vero pulls everything into **one source of truth**, one warehouse the whole team can trust.
>
> **Space 3:** From that foundation you get reporting, alerts, and AI, all on the **same trusted data**. One data foundation, not six versions of the truth.
>
> *(Space → next slide)*

---

## Slide 4: What we build

### On screen

Five forms: warehouse · models · live reporting · natural language answers · orchestration & deployment

### Spoken (~30s)

> What we actually deliver is the same five forms every time.
>
> A **unified warehouse**. **Clean models** so revenue and retention mean one thing. **Live reporting** in tools the team already uses. **Natural language answers**: ask in plain English, get a quality answer grounded in *their* definitions, not a generic LLM guess. And **orchestration and deployment** so it runs on schedule in **their** cloud.
>
> Same playbook every engagement. That is why it is repeatable.

---

## Slide 5: Delivery

### On screen

Kickoff → map sources → build foundation → reporting live → stay on retainer

### Spoken (~15s)

> Delivery is simple. Kickoff, map sources, build the foundation, reporting live, then we stay on retainer as their data team.
>
> We do not sell a month of discovery workshops. We already know the path.

---

## Slide 6: Speed

### On screen

Building in-house 4–6 weeks → With Vero 3–5 days · not a hire

### Spoken (~15s)

> Building this in-house is hire, ramp, build: weeks.
>
> With Vero we see the same problems across businesses, so we ship in **days**: sources connected, pipelines live, dashboards shipped. Fully owned by the customer. Vero is not a hire. It is a specialist team with a playbook.

---

## Slide 7: ICPs

### On screen

Founder/CEO · Ops/RevOps · CTO · Growth/Marketing · sample clients

### Spoken (~20s)

> Who we sell to: Seed and Series A SaaS with CRM, billing, product or ads data, and **no platform team**.
>
> Founders who just raised and need board metrics yesterday. Ops and RevOps stuck in request queues. CTOs who know they need dbt and Dagster but product owns the roadmap. Growth leads who cannot see CAC and pipeline in one place.
>
> That pattern is already in the room with clients like Volter, Filed, Synthflow, and others on the site.

---

## Slide 8: Proof

### On screen

9 to 1 systems · 3 dashboards · &lt; 6 weeks · [datumlabs.io/vero#Case-Studies](https://www.datumlabs.io/vero#Case-Studies)

### Spoken (~20s)

> Recent pattern from a **service-based SaaS** engagement: **nine systems into one** BigQuery warehouse. **Three dashboards** for Ops, Sales, and Product, with AI querying on top. Fixed scope, live in **under six weeks**, on their own GCP.
>
> More write-ups are on the site under case studies if you want depth later.

---

## Slide 9: How we sell it

### On screen

Upwork · LinkedIn · datumlabs.io/vero · case studies · Land / Expand / Grow

### Spoken (~20s)

> Go to market is simple. Find them on Upwork, LinkedIn, the site, and case study outreach. Quote a real scope. Land fast. Expand monthly.
>
> **Land** is fixed-fee setup. **Expand** is retainer: new sources, marts, oncall. **Grow** is apps and workflows on the same stack, still in their cloud.
>
> Build fee plus retainer. Client pays their own cloud bill.

---

## Hand-off (before dark Technical slide)

> That is the market story: problem, fix, what we build, how fast, who buys, proof, and how we sell.
>
> Next we go technical: architecture, then vero-init with the engineering team.

*(Space onto dark How it works divider; hand to technical.)*

---

## Full continuous take (Act 1)

**SLIDE 01** Hi, we're Hadiqa and Nidal. Thanks for making time. We're going to walk you through Vero, what we're offering in the market, and why we think it fits. In short, we connect a team's tools, build the warehouse and the pipelines, get dashboards live, and get everyone working from numbers they can actually trust. And we do that in days, not months.

**SLIDE 02** Here's what we keep hearing. Teams aren't short on data. They're short on a foundation. Marketing, finance, and product each have their own number. People spend half the week pulling CSVs and still don't trust the result. There's no one free to build a real stack. And when they want AI or better dashboards, they're stuck, because you can't put that on messy data. Every question still goes through someone who has to pull the export.

**SLIDE 03** Space 1: So this is the picture. Product, marketing, ecommerce, finance, CRM, support, all sitting in different tools that don't talk to each other. Space 2: What we do is bring that into one place. One warehouse. One source of truth the whole team can use. Space 3: And once that's in place, reporting, alerts, even AI, they all run off the same trusted data. Not six different versions of the truth.

**SLIDE 04** On every engagement we ship the same five things. The warehouse. Clean models, so "revenue" means one thing for everyone. Live reporting in tools they already open every day. Natural language answers, so people can ask a normal question in English and get a solid answer based on *their* definitions, not a random LLM guess. And orchestration in their own cloud, so it keeps running without someone babysitting exports. Same playbook each time, and that's why we can move fast.

**SLIDE 05** How delivery actually works is pretty straightforward. We kick off, we map the sources, we build the foundation, reporting goes live, and then we stay on as their data team on retainer. We're not selling a long discovery phase. We've run this path before.

**SLIDE 06** If they try to build this in-house, you're looking at weeks: hire, ramp, then build. We've seen the same problems across a lot of businesses, so with Vero we can usually get sources connected and dashboards live in a few days. And it's their cloud, their stack. We're not a hire. We're a team that already knows how to ship this.

**SLIDE 07** Who this is for: Seed and Series A SaaS teams. Usually CRM plus billing plus product or ads, and no platform team to build the data layer themselves. Think founders who just raised and the board wants metrics next week. Ops people who keep filing requests for pulls. CTOs who know they need dbt and Dagster, but engineers are on product. Growth people who can't see CAC and pipeline in one view. That's the same profile as clients we've already worked with.

**SLIDE 08** One recent example, a service-based SaaS. Nine systems down to one BigQuery warehouse. Three dashboards for Ops, Sales, and Product, with AI querying. Fixed scope, deployed on their own GCP in under six weeks. If you want more of those stories, they're on the site under case studies.

**SLIDE 09** Go to market is simple. Find them on Upwork, LinkedIn, the site, and case study outreach. Quote a real scope. Land fast. Expand monthly. Land is fixed-fee setup. Expand is retainer: new sources, marts, oncall. Grow is apps and workflows on the same stack, still in their cloud. Build fee plus retainer. Client pays their own cloud bill. That's the market side. Next we'll go into architecture and vero-init with engineering.
