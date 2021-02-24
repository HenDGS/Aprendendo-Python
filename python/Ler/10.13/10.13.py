import json

def get_new_name():
	a=open("nome.json","w")
	nome=input("Qual é o seu nome? ")
	json.dump(nome,a)

def get_name():
	try:
		a=open("nome.json").read()
	except FileNotFoundError:
		return None
	else:
		return a


def greet_user(b):
	if b:
		a=input(b + " Esse é o seu nome? ")
		if a=="yes":
			print(b.title())
		else:
			get_new_name()
	else:
		nome=input("Qual é o seu nome? ")
		with open("nome.json","w") as f_obj:
			json.dump(nome,f_obj)
	
greet_user(get_name())

