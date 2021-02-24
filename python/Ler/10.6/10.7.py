while True:
	a=input("Número 1: ")
	b=input("Número 2: ")
	if a=="q" or b=="q":
		break
	try:
		c=int(a)+int(b)
	except ValueError:
		print("Por favor, digite um número")
	else:
		print(c)

