cidades = {
    'curitiba':{
        'país':'brasil',
        'população':1830795,
        'fato':'Ostenta o título de capital climática mais fria do Brasil.',
        },

    'salvador':{
        'país':'brasil',
        'população':2564204,
        'fato':'Foi a primeira capital colonial do Brasil.',
        },

    'são paulo':{
        'país':'brasil',
        'população':11451999,
        'fato':'É a cidade mais populosa das Américas e de todo o Hemisfério Sul.',
        },
    }

for cidade, info in cidades.items():
    pais = info['país'].title()
    populacao = info['população']
    fato = info['fato']

    print(f"{cidade.title()} fica no {pais}, tem população de {populacao}."
          f"\n{fato}\n")