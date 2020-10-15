aliens=[]

for alien_number in range(30):
	new_alien={"cor":"verde","pontos":5,"velocidade":"lento"}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print("Quantidade de aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
	if alien["cor"]=="verde":
		alien["cor"]="amarelo",
		alien["pontos"]=10,
		alien["velocidade"]="medio"
	
	elif alien["cor"]=="amarelo":
		alien["cor"]="vermelho",
		alien["pontos"]=15,
		alien["velocidade"]="rapido"

for alien in aliens[:5]:
	print(alien)
print("...")
