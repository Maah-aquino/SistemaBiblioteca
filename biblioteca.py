import os
from livro import Livro

class Biblioteca:
    def __init__(self, arquivo="catalogo.txt"):
        self.Catalogo = []
        self.arquivo = arquivo
        self.Carregar_Catalogo()

 

    
    def Carregar_Catalogo(self):
        self.Catalogo.clear()  # Limpa o catálogo existente
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as file:
                for linha in file:
                    valores = linha.strip().split(',')
                    if len(valores) == 3:
                        titulo, autor, ano_publicacao = valores
                        disponivel = True  # Definindo como disponível por padrão
                    elif len(valores) == 4:
                        titulo, autor, ano_publicacao, disponivel_str = valores
                        disponivel = disponivel_str.lower() == 'sim'
                    else:
                        print(f"Erro: Linha no formato incorreto - {linha}")
                        continue
                    # Verificação de duplicação 
                    if any(livro.titulo == titulo and livro.autor == autor for livro in self.Catalogo): 
                        print(f"Livro '{titulo}' por '{autor}' já existe no catálogo.") 
                    else: livro = Livro(titulo, autor, ano_publicacao, disponivel) 
                    self.Catalogo.append(livro)
        else:
            print(f"Erro: O arquivo {self.arquivo} não foi encontrado.")


    def Salvar_Emprestimo(self): 
        with open(self.arquivo, 'w') as file: 
            for livro in self.Catalogo: 
                disponivel_str = 'sim' if livro.get_disponivel() else 'nao' 
                file.write(f"{livro.titulo},{livro.autor},{livro.ano_publicacao},{disponivel_str}\n")

    def Salvar_Catalogo(self):
         with open(self.arquivo, 'a') as file:
             for livro in self.Catalogo:
                 disponivel_str = 'Sim' if livro.disponivel else 'Nao'
             file.write(f"{livro.titulo},{livro.autor},{livro.ano_publicacao},{disponivel_str}\n")


    def adicionar_livro(self, livro):
        self.Catalogo.append(livro)
        self.Salvar_Catalogo()

    def buscar_livros(self, palavra):
        resultado = [livro for livro in self.Catalogo
                     if palavra.lower() in livro.titulo.lower() or palavra.lower() in livro.autor.lower()]
        return resultado

    def listar_livros(self):
        if self.Catalogo:
            print("Listando os livros disponíveis:")
            for livro in self.Catalogo:
                print(livro.mostrar_informacoes())
        return self.Catalogo
        # else:
        #     print("Nenhum livro encontrado no catálogo.")
    
    def listar_livros_emprestados(self): # Retorna uma lista de livros emprestados (disponível = False) 
        livros_emprestados = [livro for livro in self.Catalogo if not livro.get_disponivel()] 
        return livros_emprestados if livros_emprestados else []

    
    def emprestar_livro(self, titulo, usuario): 
        if usuario.autenticacao: 
            resultados = self.buscar_livros(titulo) 
            if resultados: 
                livro = resultados[0] 
                if livro.disponivel: 
                    livro.emprestar() 
                    self.Salvar_Emprestimo() 
                    return True 
                else: 
                    return False 
            else: return False 
        else: return False

    def devolver_livro(self, titulo, usuario):
        if usuario.autenticacao:
            resultados = self.buscar_livros(titulo)
            if resultados:
                livro = resultados[0]
                if not livro.disponivel:
                    livro.devolver()  
                    self.Salvar_Emprestimo() 
                    return True
                else:
                    print("Livro não encontrado.")
                return False
            else: return False
        else: return False

    def remover_livro( self, titulo):
     livro_removido = False 
     for livro in self.Catalogo: 
         if livro.titulo.lower() == titulo.lower(): 
            self.Catalogo.remove(livro) 
            livro_removido = True 
            self.Salvar_Catalogo() 
            print(f"O livro '{titulo}' foi removido com sucesso.")  
            break
     
         if not livro_removido: 
            print(f"O livro '{titulo}' não foi encontrado no catálogo.")


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
