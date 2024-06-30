const Produtos = [
    {
        id: 1,
        nome: 'abacate',
        preço:'5.00',
        exibirProdutos:function(){
            console.log(this.id, this.nome, this.preço)
        }
    },
    {
        id: 2,
        nome: 'alvejante',
        preço: '2.00',
        exibirProdutos:function(){
            console.log(this.id, this.nome, this.preço)
        }

    },    {
        id: 3,
        nome: 'pao',
        preço:'10.00',
        exibirProdutos:function(){
            console.log(this.id, this.nome, this.preço)
        }
    }
    
]
    Produtos.exibirProdutos()