#include <stdio.h>
#include <stdlib.h>

#define MAX_LINHA 1024

int main() {
    int option;
    FILE *arquivo;
    char linha[MAX_LINHA];

    do {
        printf("\n");
        printf("Menu:\n");
        printf("1. Ver catálogo de filmes\n");
        printf("2. Avaliar filmes\n");
        printf("3. Sair\n");
        printf("Escolha uma opção: ");

        scanf("%d", &option);

        switch (option) {
            case 1:
                printf("Você escolheu ver catálogo de filmes.\n\n");

                // Abrir o arquivo de texto
                arquivo = fopen("catalogo_filmes.txt", "r");
                if (arquivo == NULL) {
                    printf("Erro ao abrir o arquivo.\n");
                    break;
                }

                // Ler e exibir o catálogo de filmes
                while (fgets(linha, MAX_LINHA, arquivo) != NULL) {
                    printf("%s", linha);
                }

                // Fechar o arquivo de texto
                fclose(arquivo);
                break;
            case 2:
                printf("Você escolheu avaliar filmes.\n");

                // Abrir o arquivo de texto para ler o catálogo de filmes
                arquivo = fopen("catalogo_filmes.txt", "r");
                if (arquivo == NULL) {
                    printf("Erro ao abrir o arquivo.\n");
                    break;
                }

                // Ler o catálogo de filmes e exibir as opções para avaliação
                int filme_id = 1;
                while (fgets(linha, MAX_LINHA, arquivo) != NULL) {
                    printf("%d. %s", filme_id, linha);
                    filme_id++;
                }

                // Fechar o arquivo de texto
                fclose(arquivo);

                // Solicitar ao usuário escolher um filme para avaliar
                int filme_escolhido;
                printf("\n\nEscolha um filme para avaliar (digite o número do filme): ");
                scanf("%d", &filme_escolhido);

                // Solicitar ao usuário avaliar o filme com uma nota de 1 a 5
                int nota;
                printf("\nAvalie o filme com uma nota de 1 a 5: ");
                scanf("%d", &nota);

                // Verificar se a nota é válida
                if (nota < 1 || nota > 5) {
                    printf("Nota inválida. Tente novamente.\n");
                    break;
                }

                // Solicitar ao usuário adicionar sua opinião sobre o filme
                char opiniao[MAX_LINHA];
                printf("\nAdicione sua opinião sobre o filme: \n");
                fgets(opiniao, MAX_LINHA, stdin);

                // Remover o caractere de newline da opinião
                opiniao[strcspn(opiniao, "\n")] = 0;

                // Abrir o arquivo de texto para salvar a avaliação
                arquivo = fopen("avaliacoes_filmes.txt", "a");
                if (arquivo == NULL) {
                    printf("Erro ao abrir o arquivo.\n");
                    break;
                }

                // Salvar a avaliação no arquivo
                fprintf(arquivo, "Filme %d: Nota %d - %s\n", filme_escolhido, nota, opiniao);

                // Fechar o arquivo de texto
                fclose(arquivo);

                printf("Avaliação salva com sucesso!\n");
                break;
            case 3:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (option != 3);

    return 0;
}