lugares_favoritos = {
    'maicon':['bar', 'cinema', 'casa'],
    'leandra':['salão', 'academia', 'restaurante'],
    'vinicius':['shopping', 'parque'],
    }

for nome, lugares in lugares_favoritos.items():
    print(f"Os lugares favoritos de {nome.title()} são: ")
    for lugar in lugares:
        print(f"\t * {lugar.title()}")