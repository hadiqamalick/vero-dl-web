# Vero technical deep dive script (Act 2)

**Presenters:** Hadiqa & Nidal  
**Deck:** [`vero_v2_technical.html`](./vero_v2_technical.html)  
**Scope:** Internal working system in place today. No Q3 roadmap language.  
**Target length:** ~8–10 minutes spoken

---

## Voice rules

- Do not read every on-screen bullet. Point and expand.
- On **Architecture**, Space advances stack layers 1→6, then Space for the next slide.
- Say **DRD** (Data Requirement Document), not PRD, for the audit output.
- Say **SRC / TFM / MART** for dbt layers.
- Plugins are **not shipped**. Skills first; plugins after maturity, in a **separate repo**.
- No Pulse. No em dash in spoken or written copy.

---

## Slide map

| # | Slide | Job |
|---|--------|-----|
| 1 | Title | Name Vero |
| 2 | How it works | Agenda chips |
| 3 | Architecture | Interactive data stack |
| 4 | Vero on Kubernetes | Coded infra diagram (Admin / Pipelines / Warehouse) |
| 5 | Client onboarding | DRD + access → secrets |
| 6 | vero-ingestion | Pipeline build layer 1 |
| 7 | vero-transform | SRC / TFM / MART |
| 8 | Testing | Checklist + backfill while analytics |
| 9 | Deployment | Cloud vs open source |
| 10 | Test results | What we did / learned |
| 11 | Plugins in detail | Separate repo, after maturity |
| 12 | Close | Hold |

---

## Slide 1: Title

> Hi, we're Hadiqa and Nidal. This is the technical half of Vero: how we actually onboard, build, test, and deploy.

---

## Slide 2: How it works

> Order today: architecture, onboarding, pipeline build, testing, deploy, what testing taught us, then plugins as the next packaging step.

---

## Slide 3: Architecture (Space × 6)

> **Space 1:** Everything starts from sources the business already runs.
>
> **Space 2:** Ingestion pulls that data automatically.
>
> **Space 3:** One warehouse.
>
> **Space 4:** dbt for transform.
>
> **Space 5:** Reporting the team already uses.
>
> **Space 6:** Dagster and Kubernetes keep it running in their cloud.

---

## Slide 4: Vero on Kubernetes

> Same stack, deployed on the client cluster: AWS EKS, Hetzner, or BigQuery as the warehouse destination.
>
> Outside: GitHub, Actions, volumes, external DB.
>
> Inside k8s: Administration on the left (ArgoCD, Keycloak, Vault, Grafana, Prometheus). Pipelines in the middle: Dagster batch with dlt, dbt, and workflows. That is the Vero path. Realtime jobs sit in the same cluster when needed. Warehouse on the right: ClickHouse and Kafka.
>
> Nodes underneath. Terraform owns infra. GitOps owns the apps.

---

## Slide 5: Client onboarding

> Onboarding comes before we write pipelines.
>
> We start from work we already know how to run. We fill the data audit questionnaire and turn the answer log into a **DRD**.
>
> Then we request access in an organized way: owner, scope, due date per source. Credentials go into **env and secrets**, including Vault. Build starts only when that is clean.

---

## Slide 6: vero-ingestion

> First pipeline layer is **vero-ingestion**.
>
> We pull from a reusable catalog, load with dlt into raw tables, and hold a quality bar: incremental, merge on primary key, real backfill path, no secrets in code.
>
> Flow is init, verify source, ingest, raw tables. One client is one Dagster code location.

---

## Slide 7: vero-transform

> Second layer is **vero-transform**: dbt in three layers.
>
> **SRC** is source, close to raw. It can look repetitive as sources grow. That is fine.
>
> **TFM** is transform and shared business logic.
>
> **MART** is final metrics from the DRD.
>
> Schema design follows those three layers. Raw stays separate per source.

---

## Slide 8: Testing

> A source is not done until verify, load, SRC build, tests, Dagster materialize, and an idempotent re-run all clear.
>
> For load strategy: land a recent window so analytics can start, then backfill history in chunks beside incremental. Incremental must not block.

---

## Slide 9: Deployment

> Two deploy paths, same app layer.
>
> **Dagster Cloud:** project already scaffolds Cloud packaging.
>
> **Open source on k8s:** the diagram you saw. Terraform for infra, Dagster OSS, Vault, GitOps. That path is still maturing on Helm and full roll.
>
> Client pays their cloud bill either way.

---

## Slide 10: Test results

> Testing on real client sources taught us concrete things.
>
> We run the full path, not empty demos. Hardcoded day windows broke the load story. We moved to recent-window first, chunked backfill, and SRC / TFM / MART as the modeling rule.
>
> Coverage still grows source by source. Skills are mature when the checklist stays green without hand-tuning.

---

## Slide 11: Plugins in detail

> Plugins come after skills prove out.
>
> Same stages: init, vero-ingestion, vero-transform, orchestration, warehousing, dashboarding, infra.
>
> A plugin is a guided stage with a quality gate. Matured stages live in a **separate plugins repo**. Delivery repo stays skills and client projects.
>
> Not shipped yet. We earn them by clearing testing on the skills we run today.

---

## Slide 12: Close

> Onboard with a DRD and clean secrets. Build with ingestion and SRC / TFM / MART. Prove it in testing. Deploy on Cloud or open source. Package plugins only after the skills hold.
