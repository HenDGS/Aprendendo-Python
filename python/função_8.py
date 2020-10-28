def print_modelos(incompletos,completos):
	while incompletos:
		completos.append(incompletos.pop())
		
def modelos_completos(completos):
	for c in completos:
		print(c)

incompletos=["coringa","batman","homem-aranha"]
completos=[]
print_modelos(incompletos,completos)
modelos_completos(completos)

