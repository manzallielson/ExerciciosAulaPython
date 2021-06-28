'''
Escreva um programa que contenha uma função que calcule
o mínimo múltiplo comum (MMC) entre três números inteiros
passados como parâmetros.
Obs: Não pode ser utilizada nenhuma função pronta em Python
que faça este cálculo. Você é quem deverá implementar esta lógica.
'''

def calcularMMC(n1, n2, n3):
    i = 2
    MMC = 1

    while not(n1==1 and n2==1 and n3==1):
        mudaIncremento = True
        
        if n1%i == 0:
            n1 = n1/i
            mudaIncremento = False

        if n2%i == 0:
            n2 = n2/i
            mudaIncremento = False

        if n3%i == 0:
            n3 = n3/i
            mudaIncremento = False

        if mudaIncremento == True:
            i+=1
        else:
            MMC = MMC * i

    return MMC

# Início do Programa

print('MMC(12, 15, 18) = ', calcularMMC(12, 15, 18))
print('MMC(11, 15, 18) = ', calcularMMC(11, 15, 18))

