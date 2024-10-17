datos = (
    [1, 'Juan', 'Fernandez', 21, 'Guanacaste'],
    [2, 'Jose', 'Aguilar', 27, 'Heredia'],
    [3, 'Maria', 'Rodriguez', 22, 'San Jose'],
    [4, 'Fernanda', 'Sanchez', 24, 'Alajuela']
    )

matriz = []

for i in range(4):
    fila = []
    for j in range(5):
        fila.append(datos[i][j])
    matriz.append(fila)
    
for fila in matriz:
    print(fila)
    
        
        
        
        