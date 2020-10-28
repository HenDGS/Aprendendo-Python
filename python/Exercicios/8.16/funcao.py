def funcao(nome,fabricante,**carro):
	carros={}
	carros["nome"]=nome
	carros["fabricante"]=fabricante
	for key, value in carro.items():
		carros[key]=value
	return carros

