minhas_pizzas = ['calabresa','peperoni','queijo']
pizzas_amigo = minhas_pizzas[:]

minhas_pizzas.append('margarita')
pizzas_amigo.append('portuguesa')

print(f"Minhas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print(pizza.title())

print(f"\nAs pizzas favoritas do meu amigo são:")
for pizza in pizzas_amigo:
    print(pizza.title())