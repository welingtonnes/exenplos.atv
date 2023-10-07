class estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def texto(self):
        print(f"olá o meu nome é {self.nome} e temho {self.idade} anos.")

estudante1 = estudante("welington", 18)

print(estudante1.nome)
print(estudante1.idade)

estudante1.texto()
