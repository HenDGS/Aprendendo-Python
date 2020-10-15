rios={"nilo" : "egito", "amazonas" : "brasil", "parana" : "parana"}

for rio, pais in rios.items():
	print("O " + rio.title() + " corre pelo " + pais.title())
	
print("\n")
	
for rio in rios.keys():
	print(str(rio.title()))
	
print("\n")
	
for rio in rios.values():
	print(str(rio.title()))
