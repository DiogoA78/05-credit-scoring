# 📊 Données — German Credit Dataset

## Source

- **Nom :** Statlog (German Credit Data)
- **Éditeur :** UCI Machine Learning Repository / OpenML
- **Licence :** CC BY 4.0
- **OpenML :** [openml.org/d/31](https://www.openml.org/d/31)

## Téléchargement

```bash
python data/download_data.py
```

## Description

1 000 demandes de crédit, chacune classée comme bon (1) ou mauvais (2) payeur.

## Variables clés

| Variable | Type | Description |
|----------|------|-------------|
| `checking_status` | Catégorielle | Statut du compte courant |
| `duration` | Numérique | Durée du crédit (mois) |
| `credit_history` | Catégorielle | Historique de crédit |
| `purpose` | Catégorielle | Objet du crédit |
| `credit_amount` | Numérique | Montant du crédit |
| `savings_status` | Catégorielle | Épargne |
| `employment` | Catégorielle | Ancienneté emploi |
| `installment_commitment` | Numérique | Taux d'effort (% revenu) |
| `personal_status` | Catégorielle | Sexe et statut marital |
| `age` | Numérique | Âge |
| `housing` | Catégorielle | Type de logement |
| `job` | Catégorielle | Type d'emploi |
| `class` | Label | 1 = bon payeur, 2 = mauvais payeur |

## Variables sensibles (pour l'analyse de biais)

- `personal_status` → contient le sexe (male/female)
- `age` → permet de créer des tranches d'âge
- `foreign_worker` → statut de travailleur étranger
