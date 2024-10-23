# Ejercicio 1
colores = ["rojo","azul","verde","amarillo","morado"]
print(colores[0])
print(colores[2])
print(colores[-1])


# Ejercicio 2
animales = ["perro","gato","pajaro"]
animales.append("pez")
animales.remove("gato")
print(animales)


# Ejercicio 3
lista1 = [1,2,3,4,5,6,7,8,9,10]

lista2 = lista1[:5]
print(lista2)

lista3 = lista1[1::2]
print(lista3)


# Ejercicio 4
def naturales(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0 
    elif n < 0:
        print("Se debe ingresar un numero positivo.")
    else:
        return list(range(1, n + 1))
    
print(naturales(-10))


# Ejercicio 5
def contador(n):
    if n < 10:
        return 1
    elif n < 0:
        print("Se debe ingresar un numero positivo.")
    else:
        return 1 + contador(n // 10)

n = 12345
print(f"El numero {n} tinen {contador(n)} digitos.")