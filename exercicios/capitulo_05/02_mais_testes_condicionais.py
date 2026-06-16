# 1
carro = 'audi'
print(f"\nÉ um carro == 'audi'? Prevejo que seja True.")
print(carro == 'audi')

print(f"É um carro != 'audi'? Prevejo que seja False.")
print(carro != 'audi')

# 2
carro = 'BMW'
print(f"\nÉ um carro == 'BMW'? Prevejo que seja True.")
print(carro.lower() == 'bmw')

# 3
a = 8
b = 2

print(f"\nA == B?")
print(a == b)

print(f"\nA != B?")
print(a != b)

print(f"\nA > B?")
print(a > b)

print(f"\nA < B?")
print(a < b)

print(f"\nA >= B?")
print(a >= b)

print(f"\nA <= B?")
print(a <= b)

# 4
carro1 = 'audi'
carro2 = 'toyota'

print(f"\nÉ um carro == 'audi' e == 'toyota'? Prevejo que seja True.")
print(carro1 == 'audi' and carro2 == 'toyota')

print(f"\nÉ um carro == 'audi' e == 'subaru'? Prevejo que seja False.")
print(carro1 == 'audi' and carro2 == 'subaru')

print(f"\nÉ um carro == 'bmw' ou == 'toyota'? Prevejo que seja True.")
print(carro1 == 'bmw' or carro2 == 'toyota')

print(f"\nÉ um carro == 'bmw' ou == 'subaru'? Prevejo que seja False.")
print(carro1 == 'bmw' or carro2 == 'subaru')

# 5
numeros = list(range(2,11,2))
print(f"\nO número 3 consta na lista?")
print(3 in numeros)

# 6
print(f"\nO número 3 não consta na lista?")
print(3 not in numeros)