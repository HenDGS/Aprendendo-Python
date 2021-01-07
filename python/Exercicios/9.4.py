class Restaurante():
	def __init__(self,restaurante_nome,tipo,number_served=0):
		self.restaurante_nome=restaurante_nome
		self.tipo=tipo
		self.number_served=number_served
		
	def set_number_served(self,value):
		self.number_served=value
		
	def increment_number_served(self,value):
		self.number_served+=value
	
	def describe_restaurant(self):
		print(self.restaurante_nome + " " + self.tipo)
		if self.number_served:
			print("Clientes servidos = " + str(self.number_served))
	
	def abrir_restaurante(self):
		print("O restaurante está aberto!")
		
	
a=Restaurante("Mannus","normal",20)

a.describe_restaurant()

a.set_number_served(5)

print("\n")

a.describe_restaurant()

a.increment_number_served(5)

print("\n")

a.describe_restaurant()

