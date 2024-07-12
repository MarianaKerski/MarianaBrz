import os
produtos = (
    {'id':1, 'nome': 'abacate', 'preco': 3.99},
    {'id':2, 'nome': 'mamao', 'preco': 7.37},
    {'id':3, 'nome': 'pera', 'preco': 6.00},
    {'id':4, 'nome': 'uva verde', 'preco': 14.99},
    {'id':5, 'nome': 'pao de queijo', 'preco': 0.50},
    {'id':6, 'nome': 'pão frances', 'preco': 1.98},
    {'id':7, 'nome': 'bolo de fuba', 'preco': 20.60},
    {'id':8, 'nome': 'macarrao instantaneo Nissin', 'preco': 3.98},
    {'id':9, 'nome': 'Dúzia de ovos', 'preco':8.00},
    {'id':10, 'nome': 'Coca-cola original 2l', 'preco':14.99},
    {'id':11, 'nome': 'alvejante', 'preco': 5.99},
    {'id':12, 'nome': 'deca', 'preco': 170.00},
    {'id':13, 'nome': 'trembolona', 'preco': 250.98}
    
)

carrinho = []

def exibirOpcoes():
    print('\n')
    print('1 - Adicionar produto ao seu carrinho')
    print('2 - Remover prouto do seu carrinho')
    print('3 - Exibir prouto e o valor total')
    print('4 - Esvaziar Carrinho de compras')
    print('5 - Sair')


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))


opcao = '1'

os.system
print('BEM VINDO AO SUPERABACATO')
print ("--------------------")
print('MENU DE OPÇÕES')


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o identificador do produto: '))
        quantidade = float(input('Digite quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        id = int(input('Digite o id do produto: '))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                temp.append(item)
                carrinho = temp

    if opcao == '3':
        arquivo=open("notafiscal.txt","a")
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                    (produto['preco'] * item['quantidade'])
                    break

        import datetime
        data_atual = datetime.date.today()
        data_formatada = data_atual.strftime("%d/%m/%Y")

        print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))
        nota = input("Deseja ter sua nota fiscal?(sim/nao - sair)")
        if nota == "nao":
            print('Obrigado pela preferencia! Volte logo.')
            exit()
        if nota == "sim":
            print("Digite seu CPF:")
            cpf = input()
        print ("--------------------")
        print("DATA:", (data_atual))
        print ("---------")
        print( "CPF:", cpf)
        print ("---------")
        print("PREÇO TOTAL = ",somatorio)
        arquivo.write("cpf = ")
        arquivo.write((cpf))
        arquivo.write('\n')
        arquivo.write('Preco total: {0}'.format(somatorio))
        arquivo.write('\n')
        arquivo.write('Data:')
        arquivo.write(str(data_formatada))
        arquivo.write('\n')
        arquivo.write('--------------')
        arquivo.write('\n')
        arquivo.close()
    if opcao == '4':
        carrinho = []

    if opcao == '5':
        print("Volte logo!")
        exit()

