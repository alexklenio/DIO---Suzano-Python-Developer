def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10,35,85,46,13]))

def retornar_sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(retornar_sucessor_antecessor(47))

def salvar_carro(ano, modelo, marca, placa):
    print(f'Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}')


salvar_carro(marca='Fiat', modelo = 'Palio', ano = 1999, placa = 'ABC-1234') #RECEBE OS DADOS MARCADOS
salvar_carro(**{'marca':'Renault', 'modelo':'Sandero', 'ano': 2010, 'placa':'ABC-3214'})#RECEBE UM DICIONÁRIO