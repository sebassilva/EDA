class Vertice:
	def __init__(self,n):
		self.nombre = n
		self.vecinos = list()

		self.d = 0
		self.f = 0
		self.color = "white"
		self.pred = -1

	def agregarVecino(self, v):
		if v not in self.vecinos:
			self.vecinos.append(v)
			self.vecinos.sort()

class Graph:
	vertices = {}
	tiempo = 0

	def agregarVertice(self,vertice):
		if isinstance (vertice, Vertice) and vertice.nombre not in self.vertices:
			self.vertices[vertice.nombre] = vertice
			return True
		else:
			return False

	def agregarArista(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.agregarVecino(v)

			return True

		else:

			return False

	def imprimeGrafo(self):
		for key in sorted(list(self.vertices.keys())):
			print("Vertice: "+str(key)+ " descubierto/termino: "+ str(self.vertices[key].d)+" / "+str(self.vertices[key].f))

	def dfs(self):
		global tiempo
		tiempo = 0
		for u in sorted(list(self.vertices.keys())):
			if self.vertices[u].color == "white":
				self.dfsVisitar(self.vertices[u])

	def dfsVisitar(self,vert):
		global tiempo
		tiempo=tiempo+1
		vert.d = tiempo
		vert.color = "gris"

		for v in vert.vecinos:
			if self.vertices[v].color == 'white':
				self.vertices[v].pred=vert
				self.dfsVisitar(self.vertices[v])
				print(vert)
		vert.color = "black"
		tiempo= tiempo + 1
		vert.f=tiempo
		




v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
v4 = Vertice(4)


graph = Graph()
graph.agregarVertice(v1)
graph.agregarVertice(v2)
graph.agregarVertice(v3)
graph.agregarVertice(v4)


graph.agregarArista(v1, v2)
graph.agregarArista(v1, v3)
graph.agregarArista(v3, v4)
graph.dfs()
graph.imprimeGrafo()


