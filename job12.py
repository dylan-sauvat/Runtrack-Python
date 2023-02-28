#f = open('data.txt', 'r')
with open('data.txt', 'r') as f:
    file = f.read()

    words = file.split()
    wordCount = len(words)
    print ("La somme des mots est de :", wordCount)




#Vérification en bash
#wc -w data.txt
#-->1173361 data.txt