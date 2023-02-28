def myAddition(a,b):
    return (a+b)
    
while True:
    try:
        nb1 = int(input("Entrez un nombre : "))
        nb2 = int(input("Entrez le second nombre pour l'addition : "))

        break
    except ValueError:
        print("Saisie érronée ! ")

result = myAddition(nb1,nb2)
print("la somme est :",result)

#################autre fonction######################

# print('La somme est : %.1f' %(int(input('Entrez le premier nombre : ')) + int(input('Entrez le second nombre pour l\'addition : '))))