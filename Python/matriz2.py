personas = []
 
for i in range(2):
    persona = []
   
    cedula = input("Digite la cedula: ")
    nombre = input("Digite el nombre: ")
    apellido1 = input("Digite el apellido 1: ")
    apellido2 = input("Digite el apellido 2: ")
    edad = input("Digite la edad: ")
    canton = input("Digite el canton: ")
   
    persona.append(cedula)
    persona.append(nombre)
    persona.append(apellido1)
    persona.append(apellido2)
    persona.append(edad)
    persona.append(canton)
   
    personas.append(persona)

for persona in personas:
   print(persona)