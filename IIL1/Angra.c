#include <stdio.h>

int main() 
{
    int qtd_locals = 0, nice_places = 0;
    float  P=0.0, G=0.0, T=0.0, best_score = 0.0;
    char local[51],best_place[51];

    scanf("%d",&qtd_locals);

    for(int i=1; i<=qtd_locals; i++)
    {
        scanf("%s %f %f %f",local, &P,&G,&T);

        float score = (3*P + G + 2*T)/6.0;
        if(score>=3.5)
        {
            nice_places++;
            if(score>best_score)
            {
                int j = 0;
                while (local[j] != '\0') 
                {
                    best_place[j] = local[j];
                    j++;
                }
                best_place[j] = '\0';
                best_score=score;
            }
        }


    }

    if(nice_places==0)
    {
        printf("Temos 0 lugares pra visitar!\n",nice_places);
        printf("Puts. Melhor ficar em casa mesmo!\n");
    }
    else
    {
        printf("Temos %i lugares pra visitar!\n",nice_places);
        printf("Devo comecar por %s",best_place);
    }

    return 0;
}