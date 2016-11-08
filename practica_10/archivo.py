#-*-coding: utf-8 -*-
#Crear un archivo y escribir hola
archivo = open("archivo.txt", "w")
archivo.write("Hola")
archivo.close()
#Crear un archivo manualmente y leerlo desde python	
archivo2 = open("amigo.txt", "r")
print(archivo2.read())
archivo.close()

#Crear un arhivo y que python lea su contenido
archivoe = open("suma.txt", "r")
content = archivoe.readline()
content = content.split(",")
suma = 0
for nums in content:
	suma += int(nums)
print (suma)
archivoe.close()

def N(A, node): 
	nArray = []
	for i in range(0, len(A)):
		if A[i][0] == node:
			nArray.append(A[i][1])
	return nArray

def createNodeFromFile(file):
	lista = list()
	with open(file) as f:
		for line in f.read().splitlines():
			lista.append(line.split(" "))
	return lista

#4 Leer la representación 
node = createNodeFromFile("grafo.txt")
print(N(node, 'a'))

