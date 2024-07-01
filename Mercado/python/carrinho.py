import os
produtos = (
    {'id':1, 'nome': 'abacate', 'preco': 3.99},
    {'id':2, 'nome': 'pão', 'preco': 14.98},
    {'id':3, 'nome': 'alvejante', 'preco': 5.99},
    {'id':4, 'nome': 'mamao', 'preco': 7.37},
    {'id':5, 'nome': 'pera', 'preco': 6.00},
    {'id':6, 'nome': 'deca', 'preco': 170.00},
    {'id':7, 'nome': 'trembolona', 'preco': 250.98},
    {'id':8, 'nome': 'miojo', 'preco': 3.98}
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

os.system('clear')
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
                temp.remove(item)

    if opcao == '3':
        arquivo=open("notafiscal.txt","w")
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                    (produto['preco'] * item['quantidade'])
                    break

            print(
                'Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

        arquivo.write('\n{},\n{},'.format(obterNomeProduto(item['id']),'preço total: {0}'.format(somatorio)))
        arquivo.close()

        print("Nota fiscal:")

    with open("notafiscal.txt", "r")as arquivo:
        texto=arquivo.read()
    print(texto)
    if opcao == '4':
        carrinho = []
