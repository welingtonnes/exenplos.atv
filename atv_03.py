class Autor():
    def __init__(self, nome):
        self.nome = nome

class Livro():
    def __init__(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo
        print(f" o autor {nome} escreveu o livro {titulo}")

livro1 = Livro("quem é vc naruto","shipudem")

livro1 = Livro(nome="naruto", titulo=livro1.titulo)
