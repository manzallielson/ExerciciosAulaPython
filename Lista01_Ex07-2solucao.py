'''
7) Exercício do X

1o----o
2-o--o
3--oo
3--oo
2-o--o
1o----o
'''

num = int(input('Digite um numero: '))
metade = num//2

# 1a metade do X
for linha in range(1, metade+1, +1):
    print(' '*(linha-1)+'O'+' '*(num-linha*2)+ 'O')

# Imprimir a linha do meio qdo IMPAR
if num%2 != 0:
    print(' '*metade + 'O')

# 2a metade do X
for linha in range(metade, 0, -1):
    print(' '*(linha-1)+'O'+' '*(num-linha*2)+ 'O')
