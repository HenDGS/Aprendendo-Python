ingresso=0

print("Digite a idade e 'quit' para sair")

while True:
	idade=input()
	if idade=="quit":
		break
	elif int(idade)<3:
		ingresso+=0
	elif int(idade)<12:
		ingresso+=10
	else:
		ingresso+=15

print("O preço dos ingressos ficou em: " + str(ingresso))
	
