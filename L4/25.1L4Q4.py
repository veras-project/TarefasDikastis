#Fun?No.ções

def Fusao(fusor1,fusor2):
    
    #Variáveis Internas Auxiliares
    atingiu_perfeicao=False
    resultado_fusao=''
    tam1=0
    tam2=0
    primeira_parcela_nome=''
    segunda_parcela_nome=''

    #Casos Especiais
    if (fusor1=='Goku' and fusor2=='Vegeta') or (fusor1=='Vegeta' and fusor2=='Goku'):
        resultado_fusao='Vegito'
        atingiu_perfeicao=True

    elif (fusor1=='Goten' and fusor2=='Trunks') or (fusor1=='Trunks' and fusor2=='Goten'):
        resultado_fusao='Gotenks'
        atingiu_perfeicao=True

    #Reba
    else:   
        fusor2=fusor2.lower()
        vogal='aeiouAEIOU'
        consoante='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        tam1,tam2=len(fusor1),len(fusor2)

        #Tentativa de Fusão nº1
        if tam1<=4:
            primeira_parcela_nome=fusor1[0]
        else:
            if tam1%2==0:
                aux=int(tam1/2)
                primeira_parcela_nome=fusor1[:aux]
            else:
                aux=int((tam1+1)/2)
                primeira_parcela_nome=fusor1[:aux]
        
        if tam2<=4:
            if tam2==3:
                segunda_parcela_nome=fusor2[::-1][:2][::-1]
            else:
                segunda_parcela_nome=fusor2[::-1][:3][::-1]
        else:
            if tam2%2==0:
                aux=int((tam2/2)-1)     
                segunda_parcela_nome=fusor2[::-1][:aux][::-1]
            else:
                aux=int(((tam2+1)/2)-1)
                segunda_parcela_nome=fusor2[::-1][:aux][::-1]
        
        #Checando A Perfeição
        if(len(primeira_parcela_nome)+len(segunda_parcela_nome)<=3) or (primeira_parcela_nome[-1] in vogal and segunda_parcela_nome[0] in vogal) or (primeira_parcela_nome[-1] in consoante and segunda_parcela_nome[0] in consoante):
            atingiu_perfeicao=False
            print(f'A sincronização foi um desastre... {primeira_parcela_nome+segunda_parcela_nome} é uma fusão imperfeita!')
        else:
            atingiu_perfeicao=True
        
        #Tentativa de Fusão nº2
        if not atingiu_perfeicao:

            if tam1<=4:
                primeira_parcela_nome=fusor1[:2]
            else:
                if tam1%2==0:
                    aux=int((tam1/2)+1)
                    primeira_parcela_nome=fusor1[:aux]
                else:
                    aux=int(((tam1+1)/2)+1)
                    primeira_parcela_nome=fusor1[:aux]

        #Checando A Perfeição
        if(len(primeira_parcela_nome)+len(segunda_parcela_nome)<=3) or (primeira_parcela_nome[-1] in vogal and segunda_parcela_nome[0] in vogal) or (primeira_parcela_nome[-1] in consoante and segunda_parcela_nome[0] in consoante):
            atingiu_perfeicao=False
            print(f'A sincronização foi um desastre... {primeira_parcela_nome+segunda_parcela_nome} é uma fusão imperfeita!')
            
        else:
            atingiu_perfeicao=True
        
        #Tentativa de Fusão nº3
        if not atingiu_perfeicao:
            if tam1>4:
                if tam1%2==0:
                    aux=int(tam1/2)
                    primeira_parcela_nome=fusor1[:aux]
                else:
                    aux=int((tam1+1)/2)
                    primeira_parcela_nome=fusor1[:aux]
            if tam2<=4:
                segunda_parcela_nome=fusor2[::-1][:3][::-1]
            else:
                if tam2%2==0:
                    aux=int(tam2/2)
                    segunda_parcela_nome=fusor2[::-1][:aux][::-1]
                else:
                    aux=int((tam2+1)/2)
                    segunda_parcela_nome=fusor2[::-1][:aux][::-1]
        #Checando A Perfeição-Última Chance-
        if(len(primeira_parcela_nome)+len(segunda_parcela_nome)<=3) or (primeira_parcela_nome[-1] in vogal and segunda_parcela_nome[0] in vogal) or (primeira_parcela_nome[-1] in consoante and segunda_parcela_nome[0] in consoante):
            atingiu_perfeicao=False
            print(f'A sincronização foi um desastre... {primeira_parcela_nome+segunda_parcela_nome} é uma fusão imperfeita!')
            print("Aparentemente essa combinação é incompatível...")
        else:
            atingiu_perfeicao=True
        
        #Now, United

        if not atingiu_perfeicao:
            resultado_fusao=primeira_parcela_nome+segunda_parcela_nome
        else:
            resultado_fusao=primeira_parcela_nome+segunda_parcela_nome


    return resultado_fusao,atingiu_perfeicao

def poder_resultante(poder_nova_fusao,poder_total):
    poder_total+=poder_nova_fusao
    return poder_total

def calculo_do_poder(omanodafusao):
    lista_char_força=[2000,2250,2500,2750,3000]
    if len(omanodafusao)==4:
        return lista_char_força[0]
    elif len(omanodafusao)==5:
        return lista_char_força[1]
    elif len(omanodafusao)==6:
        return lista_char_força[2]
    elif len(omanodafusao)==7:
        return lista_char_força[3]
    elif len(omanodafusao)>=8:
        return lista_char_força[4]


#Listas Bases

herois = [
    'Gohan',
    'Goku',
    'Goten',
    'Kuririn',
    'Piccolo',
    'Tenshinhan',
    'Trunks',
    'Uub',
    'Vegeta',
    'Yamcha'
]

'e'


viloes = [
    'Babidi',
    'Baby',
    'Broly',
    'Buu',
    'Cell',
    'Cooler',
    'Frieza',
    'Hit',
    'Janemba',
    'Zamasu'
]
usados=[]
pow_viloes=0
pow_herois=0

#Função Principal


while pow_herois<=8000 and pow_viloes<=8000:
    sucesso_fusao=False
    nome_fusao=''
    nome1=input()
    print(f'{nome1} se elege para participar da fusão!')
    nome2=input()
    print(f'{nome2} se elege para participar da fusão!')

    while nome1 in usados or nome2 in usados:
        #Vendo Se Já Usou e Printando
        if nome1 in usados and not nome2 in usados:
            print(f'{nome1} já participou de uma fusão. Fusão inválida.')
        elif nome1 not in usados and nome2 in usados:
            print(f'{nome2} já participou de uma fusão. Fusão inválida.')
        else:
            print(f'{nome1} já participou de uma fusão. Fusão inválida.')
            print(f'{nome2} já participou de uma fusão. Fusão inválida.')
        nome1=input()
        print(f'{nome1} se elege para participar da fusão!')
        nome2=input()
        print(f'{nome2} se elege para participar da fusão!')
        
    if nome1 in herois and nome2 in herois:
        nome_fusao,sucesso_fusao=Fusao(nome1,nome2)
        if sucesso_fusao:
            print(f'Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!')
            poderdafusao=calculo_do_poder(nome_fusao)
            pow_herois=poder_resultante(poderdafusao,pow_herois)
            usados.append(nome1)
            usados.append(nome2)            
    elif nome1 in viloes and nome2 in viloes:
        nome_fusao,sucesso_fusao=Fusao(nome1,nome2)
        if sucesso_fusao:
            print(f'Fusão realizada com sucesso! {nome_fusao} entra em combate com sede de destruir Satan City!')
            poderdafusao=calculo_do_poder(nome_fusao)
            pow_viloes=poder_resultante(poderdafusao,pow_viloes)
            usados.append(nome1)
            usados.append(nome2)
    else:
        print('Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.')

#Quem Ganhou?

if pow_herois>=8000:
    print("O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.")
else:
    print("Os vilões são fortes demais! Satan City está em apuros!")
