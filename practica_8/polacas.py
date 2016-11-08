class Vertice: 
	def __init__(self, value):
		self.value = value
		self.izq = None
		self.der = None

	def agregar(self, izq, der):
		if izq == None:
			self.izq = Vertice('0')
		else: 
			self.izq = izq
		if der == None:
			self.der = Vertice('0')
		else: 
			self.der = der





	def imprimir(self):
		print("Nodo: " + self.value)
		print("Izq: " + self.izq.value)
		print("Der: " + self.der.value + "\n")



def preorder(vertice):
	print (vertice.value)
	if vertice.izq.value != '0': 
		preorder(vertice.izq)

	if vertice.der.value != '0':
		preorder(vertice.der)


def inorder(vertice):
	if vertice.izq.value != '0': 
		inorder(vertice.izq)
	print (vertice.value)
	if vertice.der.value != '0':
		inorder(vertice.der)




def postorder(vertice):
	if vertice.izq.value != '0': 
		postorder(vertice.izq)
	if vertice.der.value != '0':
		postorder(vertice.der)

	print(vertice.value)





#CREANDO EL GRAFO
vA = Vertice('a')
vB = Vertice('b')
vC = Vertice('c')
vD = Vertice('d')
vE = Vertice('e')
vF = Vertice('f')
vG = Vertice('g')
vH = Vertice('h')
vI = Vertice('i')
vJ = Vertice('j')
vK = Vertice('k')


vA.agregar(vB, vC)
vB.agregar(vD, vE)
vC.agregar(None, vF)
vD.agregar(vG, None)
vE.agregar(vH, vI)
vF.agregar(vJ, vK)

#hojas
vG.agregar(None, None)
vH.agregar(None, None)
vI.agregar(None, None)
vJ.agregar(None, None)
vK.agregar(None, None)


print(".......Preorder.....")
preorder(vA)


print("......Inorder......")
inorder(vA)

print("...Postorder...")
postorder(vA)




