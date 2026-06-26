# usando o break para sair de um loop

prompt = "\nPor favor, digite o nome de uma cidade que você já visitou:"
prompt += "\n(Digite “quit” quando terminar.) "

while True:
    cidade = input(prompt)
    if cidade == 'quit':
        break
    else:
        print(f"Eu adoraria ir para {cidade.title()}!")