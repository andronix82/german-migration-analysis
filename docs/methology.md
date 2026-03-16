# German Migration Analysis 🇩🇪🌍

## ⚙️ Methodology

This section documents the full data pipeline used in the project, from raw data extraction to analytical feature creation.

---

## Step 1 — Raw Data Extraction

Data source:

Destatis GENESIS Database  
https://www-genesis.destatis.de

Tables used:

- **12711-0006** — Migration of German citizens by destination country
- **12711-0008** — Migration of German citizens by age group

Time coverage:

2000–2024

Raw exports stored in:

`/data/raw`

---

## Step 2 — Data Cleaning

Cleaning steps:

- Convert GENESIS tables into long format
- Remove metadata rows
- Standardize column names
- Validate missing values
- Translate categories to English

Clean datasets stored in:

`/data/processed`

Generated files:

- migration_totals_long_clean.csv
- migration_country_long_clean.csv
- migration_age_long_clean.csv

---

## Step 3 — Dataset Integration

All datasets were merged into a **master dataset**.

Output file:

`migration_master_dataset.csv`

Structure:

year  
dimension_type  
dimension_value  
direction  
value

---

## Step 4 — Feature Engineering

Additional analytical metrics were created.

### Net Migration

`Net Migration = Immigration − Emigration`


### Return Rate

`Return Rate = Immigration ÷ Emigration`


Return rates calculated for:

- global
- country
- age group

Output datasets:

- return_rate_global.csv
- return_rate_country.csv
- return_rate_age.csv

---

## Step 5 — Exploratory Data Analysis

EDA focuses on identifying trends and structural changes.

Analyses include:

- immigration trends
- emigration trends
- net migration
- return rate development

Notebook:

`/notebooks/01_eda_migration.ipynb`

---

## Step 6 — Country-Level Migration Analysis

This step analyses migration patterns by destination country.

Metrics analyzed:

- total migration flows
- return rate by country
- volatility of migration flows
- ranking of destination countries

Main insights:

- Switzerland is the most important destination for German emigrants.
- Return rates differ strongly between countries.
- Some destinations show high volatility in migration flows.

---

## Step 7 — Migration Network Analysis

Migration flows were modeled as a **directed network**.

Nodes represent countries, edges represent migration flows.

Edge structure:

- Origin → Destination
- Weight = Migrants


Two datasets were created:

- `migration_network_flows.csv`
- `migration_network_flows_wo_ungeklaert.csv`

The second dataset excludes the category **"Unknown / Unspecified destination"** to improve interpretability.

Flows were analysed in both directions:

- Germany → Destination country
- Origin country → Germany

This allows identification of **major migration corridors**.

Visualizations created:

- Migration network graph
- Top migration flows chart

Notebook:

`/notebooks/03_migration_network.ipynb`

---

## Methodological Break in 2016

In 2016, statistical recording of emigration changed.

Key changes:

- inclusion of unknown destinations
- register cleanups of outdated migration records

This caused a spike in emigration numbers.

Therefore, **2016 migration data is not fully comparable with previous years**.

---

## Next Steps

Future extensions:

- Age structure analysis
- Integration of socio-economic indicators
- Tableau dashboard development
- Advanced migration modelling