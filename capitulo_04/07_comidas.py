# copiando uma lista

# fazendo cópia de uma lista

# exemplo 1
minhas_comidas = ['pizza', 'farofa', 'bolo']
comidas_amigo = minhas_comidas[:]

print(f"Minhas comidas favoritas são:")
print(minhas_comidas)

print(f"As comidas favoritas do meu amigo são:")
print(comidas_amigo)

# exemplo 2
minhas_comidas = ['pizza', 'farofa', 'bolo']
comidas_amigo = minhas_comidas[:]

minhas_comidas.append('macarrão')
comidas_amigo.append('sorvete')

print(f"\nMinhas comidas favoritas são:")
print(minhas_comidas)

print(f"As comidas favoritas do meu amigo são:")
print(comidas_amigo)

# exemplo 3
minhas_comidas = ['pizza', 'farofa', 'bolo']
comidas_amigo = minhas_comidas # isso não funciona para copiar lista

minhas_comidas.append('macarrão')
comidas_amigo.append('sorvete')

print(f"\nMinhas comidas favoritas são:")
print(minhas_comidas)

print(f"As comidas favoritas do meu amigo são:")
print(comidas_amigo)