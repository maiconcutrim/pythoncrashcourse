# tuplas

# definindo tuplas
dimensoes = (200, 50)
print(dimensoes[0])
print(dimensoes[1])
print(" ")

# percorrendo todos os valores em uma tupla com  um loop
dimensoes = (200, 50)
for dimensao in dimensoes:
    print(dimensao)
print(" ")

# sobrescrevendo uma tupla
dimensoes = (200, 50)
print(f"Dimensões originais:")
for dimensao in dimensoes:
    print(dimensao)

dimensoes = (400, 100)
print(f"Dimensões modificadas:")
for dimensao in dimensoes:
    print(dimensao)