
# Utiliser modulo pour définir les multiples de 3 et 5 (si "le reste" =0, c'est bien un multiple)

for i in range(1, 101) :
    if i%3 == 0 and i%5 == 0 :
        print("FizzBuzz")
    
    elif  i%3 == 0 :        #Pour les multiples de 3
        print("Fizz")

    elif i%5 == 0 :         #Pour les multiples de 5
        print("Buzz")

    else :
        print (i)           #pour le reste, afficher nombre


