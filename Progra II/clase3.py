#Practica
class Perro:
    raza = "Pastor Belga"
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self._patas = patas
    
    def ladrar(self):
        print('🐶 guuuaf')
        
maxPerro = Perro('Max', 4)
maxPerro.ladrar()
    
#Practica 2
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Trabajador(Persona):
    def __init__(self,nombre,edad, trabajo):
       super().__init__(nombre,edad)
       self.trabajo = trabajo
       
    def saludar(self):
        print(f'Hola soy {self.nombre} tengo {self.edad} anios y trabajo en {self.trabajo}')
        
jose = Persona('Jose Alvarez', 27)
print(jose.nombre)
        
jose_trabajador = Trabajador('jose', 27, 'NetInfo')
jose_trabajador.saludar()

#Practica 3
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    def dormir(self):
        return ' el animal esta durmiendo'
    
    def despertar(self):
        return 'el animal se desperto'
    
class Perro(Animal):
    def hacer_sonido(self):
        return '🐶 guuuaf'
    
class Gato(Animal):
    def hacer_sonido(self):
        return '🐱 miaaau'
    
perro = Perro()
gato = Gato()

print(gato.hacer_sonido())
print(perro.hacer_sonido())
print(gato.dormir())
print(perro.dormir())


#Practica 4
num1 = 12
num2 = 5
class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, num1, num2):
        pass

class Suma(Operacion):
    def ejecutar(self, num1, num2):
        return num1 + num2

class Resta(Operacion):
    def ejecutar(self, num1, num2):
        return num1 - num2

class Multiplicacion(Operacion):
    def ejecutar(self, num1, num2):
        return num1 * num2

class Division(Operacion):
    def ejecutar(self, num1, num2):
        return num1 / num2

suma = Suma()
resta = Resta()
multiplicacion = Multiplicacion()
division = Division()

print(suma.ejecutar(num1, num2))
print(resta.ejecutar(num1, num2))
print(multiplicacion.ejecutar(num1, num2))
print(division.ejecutar(num1, num2))