class Restaurante():
	def __init__(self,restaurante_nome,tipo):
		self.restaurante_nome=restaurante_nome
		self.tipo=tipo
	
	def describe_restaurant(self):
		print(self.restaurante_nome + " " + self.tipo)
	
	def abrir_restaurante(self):
		print("O restaurante está aberto!")
	
a=Restaurante("Mannus","normal")
print(a.restaurante_nome + " " + a.tipo)

a.describe_restaurant()

a.abrir_restaurante()

class IceCreamStand (Restaurante):
	
	def __init__(self,restaurante_nome,tipo):
		super().__init__(restaurante_nome,tipo)
		self.flavors=("chocolate","creme","napolitano")

	def sabores(self):
		for sabor in self.flavors:
			print (sabor.title())
		
a=IceCreamStand("Mannus","normal")
a.sabores()
