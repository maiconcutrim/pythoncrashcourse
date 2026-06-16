usuarios_atuais = ['user', 'TEST', 'support', 'admin', 'GUEST']
novos_usuarios = ['operator', 'guest', 'system', 'test', 'root']

# cria uma nova lista com todos os usuários atuais em minúsculo
usuarios_atuais_minusculo = [usuario.lower() for usuario in usuarios_atuais]

for usuario in novos_usuarios:
    # padroniza o novo usuário para minúsculo para comparar
    if usuario.lower() in usuarios_atuais_minusculo:
        print(f"O nomde de usário {usuario.lower()} já existe. Tente novamente!")
    else:
        print(f"O nome de usuário {usuario.lower()} está disponível!")