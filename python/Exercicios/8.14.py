def funcao(nome,fabricante,**carro):
	carros={}
	carros["nome"]=nome
	carros["fabricante"]=fabricante
	for key, value in carro.items():
		carros[key]=value
	return carros
	
a=funcao("camaro","Chevrolet",ano=2015,porência=461)
print(a)
