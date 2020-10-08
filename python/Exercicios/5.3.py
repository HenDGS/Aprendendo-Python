alien_color="red"
pontos=0

if alien_color=="green":
	print("Você ganhou 5 pontos")
	pontos+=5

elif alien_color=="red":
	print("Você perdeu 10 pontos")
	pontos-=10 

else :
	print("Não muda nada")
	
print(pontos)
