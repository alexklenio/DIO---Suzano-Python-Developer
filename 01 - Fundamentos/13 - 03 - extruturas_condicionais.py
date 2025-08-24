saldo = 2400
saque = 2000

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque.")