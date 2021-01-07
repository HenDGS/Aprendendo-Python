a=""

with open("py.txt") as file_object:
	for line in file_object.read():
		a+=line

a=a.replace("python","c")

print(a)

with open("bilada.txt","w") as file_object:
	file_object.write("pimba")

with open("bilada.txt","a") as file_object:
	file_object.write(".\nBilada")
