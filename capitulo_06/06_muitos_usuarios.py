# dicionários

# um dicionário em um dicionário
usuarios = {
    'aeinstein':{
        'nome':'albert',
        'sobrenome':'einstein',
        'local':'princeton',
         },

    'mcurie':{
        'nome':'marie',
        'sobrenome':'curie',
        'local':'paris',
        },
}

for nome_usuario, info_usuario in usuarios.items():
    print(f"\nUsuário: {nome_usuario}")

    nome_completo = f"{info_usuario['nome']} {info_usuario['sobrenome']}"
    local = info_usuario['local']

    print(f"\tNome completo: {nome_completo.title()}")
    print(f"\tLocalização: {local.title()}")
