def tribis(*args) :
    myList = []                                                 #Crée liste vide myList

    for i in args :
        myList.append(i)                                        #Ajoute i à la liste

    for i in range(len(myList)):                                #Pour inième dans la longueur de la liste
        for j in range(i + 1, len(myList)):                     #Pour jnième +1 dans la longueur de la liste
            if myList[i] > myList[j]:                           #Condition : si i > j
                myList[i], myList[j] = myList[j], myList[i]     #inverser l'ordre

    print(myList)

tribis(99, 22, 33, 55, 29, 95, 27, 12, 77)                      #Appel de la fonction


