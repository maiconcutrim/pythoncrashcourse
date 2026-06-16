animal_0 = {
    'tipo':'cachorro',
    'nome':'theo',
    'dono':'leandra',
    }

animal_1 = {
    'tipo':'cadela',
    'nome':'lua',
    'dono':'maicon',
    }

animal_2 = {
    'tipo':'cadela',
    'nome':'plotka',
    'dono':'vinicius',
    }

pets = [animal_0, animal_1, animal_2]

for pet in pets:
    nome_pet = pet['nome'].title()
    tipo_pet = pet['tipo']
    dono_pet =pet['dono'].title()

    print(f"{dono_pet} tem um(a) {tipo_pet} de estimação chamado {nome_pet}")