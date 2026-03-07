import pandas as pd

# Masterdatensatz laden
df = pd.read_csv("../data/processed/migration_master_dataset.csv")

# Nur Länderzeilen behalten
df = df[df["dimension_type"] == "country"]

# Deutschland definieren
GERMANY = "Germany"

# Emigration: Deutschland -> Ausland
df_emigration = df[df["direction"] == "emigration"].copy()
df_emigration["origin"] = GERMANY
df_emigration["destination"] = df_emigration["dimension_value"]

# Immigration: Ausland -> Deutschland
df_immigration = df[df["direction"] == "immigration"].copy()
df_immigration["origin"] = df_immigration["dimension_value"]
df_immigration["destination"] = GERMANY

# Zusammenführen
df_flows = pd.concat([df_emigration, df_immigration])

# Finales Netzwerkformat
df_network = df_flows[[
    "year",
    "origin",
    "destination",
    "value"
]].rename(columns={"value": "migrants"})

# Optional: Deutschland->Deutschland entfernen (falls vorhanden)
df_network = df_network[df_network["origin"] != df_network["destination"]]

# Export
df_network.to_csv("../data/processed/migration_network_flows.csv", index=False)

print("Network dataset created")
print(df_network.head())