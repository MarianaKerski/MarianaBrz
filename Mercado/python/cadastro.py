def menu():
    print("BEM VINDO AO SUPERABACATO")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print("MENU DE OPÇÕES")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('1-CADASTRAR USUÁRIO\n2-LOGIN\n0-SAIR')

def opção_0():
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
    answer = input("Você é um novo usuário? (sim/nao): ")
    if answer == "sim":
        return opcao_1()
    elif answer == 'nao':
        with open('cadastros.txt', 'r') as cadastros:
            conteudo_arquivo = cadastros.readlines()
        login_email = input('informe o seu email:')
        print ("--------------------")
        login_senha = input('Digite sua senha:')
    if login_email not in conteudo_arquivo:
        if login_senha not in conteudo_arquivo:
            print('E-mail não cadastrado.')
        return opcao_1()
    else:
        if login_email  in conteudo_arquivo:
             if login_senha  in conteudo_arquivo:
                import carrinho

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

