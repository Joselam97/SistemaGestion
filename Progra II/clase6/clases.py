'''Escribe una función que cree un diccionario con los datos de un estudiante'''
class Estudiante:
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_info(self):
        print(f'El nombre del estudiantes es: {self.nombre}')
        print(f'El apellido del estudiante es: {self.apellido}')
        print(f'La edad del estudiante es: {self.edad}')
        
    def llamado(self):
        nombre_profe = "Marcos"
        print(f'Requerimos que el estudiante {self.nombre} {self.apellido} se presente a clases con {nombre_profe} de Algebra '
              'hoy a las 8:00 am')
        

nombre = "Jose"
apellido = "Alvarez"
edad = 27

dicc = {
    'nombre': nombre,
    'apellido' : apellido,
    'edad' : edad
}

dicc = Estudiante(nombre,apellido,edad)
dicc.mostrar_info()




print()
'''Escribe una función que cree un diccionario con los datos de un profesor'''

class Profesor:
    def __init__ (self, nombre, materia, horario):
        self.nombre = nombre
        self.materia = materia
        self.horario = horario
        
    def mostrar_profe(self):
        print(f'El nombre del profesor es: {self.nombre}')
        print(f'La materia que da el profesor es: {self.materia}')
        print(f'El horario del profesor es: {self.horario}')
        
nombre_profe = "Marcos"
materia = "Algebra Lineal"
horario = "8:00am a 5:00pm"

dicc2 = {
    'nombre del profesor' : nombre_profe,
    'materia' : materia,
    'horario' : horario
}

dicc2 = Profesor(nombre_profe,materia,horario)
dicc2.mostrar_profe()



print()
'''Escribe una clase que reciba un diccionario de estudiante y que tengo una funcion hablar'''
class Hablar:
    def __init__ (self,estudiante):
        self.estudiante = estudiante
        
    def hablar(self):
        print(f'Hola, hablamos de la direccion para comunicarnos con el estudiante {self.estudiante}')
        
nombre = "Jose Alvarez"
estudiante = Hablar(nombre)

estudiante.hablar()



print()
'''Escribe una clase que reciba una lista de diccionario de estudiante y 
un profesor ademas una funcion llamar alumnos para selecionar un alumno por nombre y que llame la funcion hablar'''
class Llamar:
    def __init__ (self,estudiante,profesor):
        self.estudiante = estudiante
        self.profesor = profesor
    
    def llamar(self,nombre):
            if self.estudiante.nombre == nombre:
                self.estudiante.llamado()
            else:
                print(f'No se encontro al alumno de nombre {nombre}')
        
estudiante = Estudiante("Jose","Alvarez",27)
profesor = Profesor("Marcos", "Algebra Lineal", "8:00am a 5:00pm")
llamar = Llamar(estudiante,profesor)

llamar.llamar("Jose")

            