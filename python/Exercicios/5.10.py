current_users=["henrique","clara","guilherme","admin","pedro"]
new_users=["henrique","clara","joao","daniel","ana"]

for user in new_users:
	if (user.lower() in (usera.lower() for usera in current_users)):
		print("Esse nome já foi usado")
	else:
		print("Esse nome de usuário está disponível")
