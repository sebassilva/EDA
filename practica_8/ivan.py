def binary(list_1):
 	binario = list()
 	binario = [list_1[0][0],None,list_1[0][1]]
 	print (binario)
 	for a in range(1,len(list_1)-2):
 	 		binario = [list_1[0][a], list_1[0][a+1], list_1[0][a+2]]
 			print (binario)

def main():
	print("-------------")
	print("n-tree")
	print("-------------")
	list_1 = [["a","b","c","d"],["b",None,None,None],["c","e",None,None],["d","f","g","h"]]
	for item in list_1:
		print(item)
	print("-------------")
	print("Binary tree")
	print("-------------")
	binary(list_1)
	#print(binary_tree)

main()
