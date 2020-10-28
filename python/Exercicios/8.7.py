def make_album(nome,album,faixas=0):
	if faixas:
		artista={"nome_artista":nome,"album_artista":album,"numero_de_faixas":faixas}		
	else:
		artista={"nome_artista":nome,"album_artista":album}
	return artista
	
a=make_album("nirvana","rape me")
print(a)

	
a=make_album("mettalica","sandman",10)
print(a)
