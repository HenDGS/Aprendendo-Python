f=open("nome.txt","r+")
	
b=True

while b:
	nome=input("Qual o seu nome? ")
	if (nome=="end"):
		b=False
		break
	f.write(nome.title() + "\n")
	



