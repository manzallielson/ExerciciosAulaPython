'''
4)	Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:

Digite um número: 5
Resultado:
1*-*-*-*-*
2-*-*-*-*
3--*-*-*
4---*-*
5----*
'''

num = int(input('Digite um numero: '))

for linha in range(1,num+1,+1):
    # Impressão dos -
    print('-' * (linha-1), end='')
    
    # Impressão de *
    print('*', end='')

    # Impressão dos -*
    print('-*' * (num-linha))
    
