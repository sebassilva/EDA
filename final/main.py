def createArray():
	#Lee el archivo lineas.txt y lo pasa a un arreglo
	lineasMetro = list()
	with open('lineas.txt') as f:
	    for line in f:
	    	line = line.splitlines()
	    	if(line != ['']): #ignora los espacios en blanco
	    		lineasMetro.append(line[0].split(',')) #crea la lista de listas 
	return lineasMetro

def BPA(list_1,char):
	Queue=[char]
	list_BPA=[]
	while len(list_BPA) != len(list_1):
		char = Queue.pop(0)
		list_aux=partner(list_1,char)
		list_BPA.append(char)
		boolean=1
		for item in list_aux:
			for item_2 in list_BPA:
				if(item == item_2):
					boolean = 0
			if (boolean == 1):
				Queue.append(item)
				print(item)
	return list_BPA

def partner(list_1,char):
	list_partner=[]
	for i in range(0,len(list_1)-1):
		for j in range (0,1):
			if(char == list_1[i][0]):
				list_partner.append(list_1[i][1])
	return list_partner

def actiivdad1():
	lineasMetro = createArray()
	#print(lineasMetro)
	for linea in lineasMetro:
		print(linea)
	list_BPA=BPA(lineasMetro,"balderas")
	#print(algo)

#BubbleSort Optimizado
def bubbleSortOptimized(A):
    n = len(A)
    i = 1
    flag = True
    print("Numero de elementos de la lista: ", n)
    while i < n-1 and flag:
        flag = False
        print "Pasada: " + str(i)
        for j in range(0, n-i):
            print(A)
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = True
        i+=1

    return A









def actividad2():
	lista = ["ivan", "eres", "un", "palabras", "al", "azar"]
	listaOrdenada = bubbleSortOptimized(lista)

	print "Lista ordenada: " + str(listaOrdenada)

actividad2()











