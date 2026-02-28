import pandas as pd
import re
from pathlib import Path

RAW = Path("../data/raw/genesis/migration_country_genesis_raw.csv")
OUT = Path("../data/processed/migration_country_long.csv")

def clean_number(value):
    if pd.isna(value):
        return None
    s = str(value).strip()
    s = re.sub(r"[^\d\-]", "", s)
    if not s or s == "-":
        return None
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    return None

# Feste Spaltenzahl + names
colnames = list(range(7))
df_raw = pd.read_csv(
    RAW,
    sep=";",
    header=None,
    names=colnames,
    engine="python",
    dtype=str
)

records = []
current_year = None

meta_keywords = [
    "Wanderungen", "Deutschland", "Deutsche", "Zuzüge", "Anzahl",
    "Wanderungsstatistik", "Tabelle:", "©", "Stand:"
]

for _, row in df_raw.iterrows():
    first = row.iloc[0]
    if pd.isna(first):
        continue

    first_str = str(first).strip().lstrip("\ufeff")  # falls BOM vorhanden

    # Jahr erkennen (als String)
    if re.fullmatch(r"\d{4}", first_str):
        y = int(first_str)
        if 1900 < y < 2100:
            current_year = y
        continue

    if current_year is None:
        continue

    if any(k in first_str for k in meta_keywords):
        continue

    country = first_str

    immigration = clean_number(row.iloc[1])  # Zuzüge
    emigration  = clean_number(row.iloc[3])  # Fortzüge

    if immigration is not None:
        records.append({
            "year": current_year,
            "dimension_type": "country",
            "dimension_value": country,
            "direction": "immigration",
            "value": immigration
        })

    if emigration is not None:
        records.append({
            "year": current_year,
            "dimension_type": "country",
            "dimension_value": country,
            "direction": "emigration",
            "value": emigration
        })

df_clean = pd.DataFrame(records).sort_values(["year", "dimension_value", "direction"])

OUT.parent.mkdir(parents=True, exist_ok=True)
df_clean.to_csv(OUT, index=False)
print("Saved:", OUT)
