class livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def texto(self):
        print(f" o titulo do livro {self.titulo} o autor {self.autor} e {self.ano_publicacao}")

livro1 = livro("homen aranha", "welington", "2023")

print(livro1.titulo)
print(livro1.autor)
print(livro1.ano_publicacao)

livro1.texto()




