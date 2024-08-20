import os
UserAdmin = "Admin"
produtos = [
    {'id':1, 'nome': 'Abacate', 'preco': 3.99},
    {'id':2, 'nome': 'Mamão', 'preco': 7.37},
    {'id':3, 'nome': 'Pera', 'preco': 6.00},
    {'id':4, 'nome': 'Uva verde', 'preco': 14.99},
    {'id':5, 'nome': 'Pão de queijo', 'preco': 0.50},
    {'id':6, 'nome': 'Pão frances', 'preco': 1.98},
    {'id':7, 'nome': 'Bolo de fuba', 'preco': 20.60},
    {'id':8, 'nome': 'Macarrao instantaneo Nissin', 'preco': 3.98},
    {'id':9, 'nome': 'Dúzia de ovos', 'preco':8.00},
    {'id':10, 'nome': 'Coca-cola original 2l', 'preco':14.99},
    {'id':11, 'nome': 'Alvejante', 'preco': 5.99},
    {'id':12, 'nome': 'Deca', 'preco': 170.00},
    {'id':13, 'nome': 'Trembolona', 'preco': 250.98}
    
]

carrinho = []

def exibirOpcoes():
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('1 - Adicionar produto ao seu carrinho')
    print('2 - Remover prouto do seu carrinho')
    print('3 - Exibir prouto e o valor total')
    print('4 - Esvaziar Carrinho de compras')
    print('5 - Sair')
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print ("──────────────────")
    print("Funções Admin")
    print ("──────────────────")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    print('6 - Adicionar produto ao catalogo')
    print('7 - Remover produto do catalogo')
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")


def exibirProdutos():
    for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))


opcao = '1'

os.system
print('┌────────────────────────────┐')
print("│Bem vindo ao SuperAbacato 🛒│")
print('└────────────────────────────┘')
print('Menu de opções')

def remover_itemcatalogo():
    senha = input('Digite sua senha de Admin:')
    if senha == UserAdmin:
        exibirProdutos()
        id = int(input('Digite o id do produto: '))
        temp = []
        for item in produtos:
            if item['id'] != id:
                temp.append(item)
    if senha != UserAdmin:
                print('Senha Errada.')

def endereço():
    arquivo=open("endereço.txt","a")
    compra=input("Deseja ter sua compra entregue em sua residência?(sim/não)")
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
    if compra == 'sim':
        print('Digite o seu CEP:')
        cep=str(input(""))
        print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
        print('Digite o número da sua residência:')
        numero=str(input(""))
        print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
        print("Sua compra será enviada para o endereço em breve...")
        arquivo.write("CEP:")
        arquivo.write(cep)
        arquivo.write("\n")
        arquivo.write("NÚMERO:")
        arquivo.write(numero)
        arquivo.write("\n")
        arquivo.write("───────────────")
        arquivo.write("\n")
        arquivo.close
    if compra == 'não':
        print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
        print("Obrigado pela preferência, volte logo!")
    exit()

def Adicionar_podutoaocatalogo():
    senha = input('Digite sua senha de Admin:' )
    if senha == UserAdmin:
        exibirProdutos()
        id = int(input('Digite o id do produto: '))
        nome = (input('Digite o nome do produto: '))
        preco = float(input('Digite o preco: '))
        produtos.append({'id': id, 'nome': nome, 'preco': preco})
        print(nome ,'Adicionado ao catalogo \n')
    if senha != UserAdmin:
                print('Senha Errada.')


def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')
    print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")

    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o identificador do produto: '))
        quantidade = float(input('Digite quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        exibirProdutos()
        print (carrinho)
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
        
        continuarcompra = input("deseja continuar comprando?(sim/nao)")
        if continuarcompra == "nao":
            if continuarcompra == "sim":
                    break
            nota = input("Deseja ter sua nota fiscal?(sim/nao - sair)")
            if nota == "nao":
                endereço()
            if nota == "sim":
                print("Digite seu CPF:")
            cpf = input()
            print ("──────────────────")
            print("DATA:", (data_atual))
            print ("──────────────────")
            print( "CPF:", cpf)
            print ("──────────────────")
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
            endereço()
            print('Obrigado pela preferencia! Volte logo.')
            exit()
    if opcao == '4':
        carrinho = []

    if opcao == '7':
        remover_itemcatalogo()


    if opcao == '5':
        print("Volte logo!")
        exit()
    
    if opcao == '6':
       Adicionar_podutoaocatalogo()

