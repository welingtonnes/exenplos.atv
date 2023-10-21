class Estudante:
    def __init__(self, nome): # init é um contrutor. ele é chamado automaticamente quando criamos um novo objtos na classe.
        self.nome = nome

        

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []
    
    def adicionar_estudantes(self, estudantes):
        self.estudantes.append(estudantes)


joao = Estudante("joao")
maria = Estudante("maria")

turmaA = Turma("Turma A")
turmaA.adicionar_estudantes(joao)
turmaA.adicionar_estudantesa(maria)
          