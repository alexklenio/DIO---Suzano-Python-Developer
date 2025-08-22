def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10,35,85,46,13]))

def retornar_sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(retornar_sucessor_antecessor(47))