nome=input("Qual é o seu nome? ")

with open("nome.txt","w") as file_object:
	file_object.write(nome.title())
