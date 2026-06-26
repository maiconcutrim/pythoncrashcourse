# apresentando os loops while

# usando o loop while
"""
numero_atual = 1
while numero_atual <= 5:
    print(numero_atual)
    numero_atual += 1
"""

# usando continue em um loop
"""
numero_atual = 0
while numero_atual < 10:
    numero_atual  += 1
    if numero_atual % 2 == 0:
        continue
    print(numero_atual)
"""

# evitando loops infinitos
x = 1
while x <= 5:
    print(x)
    x += 1