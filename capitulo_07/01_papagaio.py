# entrada do usuário e loops while

# como a função input() funciona
"""
mensagem = input("Diga-me uma coisa, e eu vou repetir para você: ")
print(mensagem)
"""

# permitindo que o usuário encerre um programa
"""
prompt = "\nDiga-me uma coisa, e eu vou repetir para você:"
prompt += "\nDigite “quit” para encerrar o programa. "

mensagem = ""
while mensagem != 'quit':
    mensagem = input(prompt)
    if  mensagem != 'quit':
        print(mensagem)
"""

# usando flags
prompt = "\nDiga-me uma coisa, e eu vou repetir para você:"
prompt += "\nDigite “quit” para encerrar o programa. "

ativo = True
while ativo:
    mensagem = input(prompt)
    if mensagem == "quit":
        ativo = False
    else:
        print(mensagem)