🇫🇷 [Version française](README_FR.md)

# 💳 Credit Scoring — ML Pipeline, Explainability & Bias Analysis

> Building an end-to-end credit scoring model, then opening it up to understand its decisions and detect its biases.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-Explainability-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Context

Credit scoring is one of the most common Machine Learning use cases in business, but also one of the most sensitive: a poorly explained denial or a discriminatory bias can have real consequences. This project goes beyond simple prediction to address the questions companies face: why did the model deny this customer? Does the model treat all groups fairly?

## 🎯 Objectives

- Build a complete ML pipeline (EDA → features → model → evaluation)
- Benchmark 4 models (Logistic Regression, Random Forest, XGBoost, LightGBM)
- Apply SHAP and LIME to explain each prediction
- Analyze model biases with fairness metrics

## 🔧 Tech Stack

| Tool | Usage |
|------|-------|
| **Python 3.10+** | Main language |
| **Scikit-learn** | ML pipeline, preprocessing |
| **XGBoost / LightGBM** | Gradient boosting models |
| **SHAP / LIME** | Global and local explainability |
| **Fairlearn** | Bias and fairness analysis |
| **Optuna** | Hyperparameter optimization |

## 📁 Structure

```
05-credit-scoring/
├── README.md                          ← This file
├── README_FR.md                       ← French version
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

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python data/download_data.py
jupyter notebook notebooks/01_eda_features.ipynb
```

## 📊 Live Demo

> [🔗 View the app on Streamlit Cloud](https://diogoa78-07-demonstrateur-hsrfdt8xqoiobofkvqmaqd.streamlit.app/)

## 📄 Data Source

- **German Credit — UCI / OpenML**
- 1,000 credit applications with 20 attributes + label (good/bad payer)
- Sensitive attributes available (age, gender, status) for bias analysis
- URL: [OpenML](https://www.openml.org/d/31)

## 📜 License

MIT — see [LICENSE](LICENSE).
