
import re
#Se fabrica un detector de palíndromos (expresión que se lee igual de izquierda a derecha y viceversa)



def reversor(x):
    return x[::-1]

def Palindromo():
    print("Introduce una frase o palabra, te diré si es palíndromo o no")
    palabra1 = str(input())
    palabra2 =  re.sub(r"[^a-zA-Z0-9]", "", palabra1)
    palabrainvertida = reversor(palabra2)
    if (palabra2.lower() == palabrainvertida.lower()):
        print("Es palindromo")
    else:
        print("No es palíndromo")

#Se ejecuta la función de palíndromo para chequear si efectivamente lo es o no
Palindromo()





