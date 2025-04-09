import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# 🔗 API URL
url = "http://127.0.0.1:8000/kpis"
response = requests.get(url)
data_json = response.json()

seuils = {
    "Order Fulfillment Rate": 50.0,
    "Inventory Turnover": 6.0,
    "Order Accuracy": 50.0,
    "Supplier Lead Time": 20.0,  # Plus bas = mieux
    "Return Rate": 10.0,         # Plus bas = mieux
    "Lead Time": 4.0            # Plus bas = mieux
}
# ✅ Transformation en DataFrame
df = pd.DataFrame(data_json)
df["date"] = pd.to_datetime(df["date"])
# Vérification des valeurs dans les KPI avant l'agrégation
# Afficher les valeurs de chaque KPI pour voir si des zéros ou des valeurs manquantes existent
for kpi in seuils.keys():
    print(f"Valeurs pour {kpi} avant agrégation :")
    print(df[df["kpi_name"] == kpi]["value"])

# Filtrer les valeurs égales à zéro ou manquantes avant l'agrégation
df_cleaned = df[df["value"] > 0]  # Garder les valeurs strictement positives (ou remplace 0 par NaN si nécessaire)

# Agréger les données en calculant la moyenne des valeurs pour chaque KPI après nettoyage
df_aggregated = df_cleaned.groupby("kpi_name").agg({"value": "mean"}).reset_index()


# 🎯 KPI à afficher dans l’ordre souhaité
kpi_names = list(seuils.keys())

# Garder seulement les KPI dans la liste des seuils
df_aggregated = df_aggregated[df_aggregated["kpi_name"].isin(kpi_names)]

# Trier les données dans l'ordre des KPI souhaité
df_aggregated = df_aggregated.set_index("kpi_name").loc[kpi_names].reset_index()

# Valeurs moyennes et seuils
values = df_aggregated["value"].tolist()
seuils_values = [seuils[kpi] for kpi in kpi_names]

# 🕸 Préparation du Radar Chart
angles = np.linspace(0, 2 * np.pi, len(kpi_names), endpoint=False).tolist()
values += values[:1]  # Reprendre la première valeur pour fermer le cercle
seuils_values += seuils_values[:1]
angles += angles[:1]

# Affichage du graphique radar
plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)
ax.plot(angles, values, 'o-', linewidth=2, label='Valeurs Moyennes')
ax.fill(angles, values, alpha=0.25)
ax.plot(angles, seuils_values, 'o--', color='red', linewidth=2, label='Seuils')
ax.fill(angles, seuils_values, color='red', alpha=0.1)

ax.set_thetagrids(np.degrees(angles[:-1]), kpi_names)
plt.title("Comparaison KPI vs Seuils (Valeur Moyenne)", size=15)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
