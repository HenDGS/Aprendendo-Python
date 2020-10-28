respostas={}

booleano=True

while booleano:
	nome = input("Qual é o seu nome? ")
	resposta = input("Qual é o seu animal favorito? ")
	respostas[nome]=resposta
	
	a=input("Vai deixar outra pessoas responder? (sim / não) ")
	if a=="não":
		booleano=False
		
for x, y in respostas.items():
	print ("O animal favorito do(a) " + x.title() + " é o " + y)
