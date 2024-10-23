lista = [1,2,3,4,5,6,7,8,9,10]
cantidad = len(lista)

# Recursividad
def contar(list):
    if list == []:
        return 0
    else:
        return 1 + contar(list[1:])
    
print(cantidad)
print(contar(lista))


# Numeros Primos
def numPrimos(numero, divisor = 2):
    if numero == divisor:
        return True
    elif numero % divisor == 0:
        return False
    else:
        return numPrimos(numero, divisor + 1)

print(numPrimos(5))

# Potencias
def potencia(base, elevado):
    if elevado == 0:
        return 1
    else:
        return base * potencia(base, elevado - 1)
print(potencia(2,3))

# Diccionarios
estudiante = {
    "Nombre" : "Jose",
    "Apellido" : "Alvarez",
    "Edad" : "27",
}

estudiante["graduado"] = "No" #Asi se agregan keys y values
print(estudiante)

estudiante["Direccion"] = "Guanacaste"
print(estudiante)

del estudiante["Direccion"] #Asi se eliminan 
print(estudiante)


# Ejercicio Diccionario
persona = {
    "Nombre" : "Jose",
    "Ciudad" : "Guanacaste",
    }

print(persona)

persona["Profesion"] = "Full Stack Developer"
persona["Edad"] = "27"
print(persona)


# Libreria 'Pickle'
# Para serializar y deserializar datos
import pickle 

estudiante = {
    "Nombre" : "Jose",
    "Apellido" : "Alvarez",
    "Edad" : "27",
}

estudiante_serializado = pickle.dumps(estudiante)
print(estudiante_serializado)

estudiante_des_serializado = pickle.loads(estudiante_serializado)
print(estudiante_des_serializado)



import shelve

with shelve.open('ejemplo bd') as bd: #Open crea y guarda la base de datos
    bd["Nombre"] = "Jose" # Aca se crean las variables para guardarlas en 'bd'
    bd["Apellido"] = "Alvarez"

with shelve.open('ejemplo bd') as bd:
    nombre = bd['Nombre']
    apellido = bd['Apellido']
print(nombre, apellido)



# Practica 
'''Vamos a crear 2 diccionarios con los siguientes datos: nombre, edad, profesión y habilidades. Y vamos a realzar las siguientes tareas:
Serializar los diccionarios -> mostrarlo
Crear un db para guardarlo usando shelve
Recuperar el diccionario -> mostrarlo
Deserializar el diccionario -> mostrarlo'''


dicc1 = {
    "Nombre" : "Jose",
    "Edad" : "27",
    "Profesion" : "Programador",
    "Habilidades" : "Tecnologia"
}

dicc2 = {
    "Nombre" : "Juan",
    "Edad" : "30",
    "Profesion" : "Ingeniero",
    "Habilidades" : "Administrador"
}

dicc1_serializado = pickle.dumps(dicc1)
dicc2_serializado = pickle.dumps(dicc2)

with shelve.open('diccionario bd') as dicc: 
    dicc["1"] = dicc1_serializado #Aca se guarda el diccionario como con clave 1 y valor dicc_serializado
    dicc["2"] = dicc2_serializado
    
with shelve.open('diccionario bd') as dicc:
    dicc1_cargado = dicc['1'] #Aca se guarda el valor de dicc_serializado y se le asigna una variable
    dicc2_cargado = dicc['2']

    
dicc1_des_serializado = pickle.loads(dicc1_cargado)
dicc2_des_serializado = pickle.loads(dicc2_cargado)

print(dicc1)
print(dicc2)
print(dicc1_serializado)
print(dicc2_serializado)
print(dicc1_des_serializado)
print(dicc2_des_serializado)


# Copy
import copy

'Ejemplo copy'
#Diccionario original
diccionario_original = {'a':[1,2,3], 'b':[4,5,6]}

#Hacemos una copia
diccionario_copia = copy.copy(diccionario_original)

#Modificamos el valor en la copia profunda
diccionario_copia['a'][0] = 99

print("Diccionario original: ", diccionario_original)
print("Diccionario copia: ", diccionario_copia )
# Usando 'copy' se cambia el valor en los dos diccionarios

'Ejemplo deepcopy'
#Diccionario original
diccionario_original1 = {'a':[1,2,3], 'b':[4,5,6]}

#Hacemos una copia
diccionario_copia_profunda = copy.deepcopy(diccionario_original)

#Modificamos el valor en la copia profunda
diccionario_copia_profunda['a'][0] = 99

print("Diccionario original: ", diccionario_original1)
print("Diccionario copia: ", diccionario_copia_profunda )
# Usando 'deepcopy' se cambia el valor solo en la copia, el original se mantiene