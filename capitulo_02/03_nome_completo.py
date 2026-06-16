# usando variáveis em strings

# exemplo 1
primeiro_nome = "ada"
ultimo_nome = "lovelace"
nome_completo = f"{primeiro_nome} {ultimo_nome}"
print(nome_completo)

# exemplo 2
primeiro_nome = "ada"
ultimo_nome = "lovelace"
nome_completo = f"{primeiro_nome} {ultimo_nome}"
print(f"Olá, {nome_completo.title()}!")

# exemplo 3
primero_nome = "ada"
ultimo_nome = "lovelace"
nome_completo = f"{primero_nome} {ultimo_nome}"
mensagem = f"Olá, {nome_completo.title()}!"
print(mensagem)

# adicionar espaço em branco em strings usa-se \t tabulaçõe \n quebra de linha
# remover espaço em branco em strings usa-se strip(), lstrip(), rstrip()
# remover prefixo e sufixo em strings usa-se removeprefix(), removesuffix()