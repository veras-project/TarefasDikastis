#Definições Bases

docesbons=[]
docesdescartados=[]
tierdoce=[]

round_sweet=['Mentos','Jujuba']
large_sweet=['Bolo de rolo', 'Barra de chocolate','Banda de ovo de Páscoa']
holein_sweet=['Pretzel', 'Donuts']

flnddodoce=input()

itenstops=0

#O print aí de bobs

print('Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!')

#Meu Looping que espero que de certo uhul

while flnddodoce!= 'Recursos Esgotados':

    if flnddodoce == 'O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!':

        docesdescartados+=docesbons
        docesbons.clear()
        tierdoce.clear()
        print('Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO')

    else:
        auxlist=flnddodoce.split(' - ')

        if auxlist[1] == 'estragado':

            docesdescartados.append(auxlist[0])

        else:

            if auxlist[0] in round_sweet:
                alpha=0
                jatemdesse=False
                beta=None
                for i in docesbons:
                    if i in round_sweet:
                        jatemdesse=True
                        alpha+=1
                        beta=i
                        
                    elif i not in round_sweet and alpha==0:
                        jatemdesse=False

                if jatemdesse and auxlist[1]=='qualidade mediana':

                    docesdescartados.append(auxlist[0])

                elif jatemdesse and auxlist[1]=='alta qualidade':

                    isthereagod=docesbons.index(beta)

                    if tierdoce[isthereagod] =='alta qualidade':
                        docesdescartados.append(auxlist[0])
                    else:
                        doce_antigo_removido = docesbons.pop(isthereagod)
                        tierdoce.pop(isthereagod)
                        docesdescartados.append(doce_antigo_removido)
                        docesbons.append(auxlist[0])
                        tierdoce.append(auxlist[1])                
                else:
                    docesbons.append(auxlist[0])
                    tierdoce.append(auxlist[1])

            elif auxlist[0] in large_sweet:

                alpha=0
                jatemdesse=False
                beta = None

                for i in docesbons:
                    if i in large_sweet:
                        jatemdesse=True
                        alpha+=1
                        beta=i
                        
                    elif i not in large_sweet and alpha==0:
                        jatemdesse=False

                if jatemdesse and auxlist[1]=='qualidade mediana':

                    docesdescartados.append(auxlist[0])

                elif jatemdesse and auxlist[1]=='alta qualidade':

                    isthereagod=docesbons.index(beta)

                    if tierdoce[isthereagod] =='alta qualidade':
                        docesdescartados.append(auxlist[0])
                    else:
                        doce_antigo_removido = docesbons.pop(isthereagod)
                        tierdoce.pop(isthereagod)
                        docesdescartados.append(doce_antigo_removido)
                        docesbons.append(auxlist[0])
                        tierdoce.append(auxlist[1])                   
                else:
                    docesbons.append(auxlist[0])
                    tierdoce.append(auxlist[1])
                
            elif auxlist[0] in holein_sweet:
                alpha=0
                jatemdesse=False
                beta=None
                for i in docesbons:
                    if i in holein_sweet:
                        jatemdesse=True
                        alpha+=1
                        beta=i
                        
                    elif i not in holein_sweet and alpha==0:
                        jatemdesse=False

                if jatemdesse and auxlist[1]=='qualidade mediana':

                    docesdescartados.append(auxlist[0])

                elif jatemdesse and auxlist[1]=='alta qualidade':

                    isthereagod=docesbons.index(beta)

                    if tierdoce[isthereagod] =='alta qualidade':
                        docesdescartados.append(auxlist[0])
                    else:
                        doce_antigo_removido = docesbons.pop(isthereagod)
                        tierdoce.pop(isthereagod)
                        docesdescartados.append(doce_antigo_removido)
                        docesbons.append(auxlist[0])
                        tierdoce.append(auxlist[1])                     
                else:
                    docesbons.append(auxlist[0])
                    tierdoce.append(auxlist[1])


    flnddodoce=input()

for j in tierdoce:
    if j =='alta qualidade':
        itenstops+=1

#Uma Gambiarra Pro Print

for k in docesbons:
    if k in large_sweet:
        estrutura=k
    elif k in holein_sweet:
        volante=k
    elif k in round_sweet:
        doce_rodas=k    
    
#Os prints

if itenstops>=1 and len(docesbons)==3:
    print('Conseguimos! Impossível você não ganhar essa corrida, Vanellope!')
    print(f'Para fazer o carro você utilizou {estrutura} para ser a estrutura do carro, {volante} para o volante, {doce_rodas} para compor as rodas!')
elif itenstops==0 and len(docesbons)==3:
    print('Pelo menos anda! Você consegue!')
else:
    print('Sinto muito, Vanellope. Não consegui te ajudar dessa vez.')

if len(docesdescartados) != 0:
    print('Alguns doces foram descartados. São eles:')
    texto_final = ", ".join(docesdescartados)
    
    print(texto_final)
        
