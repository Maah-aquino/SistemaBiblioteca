
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from cliente import Cliente
from funcionario import Funcionario
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from biblioteca import Biblioteca
import biblioteca
from cliente import Cliente
from funcionario import Funcionario
from livro import Livro

# Definição das cores
# Cores
co0 = "0b0b64"  # Azul
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#000328"  # azul
co5 = "#e06636"  # - profit
co6 = "#b4b4b4"  # cor de fundo superior
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#008000"  # + verde
co10 = "#6e8faf"  # 
co11 = "#f2f4f2"
co12 = "#008000"
cor13 = "#194a47"
# Função para ler os dados do arquivo
def ler_dados_do_arquivo(cpf_input):
    with open('cadastro.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split(',')
            if len(dados) == 7:
                nome, cpf, email, telefone, id_, tipo_de_usuario, senha = dados
                if cpf == cpf_input:
                    if tipo_de_usuario == 'Funcionario':
                        return Funcionario(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
                    elif tipo_de_usuario == 'Cliente':
                        return Cliente(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
    return None

# Função de Autenticação
def autenticar_usuario():
    global user
    cpf_input = cpf_entry.get()
    senha_input = senha_entry.get()
    user = ler_dados_do_arquivo(cpf_input)

    if user is None:
        messagebox.showerror("Erro", "Usuário não encontrado!")
        return

    if senha_input == user.get_senha():
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
        login_window.destroy()  # Fecha a janela de login

        if isinstance(user, Funcionario):
            exibir_menu_funcionario(user)
        elif isinstance(user, Cliente):
            exibir_menu_cliente(user)
        else:
            messagebox.showerror("Erro", "Tipo de usuário inválido!")
    else:
        messagebox.showerror("Erro", "Senha inválida!")

# Função para Exibir Menu do Funcionário
def exibir_menu_funcionario(user):
   




    biblioteca = Biblioteca("catalogo.txt")


    # Criando janela de dentro
    janela = Tk()
    janela.title("Sistema de Biblioteca-COLABORADORES")
    janela.geometry('1000x700')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    style = Style(janela)
    style.theme_use("clam")
    # Configuração do tema
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


    # Frames da interface
    frameCima = Frame(janela, width=970, height=50, bg=co6, relief="flat")
    frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
    frameEsquerda.grid(row=1, column=0, sticky=NSEW)

    frameDireita = Frame(janela, width=950, height=665, bg=co1, relief="raised")
    frameDireita.grid(row=1, column=1, sticky=NSEW)

    # Logo e título
    app_logo = Label(frameCima, width=1000, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
    app_logo.place(x=5, y=0)

    app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
    app_.place(x=50, y=7)

    l_linha = Label(frameCima, width=770, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.place(x=0, y=47)

   



    def novo_usuario():
        global img_salvar

        def Cadastrar_Usuario():
            nome = e_nome.get()
            cpf = e_cpf.get()
            email = e_email.get()
            telefone = e_telefone.get()
            id_usuario = e_id.get()
            tipo_de_usuario = e_tipo_usuario.get()
            senha = e_senha.get()

            lista = [nome, cpf, email, telefone, id_usuario, tipo_de_usuario, senha]

            for i in lista:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            usuario_data = f"{nome},{cpf},{email},{telefone},{id_usuario},{tipo_de_usuario},{senha}\n"

            try:
                with open("cadastro.txt", 'a') as file:
                    file.write(usuario_data)
                messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso!')
            except Exception as e:
                messagebox.showerror('Erro', f"Erro ao salvar o usuário: {str(e)}")

            e_nome.delete(0, END)
            e_cpf.delete(0, END)
            e_email.delete(0, END)
            e_telefone.delete(0, END)
            e_id.delete(0, END)
            e_tipo_usuario.delete(0, END)
            e_senha.delete(0, END)

        app_ = Label(frameDireita, text="Cadastrar Novo Usuário", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_nome = Label(frameDireita, text="Nome*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_nome = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_nome.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_cpf = Label(frameDireita, text="CPF*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_cpf.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_cpf = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_cpf.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_email = Label(frameDireita, text="Email*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_email.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_email = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_email.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_telefone = Label(frameDireita, text="Telefone*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_telefone.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_telefone = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_telefone.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_id = Label(frameDireita, text="ID*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_id = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id.grid(row=6, column=1, pady=5, sticky=NSEW)

        l_tipo_usuario = Label(frameDireita, text="Tipo de Usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_tipo_usuario.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
        e_tipo_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_tipo_usuario.grid(row=7, column=1, pady=5, sticky=NSEW)

        l_senha = Label(frameDireita, text="Senha*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_senha.grid(row=8, column=0, padx=5, pady=5, sticky=NSEW)
        e_senha = Entry(frameDireita, width=25, justify='left', relief="solid", show="*")
        e_senha.grid(row=8, column=1, pady=5, sticky=NSEW)

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=Cadastrar_Usuario, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=9, column=1, pady=5, sticky=NSEW)


    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox

    def novo_livro():
        global img_salvar

        def adicionar_livro():
            titulo = e_titlo.get()
            autor = e_autor.get()
            ano_publicacao = e_ano.get()
            disponivel = e_disponivel.get()

            lista = [titulo, autor, ano_publicacao, disponivel]

            for i in lista:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            novo_livro = Livro(titulo, autor, ano_publicacao, disponivel)
            biblioteca.adicionar_livro(novo_livro)
            messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi cadastrado com sucesso.")

            biblioteca.listar_livros()
            e_titlo.delete(0, tk.END)
            e_autor.delete(0, tk.END)
            e_disponivel.delete(0, tk.END)
            e_ano.delete(0, tk.END)





        app_ = Label(frameDireita, text="Inserir um Novo Livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_titlo = Label(frameDireita, text="Título do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_titlo = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_autor = Label(frameDireita, text="Autor do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_disponivel = Label(frameDireita, text="Disponivel?*", height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_disponivel.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_disponivel = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_disponivel.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_ano = Label(frameDireita, text="Ano de publicação do livro*", height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

    

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=adicionar_livro, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

    def ver_usuarios():
        app_ = Label(frameDireita, text="Todos os usuários do banco de dados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = ler_usuarios_do_arquivo('cadastro.txt')  # Chame a função para ler os dados do arquivo

        # Criando uma treeview com duas barras de rolagem
        list_header = ['Nome', 'CPF', 'Email', 'Telefone', 'ID', 'Tipo de Usuário', 'Senha']
        
        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [80, 100, 120, 100, 80, 120, 80]
        n = 0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in dados:
            tree.insert('', 'end', values=item)

    def ler_usuarios_do_arquivo(caminho):
        usuarios = []
        try:
            with open(caminho, 'r') as file:
                for linha in file:
                    dados = linha.strip().split(',')
                    if len(dados) == 7:  # Certifique-se de que há 7 campos
                        usuarios.append(dados)
        except FileNotFoundError:
            print(f"Erro: O arquivo {caminho} não foi encontrado.")
        return usuarios



    def listar_livros_view(biblioteca):
        global tree, vsb, hsb

        # Limpar o frame antes de adicionar novos widgets
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Título e linha de separação
        app_ = tk.Label(frameDireita, text="Livros do Catálogo", width=130, compound=LEFT, padx=5, pady=10, relief=tk.FLAT, anchor=tk.NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        l_linha = tk.Label(frameDireita, width=400, height=1, anchor=tk.NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

        # Defina o list_header com os campos corretos
        list_header = ["Título", "Autor", "Ano de Publicação", "Disponível"]

        # Verificar se a Treeview já foi criada
        if 'tree' in globals() and tree.winfo_exists():
            # Limpa a árvore antes de inserir novos itens
            for item in tree.get_children():
                tree.delete(item)
        else:
            # Criar a Treeview se não existir
            tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
            vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(row=2, column=0, sticky='nsew')
            vsb.grid(row=2, column=1, sticky='ns')
            hsb.grid(row=3, column=0, sticky='ew')

            # Configura os cabeçalhos das colunas
            for col in list_header:
                tree.heading(col, text=col, anchor='nw')
                tree.column(col, anchor='nw', width=120)

        # Carregar e exibir livros do catálogo
        exibir_livros_catalogo(biblioteca)

    def exibir_livros_catalogo(biblioteca):
        livros = biblioteca.listar_livros()
        
        # Inserir livros na Treeview
        for livro in livros:
            detalhes_livro = livro.mostrar_informacoes().replace('Título: ', '').replace('Autor: ', '').replace('Ano de Publicação: ', '').replace('Disponível: ', '').split(', ')
            if len(detalhes_livro) == 4:  # Certifique-se de que há 4 campos
                tree.insert("", "end", values=detalhes_livro)






    # Botão para exibir os livros
    b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_livros.grid(row=0, column=0)





    def realizar_emprestimo(biblioteca):
        global img_salvar, user

        def emprestar_livro():
            titulo = e_id_livro.get()  # Obtendo o título do campo 'e_id_livro'
            sucesso = biblioteca.emprestar_livro(titulo, user)
            if sucesso:
                messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi emprestado com sucesso.")
                # biblioteca.Carregar_Catalogo()
                # biblioteca.Salvar_Catalogo()
            else:
                messagebox.showerror("Erro", f"Não foi possível emprestar o livro '{titulo}'.")

            if not titulo:  # Verificar se o campo título está vazio
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

            # Limpar campos de entrada após a operação
            e_id_usuario.delete(0, END)
            e_id_livro.delete(0, END)

        app_ = Label(frameDireita, text="Realizar um empréstimo", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_id = Label(frameDireita, text="Digite o id do usuario*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_id = Label(frameDireita, text="Digite o Titulo do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=emprestar_livro, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)

  

    def ver_livros_emprestados_view(biblioteca):
        global tree

        app_ = tk.Label(frameDireita, text="Livros Emprestados", width=120, compound=tk.LEFT, padx=5, pady=10, relief=tk.FLAT, anchor=tk.NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        l_linha = tk.Label(frameDireita, width=400, height=1, anchor=tk.NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)
        
        # Carregar o catálogo de livros
        biblioteca.Carregar_Catalogo()
        
        # Obtendo a lista de livros emprestados do objeto biblioteca
        livros = biblioteca.listar_livros_emprestados()

        list_header = ['Título', 'Autor', 'Ano de Publicação', 'Disponível']
        
        # Definição da Treeview
        tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        # Configura os cabeçalhos das colunas
        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, anchor='nw', width=120)

        # Limpa a árvore antes de inserir novos itens
        for item in tree.get_children():
            tree.delete(item)

        # Inserir os itens na árvore
        for livro in livros:
            
            informacoes = livro.mostrar_informacoes().split(', ')
            tree.insert('', 'end', values=informacoes)


    
    def devolucao_emprestimo(biblioteca):
        global img_salvar, user  # Tornar user e biblioteca globais

        def devolver_livro():
            titulo = e_id_livro.get()  # Obtendo o título do campo 'e_id_livro'
            sucesso = biblioteca.devolver_livro(titulo, user)  # Usando a função de devolução do livro
            if sucesso:
                messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi devolvido com sucesso.")
            else:
                messagebox.showerror("Erro", f"Não foi possível devolver o livro '{titulo}'.")

            if not titulo:  # Verificar se o campo título está vazio
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

            # Limpar campos de entrada após a operação
            e_id_usuario.delete(0, END)
            e_id_livro.delete(0, END)

        app_ = Label(frameDireita, text="Devolver um livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_id_usuario = Label(frameDireita, text="ID do usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_usuario.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_id_livro = Label(frameDireita, text="titulo do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=devolver_livro, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)

    # Função para controlar o Menu
    def control(i):
        for widget in frameDireita.winfo_children():
            widget.destroy()
        if i == 'novo_usuario':
            novo_usuario()
        elif i == 'novo_livro':
            novo_livro()
        elif i == 'ver_livros':
            listar_livros_view(biblioteca)
        elif i == 'ver_usuarios':
            ver_usuarios()
        elif i == 'realizar_emprestimo':
            realizar_emprestimo(biblioteca)
        elif i == 'ver_livros_emprestados':
            ver_livros_emprestados_view(biblioteca)
        elif i == 'devolucao_emprestimo':
            devolucao_emprestimo(biblioteca)

    # Menu
    b_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario'), compound=LEFT, anchor=NW, text='  Novo usuário', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

    b_novo_livro = Button(frameEsquerda, command=lambda: control('novo_livro'), compound=LEFT, anchor=NW, text='  Novo livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

    b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_livros.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

    b_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), compound=LEFT, anchor=NW, text='  Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

    b_emprestimo = Button(frameEsquerda, command=lambda: control('realizar_emprestimo'), compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    b_devolucao = Button(frameEsquerda, command=lambda: control('devolucao_emprestimo'), compound=LEFT, anchor=NW, text='  Devolução de um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    b_livros_emprestados = Button(frameEsquerda, command=lambda: control('ver_livros_emprestados'), compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)


    janela.mainloop()
# Função para Exibir Menu do Cliente
def exibir_menu_cliente(user):
   



    biblioteca = Biblioteca("catalogo.txt")


    # Criando janela de dentro
    janela = Tk()
    janela.title("Sistema de Biblioteca - Cliente")
    janela.geometry('1000x700')
    janela.configure(background=co1)
    janela.resizable(width=FALSE, height=FALSE)

    style = Style(janela)
    style.theme_use("clam")
    # Configuração do tema
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


    # Frames da interface
    frameCima = Frame(janela, width=970, height=50, bg=co6, relief="flat")
    frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    frameEsquerda = Frame(janela, width=150, height=165, bg=cor13, relief="solid")
    frameEsquerda.grid(row=1, column=0, sticky=NSEW)

    frameDireita = Frame(janela, width=950, height=665, bg=co1, relief="raised")
    frameDireita.grid(row=1, column=1, sticky=NSEW)

    # Logo e título
    app_logo = Label(frameCima, width=1000, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
    app_logo.place(x=5, y=0)

    app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros -Clientes", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
    app_.place(x=50, y=7)

    l_linha = Label(frameCima, width=770, height=1, anchor=NW, font=('Verdana 1 '), bg=co6, fg=co1)
    l_linha.place(x=0, y=47)

   
        

        



    # Funções adicionais
    # 
    from funcionario import Funcionario
    from cliente import Cliente  # Importe a classe Cliente





    def listar_livros_view(biblioteca):
        global tree, vsb, hsb

        # Limpar o frame antes de adicionar novos widgets
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Título e linha de separação
        app_ = tk.Label(frameDireita, text="Livros do Catálogo", width=130, compound=LEFT, padx=5, pady=10, relief=tk.FLAT, anchor=tk.NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        l_linha = tk.Label(frameDireita, width=400, height=1, anchor=tk.NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

        # Defina o list_header com os campos corretos
        list_header = ["Título", "Autor", "Ano de Publicação", "Disponível"]

        # Verificar se a Treeview já foi criada
        if 'tree' in globals() and tree.winfo_exists():
            # Limpa a árvore antes de inserir novos itens
            for item in tree.get_children():
                tree.delete(item)
        else:
            # Criar a Treeview se não existir
            tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
            vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(row=2, column=0, sticky='nsew')
            vsb.grid(row=2, column=1, sticky='ns')
            hsb.grid(row=3, column=0, sticky='ew')

            # Configura os cabeçalhos das colunas
            for col in list_header:
                tree.heading(col, text=col, anchor='nw')
                tree.column(col, anchor='nw', width=120)

        # Carregar e exibir livros do catálogo
        exibir_livros_catalogo(biblioteca)

    def exibir_livros_catalogo(biblioteca):
        livros = biblioteca.listar_livros()
        
        # Inserir livros na Treeview
        for livro in livros:
            detalhes_livro = livro.mostrar_informacoes().replace('Título: ', '').replace('Autor: ', '').replace('Ano de Publicação: ', '').replace('Disponível: ', '').split(', ')
            if len(detalhes_livro) == 4:  # Certifique-se de que há 4 campos
                tree.insert("", "end", values=detalhes_livro)






    # # Botão para exibir os livros
    # b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    # b_ver_livros.grid(row=0, column=0)





    def realizar_emprestimo(biblioteca):
        global img_salvar, user

        def emprestar_livro():
            titulo = e_id_livro.get()  # Obtendo o título do campo 'e_id_livro'
            sucesso = biblioteca.emprestar_livro(titulo, user)
            if sucesso:
                messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi emprestado com sucesso.")
                # biblioteca.Carregar_Catalogo()
                # biblioteca.Salvar_Catalogo()
            else:
                messagebox.showerror("Erro", f"Não foi possível emprestar o livro '{titulo}'.")

            if not titulo:  # Verificar se o campo título está vazio
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

            # Limpar campos de entrada após a operação
            e_id_usuario.delete(0, END)
            e_id_livro.delete(0, END)

        app_ = Label(frameDireita, text="Realizar um empréstimo", width=100, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_id = Label(frameDireita, text="Digite o id do usuario*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_id = Label(frameDireita, text="Digite o Titulo do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=emprestar_livro, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)


    def ver_livros_emprestados_view(biblioteca):
        global tree

        app_ = tk.Label(frameDireita, text="Livros Emprestados", width=130, compound=tk.LEFT, padx=5, pady=10, relief=tk.FLAT, anchor=tk.NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        l_linha = tk.Label(frameDireita, width=400, height=1, anchor=tk.NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)
        
        # Carregar o catálogo de livros
        biblioteca.Carregar_Catalogo()
        
        # Obtendo a lista de livros emprestados do objeto biblioteca
        livros = biblioteca.listar_livros_emprestados()

        list_header = ['Título', 'Autor', 'Ano de Publicação', 'Disponível']
        
        # Definição da Treeview
        tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        # Configura os cabeçalhos das colunas
        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, anchor='nw', width=120)

        # Limpa a árvore antes de inserir novos itens
        for item in tree.get_children():
            tree.delete(item)

        # Inserir os itens na árvore
        for livro in livros:
            
            informacoes = livro.mostrar_informacoes().split(', ')
            tree.insert('', 'end', values=informacoes)



    def devolucao_emprestimo(biblioteca):
        global img_salvar, user

        def devolver_livro():
            titulo = e_id_livro.get()  # Obtendo o título do campo 'e_id_livro'
            sucesso = biblioteca.devolver_livro(titulo, user)  # Usando a função de devolução do livro
            if sucesso:
                messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi devolvido com sucesso.")
            else:
                messagebox.showerror("Erro", f"Não foi possível devolver o livro '{titulo}'.")

            if not titulo:  # Verificar se o campo título está vazio
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

            # Limpar campos de entrada após a operação
            e_id_usuario.delete(0, END)
            e_id_livro.delete(0, END)

        app_ = Label(frameDireita, text="Devolver um livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_id_usuario = Label(frameDireita, text="ID do usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_usuario.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_id_livro = Label(frameDireita, text="titulo do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

        img_salvar = Image.open('save.png')
        img_salvar = img_salvar.resize((18, 18))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=devolver_livro, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)


    # Função para controlar o Menu
    def control(i):
        for widget in frameDireita.winfo_children():
            widget.destroy()
        if i == 'ver_livros':
            listar_livros_view(biblioteca)
        elif i == 'realizar_emprestimo':
            realizar_emprestimo(biblioteca)
        elif i == 'ver_livros_emprestados':
            ver_livros_emprestados_view(biblioteca)
        elif i == 'devolucao_emprestimo':
            devolucao_emprestimo(biblioteca)

    # Menu
   

   

    b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=cor13, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_livros.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

 

    b_emprestimo = Button(frameEsquerda, command=lambda: control('realizar_emprestimo'), compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg=cor13, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    b_devolucao = Button(frameEsquerda, command=lambda: control('devolucao_emprestimo'), compound=LEFT, anchor=NW, text='  Devolução de um empréstimo', bg=cor13, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    b_livros_emprestados = Button(frameEsquerda, command=lambda: control('ver_livros_emprestados'), compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=cor13, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)


    janela.mainloop()
# Criação da janela principal de login
login_window = ctk.CTk()
login_window.title("Sistema de Biblioteca - Login")
login_window.geometry("600x400")
login_window.configure(bg="navy")

# Título
title = ctk.CTkLabel(login_window, text="BEM VINDO A BIBLIOENG!!!", font=("impact", 20))
title.grid(row=1, column=0, pady=50, padx=100)

# Imagem
img = tk.PhotoImage(file="imagem.png")
lb_img = ctk.CTkLabel(login_window, text=None, image=img)
lb_img.grid(row=0, column=0, padx=0)
lb_img.place(relx=0.35, rely=0.6, anchor=ctk.CENTER)

# Frame centralizado
frame = ctk.CTkFrame(login_window, width=300, height=200)
frame.place(relx=0.75, rely=0.5, anchor=ctk.CENTER)

# Campos de entrada
ctk.CTkLabel(frame, text="Faça login para acessar \nCPF:").pack(pady=5)
cpf_entry = ctk.CTkEntry(frame, width=200)
cpf_entry.pack(pady=5)

ctk.CTkLabel(frame, text="Senha:").pack(pady=5)
senha_entry = ctk.CTkEntry(frame, show="*", width=200)
senha_entry.pack(pady=5)

# Botão de login
login_button = ctk.CTkButton(frame, text="Login", command=autenticar_usuario)
login_button.pack(pady=20)

# Executar a aplicação
login_window.mainloop()
