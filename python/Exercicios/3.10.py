personagens=["Shirou","Rider","Rin","Archer","Sakura","Saber"]
personagens[5]="Altria"
print("Saber revelou o seu verdadeiro nome: " + personagens[1] + "\nUm novo mestre apareceu")
personagens.append("Illya")

print("\nO novo mestre de Altria é Rin")
personagens[0]=personagens[2]
print(personagens)

print("\nArcher morreu")
del personagens[3]

print("\nIllya foi viajar")
Illya=personagens.pop()

print("\nRider morreu")
personagens.remove("Rider")
print(personagens)

print("A lista atual de servos e mestres é: " + str(sorted(personagens)) + "\nContendo um total de: " + str(len(personagens)) + " personagens.")
