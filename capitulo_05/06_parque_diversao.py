# instruções if-elif-else

# exemplo 1
idade = 12
if idade < 4:
    print("A sua entrada custa R$0.")
elif idade < 18:
    print("A sua entrada custa R$25.")
else:
    print("A sua entrada custa R$40.")
print("\n")

# exemplo 2
idade = 12
if idade < 4:
    preco = 0
elif idade < 18:
    preco = 25
else:
    preco = 40
print(f"A sua entrada cusa R${preco}.")
print("\n")

# exemplo 3
idade = 65
if idade < 4:
    preco = 0
elif idade < 18:
    preco = 25
elif idade < 65:
    preco = 40
#else:
elif idade >= 65:
    preco = 20
print(f"A sua entrada cusa R$ {preco}.")
