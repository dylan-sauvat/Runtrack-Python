from curses.ascii import isdigit

nb = input("Veuillez renseigner un nombre : ")
while nb.isdigit() == False :
    nb = input("Entrée invalide, Veuillez entrer un nombre : ")

nb = int(nb)
f = open("data.txt", "r") 
file = f.read()

list = file.split()
wordCount = 0
for i in range(len(list)):
    if len(list[i]) == nb:
        wordCount += 1
f.close()

print("Il y a", wordCount, "mots de", nb, "lettres dans le fichier")

