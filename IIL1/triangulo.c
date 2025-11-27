#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char alphabet[26]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int cade_a_letra(char letra) {
    for (int i = 0; i < 26; i++) {
        if (alphabet[i] == letra) {
            return i+1; 
        }
    }
    return 0; 
}

int main() {
    char letra;
    scanf("%c", &letra);
    int pos = cade_a_letra(letra);
    int j=0, qntd_pnts=pos-1;
    while(j<pos)
    {
        for(int i=0;i<qntd_pnts;i++)
        {
            printf(".");
        }
        for(int k=0; k<j;k++)
        {
            printf("%c",alphabet[k]);
        }
        for(int l=j;l>=0;l--)
        {
            printf("%c",alphabet[l]);
        }
        for(int i=0;i<qntd_pnts;i++)
        {
            printf(".");
        }
        printf("\n");
        j++;
        qntd_pnts--;
    }
	return 0;
}