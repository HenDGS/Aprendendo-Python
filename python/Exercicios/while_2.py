usuarios_novos=["clara","henrique","guilherme"]
usuarios_confirmados=[]

print(usuarios_novos)
print(str(usuarios_confirmados) + "\n")

while usuarios_novos:
	usuario=usuarios_novos.pop()
	
	usuarios_confirmados.append(usuario) #Passando a lista de usuarios novos para confirmados
	
print(usuarios_novos)
print(usuarios_confirmados)
