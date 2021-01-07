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
		
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size=battery_size
			
	def describe_battery(self):
		print("Esse carro tem uma bateria de " + str(self.battery_size) + " kWH")
		
	def get_range(self):
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		
		print("Esse carro pode percorrer: " + str(range) + " milhas")
		
	def upgrade_battery(self):
		 if self.battery_size!=85:
			 self.battery_size=85

class EletricCar(Carro):
	
	def __init__(self,make,mode,year):
		super().__init__(make,mode,year)
		self.battery=Battery()

b=EletricCar("tesla","model s",2016)
b.battery.describe_battery()
b.battery.get_range()
b.battery.upgrade_battery()
b.battery.get_range()





