class Passaro:
    def voar(self):
        print('Voando.......')
        
        
class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar...")
        
class Avião(Passaro):
    def voar(self):
        print("O avião está decolando.")
        

def plano_voo(object):
    object.voar()
    
p1 = Pardal()
p2 = Avestruz()
p3 = Avião()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
        