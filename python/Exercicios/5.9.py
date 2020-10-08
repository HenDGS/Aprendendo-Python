usuarios=["henrique","clara","guilherme","admin","pedro"]

if usuarios:
	for usuario in usuarios:
		if (usuario=="admin"):
			print("Olá admin, gostaria de um relatorio?")
		else :
			print(usuario.title() + ", bom dia!")
else:
	print ("Preciamos encontrar alguns usuários")


