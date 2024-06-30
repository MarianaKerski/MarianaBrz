Produtos = []
precos = []
quantidades = []
preco_total = []
total = 0
while True:
    Produto = str(input("Digite o produto a ser comprado (q para sair): ")).lower()
    if Produto == "q":
        break
    else:
        preco = float(input(f"Digite o preço do {Produto}: "))
        quantidade = int(input(f"Digite a quantidade do {Produto}: "))
        preco_totalprodutos = preco*quantidade
        total = total + preco_totalprodutos
        Produtos.append(Produto)
        precos.append(preco)
        quantidades.append(quantidade)
        preco_total.append(preco_totalprodutos)

    print("="*50)
    print("\t\tO seu carrinho de compras")
    print("="*50)
    print("\n")

    print("Nome do Produto         Quantidade     Preço Unidade     Preço Total  ")
    for b, quant, preuni,precof in zip(Produtos,quantidades, precos,preco_total ):
        print(f'{b}                      {quant}                {preuni}               {precof}'  )

    print()
    print(f"A fatura total é de: {total}")

