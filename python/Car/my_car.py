#from car import Carro, EletricCar
import car

a=car.Carro("tesla","model s",2016)
a.descricao()
a.odometer_reading=43
a.read_odometer()
print()
b=car.EletricCar("audi","a4",2018)
b.descricao()
b.battery.describe_battery()
b.battery.get_range()
