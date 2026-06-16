convidados = ['ada lovelace', 'alan turing', 'tim bernes lee']

nome = convidados[0].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[1].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[2].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

print(f"\nOlá amigos, acabo de conseguir uma mesa maior para o jantar!")
print(f"Iremos ter novos convidados!\n")
# exibe um convite para cada convidado da lista de convidados

convidados.insert(0, 'grace hopper')
convidados.insert(3, 'charles babbage')
convidados.append('linus torvalds')
# adiciona novos convidados ao início, meio e fim da lista de convidados

nome = convidados[0].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[1].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[2].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[3].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[4].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[5].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")
# exibe novamente um convite para cada convidado da lista nova de convidados

print(f"\nOlá amigos, infelizmente só poderei convidar duas pessoas para o jantar!\n")

nome = convidados.pop().title()
print(f"Olá {nome}, sinto muito não poder convidá-lo(a) para o jantar!")

nome = convidados.pop().title()
print(f"Olá {nome}, sinto muito não poder convidá-lo(a) para o jantar!")

nome = convidados.pop().title()
print(f"Olá {nome}, sinto muito não poder convidá-lo(a) para o jantar!")

nome = convidados.pop().title()
print(f"Olá {nome}, sinto muito não poder convidá-lo(a) para o jantar!\n")
# remove convidados da lista e exibe uma mesagem de desculpas

nome = convidados[0].title()
print(f"Olá {nome}, você ainda está convidado(a) para jantar!")

nome = convidados[1].title()
print(f"Olá {nome}, você ainda está convidado(a) para jantar!\n")
# exibe um convite para os convidados da lista que restaram

print(convidados)
del convidados[0]
print(convidados)
del convidados[0]
print(convidados)
# remove os convidados que restaram da lista