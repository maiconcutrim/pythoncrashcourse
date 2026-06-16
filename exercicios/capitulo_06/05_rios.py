# 1
rios = {
    'nilo':'egito',
    'amazonas':'brasil',
    'yangtzé':'china'
    }
for rio, pais in rios.items():
    print(f"O rio {rio.title()} atravessa o(a) {pais.title()}")
print("\n")

# 2
print(f"Rios:")
for rio in rios.keys():
    print(f"\tRio {rio.title()}")
print("\n")

# 3
print(f"Paises:")
for pais in rios.values():
    print(f"\t{pais.title()}")