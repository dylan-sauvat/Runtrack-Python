#Déclarer la valeur de i
i = input("> ")

#conditions
# Tant qu'on n'entre pas 'Au revoir' le script s'éxécute selon conditions
while i != "Au revoir" :
    if i == "Bonjour" :
        print("Bonjour à toi")
        i = input("> ")
    else :
        i = input("> ")

# Sinon le script se termine
exit()
