# organizando uma lista

# ordenando uma lista permanentemente com metodo sort()
carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort() # ordena a lista em ordem alfabética e de forma permanente
print(f"{carros}\n")

# ordenando uma lista permanentemente com metodo sort() de forma inversa
carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort(reverse=True) # ordena a lista em ordem alfabética de forma permanente e inversa
print(f"{carros}\n")

# ordenando uma lista temporariamente com a função sorted()
carros = ['bmw', 'audi', 'toyota', 'subaru']

print(f"Aqui está a lista original.")
print(carros)
print(f"Aqui está a lista ordenada.")
print(sorted(carros)) # ordena a lista em ordem alfabética e de forma temporária

print(f"\nAqui está a lista ordenada em ordem inversa.")
print(sorted(carros, reverse=True)) # ordena a lista em ordem alfabética de forma temporária e inversa
print(f"Aqui está a lista original novamente.")
print(f"{carros}\n")

# exibindo uma lista em ordem reversa
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros) # ordem original
carros.reverse() # ordem reversa
print(f"{carros}\n")

# identificando o tamanho de uma lista
carros = ['bmw', 'audi', 'toyota', 'subaru']
tamanho_lista = len(carros)
print(f"A lista possuí {str(tamanho_lista)} elementos.")