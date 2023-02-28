mot = input("Entrez un mot : ")

# Vérification que le mot ne contient que des lettres de l'alphabet
if not mot.isalpha():
    print("Le mot doit contenir uniquement des lettres de l'alphabet.")
    exit()

# Conversion du mot en une liste de caractères
caracteres = list(mot)

# Parcours de la liste de caractères de droite à gauche
for i in range(len(caracteres) - 2, -1, -1):
    # Si le caractère courant est plus petit que le suivant,
    # on cherche le caractère le plus petit qui est plus grand que lui
    if caracteres[i] < caracteres[i + 1]:
        plus_petit_plus_grand = i + 1
        for j in range(i + 2, len(caracteres)):
            if caracteres[i] < caracteres[j] and caracteres[j] < caracteres[plus_petit_plus_grand]:
                plus_petit_plus_grand = j

        # Échange du caractère courant avec le plus petit plus grand
        caracteres[i], caracteres[plus_petit_plus_grand] = caracteres[plus_petit_plus_grand], caracteres[i]

        # Tri des caractères situés après le caractère courant
        caracteres[i + 1:] = sorted(caracteres[i + 1:])

        # Conversion de la liste de caractères en un mot
        nouveau_mot = ''.join(caracteres)

        # Affichage du nouveau mot
        print("Le nouveau mot est :", nouveau_mot)
        break
else:
    print("Le mot est déjà le dernier dans l'ordre alphabétique.")

