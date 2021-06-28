'''
Solicite ao usuário um número e utilizando este número imprima a figura conforme exemplo abaixo:
Digite um número: 5
Resultado:
1 *
2 **
3 ***
4 ****
5 *****

Autora: Daniele Frosoni
'''

num = int(input('Digite um numero: '))

for i in range(1, num+1):
    linha = ''
    
    # Imprimir * na mesma qtd do número da linha
    for c in range(1,i+1):
        print('*', end='')

    print(linha)

    
