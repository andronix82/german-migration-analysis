# German Migration Analysis 🇩🇪🌍

## ⚙️ Methodology

This section documents the full data pipeline used in the project, from raw data extraction to analytical feature creation.

---

## Step 1 — Raw Data Extraction

### Destatis (German Federal Statistical Office)

Primary publication source:

- Source: [Statistischer Bericht – Wanderungen 2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Wanderungen/Publikationen/Downloads-Wanderungen/statistischer-bericht-wanderungen-2010120247005.html?templateQueryString=wanderungen+altersgruppen)

This report provides aggregated migration statistics and serves as a reference for validating extracted data.

---

### GENESIS Database

Data for this project was primarily extracted from the GENESIS online database provided by the Federal Statistical Office.

- Source: [Genesis - Destatis](https://www-genesis.destatis.de)
- Time period: **2000 – 2024**

Tables used:

- **12711-0006** — Migration of German citizens by destination country  
- **12711-0008** — Migration of German citizens by age group  

Extraction filters used in GENESIS:

![filter_genesis_destatis_12711_0006_destination_country](images/filter_genesis_destatis_12711_0006_destination_country.png)

![filter_genisis_destatis_12711_0008_age_groups](images/filter_genisis_destatis_12711_0008_age_groups.png)

Raw exports were stored in: `/data/raw`

---

## Step 2 — Cleaning Raw Data

The exported GENESIS tables were transformed into a standardized long-format structure.

Cleaning steps included:

- Extracting migration totals from Excel sheet `csv-12711-02`
- Converting wide tables into **long time-series format**
- Standardizing column names to **English and lowercase**
- Removing metadata rows and unnecessary header levels
- Validating missing values and formatting consistency

Standard column structure: 

- year
- direction
- value
- dimension_type
- dimension_value


Cleaned datasets were saved as:

- `migration_totals_long_clean.csv`
- `migration_country_long_clean.csv`
- `migration_age_long_clean.csv`

Stored in: `/data/processed`

---

## Step 3 — Dataset Integration

The three cleaned datasets were combined into a unified **master dataset**.

Output file: `migration_master_dataset.csv`

Dataset structure:

- year
- dimension_type
- dimension_value
- direction
- value


Dimension types:

| dimension_type | description |
|----------------|-------------|
| global | total migration flows |
| country | migration by destination country |
| age | migration by age group |

The long-format structure allows flexible pivoting for different analytical perspectives.

---

## Step 4 — Feature Engineering

Additional analytical variables were derived from the master dataset.

### Net Migration

Net migration measures the difference between immigration and emigration.

Formula:

*Net Migration = Immigration − Emigration*

---

### Return Rate

Return rate measures how many emigrants return relative to those who leave.

Formula:

*Return Rate = Immigration ÷ Emigration*

Return rates were calculated on three aggregation levels:

- Global
- By country
- By age group

Generated datasets:

- `return_rate_global.csv`
- `return_rate_country.csv`
- `return_rate_age.csv`

---

## Step 5 — Exploratory Data Analysis (EDA)

Initial exploratory analysis focuses on identifying trends and structural changes in migration flows.

EDA includes:

- Time-series visualization of **immigration and emigration**
- Calculation and visualization of **net migration**
- Analysis of **return rate trends**
- Identification of **peak years and anomalies**

The exploratory analysis is performed in: `/notebooks/01_eda_migration.ipynb`

---

## Next Steps

Further analysis will extend the project in several directions:

1. **Country-Level Migration Analysis**
   - Identify major destination countries
   - Analyze migration concentration patterns

2. **Age Structure Analysis**
   - Detect demographic shifts in migration behaviour
   - Identify potential brain drain patterns

3. **Integration of Secondary Data**
   - Economic indicators
   - Labour market data
   - Cost of living indices

4. **Visualization and Dashboard Development**
   - Interactive Tableau dashboard
   - Migration trend storytelling