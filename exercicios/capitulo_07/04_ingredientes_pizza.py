prompt = "\nInsira os ingredientes da pizza:"
prompt += "\nDigite 'quit' para finalizar. "

resposta = ""
while resposta != "quit":
    resposta = input(prompt)
    if resposta != "quit":
        print(f"\t{resposta} foi adicionado à pizza!")