class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor): #petodo contrutor (inicializador)
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Tilim, Tilim')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummmmmmmm...')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(b1)

