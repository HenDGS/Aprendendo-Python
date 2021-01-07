with open('pi.txt') as file_object:
	linhas=file_object.readlines()
	
print(linhas)

print("\n")

for linha in linhas:
	print(linha.rstrip()) #Sem pular linha
	
print("\n")
	
espaço= ""

for linha in linhas:
	espaço+=linha.rstrip()

print(espaço)
