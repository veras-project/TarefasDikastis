thanosdmg=0
arsenal=[]
atksucces=0
fim=False
armasusadas=[]

#Input

N=int(input())

for i in range(N):
    arsenal.append(input())

while not fim:
    action=input()
    if action == 'fim':
        fim=True
        print(f'Batalha encerrada! Os Vingadores utilizaram {atksucces} arma(s).')
    else:
        if((action in arsenal) and (action not in armasusadas)):
            atksucces+=1
            print(f'{action} usado(a) com sucesso!')
        else:
            if(action in armasusadas and action in arsenal):
                print(f'{action} já foi usado(a)!')
            else:
                print(f'{action} não está disponível!')

            thanosdmg+=1
    armasusadas.append(action)

if(thanosdmg==0):
    print('Vitória! Os Vingadores salvaram o UNIVERSO!')
    print('\nTony Stark:')
    print('Salvar o mundo de novo? Vou precisar de um aumento.')
    print('\nThor:')
    print('Espero que tenha cerveja depois disso!')
    print('\nHomem-Aranha:')
    print('Posso dizer que ajudei, né? Tipo… oficialmente?\nDá pra postar isso no Insta dos Vingadores?')
elif(thanosdmg==1):
    print('Os Vingadores sofreram um golpe do Thanos!\nVitória por pouco! Os Vingadores ganharam...')
    print('\nTony Stark:')
    print('Quase que eu fico sem troco para o cafezinho.')
    print('\nThor:')
    print('Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!')
    print('\nPeter Quill (Star-Lord):')
    print('Cara, quase perdi o ritmo do meu walkman!')
else:
    print(f'Os Vingadores sofreram {thanosdmg} golpes do Thanos!')
    print('Derrota... Os Vingadores não conseguiram todas as armas necessárias.')
    print('\nTony Stark:')
    print('Essa não foi das melhores ideias...')
    print('\nThor:')
    print('Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.')