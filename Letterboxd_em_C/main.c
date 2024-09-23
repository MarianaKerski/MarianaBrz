#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINHA 1024
#define MAX_CPF 12

int main() {
    int option;
    FILE *arquivo;
    char linha[MAX_LINHA];

    do {
        printf("\n");
        printf("Seja bem vindo \n");
        printf("1. Ver catálogo de filmes\n");
        printf("2. Avaliar filmes\n");
        printf("3. Alugar filmes\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");

        scanf("%d", &option);
        getchar(); // Limpar o buffer de entrada

        switch (option) {
            case 1:
                printf("\nVocê escolheu ver catálogo de filmes.\n\n");

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
                getchar(); // Limpar o buffer de entrada

                // Solicitar ao usuário avaliar o filme com uma nota de 1 a 5
                float nota;
                printf("\nAvalie o filme com uma nota de 1 a 5: ");
                scanf("%f", &nota);
                getchar(); // Limpar o buffer de entrada

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
                // Criar o arquivo se ele não existir
                arquivo = fopen("avaliacoes_filmes.txt", "w");
                    if (arquivo == NULL) {
                printf("Erro ao criar o arquivo.\n");
                break;
            }
                }

                // Salvar a avaliação no arquivo
                fprintf(arquivo, "Filme %d: Nota %f - Opinião: %s\n", filme_escolhido, nota, opiniao);

                // Fechar o arquivo de texto
                fclose(arquivo);

                printf("Avaliação salva com sucesso!\n");
                break;
                
            case 3:
                arquivo = fopen("alugar.txt", "r");
                if (arquivo == NULL) {
                    printf("Erro ao abrir o arquivo.\n");
                    break;
                }

                // Ler o catálogo de filmes e exibir as opções para alugar
                int aluga_id = 1;
                while (fgets(linha, MAX_LINHA, arquivo) != NULL) {
                    printf("%d. %s", aluga_id, linha);
                    aluga_id++;
                }

                // Fechar o arquivo de texto
                fclose(arquivo);

                //escolher um filme para alugar
                int filme_alugado;
                printf("\n\nEscolha um filme para alugar (digite o número do filme): ");
                scanf("%d", &filme_alugado);
                getchar(); // Limpar o buffer de entrada
                
                // Check if the chosen movie is valid
                if (filme_alugado < 1 || filme_alugado > aluga_id - 1) {
                    printf("Erro: Filme inválido.\n");
            } else {
                // Mark the movie as rented in the catalog file
                arquivo = fopen("alugar.txt", "r+");
                if (arquivo == NULL) {
                    printf("Erro ao abrir o arquivo.\n");
                break;
            }

                // Move the file pointer to the chosen movie's line
                fseek(arquivo, (filme_alugado - 1) * MAX_LINHA, SEEK_SET);

                 // Read the movie's title and mark it as rented
                char linha[MAX_LINHA];
                fgets(linha, MAX_LINHA, arquivo);
                char* titulo = strtok(linha, "\n");
                printf("Você escolheu alugar o filme: %s\n", titulo);

                // Update the catalog file to reflect the changes
                fseek(arquivo, (filme_alugado - 1) * MAX_LINHA, SEEK_SET);
                fprintf(arquivo, "%s (Alugado)\n", titulo);

                fclose(arquivo);
            }
            
            case 4:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
        }
    } while (option != 4);

    return 0;
}
