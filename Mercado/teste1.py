def menu():
    print("BEM VINDO AO SUPERABACATO")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print("MENU DE OPÇÕES")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('1 - CADASTRAR USUÁRIO\n2-LOGIN\n0-SAIR')

def opção_0():
    print("ATÉ LOGO")
    exit()

def opcao_1():
    arq = open('cadastros.txt', 'a')
    print('Olá, vamos criar a sua conta!')
    import re

    print("Cadastre seu email com os seguintes critérios: \n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Contendo @ e .comㅤ\n")
    email = input("Digite seu email : ")

    while not (re.search(r'@ .com', email) and   
           re.search(r'[A-Z]', email)):
        email = input("Use como base os critérios informado : ")


    print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
    senha = input("Digite sua senha : ")

    while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
        senha = input("Use como base os critérios informado : ")
        continue

    print("Senha cadastrada com sucesso!")
    arq.write('{}, {}\n'.format(email, senha))
    print('Cadastro criado com sucesso!')
    arq.close()
    return
    
def opcao_2():
    answer = input("Você é um novo usuário? Responda 'Sim' ou 'Não': ")
    if answer == "Sim".upper():
        opcao_1(opcao_2)
    else:
        login_email = input('informe o seu email:')

        login_senha = input('Digite sua senha:')
    print('Login feito com sucesso')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('Seja bem-vindo ao Superabacato')
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('Aqui está o catálogo')

    arquivo = open("Produtos.txt", "r")
    conteudo = arquivo.read()
    print("Catalogo:")
    print(conteudo)
    arquivo.close()

    import catalogo

while True:
    menu()
    opçao = input("ESCOLHA A SUA OPÇÃO:")
    if opçao == "1":
        opcao_1()
    elif opçao == "2":
        opcao_2()
    else:
        print("Valor inválido")
        break
menu()
