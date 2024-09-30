const fs = require('fs');
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const fileName = 'users.txt';
const catalogoFilmes = 'catalogo_filmes.txt';
const avaliacoesFilmes = 'avaliacoes_filmes.txt';
const alugados = 'alugados.txt';

let adminLogado = false;

function main() {
  console.log('1 - Cadastrar\n2 - Entrar\n3 - Entrar como Admin\n4 - sair');
  readline.question('Escolha uma opção: ', option => {
    switch (option) {
      case '1':
        cadastrarUsuario();
        break;
      case '2':
        loginUsuario();
        break;
      case '3':
        loginAdmin();
        break;
      case '4':
        console.log("ATÉ LOGO!!")
        exit()
        break;
      default:
        console.log('Opção inválida. Tente novamente.');
        main();
    }
  });
  console.log("\n");
}

function cadastrarUsuario() {
  readline.question('Digite o nome de usuário: ', username => {
    readline.question('Digite a senha: ', password => {
      salvarUsuario(username, password);
      main();
    });
  });
}

function salvarUsuario(username, password) {
  const user = `\n${username}:${password}`;
    fs.appendFile(fileName, user, (err) => {
    if (err) throw err;
    console.log('Usuário cadastrado com sucesso!');
  });
}

function loginUsuario() {
  readline.question('Digite o nome de usuário: ', username => {
    readline.question('Digite a senha: ', password => {
      verificarLogin(username, password);
    });
  });
}

function verificarLogin(username, password) {
  fs.readFile(fileName, 'utf8', (err, data) => {
    if (err) {
      console.log('Erro ao ler o arquivo.');
      return;
    }
    const users = data.split('\n');
    const userFound = users.find(user => {
    const [userUsername, userPassword] = user.split(':');
      return userUsername === username && userPassword === password;
    });
    if (userFound) {
      console.log('Login efetuado com sucesso!');
      menuPrincipal();
        
    } else {
        console.log('Usuário ou senha inválidos.');
      main();
    }
  });
}

function loginAdmin() {
  readline.question('Digite o nome de usuário: ', username => {
    readline.question('Digite a senha: ', password => {
      if (username === 'admin' && password === 'admin') {
        adminLogado = true;
        console.log('Login como admin efetuado com sucesso!');
        menuAdmin();
      } else {
        console.log('Usuário ou senha inválidos.');
        main();
      }
    });
  });
}

function menuPrincipal() {
  console.log('\nSeja bem vindo!\n');
  console.log('1. Ver catálogo de filmes');
  console.log('2. Avaliar filmes');
  console.log('3. Alugar filmes');
  console.log('4. Sair');
  readline.question('Escolha uma opção: ', opcao => {
    switch (opcao) {
      case '1':
        verCatalogoFilmes();
        break;
      case '2':
        avaliarFilmes();
        break;
      case '3':
        alugarFilmes();
        break;
      case '4':
        console.log('Saindo...');
        return main();
        break;
      default:
        console.log('Opção inválida. Tente novamente.');
        menuPrincipal();
    }
  });
}

function menuAdmin() {
  console.log('\nSeja bem vindo, Admin!\n');
  console.log('1. Adicionar filme ao catálogo');
  console.log('2. Remover filme do catálogo');
  console.log('3. Ver catálogo de filmes');
  console.log('4. Sair');
  readline.question('Escolha uma opção: ', opcao => {
    switch (opcao) {
      case '1':
        console.log("\n");
        adicionarFilmeAoCatalogo();
        break;
      case '2':
        console.log("\n");
        removerFilmeDoCatalogo();
        break;
      case '3':
        console.log("\n");
        verCatalogoFilmes();
        break;
      case '4':
        return main();
      default:
        console.log('Opção inválida. Tente novamente.');
        menuAdmin();
    }
  });
}

function verCatalogoFilmes() {
  fs.readFile(catalogoFilmes, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      console.log(data);
      if (adminLogado) {
        menuAdmin();
      } else {
        menuPrincipal();
      }
    }
  });
}

function avaliarFilmes() {
  fs.readFile(catalogoFilmes, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      const filmes = data.split('\n');
      let id = 1;
      for (const filme of filmes) {
        console.log(`${id}. ${filme}`);
        id++;
      }
      readline.question('\nEscolha um filme para avaliar (digite o número do filme): ', filmeEscolhido => {
        readline.question('\nAvalie o filme com uma nota de 0.5 a 5: ', nota => {
          if (nota < 0.5 || nota > 5) {
            console.log('Nota inválida. Tente novamente.');
            avaliarFilmes();
          } else {
            readline.question('\nAdicione sua opinião sobre o filme: ', opiniao => {
              fs.appendFile(avaliacoesFilmes, `Filme ${filmeEscolhido} - Nota ${nota} - Opinião: ${opiniao}\n`, (err) => {
                if (err) {
                  console.error('Erro ao criar o arquivo.');
                } else {
                  console.log('Avaliação salva com sucesso!');
                  menuPrincipal();
                }
              });
            });
          }
        });
      });
    }
  });
}

function alugarFilmes() {
  fs.readFile(catalogoFilmes, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      const filmes = data.split('\n');
      let id = 1;
      for (const filme of filmes) {
        console.log(`${id}. ${filme}. `);
        id++;
      }
      readline.question('\nEscolha um filme para alugar (digite o número do filme): ', filmeAlugado => {
        if (filmeAlugado < 1 || filmeAlugado > id - 1) {
          console.log('Erro: Filme inválido.');
          alugarFilmes();
        } else {
          const data = new Date();
          const datavenc = new Date();
          datavenc.setDate(datavenc.getDate() + 30)
          readline.question('\nDigite seu CPF: ', cpf => {
            fs.appendFile(alugados, `CPF: ${cpf} - Número do filme alugado: ${filmeAlugado} - data do aluguel: ${data.toLocaleDateString()} - data de vencimento do aluguel:${datavenc.toLocaleDateString()}\n`, (err) => {
              if (err) {
                console.error('Erro ao abrir o arquivo de alugados.');
              } else {
                console.log('Filme alugado com sucesso!');
                menuPrincipal();
              }
            });
          });
        }
      });
    }
  });
}

function adicionarFilmeAoCatalogo() {
  readline.question('Digite o título do filme: ',titulo => {
    readline.question('Digite o ano do filme: ',ano => {
         readline.question('Digite a categoria do filme: ',categoria => {
      fs.appendFile(catalogoFilmes, `\n${titulo},${ano} ,${categoria}`, (err) => {
        if (err) {
          console.error('Erro ao criar o arquivo.');
        } else {
          console.log('Filme adicionado ao catálogo com sucesso!');
          menuAdmin();
        }
      });
    });
  });
  });
}

function removerFilmeDoCatalogo() {
  fs.readFile(catalogoFilmes, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      const filmes = data.split('\n');
      let id = 1;
      for (const filme of filmes) {
        console.log(`${id}. ${filme}`);
        id++;
      }
      readline.question('Escolha um filme para remover (digite o número do filme): ', filmeRemovido => {
        const filmesArray = data.split('\n');
        filmesArray.splice(filmeRemovido - 1, 1);
        const novoCatalogo = filmesArray.join('\n');
        fs.writeFile(catalogoFilmes, novoCatalogo, (err) => {
          if (err) {
            console.error('Erro ao remover o filme do catálogo.');
          } else {
            console.log('Filme removido do catálogo com sucesso!');
            menuAdmin();
          }
        });
      });
    }
  });
}

main();
