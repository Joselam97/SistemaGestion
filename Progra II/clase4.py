'''Vamos a crear una clase abstracta llamada figura la cual va a tener 2
metodos abstractos, uno para calcular el area y otro para calcular el perimetro, ademas
vamos a crear dos funciones que reciban una figura y el perimetro y otra el area
de un triangulo (b*h)/2 y rectangulo b*h y el perimetro es la suma de todos los lados'''

from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
class Triangulo(Figura):
    def __init__(self,base,altura):
       self.base = base
       self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        hipotenusa = (self.base**2 + self.altura**2) ** 0.5
        return (self.base + self.altura + hipotenusa)
    

class Rectangulo(Figura):
    def __init__(self,base,altura):
       self.base = base
       self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
def showArea(figura):
    print(f'El area de la figura es {figura.area()}')
    
def showPerimetro(figura):
    print(f'El perimetro de la figura es {figura.perimetro()}\n')
    
triangulo = Triangulo(base = 4, altura = 7)
rectangulo = Rectangulo(base = 6, altura= 5)

print("Triangulo")
showArea(triangulo)
showPerimetro(triangulo)

print()

print("Rectangulo")
showArea(rectangulo)
showPerimetro(rectangulo)


    