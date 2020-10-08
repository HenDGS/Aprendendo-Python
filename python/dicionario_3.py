pessoas = {
	"Clara" : "Rubi",
	"Guilherme" : "C++",
	"Iuri" : "Java",
	"Henrique" : "Python",
	}

for keys in pessoas:
	print (keys)
	
print("\n")
	
for keys in pessoas.keys():
	if keys=="Henrique":
		print(keys + ", você está certo, " + pessoas[keys] + " realmente é a melhor linguagem")
	else:
		print (keys)
	
	
if "Brenny" not in pessoas.keys():
	print("\nBrenny, responda a enquete!")
	
		


