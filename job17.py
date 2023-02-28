def pairs(*args):

    myList = []                             # [créer liste vide]
    for i in args :
        myList += [i]
    p = []
    for j in myList:
        if j % 2 == 0:
            p.append(j)
    print("Les nombres pairs sont: ", p)

pairs(1, 2, 3, 4, 5, 6, 7, 8)              #affiche les nombres pairs de la list



############### METHODE AVEC PARAM sous forme de LISTE #######################


#     print("Les nombres pairs sont: ")
#     for i in range(len(liste)):
#         if liste[i] % 2 == 0 :
#             print (liste[i])

# args = list(range(1, 101, 1))

# pairs(args)

