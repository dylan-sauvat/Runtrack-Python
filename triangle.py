# Déclarer "integuer" pour la hauteur en "input"

H = int(input("Veuillez entrer la hauteur : "))
i = 0 

for n in range(H,1, -1):                        #Pour n dans la hauteur, décrémenter de 1.

    print(" " * n + "/" + " " * i * 2 + "\\")   #Définit la colonne
    i += 1

print(" /" + "__" * (H - 1) + "\\")             #Définit la ligne
