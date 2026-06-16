# verificando diferença
cobertura_solicitada = 'cogumelos'
if cobertura_solicitada != 'anchovas':
    print(f"Sem anchovas!")
print("\n")

# testando múltiplas condições

# exemplo 1
coberturas_solicitadas = ['cogumelos', 'queijo extra']
if 'cogumelos' in coberturas_solicitadas:
    print("Adicionar cogumelos.")
if 'peperoni' in coberturas_solicitadas:
    print("Adicionar peperoni.")
if 'queijo extra' in coberturas_solicitadas:
    print("Adicinar queijo extra.")
print("A sua pizza está pronta!")
print("\n")

# exemplo 2
coberturas_solicitadas = ['cogumelos', 'queijo extra']
if 'cogumelos' in coberturas_solicitadas:
    print("Adicionar cogumelos.")
elif 'peperoni' in coberturas_solicitadas: # na instrução elif a primeira condição "True" encerra a verificação
    print("Adicionar peperoni.")
elif 'queijo extra' in coberturas_solicitadas:
    print("Adicinar queijo extra.")
print("A sua pizza está pronta!")
print("\n")

# usando instruções if com listas

# exemplo 1
coberturas_solicitadas = ['cogumelos', 'pimentões verdes', 'queijo extra']
for cobertura in coberturas_solicitadas:
    print(f"Adicionando {cobertura}")
print("A sua pizza está pronta!")
print("\n")

# exemplo 2
coberturas_solicitadas = ['cogumelos', 'pimentões verdes', 'queijo extra']
for cobertura in coberturas_solicitadas:
    if cobertura == 'pimentões verdes':
        print(f"Desculpe, no momento não temos {cobertura}.")
    else:
        print(f"Adicionando {cobertura}")
print("A sua pizza está pronta!")
print("\n")

# verificando se uma lista não está vazia
coberturas_solicitadas = []
if coberturas_solicitadas:
    for cobertura in coberturas_solicitadas:
        print(f"Adicionando {cobertura}")
    print("A sua pizza está pronta!")
else:
    print(f"Tem certeza de que quer uma pizza simples?")
print("\n")

# usando múltiplas listas
coberturas_disponiveis = ['cogumelos', 'azeitonas', 'pimentões verdes', 'peperoni', 'abacaxi', 'queijo extra']
coberturas_solicitadas = ['cogumelos', 'batatas fritas', 'queijo extra']

for cobertura in coberturas_solicitadas:
    if cobertura in coberturas_disponiveis:
        print(f"Adicionando {cobertura}.")
    else:
        print(f"Desculpe, não temos {cobertura}.")
print(f"A sua pizza está pronta!")
