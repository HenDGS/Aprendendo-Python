def nome_completo(primeiro,sobrenome,meio=""): #Retorna o nome completo
	if meio:
		return (primeiro.title() + " " + meio.title() + " " + sobrenome.title())
	else:
		return (primeiro.title() + " " + sobrenome.title())
	
a=nome_completo("henrique","saczkowski")
print(a)
a=nome_completo("henrique","saczkowski",meio="da gama")
print(a)

