'''
Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:
Digite um número: 5
Resultado:
1 *
2 **
3 ***
4 ****
5 *****

'''

num = int(input('Digite um numero: '))

for i in range(1, num+1):
    print('*' * i)

    
