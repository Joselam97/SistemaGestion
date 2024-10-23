#Ejemplo 1
lista = ['jose','andres','leo','alejandro','carlos']
print(lista[2]) 

#Ejemplo 2
frutas = ['kiwi','naranja','sandia','uva','banano','coco']
frutas.append('papaya')
frutas.remove('kiwi')
frutas.pop # proporciona el ultimo elemento
print(frutas)

#Ejemplo 3
sublista = frutas[1:3] #del segundo elemento al cuarto
sublista = frutas[:4] #del inicio al cuarto elemento
print(sublista)

#Ejemplo 4
sublista = frutas[::2] #[:':'2] sirve para omitir cada elemento 2 
print(sublista)

#Ejemplo 5
print(frutas[:-1]) #Imprime el ultimo elemento
print(frutas[-2:]) #Imprime los 2 ultimos

#Ejemplo 5 Factorial
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n-1) #Funcion recursiva
print(factorial(7))

#Ejemplo 6 Fibonacci
def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
print(fibonacci(8))

#Ejemplo 7 Sumatoria
def sumatoria(x):
    # x = 123
    #sumatoria = 1+2+3
    if x < 10:
        return x
    else:
        return x%10 + sumatoria(x//10) # x%10 devuelve el ultimo digito x//10 quita el ultimo
    
print(sumatoria(123))