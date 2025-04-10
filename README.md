
---

# 📊 Radar Chart KPI Visualization

Ce script Python permet de **récupérer des indicateurs de performance (KPI)** via une API, de les **nettoyer**, d’en faire **une moyenne par type de KPI**, puis de les **visualiser sous forme de radar chart** (ou graphique en toile d’araignée) en les comparant à des **seuils de référence**.

## 🔧 Fonctionnalités

- Connexion à une API REST (`/kpis`)
- Nettoyage des données : suppression des valeurs nulles ou égales à 0
- Agrégation par moyenne pour chaque KPI
- Comparaison visuelle avec des seuils définis
- Affichage d’un radar chart clair et lisible avec Matplotlib

## 📦 Dépendances

Ce script utilise les bibliothèques suivantes :

```bash
pip install requests pandas matplotlib numpy
```

## 🚀 Utilisation

1. **Assurez-vous que votre API est en ligne** à l'adresse suivante :

```
http://127.0.0.1:8000/kpis
```

L’API doit retourner un JSON de cette forme :

```json
[
  {
    "kpi_name": "Order Fulfillment Rate",
    "value": 65.2,
    "date": "2025-04-01"
  },
  ...
]
```

2. **Lancer le script** :

```bash
python radar_kpi.py
```

Le script :

- Récupère les données de l’API
- Filtre les valeurs non valides
- Calcule la moyenne des KPI
- Affiche un radar chart comparant les moyennes aux seuils

## 📈 Liste des KPI et Seuils

| KPI                     | Seuil    | Interprétation              |
|--------------------------|----------|------------------------------|
| Order Fulfillment Rate   | ≥ 50.0   | Plus haut = mieux           |
| Inventory Turnover       | ≥ 6.0    | Plus haut = mieux           |
| Order Accuracy           | ≥ 50.0   | Plus haut = mieux           |
| Supplier Lead Time       | ≤ 20.0   | Plus bas = mieux            |
| Return Rate              | ≤ 10.0   | Plus bas = mieux            |
| Lead Time                | ≤ 4.0    | Plus bas = mieux            |

> Les seuils sont configurables directement dans le script via le dictionnaire `seuils`.

## 🧪 Exemple de résultat

Une fois exécuté, le script produit un radar chart où :

- **Ligne bleue** : valeurs moyennes des KPI
- **Ligne rouge pointillée** : seuils à atteindre
- **Zone colorée** : meilleure visualisation de la performance

## 📂 Fichiers

- `radar_kpi.py` : le script principal
- `README.md` : ce fichier d'explication

---
