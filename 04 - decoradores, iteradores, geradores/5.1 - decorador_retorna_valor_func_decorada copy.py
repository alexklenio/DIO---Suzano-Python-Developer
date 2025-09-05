def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('Faz depois antes de executar')
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f'Olá mundo {nome}!')
    return nome.upper()

#ola_mundo = meu_decorador(ola_mundo)
resultado = ola_mundo('João', 1000)
print(resultado)