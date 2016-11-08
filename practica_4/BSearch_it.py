import math
def Binary_Search(list_1,item,izq,der):
	x=0
	while izq <= der:
		medio= int((izq+der)/2)
		if list_1[medio] == item:
			print("Iteraciones: ",x)
			print("Posicion: ", medio+1 )
			return medio
		elif list_1[medio] < item:
			izq = medio +1
		else:
			der = medio-1
	x=x+1
	return -1

def main():
	list_1=[1,2,3,4,5,6,7,8]
	item=5
	size= len(list_1)
	Binary_Search(list_1,item,0,size)

main()