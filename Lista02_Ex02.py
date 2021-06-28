'''
Escreva um programa que contenha uma função que calcule o fatorial de
um número inteiro.
7! = 7*6*5*4*3*2*1
'''

def fatorial(n):
    fat = 1

    for i in range(n,0,-1):
        fat = fat * i
    
    return fat

# Início do Programa

print('7! = ', fatorial(7))

print('5! = ', fatorial(5))

print('20! = ', fatorial(20))
