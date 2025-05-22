class Tarefa:
   incrementa_id = 1 
   def __init__(self,titulo,descricao,prioridade):
      self.titulo = titulo 
      self.prioridade = prioridade 
      self.descricao= descricao
      self.status = "Pendente"
      self.id = Tarefa.incrementa_id
      Tarefa.incrementa_id += 1

   def __str__(self):
       return f"Tarefa:{self.id} - {self.descricao} - {self.prioridade} - {self.status}"
   
   
   def concluir_tarefa(self):
      self.status = "Concluída"
      print (f"Tarefa: {self.titulo} concluido")

   
   def editar_tarefa(self,novo_titulo, nova_descricao, nova_prioridade):
      self.novo_titulo = novo_titulo
      self.nova_descricao = nova_descricao 
      self.nova_prioridade = nova_prioridade

class Usuario:
   def __init__ (self,nome,email,senha):
      self.nome = nome 
      self.email = email 
      self.senha = senha
      self.lista_tarefas = []
   
   def criar_tarefa(self,titulo,descricao,prioridade):
      nova_tarefa = Tarefa (titulo,descricao,prioridade)
      self.lista_tarefas.append(nova_tarefa)

   def listar_tarefas(self,status = None):
      for Tarefa in self.lista_tarefas:
         if status is None or Tarefa.status == status :
            print (Tarefa)

   def procurar_tarefa(self,id_tarefa):
      for tarefa in self.lista_tarefas:
         if tarefa.id == id_tarefa :
            return tarefa 
      return None

   def remover_tarefa(self, id_tarefa):
      tarefa_buscada = self.procurar_tarefa(id_tarefa)
      if tarefa_buscada:
         self.lista_tarefas.remove(tarefa_buscada)
      else:
         print("Tarefa não encontrada")

   def limpar_concluidas(self):
      tarefa_ativas = []
      for tarefa in self.lista_tarefas:
         if tarefa.status != "Concluída":
            tarefa_ativas.append(tarefa)
         self.lista_tarefas = tarefa_ativas

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
         print("1 - Criar Tarefa:  \n")
         print("2 - Listar tarefas:  \n")
         print("3 - Listar tarefas pendentes:  \n")
         print("4 - Listar tarefas concluidas:  \n ")
         print("5 - Concluir Tarefas:  \n")
         print("6 - Editar tarefa:  \n")
         escolha = input ("Selecione uma opção \n:")

         if escolha  == "1":
            titulo = str(input("Digite o titulo da tarefa:"))
            descricao = str(input("Digite a descrição da tarefa:"))
            prioridade = str(input("Digite a prioridade da Tarefa (Alta, Média ou Baixa):"))
            self.usuario_logado.criar_tarefa(titulo,descricao,prioridade)

         elif escolha == "2" : 
            self.usuario_logado.listar_tarefas()

         elif escolha == "3":
            self.usuario_logado.listar_tarefas("Pendente")
         
         elif escolha == "4":
            self.usuario_logado.listar_tarefa("Concluída")

         elif escolha == "5": 
             id = input("Insira o Id da tarefa:")
             if id.isdigit():
               tarefa_buscada = self.usuario_logado.procurar_tarefa(int(id))
               if tarefa_buscada :
                  tarefa_buscada.concluir_tarefa()
               else:
                  print("Tarefa não encontrada")

         elif escolha == "6":
            id = input("Insira o Id da tarefa:")
            if id.isdigit():
             tarefa_buscada = self.usuario_logado.procurar_tarefa(int(id))
             if tarefa_buscada :
               novo_titulo = input("Insira o novo titulo:")
               nova_descriicao = input("Insira a prioridade :")
               nova_prioridade = input("Insira a nova prioridade: ")
               tarefa_buscada.editar_tarefa(novo_titulo,nova_descriicao,nova_prioridade)
             else:
               print("Tarefa não encontrada")

         elif escolha =="7":
            id = input("Insira o Id da tarefa:")
            if id.isdigit():
                tarefa_buscada = self.usuario_logado.remover_tarefa(int(id))
         elif escolha == "8":
            self.usuario_logado.limpar_concluidas()

teste = Sistema()
teste.menu_principal()     
