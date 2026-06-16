glossario = {
    'variável':'Usada para armazenar dados',
    'função':'Bloco de código reutilizável que executa uma tarefa',
    'loop':'Estrutura para repetir instruções',
    'classe':'Modelo para criar objetos na programação orientada a objetos',
    'módulo':'Arquivo que contém código python reutilizável e que pode ser importado',
    'tupla':'Coleção ordenada e imutável',
    'dicionário':'Estrutura de pares chave-valor',
    'exception':'Erro tratado com try e except.',
    'lista':'Coleção ordenada e mutável de elementos',
    'condicional':'Estrutura de decisão usando if, elif e else.',
    }

print(f"Glossário Python:")
i = 0
for chave, valor in glossario.items():
    i += 1
    print(f"{i}. {chave.title()}: \n\t{valor}.")
