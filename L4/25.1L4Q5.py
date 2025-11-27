#Math.io, hehe
def some(x,y):
    return x+y
def multiplique(x,y):
    return x*y
def divida(x,y):
    if y==0:
        return 0
    else:
        return x//y
def subtraia(x,y):
    return x-y
#Fun?No.Ções
def decodificador_polonês(expressao_alfanumerica):
    jainverteu=False
    stack=[]
    for j in expressao_alfanumerica[::-1]:
        if str(j).isnumeric():
            stack.append(j)
        else:
            if not jainverteu:
                lista_aux=stack[::-1]
                jainverteu=True
            if j =='*':
                aux1=lista_aux.pop(0)
                aux2=lista_aux.pop(0)
                lista_aux.insert(0,multiplique(aux1,aux2))

            elif j =='+':
                aux1=lista_aux.pop(0)
                aux2=lista_aux.pop(0)
                lista_aux.insert(0,some(aux1,aux2))

            elif j =='-':
                aux1=lista_aux.pop(0)
                aux2=lista_aux.pop(0)

                lista_aux.insert(0,subtraia(aux1,aux2))       
            else:
                aux1=lista_aux.pop(0)
                aux2=lista_aux.pop(0)
                lista_aux.insert(0,divida(aux1,aux2))
    return lista_aux[0]  
  
def checador_primo(num):
    if num <= 1:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False 
    return True

def con_bindec(num_bi_string):
    cont=0
    num_resultante=0
    for m in num_bi_string[::-1]:
        if m =='1':
            num_resultante+=(2**cont)*1
        cont+=1
    return num_resultante
    
def formador_cartesiano(num_decimal,n):
    int(n)
    return num_decimal%n
def esfera_mais_proxima(goku_initial_pos, all_sphere_x_coords, all_sphere_y_coords):
    esferas_disponiveis = []
    for i in range(len(all_sphere_x_coords)):
        esferas_disponiveis.append([all_sphere_x_coords[i], all_sphere_y_coords[i], i])

    trajetoria_completa = []
    current_goku_pos = list(goku_initial_pos)
    trajetoria_completa.append(current_goku_pos)

    while esferas_disponiveis:
        min_distancia_quadrada = float('inf')
        esfera_mais_proxima_info = None
        indice_a_remover = -1

        for i, esfera_info in enumerate(esferas_disponiveis):
            x_esfera, y_esfera, original_index = esfera_info
            
            distancia_quadrada = (x_esfera - current_goku_pos[0])**2 + \
                                 (y_esfera - current_goku_pos[1])**2

            if distancia_quadrada < min_distancia_quadrada:
                min_distancia_quadrada = distancia_quadrada
                esfera_mais_proxima_info = esfera_info
                indice_a_remover = i
            elif distancia_quadrada == min_distancia_quadrada:
                if original_index < esfera_mais_proxima_info[2]:
                    esfera_mais_proxima_info = esfera_info
                    indice_a_remover = i
        
        trajetoria_completa.append([esfera_mais_proxima_info[0], esfera_mais_proxima_info[1]])
        current_goku_pos = [esfera_mais_proxima_info[0], esfera_mais_proxima_info[1]]
        
        esferas_disponiveis.pop(indice_a_remover)

    return trajetoria_completa
#Variáveis Globais Auxiliares ou Essenciais
loc_Goku=[]
loc_esferas=[]
loc_esferasX=[]
loc_esferasY=[]
string_binaria=''
contaux=0
n_esferas=0
print('🟠 Vamos conquistar as esferas do dragão! 🟠')
print('--------------------------------------------------------------------------')
print()
#Função Primária
matriz_dimensao=int(input())
goku=input()
for i in goku:#Localização Do Goku Ajeitada
    if i !='(' and i!=')' and i!=',' and i!=' ':
        loc_Goku.append(int(i))

lista_pegadinha=input()#Questão Falou que ia escrever um nada

informacao_esfera=input()
while informacao_esfera!='Todos os bits foram decodificados':

    if informacao_esfera=='':
        num_decimal=con_bindec(string_binaria)
        pos_cartesiana=formador_cartesiano(num_decimal,matriz_dimensao)
        loc_esferas.append(pos_cartesiana)
        #Estou Adicionando Binário?
        if contaux%2==0:
            print(f'Coordenada x da {n_esferas+1}ª esfera do dragão obtida pelo código binário {string_binaria}: {pos_cartesiana}')
            loc_esferasX.append(pos_cartesiana)
        else:
            print(f'Coordenada y da {n_esferas+1}ª esfera do dragão obtida pelo código binário {string_binaria}: {pos_cartesiana}')
            loc_esferasY.append(pos_cartesiana)
        string_binaria=''
        contaux+=1
    elif informacao_esfera=='------------------------------------':
        if contaux>0:
            n_esferas+=1
            print(f'As coordenadas da {n_esferas}ª esfera do dragão são: ({loc_esferasX[(n_esferas-1)]}, {loc_esferasY[(n_esferas-1)]})')
            print()
    else:
        informacao_esfera_lista=informacao_esfera.split(' ')
        #Converter os valores numérico em inteiros; criação lista mista
        for i in informacao_esfera_lista:
            if str(i).isnumeric():
                aux=informacao_esfera_lista.index(i)
                informacao_esfera_lista[aux]=int(informacao_esfera_lista[aux])
        #Formação String Binária
        numero_decodificado=decodificador_polonês(informacao_esfera_lista)
        if checador_primo(numero_decodificado):
            string_binaria+='1'
        else:
            string_binaria+='0'
            
    informacao_esfera=input()
print(f'As coordenadas da {n_esferas+1}ª esfera do dragão são: ({loc_esferasX[(n_esferas)]}, {loc_esferasY[(n_esferas)]})')
print()
print('--------------------------------------------------------------------------')
print()

#Fiz umas mechidas para a matriz dar certo então eu criei uma variavel temporária para printar depois.
lista_ordem_goku=esfera_mais_proxima(loc_Goku,loc_esferasX,loc_esferasY)

frase_final = 'Trajetória completa de Goku: '
frase_final += f'({lista_ordem_goku[0][0]}, {lista_ordem_goku[0][1]})'
for o in range(1, len(lista_ordem_goku)):
    frase_final += f' -> ({lista_ordem_goku[o][0]}, {lista_ordem_goku[o][1]})'
frase_final += '\nMissão cumprida! Conseguimos todas as esferas do dragão!🟠🐉'

#Parte 3, printando a matriz

matriz_visual = []
for _ in range(matriz_dimensao):
    linha = []
    for _ in range(matriz_dimensao):
        linha.append('.')
    matriz_visual.append(linha)
matriz_visual[loc_Goku[0]][loc_Goku[1]] = 'G'
for x in range(len(loc_esferasX)):
   posx= loc_esferasX[x]
   posy = loc_esferasY[x]
   matriz_visual[posx][posy]='☆'
for linha in matriz_visual:
    print(' '.join(linha))
print()
print(f'{frase_final}')
