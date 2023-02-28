# Insérer les 2 valeurs en input 
nb1 = int(input("Entrez un nombre :  "))
nb2 = int(input("Entrez un nombre :  "))

# Conditions de l'intervale
if nb1 == nb2 :
    print("Valeurs éguales")

# Boucle en décrementation
elif nb1 > nb2 :
    for i in range(nb1-1 , nb2 , -1) :
        print(i)

# Boucle en incrémentation
else :
    for i in range(nb1+1 , nb2 , +1) :
        print(i)

