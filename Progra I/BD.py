from os import system
import time
import Conexion as conn # type: ignore
db = conn.DB()

def create():
    name = str(input("Ingrese el nombre: "))
    email = str(input("Ingrese el e-mail asociado con el nombre: "))
    if(len(name) > 0 and len(email) > 0 ):
        sql = "insert into Persona (Nombre, Email) values (?,?)"
        parametros = (name, email)
        db.ejecutar_consulta(sql,parametros)
        print("Registros ingresados con éxito")
    else:
        print("Nombre o Email no digitado")
def read():
    sql = "Select * from Persona"
    result = db.ejecutar_consulta(sql)
    for data in result: 
        print("""
              Nombre: {}
              Email: {}
              """. format (data[0],data[1]))

while True:
    print("#####################################")
    print("##   Menú principal del sistema      ##")
    print("#####################################")
    print("\t [1] Insertar un Registro")
    print("\t [2] Consultar todos los registros")
    print("\t [3] Actualizar un registro")
    print("\t [4] Eliminar un registro")
    print("\t [5] Buscar un registro en especifico")
    print("\t [6] Salir del sistema")
    try:
        opcion = int(input("Seleccione una opción: "))
        if(opcion == 1):
            create()
            time.sleep(1)
            system("clear")
        elif(opcion == 2):
            time.sleep(1)
            system("clear")
        elif(opcion == 3):
            time.sleep(1)
            system("clear")
        elif(opcion == 4):
            time.sleep(1)
            system("clear")
        elif(opcion == 5):
            time.sleep(1)
            system("clear")
        elif(opcion == 6):
            time.sleep(1)
            system("clear")
    except:
        print("Opcion inválida, seleccione una opción correcta del 1 al 6.")
        system("clear")