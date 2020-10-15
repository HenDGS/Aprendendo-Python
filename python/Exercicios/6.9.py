locais_ana=["grécia","roma"]
locais_joao=["irlanda","japão"]
locais_cesar=["russia","curitiba"]

favorite_places={"Ana" : locais_ana,"João" : locais_joao,"Cesar" : locais_cesar}


for place, k in favorite_places.items():
	print("O lugar favorito do(a) " + place.title() + " é: " + str(k).title())
