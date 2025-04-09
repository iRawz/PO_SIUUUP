import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ✅ Données simulées
data = {
    'commandes': 500,
    'commandes_livrees_a_temps': 420,
    'stock_moyen': 120000,  # en €
    'ventes_net': 600000,   # en €
    'cout_biens_vendus': 450000,
    'taux_possession': 0.25,
    'commandes_parfaites': 385,
    'cout_total_transport': 75000,  # en €
    'tonnage_total': 1500,  # en tonnes
    'delais_livraisons_fournisseurs': [True, True, False, True, False, True, True, True, False, True],
}

# ✅ Calcul des KPI
kpis = {}

# 1. Livraison à l’heure (Ponctualité client)
kpis['Ponctualité Client (%)'] = round(data['commandes_livrees_a_temps'] / data['commandes'] * 100, 2)

# 2. Ratio Stock / Ventes (ISR)
kpis['ISR (Stock/Ventes)'] = round(data['stock_moyen'] / data['ventes_net'], 2)

# 3. Coût de possession du stock
kpis['Coût de possession du stock (€)'] = round(data['stock_moyen'] * data['taux_possession'], 2)

# 4. Ponctualité fournisseurs
ponctualite_fournisseurs = sum(data['delais_livraisons_fournisseurs']) / len(data['delais_livraisons_fournisseurs']) * 100
kpis['Ponctualité Fournisseurs (%)'] = round(ponctualite_fournisseurs, 2)

# 5. DSI – Durée moyenne de rotation des stocks
kpis['DSI (jours)'] = round((data['stock_moyen'] / data['cout_biens_vendus']) * 365, 1)

# 6. Coût transport par tonne
kpis['Coût transport/tonne (€)'] = round(data['cout_total_transport'] / data['tonnage_total'], 2)

# 7. Taux de commandes parfaites
kpis['Commandes parfaites (%)'] = round(data['commandes_parfaites'] / data['commandes'] * 100, 2)

# ✅ Affichage des KPI
print("🔍 Résumé des KPI logistiques :\n")
for k, v in kpis.items():
    print(f"{k}: {v}")

# ✅ Comparaison avec les seuils standards
seuils = {
    'Ponctualité Client (%)': 95,
    'ISR (Stock/Ventes)': 0.2,
    'Ponctualité Fournisseurs (%)': 90,
    'DSI (jours)': 60,
    'Coût transport/tonne (€)': 50,
    'Commandes parfaites (%)': 98
}

# ✅ Visualisation radar
import pandas as pd

kpi_names = list(seuils.keys())
kpi_values = [kpis[k] for k in kpi_names]
kpi_seuils = [seuils[k] for k in kpi_names]

df_kpi = pd.DataFrame({
    'KPI': kpi_names,
    'Valeur Réelle': kpi_values,
    'Seuil Recommandé': kpi_seuils
})

angles = np.linspace(0, 2 * np.pi, len(kpi_names), endpoint=False).tolist()
values = df_kpi['Valeur Réelle'].tolist()
seuils_plot = df_kpi['Seuil Recommandé'].tolist()

# Fermer le cercle
values += values[:1]
seuils_plot += seuils_plot[:1]
angles += angles[:1]

# Radar chart
plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)
ax.plot(angles, values, 'o-', linewidth=2, label='Valeur Réelle')
ax.fill(angles, values, alpha=0.25)
ax.plot(angles, seuils_plot, 'o--', color='red', linewidth=2, label='Seuil')
ax.fill(angles, seuils_plot, color='red', alpha=0.1)

ax.set_thetagrids(np.degrees(angles[:-1]), kpi_names)
plt.title("Comparaison KPI vs Seuils", size=15)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# 🖼️ Générer un rapport visuel avec matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis("off")

reco_lines = [" Axes d'amélioration logistique", ""]

if kpis['Ponctualité Client (%)'] < seuils['Ponctualité Client (%)']:
    reco_lines += [
        "Ponctualité client",
        "→ Réduire les délais d’expédition",
        "→ Suivi temps réel des transporteurs",
        "→ Optimiser les tournées", ""
    ]

if kpis['ISR (Stock/Ventes)'] > seuils['ISR (Stock/Ventes)']:
    reco_lines += [
        "Ratio Stock/Ventes",
        "→ Ajuster le stock à la demande",
        "→ Réévaluer les seuils de réapprovisionnement", ""
    ]

if kpis['Ponctualité Fournisseurs (%)'] < seuils['Ponctualité Fournisseurs (%)']:
    reco_lines += [
        " Fiabilité fournisseurs",
        "→ Identifier les non-conformités",
        "→ Mettre en place des SLA",
        "→ Diversifier les fournisseurs", ""
    ]

if kpis['DSI (jours)'] > seuils['DSI (jours)']:
    reco_lines += [
        "Rotation des stocks (DSI)",
        "→ Destocker les produits lents",
        "→ Lancer des promotions ciblées",
        "→ Améliorer la prévision de la demande", ""
    ]

if kpis['Coût transport/tonne (€)'] > seuils['Coût transport/tonne (€)']:
    reco_lines += [
        " Coût de transport élevé",
        "→ Regrouper les expéditions",
        "→ Négocier avec les transporteurs",
        "→ Optimiser le chargement", ""
    ]

if kpis['Commandes parfaites (%)'] < seuils['Commandes parfaites (%)']:
    reco_lines += [
        " Commandes parfaites insuffisantes",
        "→ Améliorer le contrôle qualité",
        "→ Réduire les erreurs de picking",
        "→ Digitaliser le suivi de commande", ""
    ]

# 💬 Afficher tout le texte dans le graphe
ax.text(0.01, 1.0, "\n".join(reco_lines), fontsize=12, va="top")

plt.tight_layout()
plt.show()
