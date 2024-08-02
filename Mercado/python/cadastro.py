def menu():
    print("BEM VINDO AO SUPERABACATO")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print("MENU DE OPÇÕES")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('1-CADASTRAR USUÁRIO\n2-LOGIN\n0-SAIR')

def opcao_0():
    print("ATÉ LOGO")
    exit()

def opcao_1():
    arq = open('cadastros.txt', 'a')
    print('Olá, vamos criar a sua conta!')
    print ("--------------------")

    import re

    print("Cadastre seu email")
    print ("--------------------")
    email = input("Digite seu email : ")
    print ("--------------------")

    print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n"
      "         *Ao menos 8 digitos\n")
    senha = input("Digite sua senha : ")

    while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
        senha = input("Use como base os critérios informado : ")
        continue
    print ("--------------------")

    print("Senha cadastrada com sucesso!")
    arq.write('{}, {}\n'.format(email, senha))
    print ("--------------------")
    print('Cadastro criado com sucesso!')
    arq.close()
    return

def opcao_2():
    with open('cadastros.txt', 'r') as cadastros:
        conteudo_arquivo = cadastros.readlines()
    login_email = input('informe o seu email:')
    print ("--------------------")
    login_senha = input('Digite sua senha:')
    encontrado = False
    for linha in conteudo_arquivo:
        linha = linha.strip()  
        email, senha = linha.split(', ')  
        senha = senha.strip()  
        if email == login_email and senha == login_senha:
            encontrado = True
            print('Login efetuado com sucesso!')
            import carrinho
            carrinho
    if not encontrado:
        print('E-mail ou senha incorretos.')

while True:
    menu()
    opcao = input("ESCOLHA A SUA OPÇÃO:")
    if opcao == "1":
        opcao_1()
    elif opcao == "2":
        opcao_2()
    elif opcao == "0":
        opcao_0()
    else:
        print("Valor inválido")
        break
