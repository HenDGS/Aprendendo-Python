from user import *

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
