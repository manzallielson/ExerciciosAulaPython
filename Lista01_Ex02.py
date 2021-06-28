'''
2)	Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:

Digite um número: 5
Resultado:
*****
****
***
**
*
'''

num = int(input('Digite um numero: '))

for linha in range(num,0,-1):
    print('*' * linha)
