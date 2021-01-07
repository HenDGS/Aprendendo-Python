with open('pi_million_digits.txt') as file_object:
	contents=file_object.read()
	print(contents[:50] + "...")
	
	if str(120372) in contents:
		print("seu aniversario")
	else:
		print("pum")






