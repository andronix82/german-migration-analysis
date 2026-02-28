import pandas as pd
from pathlib import Path

# --- Pfad ---
processed_path = "../data/processed/"

# Dateien
totals_file = Path(processed_path + "migration_totals_long.csv")
country_file = Path(processed_path + "migration_country_long.csv")
age_file = Path(processed_path + "migration_age_long.csv")

# --- 1. Load raw CSVs ---
df_totals = pd.read_csv(totals_file)
df_country = pd.read_csv(country_file)
df_age = pd.read_csv(age_file)

# --- 2. Standardize column names ---
df_totals.columns = ['year', 'direction', 'value']
df_country.columns = ['year', 'dimension_type', 'dimension_value', 'direction', 'value']
df_age.columns = ['year', 'dimension_type', 'dimension_value', 'direction', 'value']

# --- 3. Check for missing values ---
print("Missing in totals:", df_totals.isna().sum())
print("Missing in country:", df_country.isna().sum())
print("Missing in age:", df_age.isna().sum())

# --- 4. Save cleaned CSVs ---
df_totals.to_csv(processed_path + "migration_totals_long_clean.csv", index=False)
df_country.to_csv(processed_path + "migration_country_long_clean.csv", index=False)
df_age.to_csv(processed_path + "migration_age_long_clean.csv", index=False)

print("Validation and cleaning done. Clean CSVs saved.")
