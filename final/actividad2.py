def createArray():
    #Lee el archivo lineas.txt y lo pasa a un arreglo
    lineasMetro = list()
    with open('lineas.txt') as f:
        for line in f:
            line = line.splitlines()
            if(line != ['']): #ignora los espacios en blanco
                lineasMetro.append(line[0].split(',')) #crea la lista de listas 
    return lineasMetro


#BubbleSort Optimizado
def bubbleSortOptimized(A):
    n = len(A)
    i = 1
    comparaciones = 0
    flag = True
    print("Numero de elementos de la lista: ", n)
    while i < n-1 and flag:
        flag = False
        print "Pasada: " + str(i)
        for j in range(0, n-i):
            print(A)
            comparaciones += 1
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = True
        i+=1
    print("comparaciones: ", comparaciones)
    print("iteraciones: ", i-1)
    return A

def save(A):
    archivo = open("lista.txt", "w")
    for linea in A:
        archivo.write(linea + "\n")
    archivo.close()





def actividad2():
    lista = ["ivan", "eres", "un", "palabras", "al", "azar"]
    listaOrdenada = bubbleSortOptimized(lista)
    save(listaOrdenada)
    print "Lista ordenada: " + str(listaOrdenada)

actividad2()

