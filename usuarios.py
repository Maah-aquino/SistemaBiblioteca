from biblioteca import Biblioteca

class Usuario:
    def __init__(self, nome, cpf, email, telefone, id, tipo_de_usuario, senha,autenticado = False):
        self._id = id
        self._tipo_de_usuario = tipo_de_usuario
        self._nome = nome
        self._senha = senha
        self._email = email
        self._telefone = telefone
        self._cpf = cpf
        self._autenticado = autenticado

    def autenticacao(self,aut):
        self._autenticado = aut

    def buscar_livros(self, biblioteca):
        palavra = input("Digite o título ou autor para buscar: ")
        resultados = biblioteca.buscar_livros(palavra)
        print("\nResultados da busca:")
        if resultados:
            for livro in resultados:
                print(livro.mostrar_informacoes())
        else:
            print("Nenhum livro encontrado com esse título ou autor.")

    def pesquisar_livro_por_autor(self, autor, biblioteca):
        return biblioteca.buscar_livros(autor)

    def emprestar_livro(self, biblioteca):
         titulo = input("Digite o título do livro que deseja emprestar: ") 
         biblioteca.emprestar_livro(titulo, self) # corrigido pela 34634634 vez
         
         
    def devolver_livro(self, biblioteca): 
        titulo = input("Digite o título do livro que deseja devolver: ") 
        biblioteca.devolver_livro(titulo)

    
    def set_id(self, id_):
        self._id = id_

    def set_tipo_usuario(self, tipo_usuario):
        self._tipo_de_usuario = tipo_usuario

    def set_nome(self, nome):
        self._nome = nome

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_senha(self, senha):
        self._senha = senha

    def set_email(self, email):
        self._email = email

    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_id(self):
        return self._id

    def get_tipo_usuario(self):
        return self._tipo_de_usuario

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_senha(self):
        return self._senha

    def get_email(self):
        return self._email

    def get_telefone(self):
        return self._telefone

    def exibe_menu(self):
        #raise NotImplementedError("Subclasses devem implementar este método")
        pass
    
    def listar_livros(self, biblioteca):
        livros = biblioteca.listar_livros()
        for livro in livros:
            print(livro.mostrar_informacoes())

