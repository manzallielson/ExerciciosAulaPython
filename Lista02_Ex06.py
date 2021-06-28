'''
Peça ao usuário para digitar vários números e armazene-os em um vetor (lista).
Se o usuário digitar um número ZERO pare de armazenar os números.
Em seguida, crie um vetor somente com os números positivos e
outro vetor somente com os números negativos.
Depois apresente o resultado do valor do somatório dos números negativos e
dos números positivos. 
'''

def lerNumeros():
    lista = []
    
    num = float(input('Digite um nro: '))

    while num!=0:
        lista.append(num)

        num = float(input('Digite um nro: '))

    return lista

def separarPositivosNegativos(lista):
    listaPOS = []
    listaNEG = []

    for elem in lista:
        if elem>=0:
            listaPOS.append(elem)
        else:
            listaNEG.append(elem)

    return listaPOS, listaNEG

def somatorioLista(lista):
    soma = 0

    for elem in lista:
        soma = soma + elem

    return soma
    
# Início do Programa

lPos=[]
lNeg=[]

lista = lerNumeros()

lPos, lNeg = separarPositivosNegativos(lista)

print('Positivos = ', lPos, 'Somatorio = ', somatorioLista(lPos))
print('Negativos = ', lNeg, 'Somatorio = ', somatorioLista(lNeg))





