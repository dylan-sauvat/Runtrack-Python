with open("domains.xml") as f:                      #Ouvre domains.xml en tant que f
    contents = f.read()                             

    counts = contents.count("domain")               #variable qui compte le nombre de mots 'domain'
    print("Le nombre de domaines est : ", counts)
f.close()
