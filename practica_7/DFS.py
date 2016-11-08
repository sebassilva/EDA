A = [['a', 'b'], 
	['a', 'c'], 
	['a', 'd'],

	['b', 'a'], 
	['b', 'c'], 
	['b', 'd'], 

	['c', 'a'], 
	['c', 'b'],
	['c', 'd'], 
	['c', 'e'],
	['c', 'f'],

	['d', 'a'], 
	['d', 'c'],
	['d', 'f'],

	['e', 'b'],
	['e', 'c'],
	['e', 'f'], 

	['g', 'e'], 
	['g', 'f']
]

lista = []
aux = []
def N(A, node): 
	nArray = []
	for i in range(0, len(A)):
		if A[i][0] == node:
			nArray.append(A[i][1])
	return nArray


def deleteN(vecino):
	for i in range (0, len(lista)-1):
		if ve
		cino == lista[i]:
			popeado = lista.pop(i)
			print("Repetido: " + str(popeado))

def DFS(A, node):
	lista.append(node)
	print("Lista1: " + str(node))
	iteracion = 0
	while len(lista) != 0: 
		print("Iteracion ................... " + str(iteracion))
		valor = lista.pop()
		aux.append(valor)
		#Si no estan en el auxiliar, meterlos a la lista aunque esten repetidos
		print("Valor: " + str(valor))
		vecinos = N(A, valor)
		print("vecinos: " + str(vecinos))
		for vecino in vecinos:
			print("vecino: " +str(vecino))
			existeEnAux = False
			for i in range(0, len(aux)):
				if vecino == aux[i]:
					existeEnAux = True
			if existeEnAux == False:
				deleteN(vecino)
				lista.insert(0, vecino)
				print("Vecino to append: " + str(vecino))
				print("Lista after append: " + str(lista))
				print("Aux: " + str(aux))
		iteracion = iteracion + 1





DFS(A, 'a')