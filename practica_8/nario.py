class Vertice: 
	def __init__(self, value):
		self.value = value
		self.childList = list()


	def agregar(self, *childs):
		for child in childs: 
			self.childList.append(child)


	def imprimir(self):
		print("Nodo: " + self.value)
		print("hijos")
		for child in self.childList: 
			print(child.value)



class VerticeBinario: 
	def __init__(self, value):
		self.value = value
		self.child = None
		self.bro = None

	def addChild(self, child):
		if child == None: 
			self.child = VerticeBinario('0')
		else:
			self.child = child
	def addBro(self, bro):
		if bro == None: 
			self.bro = VerticeBinario('0')
		else:
			self.bro = bro
	def printNode(self):
		print("Node: " + self.value)
		print("Child: " + self.child.value)
		print("Bro: " + self.bro.value + "\n")



#binVertice = VerticeBinario(vertice.value)

def getLast(vertice):
	if (vertice.child != None):
		getLast(vertice.child)
	else:
		return vertice







def bin(vertice):
	binVertice = VerticeBinario(vertice.value)
	vertice = getLast(binVertice)
	print("VERTICE: " + vertice.value)



	# binVertice = VerticeBinario(vertice.value)
	# if len(vertice.childList) > 0:
	# 	binVertice.addChild(vertice.childList[0])
	# 	for a in range(1, len(vertice.childList)-1):
	# 		binVertice.addBro(VerticeBinario(vertice.childList[a].value))
	# 		binVertice.printNode()


vA = Vertice('a')
vB = Vertice('b')
vC = Vertice('c')
vD = Vertice('d')
vE = Vertice('e')
vF = Vertice('f')
vG = Vertice('g')
vH = Vertice('H')



vA.agregar(vB, vC, vD)
vC.agregar(vE)
vD.agregar(vF, vG, vH)
bin(vA)