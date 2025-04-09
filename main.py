import requests
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Récupération des données depuis l'API
url = "http://127.0.0.1:8000/kpis"
response = requests.get(url)
data = response.json()

# Calcul des moyennes par KPI
kpi_values = defaultdict(list)
for item in data:
    kpi_values[item['kpi_name']].append(item['value'])

kpi_avg = {kpi: sum(values) / len(values)
           for kpi, values in kpi_values.items()}

# Préparation des données pour le radar chart
categories = list(kpi_avg.keys())
values = list(kpi_avg.values())
values += values[:1]  # Fermer la boucle
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Création du radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')
ax.fill(angles, values, color='blue', alpha=0.25)

# Configuration des axes
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Ajout d'étiquettes radiales pour chaque axe
for i, angle in enumerate(angles[:-1]):
    ax.text(angle, max(values) * 1.1, f"{values[i]:.2f}",
            ha='center', va='center', fontsize=8)

    # Ajout d'une échelle simple
    ax.text(angle, max(values) * 0.9, f"0-{int(max(values))}",
            ha='center', va='center', fontsize=6, rotation=90 - angle * 180 / np.pi)

# Ajout de quelques étiquettes radiales pour l'échelle
ax.set_yticks([0, max(values) * 0.5, max(values)])
ax.set_yticklabels(['0', f"{max(values) * 0.5:.1f}", f"{max(values):.1f}"], fontsize=8)

plt.title('Moyennes des KPIs', size=15, y=1.1)
plt.tight_layout()
plt.show()
