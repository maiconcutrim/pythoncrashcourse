# verificando se um valor não está em uma lista
usuarios_proibidos = ['andrew', 'carolina', 'david']
usuario = 'marie'

if usuario not in usuarios_proibidos:
    print(f"{usuario.title()}, você pode postar uma resposta, se quiser!")