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
vA = Vertice('+')
vB = Vertice('*')
vC = Vertice('-')
vD = Vertice('4')
vE = Vertice('2')
vF = Vertice('6')
vG = Vertice('4')



vA.agregar(vB, vC)
vB.agregar(vD, vE)
vC.agregar(vF, vG)


#hojas
vF.agregar(None, None)
vG.agregar(None, None)
vD.agregar(None, None)
vE.agregar(None, None)




print(".......Prefija.....")
preorder(vA)


print("......Infija......")
inorder(vA)

print("...Posfija...")
postorder(vA)




