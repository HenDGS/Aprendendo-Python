def show_magicians(magos):
	for mago in magos:
		print (mago.title())

def make_great(magia):
	for magi in magia:
		magia[magia.index(magi)]="O Grande " + magi
	return magia
		

lista=["ana","henrique","zeus"]
lista_nova=make_great(lista[:])
show_magicians(lista)
print("\n")
show_magicians(lista_nova)


