'''Desarrolle un programa utilizando el lenguaje de programación Python, en el cual se puedan registrar los siguientes datos para cada usuario.

1.	Nombre
2.	Apellido1
3.	Apelldio2
4.	Número de Cuenta
5.	Saldo disponible.

Para este desarrollo puede emplear, tuplas, arreglos, matrices o diccionarios según considere conveniente,
la cantidad de clientes lo decide el usuario. Finalmente debe acomodar los datos de mayor a menor según el saldo disponible en cada cuenta, recuerde documentar su programa.
 
'''
#Creo una lista vacia para que no tenga limite de usuarios
usuarios = []

#while loop para que sea infita la cantidad de datos a agregar
while True:
    #diccionario donde ingresar usuarios
    usuario = {}
    
    #solicito informacion
    usuario['Nombre'] = input('Ingresar el nombre del usuario: ')
    usuario['Apellido1'] = input('Ingresar el primer apellido del usuario: ')
    usuario['Apellido2'] = input('Ingresar el segundo apellido del usuario: ')
    usuario['Numero de cuenta'] = input('Ingresar el numero de cuenta del usuario: ')
    usuario['Saldo Disponible'] = float(input('Ingresar el saldo disponible del usuario: '))
    
    #Uso .append para agregar la informacion de 'usuario' a la lista de 'usuarios' 
    usuarios.append(usuario)
    
    #Pregunto al usuario si quiere seguir agregando datos
    continuar = input('Desea continuar agregando usuarios? (s/n): ')
    #.lower sirve para convertir cada caracter a minuscula
    if continuar.lower() == 'n':
        break
    
#Ordeno la lista de usuarios por saldo de mayor a menor
usuarios_ordenados = sorted(usuarios, key=lambda x: x['Saldo Disponible'], reverse=True)
    
#De aca en adelante se muestran los resultados ordenados
print('\nUsuarios ordenados por saldo disponible de mayor a menor: ')

for usuario in usuarios_ordenados:
    print(f'Nombre: {usuario['Nombre']} {usuario['Apellido1']} {usuario['Apellido2']}')
    print(f'Numero de Cuenta: {usuario['Numero de cuenta']}')
    print(f'Saldo Disponible: {usuario['Saldo Disponible']}')
    #Despues de aca termina la informacion del primer usuario 
    #e imprimire una linea separadora que los divida
    print('-' * 30)
    
    
    
    



