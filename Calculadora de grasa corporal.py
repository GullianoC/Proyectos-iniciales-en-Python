
from math import log10

#A continuación vamos a hacer una calculadora de grasa corporal
#Las variables usadas son las siguientes:
# nombre, sexo, estadoFisico como string
# altura, peso cintura, cuello, cadera, grasaCorporal como float

def calculadoraGrasaCorporal():
    print("A continuación vamos a calcular tu porcentaje de grasa corporal")
    print("¿Cuál es tu nombre?")
    nombre = str(input())
    print("¿Tu sexo es Masculino o Femenino?")
    print("Si tu sexo es Masculino, escribe M")
    print("Si tu sexo es Femenino, escribe F")
    sexo = str(input("")).upper()
    while (sexo != "M" and sexo != "F"):
        print("El sexo elegido es incorrecto, por favor ingresa M o F")
        sexo = str(input("")).upper()
    

    #Aquí se introducen los datos a ingresar
    print("Introduce tu altura en centímetros")
    altura = float(input())
    print("Introduce tu peso en kg")
    peso = float(input())
    print("Introduce tu perímetro abdominal (tamaño de cintura) en centímetros")
    cintura = float(input())
    print("Introduce tu cuello en centímetros")
    cuello = float(input())
    if sexo == "F":
        print("Ahora introduce tu cadera en centímetros")
        cadera = float(input())

    # Aquí se define el resultado final según el sexo declarado, se imprime el % de grasa corporal y se designa el estado físico

    if sexo == "M":
        grasaCorporal = 495/(1.0324-0.19077*log10(cintura-cuello)+0.15456*log10(altura)) - 450
        if grasaCorporal >=2.0 and grasaCorporal <4.0:
            estadoFisico = "Grasa esencial"
        if grasaCorporal >=6.0 and grasaCorporal <13.0:
            estadoFisico = "Atleta"
        if grasaCorporal >=13.0 and grasaCorporal <17.0:
            estadoFisico = "Fitness"
        if grasaCorporal >=17.0 and grasaCorporal <25.0:
            estadoFisico = "Aceptable"
        if grasaCorporal >=25.0:
            estadoFisico = "Obesidad"

    if sexo == "F":
        grasaCorporal = 495/(1.29579-0.35004*log10(cintura+cadera-cuello)+0.221*log10(altura)) - 450
        if grasaCorporal >=10.0 and grasaCorporal <12.0:
            estadoFisico = "Grasa esencial"
        if grasaCorporal >=12.0 and grasaCorporal <20.0:
            estadoFisico = "Atleta"
        if grasaCorporal >=20.0 and grasaCorporal <24.0:
            estadoFisico = "Fitness"
        if grasaCorporal >=24.0 and grasaCorporal <31.0:
            estadoFisico = "Aceptable"
        if grasaCorporal >=31.0:
            estadoFisico = "Obesidad"
    
    #Se imprime el resultado final en base a las medidas ingresadas:
    
    return(print("Bueno",nombre,", tu porcentaje de grasa corporal es de:", round(grasaCorporal,1),"%", "y tu estado físico es el siguiente:",estadoFisico))


#Ejecuto la función para calcular grasa corporal
calculadoraGrasaCorporal()
