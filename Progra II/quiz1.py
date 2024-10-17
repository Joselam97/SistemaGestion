'''Escriba un código en Python que a partir de una lista retorne un diccionario 
con la cantidad de veces que aparece cada elemento en la lista.
# entrada apariciones([1,2,3,4,5,5,6,3,1])'''

lista = ([1,2,3,4,5,5,6,3,1])
dic = {}

def apariciones(n):
    for i in lista:
        if i in dic:
            dic[i] += 1
            
        else:
           dic[i] = 1
    return dic
        
resultado = apariciones(dic)
print(resultado)
