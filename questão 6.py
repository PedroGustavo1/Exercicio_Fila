class Fila:
    def  __init__ (self):
        self.fila = []


    def enqueue (self):
      nome_piloto = (input("Digite o nome do Piloto do Aviao: "))
      numero_aviao = int(input("Digite o Numero do Aviao que ir� entrar na fila: "))
      self.fila.append(numero_aviao)
      print("Lista de espera atualizada:",self.fila)


    def dequeue (self):
        if not (self.isEmpty()):
            print("DECOLAGEM AUTORIZADA....")
            self.fila.pop(0)
        else:
          print("N�o tem nenhum aviao na fila de espera!")

    def isEmpty (self):
        return len(self.fila)== 0


    def Length (self):
        return print("Existem %d avioes aguardando autorizacao para o voo"%(len(self.fila)))


print("==================== Horse Air Companies ==================== \n")



print("1 - Listar o n�mero de avi�es aguardando na fila de decolagem;")
print("2 - Autorizar a decolagem do primeiro avi�o da fila;")
print("3 - Adicionar um avi�o � fila de espera;")
print("4 - Listar todos os avi�es na fila de espera;")
print("5 - Listar as caracter�sticas do primeiro avi�o da fila;\n")

fila = Fila()

n_operacoes = int(input("Digite o numero de Opera��es que voc� deseja realizar:  "))

for i in range(n_operacoes):

  opcao = int(input("\nDigite o Numero da Opera��o que Voc� Deseja Realizar: "))

  print("\n")



  if opcao == 1:
    fila.Length()


  if opcao == 3:
    fila.enqueue()

  if opcao == 2:
    fila.dequeue()

  if opcao == 4:
    print("Avioes na Lista de Espera:",fila.fila)

  if opcao == 5:
    if  fila.isEmpty():
      print("Nao tem ninguem na fila pow")
    else:
      print("Codigo do Primeir aviao na lista de espera:", fila.fila[0])
      print("Para mais informa��es acesse o site da nossa companhia.. :)")
  









