import json

def get_name():
	try:
		a=open("nome.json").read()
	except FileNotFoundError:
		return None
	else:
		return a


def greet_user(b):
	if b:
		print(b.title())
	else:
		nome=input("Qual é o seu nome? ")
		with open("nome.json","w") as f_obj:
			json.dump(nome,f_obj)
	
greet_user(get_name())
