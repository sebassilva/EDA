def BinarySearch(A, item, start, end): 
	if start > end: 
		print("False")
		return False
	center = int((end-start)/2) + start
	print("center", center)
	print("start", start)
	print("end", end)
	if A[center] == item: 
		print(center)
		print("A es igual a center")
		# print (center)
		return center + 1
	else: 
		if item < A[center]:
			BinarySearch(A, item, center+1, end)
		else: 
			BinarySearch(A, item, start, center-1)




Lista = [1, 5, 6, 3, 4, 7, 5, 4, 3]
index = BinarySearch(Lista, 4, 0, len(Lista))
