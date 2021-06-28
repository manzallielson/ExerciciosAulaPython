'''
Escreva um programa que contenha uma função que receba dois números inteiros
como parâmetros: o primeiro será a base e o segundo, o expoente.
A função retornará o valor do cálculo da potenciação destes números (base^expoente).
Ex.: base = 2; expoente = 3; a função retornará 8.
'''

def calculaPotencia(base, expoente):

    if expoente<0:
        base = 1 / base
        expoente *= -1

    res = 1

    for i in range(0, expoente):
        res = res * base

    return res


# Início do Programa

print(calculaPotencia(2, 3))

print(calculaPotencia(2, -3))

print(calculaPotencia(2, 0))
