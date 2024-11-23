import os
from livro import Livro

class Biblioteca:
    def __init__(self, arquivo="catalogo.txt"):
        self.Catalogo = []
        self.arquivo = arquivo
        self.Carregar_Catalogo()

    def Carregar_Catalogo(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as file:
                for linha in file:
                    titulo, autor, ano_publicacao = linha.strip().split(',')
                    livro = Livro(titulo, autor, int(ano_publicacao))
                    self.Catalogo.append(livro)
        else:
            print(f"Erro: O arquivo {self.arquivo} não foi encontrado.")

    def salvar_catalogo(self):
        with open(self.arquivo, 'w') as file:
            for livro in self.Catalogo:
                file.write(f'{livro.titulo},{livro.autor},{livro.ano_publicacao}\n')

    def adicionar_livro(self, livro):
        self.Catalogo.append(livro)
        self.salvar_catalogo()

    def buscar_livros(self, palavra):
        resultado = [livro for livro in self.Catalogo
                     if palavra.lower() in livro.titulo.lower() or palavra.lower() in livro.autor.lower()]
        return resultado

    def listar_livros(self):
        if self.Catalogo:
            print("Listando os livros disponíveis:")
            for livro in self.Catalogo:
                print(livro.mostrar_informacoes())
        else:
            print("Nenhum livro encontrado no catálogo.")
