

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")
        saldo -= valor
        print(f"Seu novo saldo é R$ {saldo:.2f}")
       

sacar(100)


