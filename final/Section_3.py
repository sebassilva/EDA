def Read():
	file_=open("list.txt","r")
	content = file_.read()
	content = content.split("\n")
	file_.close()
	return content

def BinarySearch(A, item, start, end,i): 
	if start > end: 
		print("Comparaciones:",i)
		return False

	center = int((end-start)/2) + start

	if A[center] == item:
		print("Comparaciones:",i)
		return center + 1
	else: 
		if item > A[center]:
			aux=BinarySearch(A, item, center+1, end,i+1)
		else: 
			aux=BinarySearch(A, item, start, center-1,i+1)

	return aux

Lista = Read()
i=0
index = BinarySearch(Lista,"conade",0,len(Lista),i)
if index != False:
	print ("Posicion:" ,index)
else:
	print ("El elemento no se encuentra en la lista")