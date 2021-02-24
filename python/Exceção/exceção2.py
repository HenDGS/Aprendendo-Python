print("Divisão:")

while (1):
	a=input("Número 1: ")
	print("\n")
	b=input("Número 2: ")
	print("\n")
	
	try:
		c=int(a)/int(b)
	except:
		print("Não tente dividir por 0")
	else:
		print(int(c))
	print("\n")
	

