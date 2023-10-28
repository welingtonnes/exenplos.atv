class Endereco():
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade


class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        print(f" pessoa {nome} mora no endereço {endereco}")


endereco1 = Endereco("avenida brasil, 123", "ivaiporã")
pessoa1 = Pessoa(nome="welington", endereco=endereco1.cidade)
    