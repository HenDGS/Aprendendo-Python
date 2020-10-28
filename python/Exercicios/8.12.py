def funcao(*ingredientes):
	print("Os ingredientes são: " + str(ingredientes))
	for ingrediente in ingredientes:
		print(ingrediente)
	print("\n")
	
funcao("queijo")
funcao("pao","maconha","carne")
funcao("pipoca","doritos","coca","agua")
