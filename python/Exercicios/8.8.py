def make_album(nome,album,faixas=0):
	if faixas:
		artista={"nome_artista":nome,"album_artista":album,"numero_de_faixas":faixas}		
	else:
		artista={"nome_artista":nome,"album_artista":album}
	return artista
	
while 1:
	print("Digite 'q' a qualquer momento para sair")
	d=input("Nome do artista: ")
	if d=="q":
		break
	e=input("Albúm do artista: ")
	if d=="q":
		break
	h=input("Número de faixas do albúm: ")
	if d=="q":
		break
	g=make_album(d,e,h)
	print(str(g) + "\n")
