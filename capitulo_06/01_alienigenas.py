# dicionários

# um dicionário simples
alien_0 = {'cor':'verde', 'pontos':5}

print(alien_0['cor'])
print(alien_0['pontos'])
print("\n")

# trabalhando com dicionários

# acessando valores em um dicionário

# exemplo 1
alien_0 = {'cor':'verde'}
print(alien_0['cor'])
print("\n")

# exemplo 2
alien_0 = {'cor':'verde', 'pontos':5}

pontos = alien_0['pontos']
print(f"Você acabou de ganhar {pontos} pontos!")
print("\n")

# adicionando novos pares chave-valor

alien_0 = {'cor':'verde', 'pontos':5}
print(alien_0)

alien_0['coordenada_x'] = 0
alien_0['coordenada_y'] = 25
print(alien_0)
print("\n")

# começando com um dicionário vazio
alien_0 = {}

alien_0['cor'] = 'verde'
alien_0['pontos'] = 5

print(alien_0)
print("\n")

# modificando valores em um dicionário

# exemplo 1
alien_0 = {'cor':'verde', 'pontos':5}
print(f"O alien é {alien_0['cor']}.")

alien_0['cor'] = 'amarelo'
print(f"O alien agora é {alien_0['cor']}.")
print("\n")

# exemplo 2
alien_0 = {'coordenada_x':0, 'coordenada_y':25, 'velocidade':'medio'}
print(f"Posição original: {alien_0['coordenada_x']}")
# desloca o alienígena para a direita
# estipula a distância que o alienígena deve percorrer conforme sua velocidade
if alien_0['velocidade'] == 'devagar':
    x_incremental = 1
elif alien_0['velocidade'] == 'medio':
    x_incremental = 2
else:
    # com isso, o alienígena fica veloz
    x_incremental = 3
# a posição nova é a posição antiga mais o incremento
alien_0['coordenada_x'] = alien_0['coordenada_x'] + x_incremental

print(f"Nova posição: {alien_0['coordenada_x']}")
print("\n")

# removendo pares de chave-valor
alien_0 = {'cor':'verde', 'pontos':5}
print(alien_0)

del alien_0['pontos']
print(alien_0)
print(f"\n")

# uma lista de dicionários
alien_0 = {'cor':'verde','pontos':5}
alien_1 = {'cor':'amarelo','pontos':10}
alien_2 = {'cor':'vermelho','pontos':15}

alienigenas = [alien_0, alien_1, alien_2]

for alien in alienigenas:
    print(alien)