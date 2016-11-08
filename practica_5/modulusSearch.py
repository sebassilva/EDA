from random import randrange

def createRandomArray(size):
	randomArray = []
	for k in range(0, size):
		randomArray.append(randrange(1000000000))
	return randomArray

def modulusHash(A):
	colisions = 0
	hashedArray = [0]*len(A) #Crea un nuevo arreglo relleno de ceros
	for k in range (0, len(A)-1):
		mod = A[k] % len(A)
		if (hashedArray[mod] != 0):
			colisions += 1
		else: 
			hashedArray[mod] = A[k]


	return hashedArray, colisions


def squareCenter(A):
	colisions = 0
	hashedArray = [0]*len(A) #Crea un nuevo arreglo relleno de ceros
	for k in range (0, len(A)-1):
		sq = str(A[k] * A[k])	
		center = int(len(sq)/2) #Calcula el centro del cuadrado
		sq = int(sq[center: center+2])
		if (hashedArray[sq] != 0):
			colisions +=1
		else: 
			hashedArray[sq] = A[k]
	return hashedArray, colisions

def selection(A): 
	colisions = 0
	hashedArray = [0]*len(A) #Crea un nuevo arreglo relleno de ceros
	for k in range (0, len(A)-1):
		d = str(A[k])
		print(d)
		d = d[0] + d[len(d)-1]
		digits = int(d)		
		if (hashedArray[digits] != 0):
			colisions +=1
		else: 
			hashedArray[digits] = A[k]
	return hashedArray





A = createRandomArray(100)
orderedA = squareCenter(A)
print("Arreglo sin ordenar: ")
print(A)
print("Arreglo Ordenado: ")
print(orderedA[0])
print("Colisiones: ", orderedA[1])	





