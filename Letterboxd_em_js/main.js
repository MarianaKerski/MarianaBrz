const fs = require('fs');
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const fileName = 'users.txt';
const catalogoFilmes = 'catalogo_filmes.txt';
const avaliacoesFilmes = 'avaliacoes_filmes.txt';
const alugados = 'alugados.txt';

function main() {
  console.log('1 - Cadastrar\n2 - Entrar');
  readline.question('Escolha uma opção: ', option => {
    switch (option) {
      case '1':
        cadastrarUsuario();
        break;
      case '2':
        loginUsuario();
        break;
      default:
        console.log('Opção inválida. Tente novamente.');
        main();
    }
  });
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
  const user = `${username}:${password}\n`;
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

function menuPrincipal() {
  console.log('\nSeja bem vindo!\n');
  console.log('1. Ver catálogo de filmes\n');
  console.log('2. Avaliar filmes\n');
  console.log('3. Alugar filmes\n');
  console.log('4. Sair\n');
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
        process.exit();
        break;
      default:
        console.log('Opção inválida. Tente novamente.');
        menuPrincipal();
    }
  });
}

function verCatalogoFilmes() {
  fs.readFile(catalogoFilmes, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      console.log(data);
      menuPrincipal();
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
      readline.question('Escolha um filme para avaliar (digite o número do filme): ', filmeEscolhido => {
        readline.question('Avalie o filme com uma nota de 1 a 5: ', nota => {
          if (nota < 0.5 || nota > 5) {
            console.log('Nota inválida. Tente novamente.');
            avaliarFilmes();
          } else {
            readline.question('Adicione sua opinião sobre o filme: ', opiniao => {
              fs.appendFile(avaliacoesFilmes, `Filme ${filmeEscolhido}: Nota ${nota} - Opinião: ${opiniao}\n`, (err) => {
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
  fs.readFile(alugados, 'utf8', (err, data) => {
    if (err) {
      console.error('Erro ao abrir o arquivo.');
    } else {
      const filmes = data.split('\n');
      let id = 1;
      for (const filme of filmes) {
        console.log(`${id}. ${filme}`);
        id++;
      }
      readline.question('Escolha um filme para alugar (digite o número do filme): ', filmeAlugado => {
        if (filmeAlugado < 1 || filmeAlugado > id - 1) {
          console.log('Erro: Filme inválido.');
          alugarFilmes();
        } else {
          readline.question('Digite seu CPF: ', cpf => {
            fs.appendFile(alugados, `${cpf} - ${filmeAlugado}\n`, (err) => {
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

main();