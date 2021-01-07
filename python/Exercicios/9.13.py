from collections import OrderedDict

dicionarios=OrderedDict()

dicionarios = {
	"while" : "loop",
	"dicionario" : "valores conectados",
	"for" : "loop",
	"print" : "printar",
	"scan" : "scanear",
	}

for dicionario, valores in dicionarios.items():
	print (dicionario.title() + " " + valores.title() + "\n")


