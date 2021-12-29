from csv import DictReader

from typing import List


def charge_fichier(chemin: str, colonne_num: List[str]) -> None:
    with DictReader(chemin, delimiter=';') as f:
        f.read()



if __name__ == '__main__':
    charge_fichier("movie.csv", ["mid", "runtime", "year", "rank"])
