pessoa_0 = {
    'nome':'maicon',
    'sobrenome':'cutrim',
    'idade':33,
    'cidade':'são luís',
    }

pessoa_1 = {
    'nome':'leandra',
    'sobrenome':'carvalho',
    'idade':26,
    'cidade':'são luís',
    }

pessoa_2 = {
    'nome':'vinicius',
    'sobrenome':'nascimento',
    'idade':12,
    'cidade':'são luís',
    }

pessoas = [pessoa_0, pessoa_1, pessoa_2]

for pessoa in pessoas:
    nome_completo = f"{pessoa['nome'].title()} {pessoa['sobrenome'].title()}"
    idade = pessoa['idade']
    cidade = pessoa['cidade'].title()

    print(f"{nome_completo} da cidade de {cidade}, tem {idade} anos.")