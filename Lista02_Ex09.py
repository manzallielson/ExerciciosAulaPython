'''
Faça um programa que leia uma lista de 10 números.
Leia um número x.
Conte os múltiplos de um número inteiro x contidos na lista e
mostre-os na tela. 
'''

def lerNumeros():
    lista = []

    for i in range(0, 10, 1):
        num = float(input('Digite um nro: '))      
        lista.append(num)

    return lista

def contarMultiplos(lista, num):
    qtdMultiplos = 0
    
    for elem in lista:
        if elem%num == 0:
            qtdMultiplos += 1

    return qtdMultiplos

# Início do Programa

lista = lerNumeros()

x = float(input('Digite um numero: '))

print(contarMultiplos(lista, x))




