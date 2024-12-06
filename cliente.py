from usuarios import Usuario

class Cliente(Usuario):
    def __init__(self, nome, cpf, email, telefone, id, tipo_de_usuario, senha, autenticado = False):
        super().__init__(nome, cpf, email, telefone, id, tipo_de_usuario, senha, autenticado = False)
        self._tipo_de_usuario = tipo_de_usuario
    
    def exibe_menu(self, biblioteca):
        texto_menu_cliente = (
            "1 - Listar Catalogo \n"
            "2 - Pesquisar livro \n"
            "3 - Emprestar livro \n"
            "4 - Devolver livro \n"
            "5 - Logoff \n"
            "0 - Sair \n"
        )

        while True:
            print(texto_menu_cliente)
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
                print("Realizando Logout...")
                break
            elif opcao == '0':
                print("Encerrando o programa.")
                exit()
            else:
                print("Opção inválida. Tente novamente.")

                print("Encerrando o programa.")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
