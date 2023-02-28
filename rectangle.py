# Déclarer "integuer" pour le "input"

l = int(input("Veuillez entrer la largeur : "))
h = int(input("Veuillez entrer la hauteur : "))

# Pour la hauteur, définir le 1er caractère et le dernier, soit le pipe

for i in range(h) :
    if i == 0 or i == h-1 :     # "-1" parce que le compte commence à zero
        print("|", end="")      #le 'end' empêche le retour à la ligne après chaque caractère
        #boucle pour la largeur
        for i in range(l-2) :   # soustraire les 2 caractères aux extrémités (pipes)
            print("-", end="")  # remplir de tirets sans retour à la ligne
        print("|")              # fermer la ligne avec un pipe
    else :
        # sinon
        print("|", end="")      # un pipe et des espaces vides
        for i in range(l-2) :   # insérer les espaces vides entre les pipes
            print(" ", end="")
        print("|")              # fermer avec un pipe   