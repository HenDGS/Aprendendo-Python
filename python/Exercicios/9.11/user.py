class User():
	def __init__(self,first_name,last_name,idade=0,login_attempts=0):
		self.first_name=first_name
		self.last_name=last_name
		self.idade=idade
		self.login_attempts=login_attempts
	
	def describe_user(self):
		print("O seu primeiro nome é: " + self.first_name.title() + "\n" + "O seu sobrenome é: " + self.last_name.title())
		if (self.idade):
			print("Sua idade é: " + str(self.idade))
	
	def greet_user(self):
		print("Olá " + self.first_name.title() + "\n")
	
	def increment_login_attempts(self):
		self.login_attempts+=1
		
	def reset_login_attempts(self):
		self.login_attempts=0
			
class Privileges():
	def __init__(self,privileges=("can add post","can delete post","can ban user")):
		self.privileges=privileges
	
	def show_privileges(self):
		for privilige in self.privileges:
			print (privilige.title())

class Admin (User):
	def __init__(self,first_name,last_name,idade=0,login_attempts=0):
		super().__init__(first_name,last_name,idade=0,login_attempts=0)
		self.pri=Privileges()

