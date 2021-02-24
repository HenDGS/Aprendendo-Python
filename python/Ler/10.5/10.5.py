f=open("nome.txt","r+")
	
b=True

while b:
	nome=input("Qual o seu nome? ")
	if (nome=="end"):
		b=False
		break
	respota=input("Pq vc gosta de programação? ")
	f.write(nome.title() + " : " + respota + "\n")
	




