

bodega_dicc={'cucharas':['es una cuchara'],'tazas':['es una taza'], 'tenedor': ['es un tenedor']}

for k in bodega_dicc.keys():
        bodega_dicc[k].append(random.randint(300,500))
print(bodega_dicc)

{'cucharas': ['es una cuchara', 303], 'tazas': ['es una taza', 438], 'tenedor': ['es un tenedor', 30