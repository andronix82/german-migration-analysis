import pandas as pd

# Masterdatensatz laden
df = pd.read_csv("../data/processed/migration_master_dataset.csv")

# Nur Länderzeilen
df = df[df["dimension_type"] == "country"]

# Ohne Ungeklärt / Ohne Angabe
df = df[df["dimension_value"] != "Ungeklärt / Ohne Angabe"]

GERMANY = "Germany"

# Emigration: Germany -> foreign country
df_emigration = df[df["direction"] == "emigration"].copy()
df_emigration["origin"] = GERMANY
df_emigration["destination"] = df_emigration["dimension_value"]

# Immigration: foreign country -> Germany
df_immigration = df[df["direction"] == "immigration"].copy()
df_immigration["origin"] = df_immigration["dimension_value"]
df_immigration["destination"] = GERMANY

# Zusammenführen
df_flows = pd.concat([df_emigration, df_immigration])

# Netzwerkformat
df_network = df_flows[[
    "year",
    "origin",
    "destination",
    "value"
]].rename(columns={"value": "migrants"})

# Deutschland -> Deutschland entfernen
df_network = df_network[df_network["origin"] != df_network["destination"]]

# 🔹 Aggregation (die 3 wichtigen Zusatzzeilen)
df_network = (
    df_network
    .groupby(["year", "origin", "destination"], as_index=False)
    .sum()
)

# Export
df_network.to_csv("../data/processed/migration_network_flows_wo_ungeklärt.csv", index=False)

print("Network dataset created")
print(df_network.head())