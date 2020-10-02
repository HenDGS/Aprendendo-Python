minhas_comidas=["pizza","hamburguer","kitkat"]

comidas_do_meu_amigo=minhas_comidas[0:2] #amigo não gosta de kitkat \ Se fizer sem usar fatia, vai linkar com a outra lista

print(minhas_comidas)
print(comidas_do_meu_amigo)

minhas_comidas.append("bolo")

print(minhas_comidas)
print(comidas_do_meu_amigo)

for comida in minhas_comidas:
	print(comida)
	
print("\n")

for comida in comidas_do_meu_amigo:
	print(comida)
