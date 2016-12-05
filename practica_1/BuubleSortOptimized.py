#BubbleSort Optimizado
def BubbleSort(A):
    n = len(A)
    i = 1
    flag = True
    print("Numero de elementos de la lista: ", n)
    while i < n-1 and flag:
        flag = False
        print "Pasada: " + str(i)
        for j in range(0, n-i-1):
            print(A)
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = True
        i+=1

    return A


lista = ["balderas", "cuauhtemc", "juarez", "hidalgo", "ninosheroes"]
listaOrdenada = BubbleSort(lista)
print "Lista ordenada: " + str(listaOrdenada)

