class Pila:
	lista=[]
	tope=0
	def inicializar(self):
		self.lista=[]
		self.lista.append('Z0')
		self.tope=self.tope+1

	def push (self):
		self.lista.insert(self.tope-1, 'X')
		self.tope= self.tope+1

	def pop (self):
		del self.lista[0]
		self.tope=self.tope-1

