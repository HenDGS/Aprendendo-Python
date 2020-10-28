def show_magicians(magos):
	for mago in magos:
		print (mago.title())

def make_great(magia):
	for magi in magia:
		magia[magia.index(magi)]="O Grande " + magi
		

lista=["ana","henrique","zeus"]
make_great(lista)
show_magicians(lista)

