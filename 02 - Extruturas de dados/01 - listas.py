frutas = ['maçã', 'laranja', 'uva', 'pêra']

frutas[0] #maçã
frutas[2] #uva

frutas[-1] #pêra
frutas[-3] #laranja

#matriz = [
#    [ 1 ,'a', 2]
#    ['b', 3 , 4]
#    ['c', 5 , 6]
#]

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(f'O modelo do veículo é {carro}.')

print()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

print()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
print()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

pares2=[numero for numero in numeros if numero % 2 != 0]

print(pares2)
print()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
