def bubbleSort(A):
    n = len(A)
    print("Numero de elementos de la lista: ", n)
    for i in range(0, n-1):
        print("Pasada ", i)
        for j in range(0, n-1):
            print(A)
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

lista = [3, 0, 2, 2, 6, 2, 9, 8]
print("Lista original")
print(lista)
print("Lista ordenada de mayor a menor")
print(bubbleSort(lista))
