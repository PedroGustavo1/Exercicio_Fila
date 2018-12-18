class Fila:
    def  __init__ (self):
        self.fila = []


    def enqueue (self,valor):
        self.fila.append(valor)


    def dequeue (self):
        if not (self.isEmpty()):
            self.fila.pop(0)

    def isEmpty (self):
        return len(self.fila)== 0


    def Length (self):
        return len(self.fila)




uma_fila = Fila()

uma_fila.enqueue(12)

uma_fila.dequeue()

print(uma_fila.fila)

print(uma_fila.isEmpty())

print(uma_fila.Length())



        
    
    
