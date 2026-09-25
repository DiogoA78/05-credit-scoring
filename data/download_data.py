"""
Téléchargement du dataset German Credit depuis OpenML.

Source : https://www.openml.org/d/31
1000 demandes de crédit, 20 attributs, label bon/mauvais payeur.

Usage : python data/download_data.py
"""

from pathlib import Path
import requests

SCRIPT_DIR = Path(__file__).parent
RAW_DIR = SCRIPT_DIR / "raw"

SOURCES = {
    "german_credit.csv": "https://www.openml.org/data/get_csv/31/dataset_31_credit-g.arff",
}

# Alternative : télécharger depuis UCI directement
UCI_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"


def download_openml():
    """Télécharge via l'API OpenML (format CSV)."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    try:
        from sklearn.datasets import fetch_openml
        print("  Téléchargement via sklearn.datasets.fetch_openml...")
        data = fetch_openml(data_id=31, as_frame=True, parser="auto")

        df = data.frame
        filepath = RAW_DIR / "german_credit.csv"
        df.to_csv(filepath, index=False)
        print(f"  ✓ german_credit.csv ({len(df)} lignes, {df.shape[1]} colonnes)")
        return True

    except Exception as e:
        print(f"  ⚠️  OpenML échoué : {e}")
        return False


def download_uci_fallback():
    """Fallback : télécharger depuis UCI."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    filepath = RAW_DIR / "german_credit_uci.data"

    if filepath.exists():
        print(f"  ✓ Fichier UCI déjà présent")
        return True

    print("  Téléchargement depuis UCI...")
    try:
        r = requests.get(UCI_URL, timeout=30)
        r.raise_for_status()
        filepath.write_text(r.text)
        print(f"  ✓ german_credit_uci.data téléchargé")
        return True
    except Exception as e:
        print(f"  ❌ Échec : {e}")
        return False


def main():
    print("=" * 60)
    print("📥 Téléchargement German Credit Dataset")
    print("=" * 60)

    filepath = RAW_DIR / "german_credit.csv"
    if filepath.exists() and filepath.stat().st_size > 0:
        print(f"\n✓ Déjà présent : {filepath.name}")
        return

    print("\n1. Tentative OpenML (sklearn)...")
    if download_openml():
        return

    print("\n2. Fallback UCI...")
    download_uci_fallback()

    print("\n" + "=" * 60)
    print("📊 Terminé")
    print("=" * 60)


if __name__ == "__main__":
    main()
