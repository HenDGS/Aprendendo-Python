mestres=["shirou","rin","sakura","shinji","kirei"]
print(mestres[0:3])
print(mestres[:3]) #parte do principio q deve iniciar do 0
print(mestres[0:]) #mesma coisa para o final
print(str(mestres[-3:]) + "\n") #3 ultimos

for mestre in mestres:
	print (mestre.title())
