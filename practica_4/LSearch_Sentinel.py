def Lineal_Search(list_1,n,item):
	aux=list_1[n-1]
	list_1[n-1]=item
	k=0
	while list_1[k] != item:
		k=k+1

	list_1[n-1]=aux

	if k<n-1 or list_1[n-1] == item:
		print("Iteraciones ",k)
		return k
	else:
		return -1

def main():
	list_1=[1,2,3,4,5,6,7]
	item=5
	print("Posicion: ",Lineal_Search(list_1,len(list_1),item)+1)

main()