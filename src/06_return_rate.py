import pandas as pd

# --- Pfade ---
processed_path = "../data/processed/"
master_file = processed_path + "migration_master_dataset.csv"
country_file = processed_path + "migration_country_long.csv"
age_file = processed_path + "migration_age_long.csv"

# --- 1. Master-Dataset laden ---
df_master = pd.read_csv(master_file)

# Header auf Englisch und klein
df_master.rename(columns={
    'jahr': 'year',
    'total_value': 'value',
    'dimension_type_x': 'dimension_type',
    'dimension_value_x': 'dimension_value',
    'country_value': 'country',
    'dimension_type_y': 'dimension_type_y',
    'dimension_value_y': 'dimension_value_y',
    'age_value': 'age'
}, inplace=True)

# Filter: nur ab 2000
df_master = df_master[df_master['year'] >= 2000]

# --- 2. Return Rate Global ---
pivot_global = df_master.pivot_table(
    index='year',
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_global['return_rate_global'] = pivot_global['immigration'] / pivot_global['emigration']

pivot_global.to_csv(processed_path + "return_rate_global.csv", index=False)
print("✅ Global return rate calculated and saved.")

# --- 3. Return Rate nach Ländern ---
df_country = pd.read_csv(country_file)

# Header auf Englisch klein
df_country.rename(columns={
    'year': 'year',
    'dimension_type': 'dimension_type',
    'dimension_value': 'country',
    'direction': 'direction',
    'value': 'value'
}, inplace=True)

# Filter ab 2000
df_country = df_country[df_country['year'] >= 2000]

pivot_country = df_country.pivot_table(
    index=['year', 'country'],
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_country['return_rate_country'] = pivot_country['immigration'] / pivot_country['emigration']

pivot_country.to_csv(processed_path + "return_rate_country.csv", index=False)
print("✅ Return rate by country calculated and saved.")

# --- 4. Return Rate nach Altersgruppen ---
df_age = pd.read_csv(age_file)

# Header auf Englisch klein
df_age.rename(columns={
    'year': 'year',
    'dimension_type': 'dimension_type',
    'dimension_value': 'age',
    'direction': 'direction',
    'value': 'value'
}, inplace=True)

# Filter ab 2000
df_age = df_age[df_age['year'] >= 2000]

pivot_age = df_age.pivot_table(
    index=['year', 'age'],
    columns='direction',
    values='value',
    aggfunc='sum'
).reset_index()

pivot_age['return_rate_age'] = pivot_age['immigration'] / pivot_age['emigration']

pivot_age.to_csv(processed_path + "return_rate_age.csv", index=False)
print("✅ Return rate by age group calculated and saved.")
