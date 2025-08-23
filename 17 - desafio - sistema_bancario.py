
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'\nDepósito realizado com sucesso no valor de R$ {valor:.2f}')
            print(f'\n Seu saldo atual é de R$ {saldo:.2f}.')

        else: print('Operação falhou! O valor informado é inválido')

    elif opcao == "s":
       valor = float(input("Informe o valor do saque: R$ "))

       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       excedeu_saques = numero_saques > LIMITE_SAQUES

       if excedeu_saldo:
           print('Operação falhou! Você não tem saldo suficiente.')

       elif excedeu_limite:
           print('Operação falhou! Você excedeu o limite para saque.')

       elif excedeu_saques:
           print('Operação falhou! VOcê excedeu o limite de saques diários.')
    
       elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'\nSaque realizado com sucesso no valor de R$ {valor:.2f}')
            print(f'\n Seu saldo atual é de R$ {saldo:.2f}.')

       else:
           print('Operação falhou! O valor informado é inválido')

    elif opcao == "e":

        print("\n================ EXTRATO ================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print('\nObrigado por utilizar nossos serviços e volte sempre!')
        break

    else:
        print("operação inválida, por favor selecione novamente aoperação desejada.")