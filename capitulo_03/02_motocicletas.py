# modificando, adicionando e removendo elementos de uma lista

# modificando elementos em uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas) # lista original
motocicletas[0] = 'ducati'
print(f"{motocicletas}\n")

# adicionando elementos a uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas) # lista original
motocicletas.append('ducati') # anexando elementos ao final de uma lista
print(f"{motocicletas}\n")

# adicionando elementos em uma lista vazia
motocicletas = []
print(motocicletas) # lista vazia
motocicletas.append('honda')
motocicletas.append('yamaha')
motocicletas.append('suzuki')
print(f"{motocicletas}\n") # lista preenchida

# inserindo elementos em uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas) # lista original
motocicletas.insert(0, 'ducati')
print(f"{motocicletas}\n")

# removendo elementos de uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas) # lista original
del motocicletas[0] # removendo um elemento usando a instrução del
print(f"{motocicletas}\n")

# removendo um elemento com o metodo pop()
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas) # lista original
motocicleta_removida = motocicletas.pop() # o metodo pop() possibilita o armazenamento da informação antes da exclusão
print(motocicletas)
print(f"{motocicleta_removida}\n")

# removendo elemento de qualquer posição em uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
ultima_moto = motocicletas.pop()
#ultima_moto = motocicletas[-1]
print(f"A última motocicleta que tive foi uma {ultima_moto.title()}.")
primeira_moto = motocicletas.pop(0)
print(f"A primeira motocicleta que tive foi uma {primeira_moto.title()}.\n")
#print(motocicletas)

# removendo um elemento por valor
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas) # lista original
motocicletas.remove('ducati')
print(f"{motocicletas}\n")

# removendo um elemento por valor armazenado em uma variável
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas) # lista original
muito_caro = 'ducati'
motocicletas.remove(muito_caro)
print(motocicletas)
print(f"Uma motocicleta da {muito_caro.title()} é muito caro para mim.")