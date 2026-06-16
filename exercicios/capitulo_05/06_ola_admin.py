nomes_usuarios = ['user', 'test', 'support', 'admin', 'guest']

# percorre uma lista e exibe mensagem personalizada para o usuário administrador
for usuario in nomes_usuarios:
    if usuario == 'admin':
        print(f"Olá Administrador, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {usuario.title()}, obrigado por fazer login novamente.")
