def Lineal_Search(list_1,item,ini,end):
	if ini>end:
		found = -1
	else:
		if list_1[ini] == item:
			found= ini
			print("Iteraciones ",ini)
			print ("posicion: ",ini+1)
		else:
			found = Lineal_Search(list_1,item,ini+1,end)


def main():
	list_1=[1,2,3,4,5,6,7]
	item=5
	Lineal_Search(list_1,item,0,len(list_1)+1)

main()