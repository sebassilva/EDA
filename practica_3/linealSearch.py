def linearSearch(A, item):
	for i in range(0, len(A)): 
		if A[i] == item: 
			return i
	return False



Lista = ['hola', 'como', 'estas', 'she', 'said', 'konichiwa']
print(linearSearch(Lista, 'hola'))
