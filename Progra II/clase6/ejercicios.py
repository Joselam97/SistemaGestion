'''Escribe una función que recorra una lista de números y separe los pares de los impares.'''
def separar_impares(lista):
    impares = []
    if(len(lista)%2 == 0):
        for i in range(0, len(lista), 2):
            impares.append(lista[i])
    else:
        return "la lista no es par"
    return impares

print(f'Los impares son: {separar_impares([1,2,3,4,5,6,7,8,9,10])}')


'''Escribe una función recursiva que cuente cuántas letras hay en una cadena de texto.'''
def contar_letras(cadena):
    if(len(cadena) == 0):
        return 0 
    else:
        return 1 + contar_letras(cadena[1:])
    
print(f'El numero de letras de la cadena es: {contar_letras("Hola, mi nombre es Jose")}')


'''Escribe una función recursiva que invierta una cadena (use la funcion de contar).'''
def invertir(cadena):
    if(len(cadena) == 0):
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]
    
print(f'La palabra \'Hola estoy practicando Python\' invertida es: {invertir("Hola, estoy practicando Python")}')


'''Escribe una función que determine si una palabra es un palíndromo (se lee igual al revés y use la funcion de invertir).'''
def es_palindromo(palabra):
    if(len(palabra) == 0):
        return True
    elif(len(palabra) == 1):
        return True
    elif(palabra[0] == palabra[-1]):
        return es_palindromo(invertir(palabra[1:-1]))
    else:
        return False
        
print(f'La palabra \'sanas\' es palindroma? {es_palindromo("sanas")}')


'''Escribe una función que devuelva el número mayor en una lista. (no se puede usar `max`).'''
def mayor(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if(lista[i] > mayor):
            mayor = lista[i]
    return mayor

print(f'El numero mayor en la lista [1,20,13,14,55,16,17,18,99,10] es: {mayor([1,20,13,14,55,16,17,18,99,10])}')


'''Escribe una función que devuelva el número mayor en una lista. (no se puede usar `min`).'''
def menor(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if(lista[i] < menor):
            menor = lista[i]
    return menor

print(f'El numero menor en la lista [1,20,13,14,55,16,17,18,99,10] es: {menor([1,20,13,14,55,16,17,18,99,10])}')


'''Escribe una función que elimine un número en una lista. (no se puede usar `remove`)'''
def eliminar(lista, numero):
    for i in range(len(lista)):
        if(lista[i] == numero):
            lista.pop(i)
            break
    return lista
 
print(f'La lista despues de eliminar el numero 10 es: {eliminar([1,20,13,14,55,16,17,18,99,10], 10)}')


'''Escribe una función que ordene una lista de menos a mayor. (haga uso de las funciones de numero_menor y elimiar)'''
def menor(lista):
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

def eliminar(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            lista.pop(i)
            break  
    return lista

def ordenar(lista):
    lista_ordenada = []
    while len(lista) > 0:
        num_menor = menor(lista)  
        lista_ordenada.append(num_menor) 
        eliminar(lista, num_menor)  
    return lista_ordenada

print(f'La lista [1, 20, 13, 14, 55, 16, 17, 18, 99, 10] ordenada es: {ordenar([1, 20, 13, 14, 55, 16, 17, 18, 99, 10])}')


'''Escribe una función que ordene una lista de mayor a menor. (haga uso de las funciones de numero_mayor y elimiar)'''
def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def eliminar(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            lista.pop(i)
            break
    return lista

def ordenar_mayor_a_menor(lista):
    lista_ordenada = []
    while len(lista) > 0:
        num_mayor = mayor(lista)
        lista_ordenada.append(num_mayor)
        eliminar(lista, num_mayor)
    return lista_ordenada

print(f'La lista [1, 20, 13, 14, 55, 16, 17, 18, 99, 10] ordenada de mayor a menor es: {ordenar_mayor_a_menor([1, 20, 13, 14, 55, 16, 17, 18, 99, 10])}')



'''Escribe una función recursiva que imprima cada elemento de una lista.'''
def imprimir_elementos(lista):
    if len(lista) == 0:
        return
    else:
        print(lista[0])
        imprimir_elementos(lista[1:])

lista = [1,2,3,4,5]
imprimir_elementos(lista)