#open ("a.txt") as nomes:
arquivo="a.txt"
try:
	nomes=open(arquivo)
except:
	print("Erro")
else:
	conteúdo=nomes.read()
	quantidade=conteúdo.split()
	quan=len(quantidade)
	print("O arquivo " + arquivo + " tem " + str(quan) + " palavras")
