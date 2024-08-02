
const products = [
    { id: 1, name: "Alvejante", price: 5.99,  },
    { id: 2, name: "Abacate", price: 3.99,  },
    { id: 3, name: "Pao", price: 14.98,  },
    { id: 4, name: "Trembolona", price: 250.99,  },
    { id: 5, name: "Miojo", price: 4.99, }
  ];
  
  function printCatalog() {
    console.log("Catálogo de Produtos");
    console.log("--------------------");
  
    const catalog = products.map((product) => {
      return `
  ID: ${product.id}
  Nome: ${product.name}
  Preço: R$ ${product.price.toFixed(2)}
  --------------------`;
    }).join("\n");
  
    console.log(catalog);
  }
  
  printCatalog();
