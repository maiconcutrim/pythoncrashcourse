# dicionários

# percorrendo um dicionário com um loop
user_0 = {
    'usuario':'efermi',
    'nome':'enrico',
    'sobrenome':'fermi',
    }

for chave, valor in user_0.items():
    # percorrendo todos os pares chave-valor com um loop
    print(f"\nChave: {chave}")
    print(f"Valor: {valor}")
