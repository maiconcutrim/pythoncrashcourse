linguagens_favoritas = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for nome, linguagem in linguagens_favoritas.items():
    print(f"A linguagem de programação favorita da(o) {nome.title()} é {linguagem.title()}.")
print("\n")

programadores = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for programador in programadores:
    if programador in linguagens_favoritas.keys():
        print(f"Obrigado por participar da pesquisa, {programador.title()}!")
    else:
        print(f"{programador.title()}, qual é a sua linguagem de programação favorita?")
