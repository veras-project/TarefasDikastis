#Começando as Definições

purchase_list=[]

over=False

while not over:
    action=input()
    
    if action =='Anotar ingrediente':
        purchase_list.append(input())
    
    elif action == 'Ingrediente Urgente!':
        purchase_list.insert(0,input())

    elif action == 'Saci disse que já tem':
      
        element0=input()
        
        if element0 in purchase_list:
            purchase_list.remove(element0) 
             
    elif action == 'Saci trocou a ordem':
        posinit=int(input())
        lastpos=int(input())

        purchase_list[posinit], purchase_list[lastpos]=purchase_list[lastpos], purchase_list[posinit]

    elif action == 'Organizar a lista':
        elemento1=input()
        elemento2=input()

        p1=purchase_list.index(elemento1)
        p2=purchase_list.index(elemento2)   

        purchase_list[p1], purchase_list[p2]=purchase_list[p2], purchase_list[p1]
       

    elif action == 'Deixar para depois':
        uselselmnt=input()

        purchase_list.remove(uselselmnt)

        purchase_list.append(uselselmnt)
        
    elif action == 'Ler a lista para a vovó':

        for i in purchase_list:
            if(i==purchase_list[-1]):
                print(f'{i}')
            else:
                print(f'{i},', end=' ')

    else:
        over=True
        
        print(f'Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: ', end='')

        for i in purchase_list:
            if(i==purchase_list[-1]):
                print(f'{i}')
            else:
                print(f'{i},', end=' ')