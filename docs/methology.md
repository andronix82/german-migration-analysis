# German Migration Analysis 🇩🇪🌍

## ⚙️ Methology

### Step 1: Export raw data

#### Destatis

- Source: [Statistischer Bericht - Wanderungen - 2024](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Wanderungen/Publikationen/Downloads-Wanderungen/statistischer-bericht-wanderungen-2010120247005.html?templateQueryString=wanderungen+altersgruppen)

#### GENESIS

- Source: ([genesis.destatis.de](https://www-genesis.destatis.de))

- Period: 2000 - 2024

- Table Codes: 12711-0006, 12711-0008

- Filters: ![filter_genesis_destatis_12711_0006_destination_country](images/filter_genesis_destatis_12711_0006_destination_country.png) ![filter_genisis_destatis_12711_0008_age_groups](images/filter_genisis_destatis_12711_0008_age_groups.png)

---

### Step 2: Cleaning raw data

- Extracted migration totals from Excel sheet `csv-12711-02` and transformed into long time-series format.

- 