'''
Faça um programa que leia uma lista com 20 números inteiros.
Escreva os elementos da lista eliminando os elementos repetidos.
'''

def lerNumeros():
    lista = []

    for i in range(0, 20, 1):
        num = int(input('Digite um nro: '))      
        lista.append(num)

    return lista

def eliminarRepetidos(lista):
    tam = len(lista)

    i=0
    while (i<tam):
        if i<tam:
            if lista[i] in lista[i+1:]:
                print(lista[i], ' --> ', lista[i+1:])
                del(lista[i])
                i-=1
                tam = len(lista)
        i+=1      

# Início do Programa

lista = lerNumeros()

print('ANTES remover repetidos: ', lista)

eliminarRepetidos(lista)

print('DEPOIS remover repetidos: ', lista)



