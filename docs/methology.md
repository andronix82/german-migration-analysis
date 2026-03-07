# German Migration Analysis 🇩🇪🌍

## ⚙️ Methodology

This section documents the full data pipeline used in the project, from raw data extraction to analytical feature creation.

---

## Step 1 — Raw Data Extraction

### Destatis (German Federal Statistical Office)

Primary publication source:

- Source: [Statistischer Bericht – Wanderungen 2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Wanderungen/Publikationen/Downloads-Wanderungen/statistischer-bericht-wanderungen-2010120247005.html?templateQueryString=wanderungen+altersgruppen)

---

### GENESIS Database

Data for this project was primarily extracted from the GENESIS online database provided by the Federal Statistical Office.

- Source: [Genesis - Destatis](https://www-genesis.destatis.de)
- Time period: **2000 – 2024**

Tables used:

- **12711-0006** — Migration of German citizens by destination country  
- **12711-0008** — Migration of German citizens by age group  

Raw exports were stored in: `/data/raw`

---

## Step 2 — Cleaning Raw Data

Cleaning steps included:

- Extracting migration totals from Excel sheet `csv-12711-02`
- Converting wide tables into **long time-series format**
- Standardizing column names to **English and lowercase**
- Removing metadata rows and unnecessary header levels
- Validating missing values and formatting consistency

Cleaned datasets saved in: `/data/processed`

---

## Step 3 — Dataset Integration

Combined datasets into a unified **master dataset**:

- `migration_master_dataset.csv`
- Structure: year, dimension_type, dimension_value, direction, value
- Dimension types: global, country, age

---

## Step 4 — Feature Engineering

### Net Migration

*Net Migration = Immigration − Emigration*

### Return Rate

*Return Rate = Immigration ÷ Emigration*

Calculated at:

- Global
- By country
- By age group

Generated datasets:

- `return_rate_global.csv`
- `return_rate_country.csv`
- `return_rate_age.csv`

---

## Step 5 — Exploratory Data Analysis (EDA)

EDA includes:

- Time-series visualization of **immigration and emigration**
- Calculation and visualization of **net migration**
- Analysis of **return rate trends**
- Identification of **peak years and anomalies**

---

## Step 6 — Country-Level Analysis (Block 2)

Country-level analysis added after initial EDA:

- Top destination countries: Switzerland, United States, Austria  
- Return rates highlight temporary vs permanent migration:
  - Highest return rate: Kazakhstan  
  - Lowest return rate: Switzerland  
- Migration flow volatility observed for key countries, especially Switzerland

This step allows deeper insights into **destination-specific migration trends** and **country-level volatility**, which is critical for workforce and talent planning.

---

### Methodological Break in 2016

Statistical recording of emigration changed in 2016, including systematic inclusion of unknown destinations and register cleanups. This must be considered when interpreting trends.

---

## Next Steps

1. Age structure analysis
2. Integration of secondary socio-economic data
3. Dashboard creation
4. Migration Network analysis (Block 3)