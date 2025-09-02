class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*obj):
    for obj in obj:
        print(obj)
    

alun_1 = Estudante("Alex", 1)
alun_2 = Estudante("Lopes", 2)
mostrar_valores(alun_1, alun_2)

Estudante.escola = "Python"
alun_3 = Estudante("Ferreira", 3)
mostrar_valores(alun_1, alun_2, alun_3)
