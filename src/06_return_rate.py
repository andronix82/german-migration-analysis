import pandas as pd

# --- Pfade ---
processed_path = "../data/processed/"
master_file = processed_path + "migration_master_dataset.csv"

# --- 1. Load master dataset ---
master_df = pd.read_csv(master_file)

# --- 2. Global Return Rate ---
pivot_global = master_df[master_df['dimension_type'] == 'global'].pivot_table(
    index='year',
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_global['return_rate_global'] = pivot_global['immigration'] / pivot_global['emigration']

pivot_global.to_csv(processed_path + "return_rate_global.csv", index=False)
print("Global Return Rate saved.")

# --- 3. Return Rate by country ---
pivot_country = master_df[master_df['dimension_type'] == 'country'].pivot_table(
    index=['year', 'dimension_value'],
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_country['return_rate_country'] = pivot_country['immigration'] / pivot_country['emigration']

pivot_country.to_csv(processed_path + "return_rate_country.csv", index=False)
print("Return Rate by country saved.")

# --- 4. Return Rate by age ---
pivot_age = master_df[master_df['dimension_type'] == 'age'].pivot_table(
    index=['year', 'dimension_value'],
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_age['return_rate_age'] = pivot_age['immigration'] / pivot_age['emigration']

pivot_age.to_csv(processed_path + "return_rate_age.csv", index=False)
print("Return Rate by age saved.")
