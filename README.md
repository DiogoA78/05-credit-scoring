# 💳 Scoring crédit — Pipeline ML, Explicabilité & Analyse de biais

> Construire un modèle de scoring crédit de bout en bout, puis l'ouvrir pour comprendre ses décisions et détecter ses biais.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-Explainability-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Contexte

Le scoring crédit est l'un des cas d'usage les plus courants du Machine Learning en entreprise, mais aussi l'un des plus sensibles : un refus mal expliqué ou un biais discriminatoire peuvent avoir des conséquences réelles. Ce projet va au-delà de la simple prédiction pour aborder les questions que les entreprises se posent : pourquoi le modèle refuse-t-il ce client ? Le modèle traite-t-il tous les groupes équitablement ?

## 🎯 Objectifs

- Construire un pipeline ML complet (EDA → features → modèle → évaluation)
- Benchmarker 4 modèles (Logistic Regression, Random Forest, XGBoost, LightGBM)
- Appliquer SHAP et LIME pour expliquer chaque prédiction
- Analyser les biais du modèle avec des métriques de fairness

## 🔧 Stack technique

| Outil | Usage |
|-------|-------|
| **Python 3.10+** | Langage principal |
| **Scikit-learn** | Pipeline ML, préprocessing |
| **XGBoost / LightGBM** | Modèles gradient boosting |
| **SHAP / LIME** | Explicabilité globale et locale |
| **Fairlearn** | Analyse de biais et fairness |
| **Optuna** | Optimisation d'hyperparamètres |

## 📁 Structure

```
05-credit-scoring/
├── README.md
├── requirements.txt
├── .gitignore / LICENSE
├── data/
│   ├── README.md
│   ├── download_data.py
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda_features.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_explainability_fairness.ipynb
├── src/
├── assets/
└── scripts/
```

## 🚀 Démarrage

```bash
pip install -r requirements.txt
python data/download_data.py
jupyter notebook notebooks/01_eda_features.ipynb
```

## 📊 Démo live

> [🔗 Voir l'app sur Streamlit Cloud](https://diogoa78-07-demonstrateur-hsrfdt8xqoiobofkvqmaqd.streamlit.app/)

## 📄 Source des données

- **German Credit — UCI / OpenML**
- 1 000 demandes de crédit avec 20 attributs + label (bon/mauvais payeur)
- Attributs sensibles disponibles (âge, sexe, statut) pour l'analyse de biais
- URL : [OpenML](https://www.openml.org/d/31)

## 📜 Licence

MIT — voir [LICENSE](LICENSE).
