try:
	nomes_gatos=open("cats.txt").read()
	nomes_cachorros=open("dogs.txt").read()
except FileNotFoundError:
	print("Arquivo não existe")
else:
	print(nomes_gatos + "\n" + nomes_cachorros)

