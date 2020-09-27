jantar=["Merlin","Altria","Gilgamesh"]
print("Infelizmente " + jantar[0] + " não poderá comparecer")
jantar[0]="Kiritsugu"
print("O novo convidado é: " + jantar[0])

jantar.insert(0,"Medusa")
jantar.insert(2,"Lancelot")
jantar.append("Mordred")
print(jantar)
