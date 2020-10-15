pessoa_1 = {
	"first_name" : "Henrique",
	"last_name" : "Saczkowski",
	"Cidade" : "Curitiba",
	}

pessoa_2 = {
	"first_name" : "Guilherme",
	"last_name" : "Saczkowski",
	"Cidade" : "Curitiba",
	}

pessoa_3 = {
	"first_name" : "Clara",
	"last_name" : "Saczkowski",
	"Cidade" : "Curitiba",
	}

pessoas=(pessoa_1,pessoa_2,pessoa_3)

for p in pessoas:
	print("Nome: " + p["first_name"])
	print("Sobrenome: " + p["last_name"])	
	print("Cidade: " + p["Cidade"] + "\n")			

