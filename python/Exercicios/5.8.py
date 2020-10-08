usuarios=["henrique","clara","guilherme","admin","pedro"]

for usuario in usuarios:
	if (usuario=="admin"):
		print("Olá admin, gostaria de um relatorio?")
	else :
		print(usuario.title() + ", bom dia!")

