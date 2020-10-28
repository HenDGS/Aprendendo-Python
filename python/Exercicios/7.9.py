sandwich_orders=["hamburguer","hot-god","natural","cheedar","pastrami","pastrami","pastrami"]

print("Estamos sem pastrami")

finished_sandwichs=[]

while sandwich_orders:
	sanduiche=sandwich_orders.pop()
	if sanduiche=="pastrami":
		continue
	finished_sandwichs.append(sanduiche)

print(finished_sandwichs)

