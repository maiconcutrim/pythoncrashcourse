# dicionários

# um dicionário de objetos parecidos
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

linguagem = linguagens_favoritas['sarah'].title()
print(f"A linguagem favorita de Sarah é {linguagem}.")
print("\n")

# percorrendo todos os pares chave-valor com um loop
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

for nome, linguagem in linguagens_favoritas.items():
    print(f"A linguagem de programação favorita da(o) {nome.title()} é {linguagem.title()}.")
print("\n")

# percorrendo todas as chaves de um dicionário com um loop
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

#for nome in linguagens_favoritas.keys():
for nome in linguagens_favoritas.keys():
    print(nome.title())
print("\n")

# exemplo 2
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

amigos = ['phil','sarah']
for nome in linguagens_favoritas.keys():
    print(f"Oi {nome.title()}.")

    if nome in amigos:
        linguagem = linguagens_favoritas[nome].title()
        print(f"\t{nome.title()}, vejo que você adora {linguagem}!")
print("\n")

# exemplo 3
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }
if 'erin' not in linguagens_favoritas.keys():
    print(f"Erin, por favor, participe da nossa enquete!")
print("\n")

# percorrendo as chaves de um dicionário com um loop em uma ordem específica
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

for nome in sorted(linguagens_favoritas.keys()):
    print(f"{nome.title()}, obrigado por participar da enquete.")
print(f"\n")

# percorrendo todos os valores de um dicionário com um loop
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

print(f"Foram mencionadas as seguintes línguas:")
i = 0
for linguagem in linguagens_favoritas.values():
    i += 1
    print(f"\t{i}. {linguagem.title()}")
print("\n")

# exemplo 2 - tratando repetições
linguagens_favoritas = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

print(f"Foram mencionadas as seguintes línguas:")
i = 0
for linguagem in set(linguagens_favoritas.values()):
    i += 1
    print(f"\t{i}. {linguagem.title()}")
print(f"\n")

# uma lista em um dicionário
linguagens_favoritas = {
    'jen': ['python', 'rust'],
    'sarah':['c'],
    'edward':['rust', 'go'],
    'phil':['python', 'haskell'],
    }

for nome, linguagens in linguagens_favoritas.items():
    print(f"\nAs línguagens favoritas da(o) {nome.title()} são:")
    for linguagem in linguagens:
        print(f"\t{linguagem.title()}")

# dicionario.items() recupera as informações da chave e valor
# dicionario.kyes() recupera as informações da chave
# dicionario.values() recupera as informações do valor

# sorted(dicionario.keys()) ou sorted(dicionario.values()) organiza as informações em ordem alfabetica
# set(dicionario.keys()) ou set(dicionario.values()) trata as informações repetidas.
