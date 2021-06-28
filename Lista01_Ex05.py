'''
5)	Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:

Digite um número: 5
Resultado:
*
**
***
**
*
Digite um número: 6
Resultado:
1*
2**
3***
3***
2**
1*

'''

num = int(input('Digite um numero: '))
metade = num//2

for linha in range(1,metade+1,+1):
    # Impressão dos *
    print('*' * linha)

# Impressao qdo impar
if num%2 != 0:
    print('*' * (metade+1))

for linha in range(metade,0,-1):
    # Impressão dos *
    print('*' * linha)
    
   
