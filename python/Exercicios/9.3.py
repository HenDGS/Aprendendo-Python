class User():
	def __init__(self,first_name,last_name,idade=0):
		self.first_name=first_name
		self.last_name=last_name
		self.idade=idade
	
	def describe_user(self):
		print("O seu primeiro nome é: " + self.first_name.title() + "\n" + "O seu sobrenome é: " + self.last_name.title())
		if (self.idade):
			print("Sua idade é: " + str(self.idade))
	
	def greet_user(self):
		print("Olá " + self.first_name.title() + "\n")
		
a=User("Henrique","da gama saczkowski",21)
a.describe_user()
a.greet_user()

b=User("clara","da gama saczkowski",16)
b.describe_user()
b.greet_user()

c=User("joãozinho","costa")
c.describe_user()
c.greet_user()


