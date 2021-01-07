class Carro():
	def __init__(self,make,mode,year):
		self.make=make
		self.mode=mode
		self.year=year
		self.odometer_reading=5

	def descricao(self):
		print(self.make.title() + " " + self.mode.title() + ", " + str(self.year))
		
	def update_odomter(self,value):
		if value>=self.odometer_reading:
			self.odometer_reading=value
		else:
			print("Não tenta falsificar essa merda")
		
	def incrementar_odometro(self,value):
		if value<0:
			print("Vtnc")
		else:
			self.odometer_reading+=value
		
	def read_odometer(self):
		print(self.odometer_reading)

a=Carro("audi","a4",2016)
a.descricao()
a.update_odomter(10)
a.incrementar_odometro(20)
a.read_odometer()		

