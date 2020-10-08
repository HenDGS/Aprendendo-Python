alien_0={"cor" : "verde", "pontos" : 5}

pontos=0

print(alien_0["cor"] + " " + str(alien_0["pontos"]))

pontos+=alien_0["pontos"]
print("Você ganhou " + str(pontos) + " pontos")

alien_0["cor"]="amarelo"
print("A nova cor do alien e: " + alien_0["cor"])
