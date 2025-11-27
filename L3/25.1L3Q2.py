#Primeros Infos

n_jinwoo=int(input())
qtd=int(input())
morreu=False
aux=1
armyjin=[]
listafinal=[]

#Looping

while(not morreu and aux<=qtd):
    aux+=1

    nome_criatura=input()
    nivel_criatura=int(input())
    
    if nivel_criatura<n_jinwoo:
        resposta=input()

        if resposta=='Erga-se':
            armyjin.append(nome_criatura)
            n_jinwoo+=(nivel_criatura//3)   
    else:
        morreu=True  
        print(f'Jin-Woo foi derrotado por {nome_criatura}...') 

if(not morreu):
    print(f'Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!')
    print(f'===== Exército das Sombras de Jin-Woo =====')
    if(len(armyjin)==0):
        print('Jin-Woo não conseguiu formar seu exército...')
    else:
        for i in armyjin:
            if i not in listafinal:
                listafinal.append(i)
                print(f'{i}: {armyjin.count(i)}')

else:
    print(f'===== Exército das Sombras de Jin-Woo =====')
    if(len(armyjin)==0):
        print('Jin-Woo não conseguiu formar seu exército...')
    else:
        for i in armyjin:
            if i not in listafinal:
                listafinal.append(i)
                print(f'{i}: {armyjin.count(i)}')