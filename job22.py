
def myUpper (a) :
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïABCDEFGHIJKLMNOPQRSTUVWXYZAAEEEEII'
    result = ''
    for x in a:
        if x not in alphabet or alphabet.index(x)>=34:
            result += x
        else:
            result += alphabet[alphabet.index(x)+34]
    return result

def myLower (b) :
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in b:
        if x not in alphabet or alphabet.index(x)<=26:
            result += x
        else:
            result += alphabet[alphabet.index(x)-26]
    return result

def myTitle (c) :
    words = c.split()
    result = ''
    for y in range(len(words)) :
        maj = words[y][0]
        title = myUpper(maj)+words[y][1:]
        result += title + " "
    return result

def myClean (d) :
    words = d.split()
    result = ''
    for i in range(len(words)) :
        result += words[i] + " "
    return result


texte = input("Entrez une phrase : ")
param = input("Choisissez un paramètre : upper lower title clean : " )

while param != "upper" and param != "lower" and param != "title" and param != "clean" :
    print("Entrée invalide !")
    param = input("Veuillez choisir un paramètre parmi les suivants : \n upper \n lower \ntitle \nclean")

if param == "upper" :
    print(myUpper(texte))
elif param == "lower" :
    print(myLower(texte))
elif param == "title" :
   print(myTitle(texte))
elif param == "clean" :
   print(myClean(texte))


   