
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def mostrar_informacoes(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Disponível: {self.disponivel}'

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso.")
        else:
            print(f"O livro {self.titulo} não está disponível para empréstimos no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso.")
        else:
            print(f"O livro {self.titulo} já estava disponível.")
