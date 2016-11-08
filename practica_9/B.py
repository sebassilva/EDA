class B:
	def __init__(self, *values):
		self.children = list()	#Creates list of children, instances of B
		self.values = list()
		for value in values: 
			self.values.append(value)

	def addChildren(self, *children):
		for child in children:
			self.children.append(child)

	def printValues(self):
		vals = list()	#creates an array for displaying it
		for value in self.values:
			vals.append(value)	#Ads every child`s value to array
		print(vals)


	def printFirst(self):
		print(self.values[0])


	def printChildren(self):
		for child in self.children: #Iterates over its children
			child.printValues()
			print("\n")

	def getChildren(self):
		return self.children

v1 = B(25)
v2 = B(5, 10, 15, 20)
v3 = B(30, 35, 40, 45)
v4 = B(1, 2, 3, 4)
v5 = B(11, 13, 14)
v6 = B(21, 22, 23)
v7 = B(26, 27, 28)
v8 = B(36, 37, 38, 39)
v9 = B(46, 47, 48, 49)
v10 = B(6, 7, 8, 9)
v11 = B(16, 18, 19)

v12 = B(31, 32, 33, 34)
v13 = B(41, 43, 44)

v1.addChildren(v2)
v1.addChildren(v3)

v2.addChildren(v4)
v2.addChildren(v5)
v2.addChildren(v6)
v2.addChildren(v10)
v2.addChildren(v11)

v3.addChildren(v7)
v3.addChildren(v8)
v3.addChildren(v9)
v3.addChildren(v12)
v3.addChildren(v13)

aux = list()
queue = list()


def DFS(node):
	queue.append(node)
	node = queue.pop()
	aux.append(node.values)
	v = node.getChildren()
	for child in v:
		if child not in aux and child not in queue:
			queue.append(child)
	if len(queue) > 0:
		DFS(queue.pop(0))
	return aux



print(DFS(v1))
# for a in aux:
# 	print(a.printChildren())









