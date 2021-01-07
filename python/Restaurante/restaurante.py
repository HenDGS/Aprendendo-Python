class Restaurante():
	def __init__(self,restaurante_nome,tipo):
		self.restaurante_nome=restaurante_nome
		self.tipo=tipo
	
	def describe_restaurant(self):
		print(self.restaurante_nome.title() + ", " + self.tipo.title())
	
	def abrir_restaurante(self):
		print("O restaurante está aberto!")


