numeros = list(range(1,10))

# percorre uma lista de números
for n in numeros:
    # faz verificações if-elif-else para exibir em forma ordinal em inglês
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")