#Abrindo o Código, Galvão.

actioncommands=input()
print('Go! Go! Power Rangers!')

#Variáveis de Apoio

zordlist=[]
ztp1=[]
ztp2=[]
ztp3=[]

redzord=''

greenzord=''

yellowzord=''

blackzord=''

pinkzord=''

bluezord=''


zt1=0

zt2=0

zt3=0


#Transformando Minha String em Lista

zordlist=actioncommands.split('-')

#Transformando Minha String Em Lista Mista

for i in range(1,len(zordlist),2):
    zordlist[i]=int(zordlist[i])

#Caso Mór
if 'robocin' in zordlist:

  print('Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!')

else:

    #Contando Os Tipos de Zords

    for i in range(1,len(zordlist), 2):
        pwrzord=zordlist[i]
        if(pwrzord>30):
            zt1+=1
            redzord=zordlist[i-1]
        elif(pwrzord>10 and pwrzord<=30):
            zt2+=1
            pinkzord=zordlist[i-1]
        else:
            zt3+=1 
            bluezord=zordlist[i-1]
    
    #Trabalhando Com Quem Ficou Com O Guê

    for j in range(1,len(zordlist), 2):

        pwrzord=zordlist[i]

        if(pwrzord>30):
            if(pwrzord>zordlist[zordlist.index(redzord) + 1]):
                greenzord=redzord
                redzord=zordlist[i-1]
            else:
                greenzord=zordlist[i-1]
        elif(pwrzord>10 and pwrzord<=30):
            if(pwrzord>zordlist[zordlist.index(pinkzord) + 1]):
                blackzord=pinkzord
                pinkzord=zordlist[i-1]
            else:
                blackzord=zordlist[i-1]
        else:
            if(pwrzord>zordlist[zordlist.index(bluezord)]):
                yellowzord=bluezord
                bluezord=zordlist[i-1]
            else:
                yellowzord=zordlist[i-1]

    
    #Hora Dos Print, Meu Jesus Cristo, Espero Que Dê Certo

    if zt1>=2:
        print(f'Zord do Ranger Vermelho: {redzord}')
        print(f'Zord do Ranger Verde: {greenzord}')
    elif zt1==1:
        print(f'Zord do Ranger Vermelho: {redzord}')
        print('Ranger Verde ficou sem zord!')
    else:
        print('Ranger Vermelho ficou sem zord!')
        print('Ranger Verde ficou sem zord!')

    if zt2>=2:
        print(f'Zord da Ranger Rosa: {pinkzord}')
        print(f'Zord do Ranger Preto: {blackzord}')
    elif zt2==1:
        print(f'Zord da Ranger Rosa: {pinkzord}')
        print('Ranger Preto ficou sem zord!')
    else:
        print('Ranger Rosa ficou sem zord!')
        print('Ranger Preto ficou sem zord!')

    if zt3>=2:
        print(f'Zord do Ranger Azul: {bluezord}')
        print(f'Zord da Ranger Rosa: {pinkzord}')
    elif zt3==1:
        print(f'Zord do Ranger Azul: {bluezord}')
        print('Ranger Rosa ficou sem zord!')
    else:
        print('Ranger Azul ficou sem zord!')
        print('Ranger Rosa ficou sem zord!')

    #Organizando os Zord em lista por que eu percebi tarde demais que dava pra fzr isso

    if ztp1:
        n = len(ztp1)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if ztp1[j][1] < ztp1[j + 1][1]:
                    ztp1[j], ztp1[j + 1] = ztp1[j + 1], ztp1[j]
        
        nomes_ordenados = [zord[0] for zord in ztp1]
        print(f"Zords do tipo 1: {', '.join(nomes_ordenados)}")
    else:
        print("Não temos nenhum zord do tipo 1 :(")

    if ztp2:
        n = len(ztp2)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if ztp2[j][1] < ztp2[j + 1][1]:
                    ztp2[j], ztp2[j + 1] = ztp2[j + 1], ztp2[j]

        nomes_ordenados = [zord[0] for zord in ztp2]
        print(f"Zords do tipo 2: {', '.join(nomes_ordenados)}")
    else:
        print("Não temos nenhum zord do tipo 2 :(")

    if ztp3:
        n = len(ztp3)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if ztp3[j][1] < ztp3[j + 1][1]:
                    ztp3[j], ztp3[j + 1] = ztp3[j + 1], ztp3[j]
        
        nomes_ordenados = [zord[0] for zord in ztp3]
        print(f"Zords do tipo 3: {', '.join(nomes_ordenados)}")
    else:
        print("Não temos nenhum zord do tipo 3 :(")
            
    #Os Prints + EZ

    if(zt1>1 and zt2>1 and zt3>1):
        print('Os Rangers estão prontos para montar o Megazord e derrotar Rita!')
    else:
        print('Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!')
