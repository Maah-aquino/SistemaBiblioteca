from usuarios import Usuario
from biblioteca import Biblioteca
from livro import Livro
import biblioteca
import os

class Funcionario(Usuario):
    def __init__(self, nome, cpf, email, telefone, id, tipo_de_usuario, senha, autenticado = False, arquivo="Cadastro.txt"):
        super().__init__(nome, cpf, email, telefone, id, tipo_de_usuario, senha, autenticado = False)
        self.Cadastro = []
        self.arquivo = arquivo
        self.carregar_usuarios()
        self._tipo_de_usuario = tipo_de_usuario

    def cadastrar_livro(self, biblioteca):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = int(input("Ano de Publicação: "))
        Novo_Livro = Livro(titulo, autor, ano_publicacao)
        biblioteca.adicionar_livro(Novo_Livro)
        print(f"O livro '{titulo}' foi cadastrado com sucesso.")

    def carregar_usuarios(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as file:
                for linha in file:
                    nome, cpf, email, telefone, id_, tipo_de_usuario, senha = linha.strip().split(',')
                    usuario = Usuario(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
                    self.Cadastro.append(usuario)
        else:
            print(f"Erro: O arquivo {self.arquivo} não foi encontrado.")

    def Cadastrar_Usuario(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        id_ = input("ID: ")
        tipo_de_usuario = input("Tipo de Usuário (Funcionario/Cliente): ")
        senha = input("Senha: ")
        novo_usuario = f"{nome},{cpf},{email},{telefone},{id_},{tipo_de_usuario},{senha}\n"

        with open(self.arquivo, 'a') as file:
            file.write(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso.")

    def adicionar_Usuario(self, usuario):
        self.Cadastro.append(usuario)
        self.Salvar_Cadastro()

    def Salvar_Cadastro(self):
        with open(self.arquivo, 'w') as file:
            for usuario in self.Cadastro:
                file.write(f'{usuario.get_nome()},{usuario.get_cpf()},{usuario.get_email()},{usuario.get_telefone()},{usuario.get_id()},{usuario.get_tipo_usuario()},{usuario.get_senha()}\n')

    def imprimir_cadastro(self):
        for usuario in self.Cadastro:
            print(f"Nome: {usuario.get_nome()}, CPF: {usuario.get_cpf()}, Email: {usuario.get_email()}, Telefone: {usuario.get_telefone()}, ID: {usuario.get_id()}, Tipo de Usuário: {usuario.get_tipo_usuario()}, Senha: {usuario.get_senha()}")

    def remover_livro(self, biblioteca): 
        titulo = input("Digite o título do livro que deseja remover: ") 
        biblioteca.remover_livro(titulo)

    def remover_usuario(self, input_cpf):
        usuario_removido = False 
        for usuario in self.Cadastro:
            if usuario.get_cpf() == input_cpf:  #
                self.Cadastro.remove(usuario) 
                usuario_removido = True 
                self.Salvar_Cadastro()  
                print(f"O usuário '{usuario.get_nome()}' foi removido com sucesso.")  
                break  

            else:
                print(f"Usuário com CPF '{input_cpf}' não foi encontrado.")


    def exibe_menu(self, biblioteca):
        texto_menu_bibliotecario = (
            "1 - Listar Catalogo \n"
            "2 - Pesquisar livro  \n"
            "3 - Emprestar livro \n"
            "4 - Devolver livro  \n"
            "5 - Cadastrar livro\n"
            "6 - Cadastrar Usuario \n"
            "7 - Exibir catalogo de livros \n"
            "8 - Exibir cadastro de usuarios \n"
            "9 - Remover livro do catalogo \n"
            "10- Remover cadastro \n"
            "11- Logoff \n"
            "0 - Sair \n"
        )

        while True:
            print(texto_menu_bibliotecario)
            opcao = input("Digite a opcao escolhida: ")

            if opcao == '1':
                biblioteca.listar_livros()
            elif opcao == '2':
                palavra = input("Digite o título ou autor para buscar: ")
                resultados = biblioteca.buscar_livros(palavra)
                print("\nResultados da busca:")
                if resultados:
                    for livro in resultados:
                        print(livro.mostrar_informacoes())
                else:
                    print("Nenhum livro encontrado com esse título ou autor.")
            elif opcao == '3':
                titulo = input("Digite o título do livro que deseja emprestar: ")
                biblioteca.emprestar_livro(titulo,Usuario)
            elif opcao == '4':
                titulo = input("Digite o título do livro que deseja devolver: ")
                biblioteca.devolver_livro(titulo,Usuario)
            elif opcao == '5':
                self.cadastrar_livro(biblioteca)
            elif opcao == '6':
                self.Cadastrar_Usuario()
            elif opcao == '7':
                biblioteca.listar_livros()
            elif opcao == '8':
                self.imprimir_cadastro()
            elif opcao == "9": 
                self.remover_livro(biblioteca)
            elif opcao == "10": 
                input_cpf = input("Digite o CPF do Usuario que deseja desativar: ")
                self.remover_usuario(input_cpf)
            elif opcao == '11':
                print("Realizando Logout...")
                break
                
            elif opcao == '0':
                print("Encerrando o programa.")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
