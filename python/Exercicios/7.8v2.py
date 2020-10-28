sandwich_orders=["hamburguer","hot-god","natural","cheedar"]

finished_sandwichs=[]

while sandwich_orders:
	sandwich=sandwich_orders[0]
	finished_sandwichs.append(sandwich)
	sandwich_orders.remove(sandwich)

print(finished_sandwichs)

