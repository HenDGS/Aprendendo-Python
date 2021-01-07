class Carro():
	def __init__(self,make,mode,year):
		self.make=make
		self.mode=mode
		self.year=year
		self.odometer_reading=0

	def descricao(self):
		print(self.make.title() + " " + self.mode.title() + ", " + str(self.year))
		
	def read_odometer(self):
		print(self.odometer_reading)

a=Carro("audi","a4",2016)
a.descricao()
a.odometer_reading=10
a.read_odometer()		
