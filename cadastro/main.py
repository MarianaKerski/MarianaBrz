def registrar_usuario(dados):
    cadastro_usuario = input("\n\nNome Completo: ")
    if cadastro_usuario in dados:
        print("ERRO! Ja existe um usuario com esse nome")
        return
    cadastro_senha = input("\n\nCrie uma senha: ")
    print("Cadatro realizado com sucesso!")
    dados[cadastro_usuario] = cadastro_senha

dados_login_e_senha = {}
answer = input("Você é um novo usuário? Responda 'Sim' ou 'Não': ")

if answer == "Sim" or answer == "sim": 
    print("Vamos nos cadatrar!")
    registrar_usuario(dados_login_e_senha)

usuario = input("Entre com seu usuario: ")
senha = input("Informe a senha: ")
if usuario in dados_login_e_senha:
    if dados_login_e_senha[usuario] == senha:
        print("Login efetuado")
    else:
        print("Senha incorreta")
else:
    print("Nao existe nenhum cadastro com esse nome de usuario")
