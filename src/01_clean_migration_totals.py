import pandas as pd
from pathlib import Path

RAW = Path("data/raw/genesis/migration_totals_raw.xlsx")
OUT = Path("data/processed/migration_totals_long.csv")

# --- 1. Excel laden (nur Blatt)
df = pd.read_excel(
    RAW,
    sheet_name="csv-12711-02"
)

# --- 2. Spalten vereinheitlichen
df.columns = [c.lower().strip() for c in df.columns]

# Erwartete Namen nach deinem Beispiel:
# gebiet, nationalitaet, jahr, zuzuege_aus_dem_ausland, fortzuege_in_das_ausland

# --- 3. Nur Deutschland gesamt behalten
df = df[
    (df["nationalitaet"] == "Deutsche")
]

# --- 4. "-" → NaN
df = df.replace("-", pd.NA)

# --- 5. Zahlen konvertieren
df["zuzuege_aus_dem_ausland"] = pd.to_numeric(
    df["zuzuege_aus_dem_ausland"],
    errors="coerce"
)

df["fortzuege_in_das_ausland"] = pd.to_numeric(
    df["fortzuege_in_das_ausland"],
    errors="coerce"
)

# --- 6. Nur relevante Spalten
df = df[[
    "jahr",
    "zuzuege_aus_dem_ausland",
    "fortzuege_in_das_ausland"
]]

# --- 7. Unpivot
df_long = df.melt(
    id_vars="jahr",
    value_vars=[
        "zuzuege_aus_dem_ausland",
        "fortzuege_in_das_ausland"
    ],
    var_name="direction",
    value_name="value"
)

# --- 8. Labels schöner
df_long["direction"] = df_long["direction"].map({
    "zuzuege_aus_dem_ausland": "immigration",
    "fortzuege_in_das_ausland": "emigration"
})

# --- 9. Sortieren
df_long = df_long.sort_values(["jahr", "direction"])

# --- 10. Speichern
df_long.to_csv(OUT, index=False)

print("Saved:", OUT)