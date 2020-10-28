ferias={}

while True:
	nome=input("Qual é o seu nome? ")
	lugar=input("Qual local vc gostaria de visitar nas suas férias? ")
	ferias[nome]=lugar	
	x=input("Mais alguém vai responder? (s/n) ")
	if x=="n":
		break

print(ferias)
