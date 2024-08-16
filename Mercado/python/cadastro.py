def menu():
    print('┌────────────────────────────┐')
    print("│Bem vindo ao SuperAbacato 🛒│")
    print('└────────────────────────────┘')
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print("Menu de opções")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('1-Cadastrar usuário\n2-Login\n0-Sair')

def opcao_0():
    print("ATÉ LOGO")
    exit()

def opcao_1():
    arq = open('cadastros.txt', 'a')
    print('┌─────────────────────────────┐')
    print('│Olá, vamos criar a sua conta!│')
    print('└─────────────────────────────┘')

    import re

    print("Vamos cadastrar seu email!")
    print ("……")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    email = input("Digite seu email : ")
    print ("\n")

    print("Cadastre aqui sua senha com os seguintes critérios: \n"
        "\n"
      "       *Ao menos uma letra MAIÚSCULA\n"
      "       *Ao menos um número\n"
      "       *Ao menos um caractere especial(!@#$%¨&*)\n"
      "       *Ao menos 8 digitos\n")
    senha = input("Digite sua senha : ")

    while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
        senha = input("Use como base os critérios informado : ")
        continue
    arq.write('{}, {}\n'.format(email, senha))
    arq.close()
    opcao_2()

def opcao_2():
    print ("──────────────────")
    print("Faça o seu login:")
    print ("──────────────────")
    with open('cadastros.txt', 'r') as cadastros:
        conteudo_arquivo = cadastros.readlines()
    login_email = input('Informe o seu email:')
    print ("\n")
    login_senha = input('Digite sua senha:')
    print('\n')
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
    opcao = input("Escolha a sua opção:")
    if opcao == "1":
        opcao_1()
    elif opcao == "2":
        opcao_2()
    elif opcao == "0":
        opcao_0()
    else:
        print("Valor inválido")
        break
