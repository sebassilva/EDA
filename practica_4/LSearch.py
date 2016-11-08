def Lineal_Search(list_1,n,item):
	flag=-1
	for k in range(0,n-1):
		if list_1[k] == item:
			found=k
			print("Iteraciones: ",k)
	return found

def main():
	list_1=[1,2,3,4,5,6,7]
	item=5
	print("Posicion: ",Lineal_Search(list_1,len(list_1),item)+1)

main()