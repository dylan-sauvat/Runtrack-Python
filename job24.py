import itertools

# Dictionnaire de points pour chaque lettre
points = {
    'E': 1, 'A': 1, 'I': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'L': 1,
    'D': 2, 'G': 2, 'M': 2,
    'B': 3, 'C': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4,
    'J': 8, 'Q': 8,
    'K': 10, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

# Liste des mots dans le dictionnaire
with open('dictionnaire.txt', 'r') as f:
    dictionnaire = f.read().splitlines()

# Demande à l'utilisateur d'entrer des lettres
lettres = input("Entrez des lettres : ")

# Vérification que les lettres ne contiennent que des lettres de l'alphabet
if not lettres.isalpha():
    print("Les lettres doivent contenir uniquement des lettres de l'alphabet.")
    exit()

# Conversion des lettres en une liste de caractères
lettres = list(lettres)

# Parcours de toutes les combinaisons de lettres possibles
mots = []
for i in range(1, len(lettres) + 1):
    for combinaison in itertools.combinations(lettres, i):
        mot = ''.join(combinaison)
        if mot in dictionnaire:
            points_mot = sum(points[lettre] for lettre in mot)
            mots.append((points_mot, mot))

# Affichage des mots par ordre décroissant de points
mots_tries = sorted(mots, reverse=True)
for points_mot, mot in mots_tries:
    print(mot, ":", points_mot, "points")
