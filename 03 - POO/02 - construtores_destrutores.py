class Cachorro:
    def __init__(self, nome, cor,acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
      

    def __del__(self):
            print('Removendo a instância da classe.')

    def falar(self):
            print('Au AU')

    


c = Cachorro('CHappie', 'amarelo')

c.falar()