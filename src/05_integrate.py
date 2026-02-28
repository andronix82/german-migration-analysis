import pandas as pd

# --- Pfade ---
processed_path = "../data/processed/"

totals_file = processed_path + "migration_totals_long_clean.csv"
country_file = processed_path + "migration_country_long_clean.csv"
age_file = processed_path + "migration_age_long_clean.csv"

# --- 1. Load cleaned datasets ---
df_totals = pd.read_csv(totals_file)
df_country = pd.read_csv(country_file)
df_age = pd.read_csv(age_file)

# --- 2. Add identifiers for merging ---
# dimension_type/value for totals is "global"
df_totals['dimension_type'] = 'global'
df_totals['dimension_value'] = 'global'

# --- 3. Concatenate all into one long-form master ---
master_df = pd.concat([df_totals, df_country, df_age], ignore_index=True)

# --- 4. Standardize column order ---
master_df = master_df[['year', 'dimension_type', 'dimension_value', 'direction', 'value']]

# --- 5. Ensure all lowercase ---
master_df.columns = [c.lower() for c in master_df.columns]

# --- 6. Save master dataset ---
master_df.to_csv(processed_path + "migration_master_dataset.csv", index=False)
print("Master dataset created and saved.")
