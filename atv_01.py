class caneta:
    def __init__(self, cor):
       self.cor = cor
       self.dono = None

class pessoa:
    def __init__(self, nome):
        self.nome = nome 
        self.caneta = None

    def pegar_caneta(self,caneta):
        self.caneta = caneta
        caneta.dono =self.nome

pessoa1 = pessoa("gui")
caneta1 = caneta("azul")

pessoa1.pegar_caneta(caneta1)
print(caneta1.dono)