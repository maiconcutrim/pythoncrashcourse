minhas_comidas = ['pizza', 'farofa', 'bolo']
comidas_amigo = minhas_comidas[:]

minhas_comidas.append('macarrão')
comidas_amigo.append('sorvete')

print(f"Minhas comidas favoritas são:")
for comida in minhas_comidas:
    print(comida.title())

print(f"\nAs comidas favoritas do meu amigo são:")
for comida in comidas_amigo:
    print(comida.title())