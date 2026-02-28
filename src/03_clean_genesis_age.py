import pandas as pd
import re
from pathlib import Path

RAW = Path("../data/raw/genesis/migration_age_genesis_raw.csv")
OUT = Path("../data/processed/migration_age_long.csv")

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

# In dieser Datei gibt es Zeilen mit bis zu 19 Feldern (18 Semikolons)
colnames = list(range(19))
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
    "Wanderungen",
    "Deutschland",
    "Deutsche",
    "Zuzüge",
    "Fortzüge",
    "Wanderungssaldo",
    "Anzahl",
    "Wanderungsstatistik",
    "Tabelle:",
    "©",
    "Stand:",
    "männlich",
    "weiblich",
]

for _, row in df_raw.iterrows():
    first = row.iloc[0]
    if pd.isna(first):
        continue

    first_str = str(first).strip().lstrip("\ufeff")  # BOM falls vorhanden

    # Jahr erkennen (z.B. "2000")
    if re.fullmatch(r"\d{4}", first_str):
        y = int(first_str)
        if 1900 < y < 2100:
            current_year = y
        continue

    if current_year is None:
        continue

    # Meta-Zeilen überspringen
    if any(k in first_str for k in meta_keywords):
        continue

    # Optional: die Gesamtzeile der Altersdimension rauslassen (verhindert Double Counting)
    if first_str == "Insgesamt":
        continue

    age = first_str

    # Insgesamt-Block: Zuzüge=col13, Fortzüge=col15
    immigration = clean_number(row.iloc[13])
    emigration  = clean_number(row.iloc[15])

    if immigration is not None:
        records.append({
            "year": current_year,
            "dimension_type": "age",
            "dimension_value": age,
            "direction": "immigration",
            "value": immigration
        })

    if emigration is not None:
        records.append({
            "year": current_year,
            "dimension_type": "age",
            "dimension_value": age,
            "direction": "emigration",
            "value": emigration
        })

df_clean = pd.DataFrame(records).sort_values(["year", "dimension_value", "direction"])

OUT.parent.mkdir(parents=True, exist_ok=True)
df_clean.to_csv(OUT, index=False)
print("Saved:", OUT)
