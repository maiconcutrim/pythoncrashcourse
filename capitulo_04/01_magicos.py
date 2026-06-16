# trabalhando com listas

# percorrendo uma lista utilizando o loop for
magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico)
print(f"\n")

# fazendo mais tarefas dentro de um loop for

#exemplo 1
magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f"{magico.title()}, que truque incrível!")
print(f"\n")

# exemplo 2
magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f"{magico.title()}, que truque incrível!")
    print(f"Mal posso esperar para ver o seu próximo truque, {magico.title()}.\n")
print(f"\n")

# fazendo mais tarefas após usar um loop for
magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f"{magico.title()}, que truque incrível!")
    print(f"Mal posso esperar para ver o seu próximo truque, {magico.title()}.\n")
print(f"Obrigado a todos. Foi um espetáculo de mágica fantástico")
