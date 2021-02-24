a=input("Número 1: ")
b=input("Número 2: ")
try:
	c=int(a)+int(b)
except ValueError:
	print("Por favor, digite um número")
else:
	print(c)
