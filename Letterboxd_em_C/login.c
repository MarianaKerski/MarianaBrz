#include <stdio.h>
#include <string.h>

#define MAX_CPF 12
#define MAX_SENHA 20
#define BANCO_DE_DADOS "banco_de_dados.txt"

void registrar_usuario() {
    char cpf[MAX_CPF];
    char senha[MAX_SENHA];

    printf("Digite seu CPF: ");
    scanf("%11s", cpf);

    printf("Digite sua senha: ");
    scanf("%19s", senha);

    FILE *fp = fopen(BANCO_DE_DADOS, "a");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo de banco de dados!\n");
        return;
    }

    fprintf(fp, "%s:%s\n", cpf, senha);
    fclose(fp);

    printf("Usuário registrado com sucesso!\n");
    return main();
}

int login_usuario() {
    char cpf[MAX_CPF];
    char senha[MAX_SENHA];

    printf("Digite seu CPF: ");
    scanf("%11s", cpf);

    printf("Digite sua senha: ");
    scanf("%19s", senha);

    FILE *fp = fopen(BANCO_DE_DADOS, "r");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo de banco de dados!\n");
        return 0;
    }

    char linha[256];
    while (fgets(linha, sizeof(linha), fp)) {
        char *token = strtok(linha, ":");
        if (strcmp(token, cpf) == 0) {
            token = strtok(NULL, "\n");
            if (strcmp(token, senha) == 0) {
                fclose(fp);
                return 1; // login bem-sucedido
            }
        }
    }

    fclose(fp);
        int escolha1;
    printf("deseja Registrar-se ou tentar novamente?\n");
    printf("1. Registrar\n2. tentar novamente\n");
    printf("Digite sua escolha: ");
    scanf("%d", &escolha1);
         
    if (escolha1 == 1) {
        registrar_usuario();
    } else if (escolha1 == 2) {
        login_usuario(); 
    }
    return 0; // login falhou
}

int main() {
    int escolha;
    printf("1. Registrar\n2. Login\n");
    printf("Digite sua escolha: ");
    scanf("%d", &escolha);

    if (escolha == 1) {
        registrar_usuario();
    } else if (escolha == 2) {
        if (login_usuario()) {
            printf("Login bem-sucedido!\n");
    } else {
        printf("CPF ou senha inválidos!\n");
           
        }
    } else {
        printf("Escolha inválida!\n");
        return main();
    }

    return 0;
}