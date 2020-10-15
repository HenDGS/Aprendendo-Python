numeros = {
	"Henrique" : [5,10],
	"Clara" : [2,4],
	"Guilherme" : [3,6],
	"Pai" : [5,10],
	"Mãe" : [1,2],
	}
	
for numero, x in numeros.items():
	print("Os números favoritos do(a) " + numero + " são: ")
	for y in x:
		print(y)
