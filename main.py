import biblioteca
from cliente import Cliente
from funcionario import Funcionario
from biblioteca import Biblioteca
from usuarios import Usuario

#def verifica_login(func):
#    def wrapper(*args, **kwargs):
 #       cpf_input = input("\tCPF: ")
 #       senha_input = input("\tSenha: ")
   #       print("\n\nValidando login... Aguarde...\n\n")
   #       with open('cadastro.txt', 'r') as file:
   #           for linha in file:
   #               dados = linha.strip().split(',')
    #              if len(dados) == 7: #Lembra de apagar depois
    #                  #nome, cpf, email, telefone, id_, tipo_de_usuario, senha = dados
    #                  if cpf == cpf_input and senha == senha_input:
     #                     if tipo_de_usuario == 'Funcionario':
     #                         return Funcionario(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
       #                   else:
        #                      return Cliente(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
       #           else:
       #               print(f"Linha ignorada devido a formato incorreto ou não preenchido: {linha}")
       #   print("CPF ou senha inválidos")
       #   return None
     # return wrapper

def ler_dados_do_arquivo(cpf_input):
    with open('cadastro.txt', 'r') as file:
        for linha in file:
            dados = linha.strip().split(',')
            if len(dados) == 7:
                nome, cpf, email, telefone, id_, tipo_de_usuario, senha = dados
                if cpf == cpf_input:
                    if tipo_de_usuario == 'Funcionario':
                        return Funcionario(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
                    else:
                        return Cliente(nome, cpf, email, telefone, id_, tipo_de_usuario, senha)
            else:
                print(f"Linha ignorada devido a formato incorreto ou não preenchido: {linha}")
    print("Usuário não encontrado")
    return None

def verifica_login(func):
    def wrapper(user):

        #cpf_input = input("\tCPF: ")
        senha_input = input("\tSenha: ")
        print("\n\nValidando login... Aguarde...\n\n")
        if  (senha_input == (user.get_senha())):
            user.autenticado = True
            return func(user)
        else:
            print("CPF ou senha inválidos")
            return None
    return wrapper

@verifica_login
def menu_login(user):
   
   #if user:
    print(f"Bem-vindo(a), {user.get_nome()}! Você está logado(a) como {user.get_tipo_usuario()}.") # NAO FUNCIONA ------------------------------
    return user

def main(): 
 biblioteca = Biblioteca()  # instância 
autenticado = False 
while True:

  print("---- Bem-vindo a BiblioEng!!! -----") 
  print("\t-- Faça login para acessar o sistema --\n") 
  cpf_input = input("\tCPF: ") 
  user = ler_dados_do_arquivo(cpf_input) 
  if user is not None: 
      user = menu_login(user) 
      if isinstance(user, Funcionario): 
          user.exibe_menu(biblioteca) # Passe a instância da biblioteca 
      elif isinstance(user, Cliente): 
        user.exibe_menu(biblioteca) 
      else: print("Usuário não encontrado. Tente novamente.")
        

# Chama a função principal
if __name__ == "__main__":
    main()
