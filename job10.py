x = input("Entrez un texte : ")     #Récupérer input et lui assigner une variable
#y = open('output.txt', 'w')        #Créer ou écraser fichier.txt et lui assigner variable
y = open('output.txt', 'a')         #Créer et/ou écrire à la suite
y.write(x)                          #Ecrire input dans le fichier.txt
y.write('\n')                       #Retour à la ligne en fin de phrase
print("Votre texte est enregistré dans un fichier nommé 'output.txt'")
print("Vous avez écrit :")
y = open('output.txt', 'r')         #Lecture du fichier.txt 
contents = y.read()                 #Déclaration variable du contenu
print(contents)                     #Ecriture sur le terminal