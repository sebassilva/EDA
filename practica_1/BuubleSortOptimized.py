#BubbleSort Optimizado
def bubbleSortOptimized(A):
    n = len(A)
    i = 1
    flag = True
    print("Numero de elementos de la lista: ", n)
    while i < n-1 and flag:
        flag = False
        print "Pasada: " + str(i)
        for j in range(0, n-i-1):
            print(A)
            if A[j] < A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = True
        i+=1

    return A


lista = [3, 0, 2, 2, 6, 2, 9, 8]
listaOrdenada = bubbleSortOptimized(lista)
print "Lista ordenada: " + str(listaOrdenada)

