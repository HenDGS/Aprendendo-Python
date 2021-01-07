with open("py.txt") as file_object:
	py=file_object.read()
	print(py)

a=""

with open("py.txt") as file_object:
	for line in file_object.read():
		a+=line
print(a)

b=[]

with open("py.txt") as file_object:
	b.append(file_object.readlines())
	
print(b)
