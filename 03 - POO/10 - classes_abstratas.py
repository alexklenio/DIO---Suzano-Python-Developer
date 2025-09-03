from abc import ABC, abstractmethod 

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(celf):
        pass

    @abstractmethod    
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass
    

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Tv Ligada")
    
    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")
            
    @property
    def marca(self):
        return "philco"


controle = ControleTv()
controle.ligar()
controle.desligar()