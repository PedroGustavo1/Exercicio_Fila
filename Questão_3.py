print("O valor m�ximo da sua fila � 20")
class Fila():
#===================Construtor======================

  def __init__(self):
    self.fila = []
    self.atingiu_maximo = 0

#=======Adciona Um Elemento ao Topo da Fila========

  def Enqueue(self):
    elemento = int(input("Digite o Numero do Paciente: "))
    if len(self.fila) == 20:
      print("Sua Fila j� Atingiu o Tamanho M�ximo!")
      self.atingiu_maximo = 1

    if self.atingiu_maximo == 0:
      self.fila.append(elemento)

    self.atingiu_maximo = 0 
    print("Sua fila:",self.fila)

#=======Retira Um Elemento do Topo da Fila=========
  
  def Dequeue(self):
    if (len(self.fila)==0):
      print("N�o H� Elementos na Sua Fila!")
    else:  
      self.fila.pop()
      print("Sua Fila Agora �",self.fila)

#==========Verifica se a Pilha est� Fila============
  
  def IsEmpty(self):
    if len(self.fila) == 0:
      print("Sua Fila Esta Vazia")
    else:
      print("Sua Fila Contem Elementos")

      

#========Verifica o Tamanho da Fila===============  
  def Length(self):
    tamanho = (len(self.fila))
    if tamanho >1:
      print("Sua Fila Contem %d Elementos"%(tamanho))
    elif tamanho ==1:
      print("Sua Fila Contem 1 Elemento!")
    else:
      print("Sua Fila N�o Contem Nenhum Elemento!")

p = Fila()
for i in range(3):
    p.Enqueue()
    p.Enqueue()
    p.Enqueue()
    p.Enqueue()
    p.Enqueue()
    p.Enqueue()
    p.Enqueue() 
    p.Enqueue()
    
print(p.fila)
