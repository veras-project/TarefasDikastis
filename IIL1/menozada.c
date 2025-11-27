#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

float calcular_media_final(float todas_notas[], int tamanho)
{
    float menor_nota=999, segunda_menor_nota=999;
    for(int i=0;i<tamanho;i++)
    {
        if(todas_notas[i]<menor_nota)
        {
            segunda_menor_nota=menor_nota;
            menor_nota=todas_notas[i];
        }
        else if(todas_notas[i]<segunda_menor_nota)
        {
            segunda_menor_nota=todas_notas[i];
        }
    }
    float sum=0;
    for(int j=0;j<tamanho;j++)
    {
        sum+=todas_notas[j];
    }
    sum=sum-menor_nota-segunda_menor_nota;
    return sum/(tamanho-2);
}

int main() 
{
    int N=0;
    scanf("%d",&N);
    if(N<=3)
    {
        printf("Numero de notas insuficiente.\n");
    }
    else
    {
        float numbers[101];
        for(int i=0;i<N;i++)
        {
            scanf("%f",&numbers[i]);
        }
        float media_no_jeitin=calcular_media_final(numbers,N);
        printf("%.2f",media_no_jeitin);
    }
	return 0;
}