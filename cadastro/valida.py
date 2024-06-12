import defs

def nome():
    while True:
        nome = input('Nome Completo: ')

        continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i .isdigit():
                print('Digite um nome valido.')
                break
        else:
            return nome.strip(' ')

def senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Error! Entrada vazia.')
            continue
            return senha.strip(' ')

def Email():
    while True:
        email = input('Email: ')
        if email == ' ':
            print('Error! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email inválido! deve conter "@" e ".com" ')

def login():
    while True:
        login = input('Login: ')
        if login == '':
            print('Error! Entrada vazia.')
            continue
            return login.strip(' ')

def ender():
    while True:
        print('=== < ''\033[1;32m''Seu endereço completo!' '\033[0;0m''> ===')
        dados = {
            'Rua': input('Rua: '),
            'Numero': input('Numero: '),
            'Complemento': input('Complemento: '),
            'Bairro': input('Bairro: '),
            'Cep': input('Cep: '),
            'Cidade': input('Cidade: '),
            'Referencia': input('Referencia: '),
        }

        return dados
