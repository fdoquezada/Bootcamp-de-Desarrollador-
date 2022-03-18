from enum import auto


class Vehiculo:
    folio = 0
    
    def __init__ (self,color):
        Vehiculo.folio +=1
        self.serie = Vehiculo.folio
        self.color = color
        
    def __str__ (self):
        return str(self.serie) + " " + self.color
    
auto1 = Vehiculo("azul")
auto2 = Vehiculo("cafe")
auto3 = Vehiculo ("morado")
print(auto1)
print(auto2) 
print(auto3)
      
print(auto1.folio)
      
      