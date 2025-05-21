class Tarefa:
   def __init__(self,titulo,descricao,priordade):
      self.titulo = titulo 
      self.prioridade = priordade 
      self.descricao= descricao

   def __str__(self):
       return f"Tarefa:{self.titulo} - {self.descricao} - {self.prioridade}"

class Usuario:
   def __init__ (self,nome,email,senha):
      self.nome = nome 
      self.email = email 
      self.senha = senha
      self.lista_tarefas = []
   
   def criar_tarefa(self,titulo,descricao,prioridade):
      nova_tarefa = Tarefa (titulo,descricao,prioridade)
      self.lista_tarefas.append(nova_tarefa)

   def condicoes_tarefas(self,prioridade, status):
      self.prioridade = prioridade
      self.status = status
   
   def tarefas_concluidas(self, status):
      self.status = status 

   def limpar_tarefas_concluidas(self,status):
      self.status = status      

   def editar_tarefa(self,titulo):
      self.titulo = titulo

   def listar_tarefas(self):
      for Tarefa in self.lista_tarefas:
         print (Tarefa)

class Sistema:
   def __init__(self):
      self.lista_usuarios = []
      self.usuario_logado = None

   def cadastrar_usuario(self):
      nome = input("Digite o nome:")
      email = input("Digite o email:")
      senha = input ("Crie uma senha : ")
      if "@"not in email:
         print("E-mail inválido\n")
         return
      if len ( senha )<4:
         print("Senha muito curta: ")
      else:
         novo_usuario = Usuario (nome,email,senha)    
         self.lista_usuarios.append(novo_usuario)
         print("Usuario cadastrado com sucesso\n")

   def login(self):
      email = input("Entre com o email: ")
      senha = input("Digite a senha: ")
      
      for usuario in self.lista_usuarios:
         if (usuario.email == email) and (usuario.senha == senha) :
            self.usuario_logado = usuario
            print(f"Bem vindo \n {self.usuario_logado.nome}:")
            self.menu_tarefas()
            return
         
      print("Usuário inexistente ou senha inválidade: ")
   
   def menu_principal(self):
     opcao_escolhida = ""
     while opcao_escolhida != "0":
      print("Bem,vindo! Escolha uma opção\n")
      print("1. Cadastrar usuário novo")
      print("2. Fazer login")
      print("0. Sair \n ")
      opcao_escolhida = input("Escolha uma opção: ")

      if opcao_escolhida == "1":
         self.cadastrar_usuario()
      elif opcao_escolhida == "2":
          self.login()
      elif opcao_escolhida == "0":
         print("Saindo...")
      else:
         print ("Opção inválida")
   def menu_tarefas(self):
      escolha = ""
      while escolha != "0" :
         print ("\n ------------- Tarefas -------------- \n")
         print("1 - Criar Tarefa: \n")
         print("2 - Listar tarefas: \n")
         print("0 - Sair: \n")
   
         escolha = input ("Selecione uma opção:")

         if escolha  == "1":
            titulo = str(input("Digite o titulo da tarefa:"))
            descricao = str(input("Digite a descrição da tarefa:"))
            prioridade = str(input("Digite a prioridade da Tarefa (Alta, Méida ou Baixa):"))
            self.usuario_logado.criar_tarefa(titulo,descricao,prioridade)
         elif escolha == "2" : 
            self.usuario_logado.listar_tarefas()

teste = Sistema()
teste.menu_principal()     

  # def login(self):
