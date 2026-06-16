# dicionários

# usando get() para acessar valores
alien_0 = {'cor':'verde', 'velocidade':'lento'}
#print(alien_0['pontos']) #
valor_pontos = alien_0.get('pontos', 'Não foi atribuído nenhum valor em pontos')
print(valor_pontos)