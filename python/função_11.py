def pizza (nome,sobrenome,**ingredientes): 
	profile={}
	profile["nome"]=nome
	profile["sobrenome"]=sobrenome
	for x,y in ingredientes.items():
		profile[x]=y
	return profile

user_profile = pizza("albert","eintein",
					location="princenton",
					field="physics")

print(user_profile)

