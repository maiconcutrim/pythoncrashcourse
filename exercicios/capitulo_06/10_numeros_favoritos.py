numeros_favoritos = {
    'maicon':[7, 9, 92],
    'leandra':[5, 6],
    'vinicius':[2, 14],
    'nora':[3, 23, 73],
    'sebastião':[1, 19],
    }

for nome, numeros in numeros_favoritos.items():
    print(f"Os números favoritos de {nome.title()} são:")
    for numero in numeros:
        print(f"\t * {numero}")