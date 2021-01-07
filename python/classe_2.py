class Cachorro():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def sit(self):
		print(self.name.title() + " está sentando.")
	
	def roll_over(self):
		print(self.name.title() + " rolou!")
		
a=Cachorro("bob",6)
print(a.name.title())
a.sit()
a.roll_over()
print("\n")
b=Cachorro("Thor",5)
b.sit()
