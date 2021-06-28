'''
Peça ao usuário para digitar vários números e armazene-os em um vetor (lista).
Se o usuário digitar um número ZERO pare de armazenar os números.
Depois apresente a quantidade de números negativos e dos números
positivos digitados. 
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
    
# Início do Programa

lPos=[]
lNeg=[]

lista = lerNumeros()

lPos, lNeg = separarPositivosNegativos(lista)

print('Qtd Positivos = ', len(lPos))
print('Qtd Negativos = ', len(lNeg))



