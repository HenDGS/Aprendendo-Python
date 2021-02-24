import json

def load_number():
	try:
		#a=open("number.json").read()
		#print(a)
		with open("number.json") as a:
			print(a.read())
	except FileNotFoundError:
		get_number()

def get_number():
	num=input("Número: ")
	with open("number.json","w") as obj:
		json.dump(num,obj)
		
load_number()
		
