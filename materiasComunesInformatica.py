"""
La finalidad de este algoritmo es la de poder comparar entre asignaturas de las carreras relacionadas a la Informática.
En este algoritmo se hace una comparación entre las asignaturas de la Facultad de Ciencias Exactas y Tecnología (UNT), y se consideran las tres carreras principales relacionadas con la informática.
Las carreras son:
1) Programador Universitario
2) Licenciatura en Informática
3) Ingeniería en Informática

"""

programador = "Programador Universitario"
licinformatica = "Lic. en Informática"
inginformatica = "Ing. en Informática"

ProgU = ["Calculo I", "Algebra I", "Elementos de Computacion y Logica", "Laboratorio I", "Calculo II", "Algebra II", "Programacion", "Laboratorio II", "Algoritmos y Estructuras de Datos I", "Arquitectura y Org I", "Taller de Lenguajes I", "Metodos Numericos", "Probabilidad y Estadistica", "Paradigmas de la Programacion", "Bases de Datos I", "Taller de Lenguajes II", "Sistemas de Informacion", "Comunicaciones I", "Sistemas Operativos I", "Bases de Datos II", "Ingenieria de Software", "Comunicaciones II", "Sistemas Abiertos", "Legislacion y Organizaciones", "Proyecto Final", "Certificacion Ingles"]
LicInf = ["Calculo I", "Algebra I", "Elementos de Computacion y Logica", "Laboratorio I", "Calculo II", "Algebra II", "Programacion", "Laboratorio II", "Algoritmos y Estructuras de Datos I", "Calculo III", "Taller de Lenguajes I", "Paradigmas de la Programacion", "Probabilidad y Estadistica", "Bases de Datos I", "Arquitectura y Org I", "Metodos Numericos", "Bases de Datos II", "Arquitectura y Org I", "Arquitectura y Org II", "Taller de Lenguajes II", "Metodos Numericos II", "Matematica Discreta", "Ingenieria de Software I", "Sistemas Operativos I", "Comunicaciones I", "Ingenieria de Software II", "Sistemas Operativos II", "Comunicaciones II", "Sistemas Abiertos", "Proyecto Final", "Sistemas de Informacion", "Conceptos de Lenguajes", "Optativa I", "Administracion Avanzada de S.O", "Algoritmos y Estructuras de Datos II", "Legislacion y Organizaciones", "Optativa II", "Tesis de Licenciatura", "Certificacion Ingles"]
IngInf = ["Calculo I", "Algebra I", "Fisica 1", "Fundamentos de Quimica General", "Calculo II", "Algebra II", "Fisica II", "Informatica", "Sistemas de Representacion", "Calculo III", "Elementos de Computacion y Logica", "Fisica III", "Laboratorio I", "Calculo IV", "Probabilidad y Estadistica", "Laboratorio II", "Programacion", "Algoritmos y Estructuras de Datos I", "Arquitectura y Org I", "Taller de Lenguajes I", "Matematica Discreta", "Metodos Numericos", "Algoritmos y Estructuras de Datos II", "Bases de Datos I", "Paradigmas de la Programacion", "Taller de Lenguajes II", "Comunicaciones I", "Bases de Datos II", "Ingenieria de Software I", "Sistemas Operativos I", "Arquitectura y Org II", "Sistemas Operativos II", "Administracion de Proyectos", "Sistemas de Informacion", "Conceptos de Lenguajes", "Computacion Cientifica", "Administracion de Sistemas Operativos II", "Legislacion y Organizaciones", "Gestion Ambiental", "Practica Profesional Supervisada", "Proyecto Final", "Certificacion Ingles"]




def CompararMateriasInformatica():
	print("Cuando selecciones ambas carreras, se mostrarán las asignaturas que no estén en la primera")
	print("Elige la primera carrera para comparar")
	print("1. Programador Universitario")
	print("2. Licenciatura en Informática")
	print("3. Ingeniería en Informática")
	carrera1 = int(input())
	if carrera1 == 1:
		carr = programador
		materia1 = ProgU
		print("Tu primera carrera elegida es Programador Universitario")
	elif carrera1 == 2:
		carr = licinformatica
		materia1 = LicInf
		print("Tu primera carrera elegida es Licenciatura en Informática")
	elif carrera1 == 3:
		carr = inginformatica
		materia1 = IngInf
		print("Tu primera carrera elegida es Ingeniería en Informática")
	else:
		return("Carrera incorrecta")

	print("Elige la segunda carrera para comparar")
	print("1. Programador Universitario")
	print("2. Licenciatura en Informática")
	print("3. Ingeniería en Informática")

	carrera2 = int(input())
	if carrera2 == 1:
		carr2 = programador
		materia2 = ProgU
		print("Tu segunda carrera elegida es Programador Universitario")
	elif carrera2 == 2:
		carr2 = licinformatica
		materia2 = LicInf
		print("Tu segunda carrera elegida es Licenciatura en Informática")
	elif carrera2 == 3:
		carr2 = inginformatica
		materia2 = IngInf
		print("Tu segunda carrera elegida es Ingeniería en Informática")
	else:
		return("Carrera incorrecta")
	print("Las materias de la carrera", carr, "que no están en", carr2, "son:")
	for compara in materia1:
		if compara not in materia2:
			print(compara)


#Se ejecuta la función para comparar carreras de informática en la Facultad de Ciencias Exactas y Tecnología - UNT
CompararMateriasInformatica()



