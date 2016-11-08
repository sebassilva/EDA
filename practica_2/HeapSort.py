import math

def hIzq(i):
	return 2*i

def hDer(i):
	return 2*i+1

def Exchange (lista,x,y):
	aux = lista[x]
	lista[x] = lista[y]
	lista[y] = aux

def MaxHeapify(lista,i,size_hip):
	L=hIzq(i)
	R=hDer(i)
	if (L <= size_hip and lista[L] < lista[i]):
		posMax = L
	else:
		posMax = i

	if (R <= size_hip and lista[R] < lista[posMax]):
		posMax = R
	if (posMax != i):
		Exchange(lista,i,posMax)
		MaxHeapify(lista,posMax,size_hip)

def BuildHeapMaxIni(lista,size_hip):
	for i in range(int(math.ceil(size_hip/2)),0,-1):
		MaxHeapify(lista,i,size_hip)

def HeapSort(lista,size_hip):
	BuildHeapMaxIni(lista,size_hip)
	for i in range (len(lista[1:]),1,-1):
		Exchange(lista,1,i)
		size_hip = size_hip - 1
		MaxHeapify(lista,1,size_hip)

def main():
	lista=[0,8,9,7,5,6,4]
	print(lista)
	HeapSort(lista,len(lista)-1)
	print(lista)

main()

