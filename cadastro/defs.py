import valida
import os

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

    def criaBarra():
        return print('-' * 32)

    def menu():
        print('===== <<<' '\033[1;96m''Mercadinho abacato''\033[0;0m''>>> =====')
        print('Cadastrar Cliente')
        print('Dados do cliente')
        print('Mostrar clientes')
        print('Gerar relatorio')
        print('sair')
        print('------------------------------')
        x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
        print('------------------------------')
        return x



    def cadastro():
        limpaTerminal()
        print('=== < ''\033[1;92m''Cadastrar Usuario''\033[0;0m'' > ===')
        nome = valida.nome()
        login = valida.login()

        lerlogins = open('logins.txt', 'r')
        for linha in lerlogins.readlines():
            valores = linha.split('-')
            if login == valores [1].split(':')[1].strip():

                limpaTerminal()
                criaBarra()
                print('\033[1;31m''login já existente''\033[0;0m')
                criaBarra()
                return
        lerlogins.close()

        senha = valida.Senha()
        email = valida.Email()
        data = valida.Data()
        tele = valida.tele()
        ender = valida.ender()

        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Cliente cadastrado com suceso!''\033[0;0m')
        criaBarra()

        logins = open("logins.txt", 'a')
        logins.write(f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Data de nascimento:
        {data} -Numero de celular: {tele} -Endereco: {ender} \n')
        logins.close()
        return
