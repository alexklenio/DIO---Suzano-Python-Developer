def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar')
        funcao(*args, **kwargs)
        print('Faz depois antes de executar')

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f'Olá mundo {nome}!')

#ola_mundo = meu_decorador(ola_mundo)
ola_mundo('João')