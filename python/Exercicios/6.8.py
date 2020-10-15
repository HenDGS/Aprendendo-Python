Bob = {
	"tipo" : "cachorro",
	"dono" : "joao",
	}

Thor = {
	"tipo" : "cachorro",
	"dono" : "henrique",
	}

Zeus = {
	"tipo" : "gato",
	"dono" : "daniel",
	}	

Odin = {
	"tipo" : "cavalo",
	"dono" : "ana",
	}	

pets=(Bob,Thor,Zeus,Odin)

for pet in pets:
	print("Tipo: " + pet["tipo"])
	print("Dono: " + pet["dono"] + "\n")
