'''
Escreva um programa que contenha uma função que receba um número
inteiro como parâmetro e retorne se ele é primo ou não.
'''

def verificarPrimo(n):
    ehPrimo = True

    for i in range(n-1, 1, -1):
        if n%i == 0:
            ehPrimo = False
    
    return ehPrimo

# Início do Programa

print('7 é primo?', verificarPrimo(7))

print('10 é primo?', verificarPrimo(10))

print('77 é primo?', verificarPrimo(77))
