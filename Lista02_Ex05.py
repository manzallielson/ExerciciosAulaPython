'''
Peça ao usuário para digitar vários números positivos e armazene-os
em um vetor (lista).
Se o usuário digitar um número negativo pare de armazenar os números.
Em seguida, crie um outro vetor com estes números armazenados em
ordem invertida. 
'''

def lerNumeros():
    lista = []
    
    num = float(input('Digite um nro: '))

    while num>=0:
        lista.append(num)

        num = float(input('Digite um nro: '))

    return lista

def inverteLista(lista_para_inverter):
    lista_invertida = []

    lista_invertida = lista_para_inverter[::-1]
        
    return lista_invertida
    
# Início do Programa

lista = lerNumeros()

listainv = inverteLista(lista)

print(lista)
print(listainv)


