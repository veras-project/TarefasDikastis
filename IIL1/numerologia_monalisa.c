#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int d_dia, d_mes, d_ano, niver_dia, niver_mes, niver_ano;
    
    scanf("%d/%d/%d", &d_dia, &d_mes, &d_ano);
    scanf("%d/%d/%d", &niver_dia, &niver_mes, &niver_ano);

    //Amor
    int prob_amor = ((d_dia + d_mes + d_ano + niver_dia + niver_mes + niver_ano)*7)%101;
    printf("Amor: %d%% ", prob_amor);
    if(prob_amor < 20)
    {
        printf("Pessimo dia para se apaixonar.\n");
    }
    else if(prob_amor <= 40)
    {
        printf("Melhor manter o coracao <3 longe de perigo.\n");
    }
    else if(prob_amor <= 69) 
    {
        printf("Se o papo e as ideias baterem, esta liberado pensar em algo.\n");
    }
    else if(prob_amor <= 80)
    {
        printf("Saia com o coracao aberto, mas lembre, nem toda troca de olhar em onibus e sinal de romance.\n");
    }
    else
    {
        printf("Um dia deslumbrantemente lindo para amar. Ps: Cuidado com a intensidade.\n");
    }
    //Sorte

    int prob_sorte = (((d_dia +d_mes + niver_dia + niver_mes)*9)+abs(d_ano-niver_ano))%101;

    printf("Sorte: %d%% ", prob_sorte);

    if (prob_sorte < 30) 
    {
        printf("Nem jogue moedas pra cima hoje.");
    } 
    else if (prob_sorte <= 50) 
    {
        printf("Melhor nao arriscar.");
    }
    else if (prob_sorte <= 79)
    { 
        printf("Por sua conta em risco.");
    }
    else if (prob_sorte <= 90)
    { 
        printf("Hoje vale a pena arriscar.");
    }
    else
    {
        printf("Nao tenha medo de virar cartas hoje.");
    }
    printf(" Sem tigrinho nem jogos de azar, por favor!\n");

    //Trabalho

    int prob_trabalho = abs((((d_ano+niver_ano)-((d_dia+niver_dia+d_mes+niver_mes)*8))))%101;

    printf("Trabalho: %d%% ", prob_trabalho);   


    if (prob_trabalho < 40)
    {
        printf("Hoje nao sera um dia tao proveitoso, keep calm e faca o basico.\n");
    }
    else if (prob_trabalho <= 50)
    { 
        printf("Segura a emocao, nao xinga ninguem, nao esquece de beber agua.\n");
    }
    else if (prob_trabalho <= 69) 
    { 
        printf("Um dia proveitoso com certeza, leve sua simpatia consigo.\n");
    }
    else if (prob_trabalho <= 84)
    { 
        printf("Boas vibracoes hoje, chances podem estar ao seu redor.\n");
    }
    else
    { 
        printf("Use do maximo de networking possível hoje, dia bom para negocios.\n");
    }

    //Cor
    int numero_cor = ((d_dia * d_dia) + (d_mes * d_mes) + (d_ano * d_ano)+(niver_dia * niver_dia) + (niver_mes * niver_mes) + (niver_ano * niver_ano)) % 11;

    printf("Cor: ");

    switch (numero_cor) 
    {
        case 0:
            printf("Cinza.\n");
            break; 
        case 1:
            printf("Vermelho.\n");
            break;
        case 2:
            printf("Laranja.\n");
            break;
        case 3:
            printf("Amarelo.\n");
            break;
        case 4:
            printf("Verde.\n"); 
            break;
        case 5:
            printf("Azul.\n");
            break;
        case 6:
            printf("Roxo.\n");
            break;
        case 7:
            printf("Marrom.\n");
            break;
        case 8:
            printf("Rosa.\n");
            break;
        case 9:
            printf("Preto.\n");
            break;
        case 10:
            printf("Branco.\n");
            break;
        default:
            printf("Se apareceu isso, deu bronca hehe");
            break;
    }
    return 0;
}