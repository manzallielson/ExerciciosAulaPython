15
18
'''
Escreva um programa que contenha uma função que calcule
o mínimo múltiplo comum (MMC) entre três números inteiros
passados como parâmetros.
Obs: Não pode ser utilizada nenhuma função pronta em Python
que faça este cálculo. Você é quem deverá implementar esta lógica.
'''

def calcularMMC(num1, num2, num3):
    count = 2
    aux = 0
    elem =1

    while not(num1 == 1 and num2 == 1 and num3 == 1):
        if(num1%count != 0 and num2%count != 0 and num3% count != 0):
            count = count +1
        else:
            if(num1%count ==0):
                aux= num1//count
                num1 = aux
            if(num2%count ==0):
                aux= num2//count
                num2 = aux
            if(num3%count ==0):
                aux= num3//count
                num3 = aux
                
            elem *=count

    return elem

# Início do Programa

num1 = int(input("digite um numero :"))
num2 = int(input("digite um numero :"))
num3 = int(input("digite um numero :"))

print('MMC(', num1, ', ', num2,', ', num3,') = ', calcularMMC(num1, num2, num3))


