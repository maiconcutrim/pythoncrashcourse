# escrevendo prompts limpos

"""
nome = input("Por favor, digite seu nome: ")
print(f"Olá, {nome.title().strip()}!")
"""

prompt = "Se você nos informar seu nome, poderemos personalizar as mensagens que você vê."
prompt += "\nQual é o seu primeiro nome? "

nome = input(prompt)
print(f"\nOlá, {nome.title().strip()}!")
