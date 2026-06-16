# trabalhando com parte de uma lista

# fatiando uma lista
jogadores = ['charles', 'martina', 'michael', 'florece', 'eli']
print(jogadores[0:3])
print(jogadores[1:4])
print(jogadores[:4])
print(jogadores[2:])
print(jogadores[-3:])
print("\n")

# percorrendo uma fatia com loop
jogadores = ['charles', 'martina', 'michael', 'florece', 'eli']
print(f"Aqui estão os três primeiros jogadores do meu time:")
for jogador in jogadores[:3]:
    print(jogador.title())