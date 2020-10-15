cities = {
	"curitiba" : {
		"country" : "Brazil",
		"population" : 2000000,
		"fact" : "Eu moro aqui",
		},
	"são paulo" : {
		"country" : "Brazil",
		"population" : 13000000,
		"fact" : "Maior cidade",
		},
	"maringa" : {
		"country" : "Brazil",
		"population" : 342000,
		"fact" : "Tenho parentes aqui",
		},
	}

for x, y in cities.items():
	print("Cidade: " + x.title() + "\nPaís: " + y["country"] + "\nPopulação: " + str(y["population"]) + "\nFato: " + y["fact"] + "\n")

