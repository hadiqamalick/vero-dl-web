# Project Context Brief — for the marketing / case-study team

Purpose: give the marketing team the raw, verified context to write a case study — what the
project is, the problem it solves, the architecture, and specifically the work done on it. This
is source material, not copy. Every fact here is grounded in the codebase; judgment calls
(anonymization, outcome claims, quotes) are flagged as **[MARKETING TO SOURCE]** because they're
yours to decide, not mine to invent.

Format precedent: the existing Datum Labs case study for the AI-voice client is published
anonymized ("Vero") at https://www.datumlabs.io/vero/ai-voice-agent-saas. Same treatment likely
applies here.

---

## 1. Who the client is

- **Research arm** — a Swiss non-profit institute focused on healthy aging and preventive-care
  research. Owns the science: the definitions of who counts as a "healthy" vs "sick" population
  came from them, upstream of our work.
- **Product arm** — a health-tech company that turns that science into consumer tools powered by
  machine learning:
  - a **biological-age score** (compares your body's age to your calendar age),
  - **personalized lab reference ranges** (tailored to your profile, not population averages),
  - **per-body-system health snapshots**.
- **Datum Labs' role** — external data-engineering contractor. We build the data pipeline and
  warehouse that produce the training and reference datasets these ML models run on. Work is
  organized under the client's GitHub org and tracked as `DATA-###` tickets.

**[MARKETING TO SOURCE]** whether to name the client or anonymize (codename). If anonymizing,
pick a codename; a working placeholder used in an earlier draft was "Aeon."

## 2. The problem the project solves

The client's aging models are only as good as the data they train on. That data arrives as
public/clinical **cohort studies** — decades-long studies that track thousands of participants
across repeated exam visits. In raw form it's unusable for ML:

- **Fragmentation** — a single participant is spread across dozens of separate CSV files per
  study, keyed by an ID column whose name and casing vary file to file. Not queryable as one
  record.
- **Demographic confounding** — the naive way to build a "healthy vs sick" cohort yields two
  groups with very different age/gender mixes. A model trained on that learns *"older = sicker"*
  instead of the biomarker signal. The demographics have to be balanced out.
- **Cross-study inconsistency** — different studies use different biomarker names, units, and
  encodings; reference ranges come from different lab vendors in different units. No common
  vocabulary to merge on.

Result before this work: every model retrain started from loose files plus hand-built,
non-reproducible sampling decisions.

## 3. What was built (architecture, four layers)

1. **Ingestion** (`gcs-bq-pipelines` repo) — Python pipeline that lists a study's raw CSVs in the
   GCS staging bucket, recovers from mixed text encodings, drops duplicate/case-clashing columns,
   collapses each participant's many rows into one row keyed on subject ID, outer-joins every file
   in the study on that ID (tagging cross-file columns for traceability), and loads one clean
   subject-keyed table per study into BigQuery.
2. **Common vocabulary** (dbt `shared_ino` + intermediate layers) — maps every study's biomarkers
   to one canonical set of names and units, with explicit unit conversions (e.g. lb→kg) and
   per-biomarker directionality, so the same measurement from different studies means the same
   thing.
3. **Uniform-matching engine** (dbt `ageile_v2_dev` mart) — *the centerpiece*. Sorts participants
   into 5-year age bands within gender, then caps sampling per bucket by two limits at once: an
   **availability cap** (never exceed the smaller of the bucket's healthy/sick counts) and a
   **synthetic uniform cap** (a flat baseline so big buckets can't dominate). Final sample = the
   smaller of the two. Runs off a fixed seed, so the same cohort regenerates identically every
   time. Produces age/gender-matched healthy vs sick training sets where demographics are balanced
   by construction. Runs per-study and on a cross-study merged view.
4. **CI automation** (Cloud Build) — chains the dbt build + the ML model-training step into one
   workflow: build/test the data models, clone the model-training repo, run the population-
   generation script, export finished cohorts to BigQuery.

The same warehouse + vocabulary also feed the reference-range product and a newer biomarker line.

GCP project throughout: `gls-age-predictor`. Warehouse: BigQuery. Transformation: dbt. Ingestion &
model-training glue: Python. Orchestration: Cloud Build.

## 4. Tech stack

Core stack: **GCP services + dbt.**

- **BigQuery** — the data warehouse (EU region; GCP project `gls-age-predictor`).
- **dbt** — all transformation and modeling (~230 models, custom sampling macros).
- **Cloud Build** — CI/CD; runs the dbt build and the chained Python model-training step.
- **Cloud Run** — hosts the service that triggers dbt runs on request.
- **Artifact Registry** — Docker images and private Python packages consumed by the builds.

Supporting detail: ingestion and the ML-training glue are **Python** (pandas +
google-cloud-storage for GCS→BigQuery; Python 3.10 for the population step); the Cloud Run
service is **FastAPI**; builds run in **Docker** with secrets via **Secret Manager**; source
control is **GitHub** with a `DATA-###` PR-per-ticket workflow.

## 5. The work done on this project (~3–4 months, Oct 2025 – Feb 2026)

Roughly 69 commits on the dbt repo (+5.3k / −1.5k lines) plus the full ingestion repo. By stream:

- **Data ingestion — 5 studies.** Built the GCS→BigQuery merge pipeline and brought in **ARIC,
  CARDIA, JHS, MESA, and NHANES** — each a separate study with its own file layout, encodings,
  ID naming, and visit structure. This is the entry point of the whole data platform.
- **Uniform age/gender matching engine.** The headline dbt work. Built the two-cap matching
  (availability + synthetic-uniform baseline) and the deterministic sampling, across NHANES-only,
  UKBB-only, and a merged cross-study view. Tickets DATA-815, 898, 944/946/947.
- **Extended cohort definitions.** Added disease- and mortality-based "super sick" population
  variants on top of the baseline definitions (DATA-943/944/946/947).
- **Synthetic-dataset macros.** Reusable dbt macros generating the uniform baselines, single- and
  dual-source.
- **Reference-range work.** Refreshed and converted multi-vendor lab reference ranges (feeds the
  personalized-range product).
- **New biomarker line.** Config-driven bandwidth setting and a bounded-capping test for a newer
  biomarker panel (DATA-970, 988).
- **CARDIA source onboarding.** New staging layer, biomarker mapping to the canonical set, unit
  conversions (DATA-995).
- **CI integration.** Extended Cloud Build to run the dbt build and the Python model-training
  step as one automated workflow, pulling private deps and exporting to BigQuery (DATA-942,
  currently on a branch, not yet merged to develop).
- **Documentation.** Wrote the internal note explaining the uniform-matching pipeline
  (`docs/ageile_v2_uniform_age_gender_matching.md`).

## 6. Scale numbers (verified from the repo — safe to use)

- **5** cohort studies ingested (ARIC, CARDIA, JHS, MESA, NHANES).
- **3** data sources currently modeled in dbt (NHANES, UKBB, CARDIA). *Note the distinction:*
  the ingestion pipeline handled the 5 studies above; UKBB enters through a separate source.
- **230** dbt models total, of which **102** are in the biological-age matching mart.
- **372**-row canonical biomarker metadata catalog; per-product allowed-biomarker sets of
  **163** (biological age), **83** (reference ranges), **139** (new biomarker line).
- **6** reusable dbt macros; **19** seed files.
- Timeline: **~4 months**, Oct 2025 – Feb 2026.

## 7. What only marketing / the client can supply — **[MARKETING TO SOURCE]**

These would make the case study land but are NOT in the codebase — please source them:

- **Impact metrics** — did matched/reproducible data measurably improve the biological-age model
  (accuracy, calibration)? Did retrain cycles get faster? By how much?
- **Total participant count** across the five studies (derivable from BigQuery with warehouse
  access; not computed here).
- **Client quote or before/after anecdote** — e.g. what the data-science team used to do manually.
- **Anonymization decision** and, if anonymized, the codename.
- **What's public** — some of these studies (ARIC, CARDIA, JHS, MESA, NHANES) and the client's
  products are named/public; confirm what can appear in published copy.

## 8. Pointers

- dbt / warehouse repo: `dbt-elt-bq` (this repo). Matching engine: `models/marts/ageile_v2_dev/`.
  Shared vocabulary: `models/shared_ino/`. Macros: `macros/get_uniform_synthetic_dataset*.sql`.
- Matching pipeline explainer: `docs/ageile_v2_uniform_age_gender_matching.md`.
- Ingestion repo: `gcs-bq-pipelines` (`gcs_csv_pipeline.py`, plus `SCRIPT_DOCS.md`).
- CI: `cloudbuild*.yml` in this repo; the dbt+ML chaining is on branch
  `DATA-942-integrate-python-scripts-in-dbt-workflow`.
- Format precedent: https://www.datumlabs.io/vero/ai-voice-agent-saas
