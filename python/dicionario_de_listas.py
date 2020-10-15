pizza = {
		"borda" : "fina",
		"ingredientes" : ["queijo","frango"]
		}

print ("Você pediu uma pizza com a borda " + pizza["borda"] + ". E com esses ingredientes: " + str(pizza["ingredientes"]))

for ingrediente in pizza["ingredientes"]:
	print (ingrediente)
