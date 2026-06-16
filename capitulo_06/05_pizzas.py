# dicionários

# uma lista em um dicionário

# armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'massa':'grossa',
    'coberturas':['cogumelos', 'queijo extra'],
    }

# resume o pedido
print(f"Você pediu uma pizza de massa {pizza['massa']}" 
      " com as seguintes coberturas:")

for cobertura in pizza['coberturas']:
    print(f"\t{cobertura}")