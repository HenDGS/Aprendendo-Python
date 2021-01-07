class Restaurante():
	def __init__(self,restaurante_nome,tipo):
		self.restaurante_nome=restaurante_nome
		self.tipo=tipo
	
	def describe_restaurant(self):
		print(self.restaurante_nome + " " + self.tipo)
	
	def abrir_restaurante(self):
		print("O restaurante está aberto!")
	
a=Restaurante("Mannus","normal")
b=Restaurante("Predileta","pizzaria")
c=Restaurante("Madero","hamburgueria")

a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()


