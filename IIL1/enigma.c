#include <stdio.h>

int main() {

    char alfabeto[53] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int chave;
    char mensagem_cifrada[52];

    scanf("%d", &chave);
    getchar();

    do {
        scanf("%[^\n]", mensagem_cifrada);
        getchar();

        if (!(mensagem_cifrada[0] == 'F' && mensagem_cifrada[1] == 'I' && mensagem_cifrada[2] == 'M' && mensagem_cifrada[3] == '\0')) {
            
            int posicao_letra = 1;
            for (int i = 0; mensagem_cifrada[i] != '\0'; i++) {

                char letra_atual = mensagem_cifrada[i];

                if (letra_atual == ' ') {
                    printf(" ");
                    continue;
                }

                int indice_original = -1;
                for (int j = 0; j < 52; j++) {
                    if (alfabeto[j] == letra_atual) {
                        indice_original = j;
                        break;
                    }
                }

                if (indice_original != -1) {
                    int deslocamento = chave + posicao_letra;
                    int novo_indice = indice_original - deslocamento;

                    while (novo_indice < 0) {
                        novo_indice = novo_indice + 52;
                    }
                    
                    novo_indice = novo_indice % 52;

                    printf("%c", alfabeto[novo_indice]);
                    posicao_letra++;
                }
            }
            printf("\n");
        }

 
    } while (!(mensagem_cifrada[0] == 'F' && mensagem_cifrada[1] == 'I' && mensagem_cifrada[2] == 'M' && mensagem_cifrada[3] == '\0'));

    return 0;
}