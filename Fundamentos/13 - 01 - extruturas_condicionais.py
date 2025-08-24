saldo = 2000
saque = float(input("Informe o valor do saque: R$ "))

if saldo >= saque:
    saldo-=saque
    print(f"Saque realizado, novo saldo R$ {saldo}")

else:
    print('Saldo insuficiente.')