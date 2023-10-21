class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade
        
    def mostrar_endereco(self):
        return f"{self.rua}, {self.cidade}"


class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco     # a associaçao acontece aqui!


    def mostrar_informacoes(self):
        return f"{self.nome} mora em {self.endereco.mostrar_endereco()}" #mostrar a resposta
         
endereco_maria = Endereco("av. principal", "são paulo") 
maria = Pessoa ("maria", endereco_maria)
print(maria.mostrar_informacoes())