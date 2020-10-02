mestres=["shirou","rin","sakura","shinji","kirei"]

for mestre in mestres:
	if (mestre=="shirou"):
		print(mestre.upper())
	else :
		print(mestre.title())

a=mestres[0].upper()=="shirou"
print(a) #Python vai diferenciar minusculas de maiusculas

a=mestres[0]=="shirou"
print(a) #Python vai diferenciar minusculas de maiusculas

if (mestres[0]!="rin"): #Operadores são iguais como em C
	print ("pum")
