def nome_completo(primeiro,sobrenome,meio=""): #Retorna o nome completo
	if meio:
		return (primeiro.title() + " " + meio.title() + " " + sobrenome.title())
	else:
		return (primeiro.title() + " " + sobrenome.title())
	
while 1:
	print("Diga o seu nome")
	print("Digite 'q' a qualquer momento para sair")
	
	primeiro=input("Seu primeiro nome ")
	if primeiro=="q":
		break
	sobrenome=input("Seu sobrenome ")
	if sobrenome=="q":
		break
	a=nome_completo(primeiro,sobrenome)
	print(a + "\n")

