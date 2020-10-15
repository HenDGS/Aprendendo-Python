usuarios = {
	"henrique" : {
		"primeiro" : "henrique",
		"ultimo" : "saczkowski",
		"local" : "curitiba",
		},
	"brenny" : {
		"primeiro" : "felipe",
		"ultimo" : "brenny",
		"local" : "sp",
		},
	}

for nome, info in usuarios.items():
	print("Username: " + nome.title() + "\n    Nome completo: " + info["primeiro"].title() + " " + info["ultimo"].title() + "\n    Local: " + info["local"].title() + "\n")

