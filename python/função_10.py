def pizza (tamanho,*ingredientes): 
	print ("Fazendo uma pizza tamanho " + str(tamanho) + ", com os seguintes ingredientes: ")
	for ingrediente in ingredientes:
		print(ingrediente)

pizza(10,"queijo","tomate","carne")
