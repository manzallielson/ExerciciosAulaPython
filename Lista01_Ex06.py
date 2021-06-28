'''
6)	Utilizando o mesmo conceito anterior, solicite ao usuário um número
e com este número construa um quadrado conforme exemplo abaixo:

Digite um número: 5
Resultado:
O-----O
-     -
-     -
-     -
O-----O
'''

num = int(input('Digite um numero: '))

for linha in range(1, num+1, +1):
    if linha == 1 or linha == num:
        print('O' + '-'*num + 'O')
    else:
        print('-' + ' '*num + '-')
