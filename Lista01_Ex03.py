'''
3)	Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:

Digite um número: 5
Resultado:
5----*
4---*-*
3--*-*-*
2-*-*-*-*
1*-*-*-*-*
'''

num = int(input('Digite um numero: '))

for linha in range(num,0,-1):
    # Impressão dos -
    print('-' * (linha-1), end='')
    
    # Impressão de *
    print('*', end='')

    # Impressão dos -*
    print('-*' * (num-linha))
    
