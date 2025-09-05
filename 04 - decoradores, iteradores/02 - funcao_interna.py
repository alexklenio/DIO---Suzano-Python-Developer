def principal():
    print("Executando a função principal")

    def funcao_interna():
        print("exevutando a funcao interna")

    def funcao_02():
        print('executando a funcao 2')


    funcao_interna()
    funcao_02()


principal()