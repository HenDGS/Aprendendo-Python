def pizza (nome,sobrenome,**ingredientes): 
	profile={}
	profile["nome"]=nome
	profile["sobrenome"]=sobrenome
	for x,y in ingredientes.items():
		profile[x]=y
	return profile

user_profile = pizza("henrique","da gama saczkowski",
					location="curitiba",
					field="ti",idade=21,familia=5)

print(user_profile)


