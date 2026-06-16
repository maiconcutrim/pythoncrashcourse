cidades = ['brasília', 'salvador', 'rio de janeiro', 'são paulo', 'curitiba', 'fortaleza']
print(f"Esta é minha lista de cidades brasileiras:\n{cidades}\n")

cidades.append('são luís')
print(f"Adicionei mais uma cidade à lista:\n{cidades}\n")

cidades.insert(0, 'belo horizonte')
print(f"Inseri uma cidade no início da lista:\n{cidades}\n")

del cidades[1]
print(f"Deletei uma cidade da lista:\n{cidades}\n")

cidade_removida = cidades.pop()
print(f"Tirei esta cidade da lista: {cidade_removida.title()}:\n{cidades}\n")

cidades.remove('salvador')
print(f"Removi mais uma cidade da lista:\n{cidades}\n")

print(f"Ordenei a lista em ordem alfabética temporária:\n{sorted(cidades)}\n")

print(f"Reordenei a lista em ordem alfabética inversa temporária:\n{sorted(cidades, reverse=True)}\n")

cidades.reverse()
print(f"Coloquei a lista original em ordem inversa:\n{cidades}\n")

cidades.sort()
print(f"Ordenei a lista em ordem alfabética definitiva:\n{cidades}\n")

cidades.sort(reverse=True)
print(f"Ordenei a lista em ordem alfabética reversa definitiva:\n{cidades}\n")

tam_lista = len(cidades)
print(f"Este é o tamanho atual da minha lista: {tam_lista}")