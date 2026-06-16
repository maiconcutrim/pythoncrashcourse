convidados = ['tim bernes lee', 'ada lovelace', 'alan turing']

nome = convidados[0].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[1].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[2].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")
# exibe um convite para cada convidado da lista de convidados

nome = convidados[1].title()
print(f"\n{nome}, não poderá ir ao jantar. Estes são os novos convidados:")

del convidados[1]
convidados.insert(1, 'guido von rossum')
# remove um convidado da lista e insere outro no lugar

nome = convidados[0].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[1].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")

nome = convidados[2].title()
print(f"Olá {nome}, você está convidado(a) para o jantar!")
# exibe novamente um convite para cada convidado da lista de convidados alterada