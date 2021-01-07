from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides=sides
		
	def roll_die(self):
		x=randint(1,self.sides)
		print(x)

a=Die()
i=10
while (i>0):
	a.roll_die()
	i=i-1
print("\n")

a=Die(10)
i=10
while (i>0):
	a.roll_die()
	i=i-1
print("\n")
