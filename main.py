from csv import DictReader


# Exercice.Question

# 1.1
def charge_fichier(chemin, colonne_num):
    with open(chemin, 'r') as f:
        table = list(DictReader(f, delimiter=";"))
        f.close()

    for line in table:
        for i in line:
            if i in colonne_num:
                line[i] = int(line[i])

    return table


# 1.2
MOVIE = charge_fichier("movie.csv", ["mid", "runtime", "year", "rank"])
PEOPLE = charge_fichier("people.csv", ["pid"])
ROLE = charge_fichier("role.csv", ["mid", "pid"])
DIRECTOR = charge_fichier("director.csv", ["mid", "pid"])


# 1.3
def affiche(l):
    """
    for i in l:
        print(i)
    print("--")

    Ce code marche mais c'est lent car la fonction print est LENTE
    Donc, on peut 'factoriser' tout ça en faisant un seul print
    """

    result = ""

    for i in l:
        result += str(i) + '\n'
    result += "--"

    print(result)


# 2.1
def anne_entre(m, y1, y2):
    """ Version chiante même si ça marche
    result = []
    for film in m:
        if y1 <= film["year"] <= y2:  # ya écrit 'inclus' dans l'énoncé donc c'est <= et pas <
            result += [film]

    return result
    """

    # Version cool
    return [film for film in m if y1 <= film["year"] <= y2]


# 2.2
def prenom(p, pr):
    """ Version chiante
    result = []
    for people in p:
        if people["firstname"] == pr:
            result += [people]
    return result
    """

    # Version cool
    return [people for people in p if people["firstname"] == pr]


# 2.3
def movie_director(movie, director, people):
    """En suivant l'algorithme de l'énoncé:

    1 - initialiser un tableau vide r
    2 - pour chaque dictionnaire d dans director:
    3 - soit p le dictionnaire de people tel que d["pid"] == p["pid"]
    4 - s’il n’y a pas de tel p, passer au d suivant
    5 - soit m le dictionnaire de movie tel que d["movie"] == m["movie"]
    6 - s’il n’y a pas de tel m, passer au d suivant
    7 - ajouter (m, p) à la fin de r

    """

    r = []  # 1
    for d in director:  # 2
        p = [p for p in people if d["pid"] == p["pid"]]  # 3
        """ 4 """
        if not p:
            continue
        """"""

        m = [m for m in movie if d["mid"] == m["mid"]]  # 5

        """ 6 """
        if not m:
            continue
        """"""

        r += [(m, p)]  # 7

    return r
    # Pour cette question j'ai pas réfléchi, y'a juste a recopier bêtement l'algorithme qu'il demande


# 2.4
def movie_role(movie, role, people):
    """
        J'ai fait un copié collé de la fonction d'avant, en remplaçant "director" par "role" à la 2e ligne
        D'ailleurs c'est con car on pourrait mettre tout ça en une seule fonction du coup vu que c'est là même.
    """

    r = []  # 1
    for d in role:  # 2
        p = [p for p in people if d["pid"] == p["pid"]]  # 3
        """ 4 """
        if not p:
            continue
        """"""

        m = [m for m in movie if d["mid"] == m["mid"]]  # 5

        """ 6 """
        if not m:
            continue
        """"""

        r += [(m, p)]  # 7

    return r

#


if __name__ == '__main__':
    # affiche(MOVIE)
    # affiche(anne_entre(MOVIE, 2000, 2001))
    # affiche(prenom(PEOPLE, "John"))
    # affiche(movie_director(MOVIE, DIRECTOR, PEOPLE))
    affiche(movie_role(MOVIE, DIRECTOR, PEOPLE))
