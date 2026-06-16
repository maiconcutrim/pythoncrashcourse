# o que é uma lista?

# exemplo do que é uma lista
bicicletas = ['trek','cannondale','redline','specialized']
print(f"{bicicletas}")

# acessando um elemento em uma lista
bicicletas = ['trek','cannondale','redline','specialized']
print(f"{bicicletas[0]}")

# acessando um elemento em uma lista e exibindo a string formatada
bicicletas = ['trek','cannondale','redline','specialized']
print(f"{bicicletas[0].title()}")

# as posições do índice começam  em 0, não em 1
bicicletas = ['trek','cannondale','redline','specialized']
print(f"{bicicletas[1]}") # segundo elemento
print(f"{bicicletas[3]}") # quarto elemento

# acessando o último elemento em uma lista
bicicletas = ['trek','cannondale','redline','specialized']
print(f"{bicicletas[-1]}")

# acessando valores individuais em uma lista
bicicletas = ['trek','cannondale','redline','specialized']
mensagem = f"Minha primeira bicicleta foi uma {bicicletas[0].title()}"
print(mensagem)