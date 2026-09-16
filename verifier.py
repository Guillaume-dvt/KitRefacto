"""Vérifie que le refactoring n'a rien cassé.
Usage : python verifier.py   (après avoir exécuté nettoyage.py)
Compare les sorties aux références figées dans reference/."""
import sys
import pandas as pd

FICHIERS = ["ventes_propres.csv", "total_par_ville.csv", "total_par_produit.csv"]

def main() -> int:
    erreurs = 0
    for nom in FICHIERS:
        try:
            obtenu = pd.read_csv(f"data/{nom}", sep=";")
            attendu = pd.read_csv(f"reference/{nom}", sep=";")
            pd.testing.assert_frame_equal(obtenu, attendu, check_dtype=False)
            print(f"OK    {nom}")
        except FileNotFoundError as e:
            print(f"ABSENT {nom} : {e.filename}"); erreurs += 1
        except AssertionError as e:
            print(f"ÉCART {nom}\n{e}"); erreurs += 1
    print("\nRésultat :", "tout est identique ✅" if erreurs == 0 else f"{erreurs} problème(s) ❌")
    return 1 if erreurs else 0

if __name__ == "__main__":
    sys.exit(main())
