arreglo = ["Calculo", "Algebra", "Ingles", "Estadistica", "Algoritmos"]

for i in range(len(arreglo)):
  print(arreglo[i])
  
print("  \nSolo estoy practicando\n   ")

notas = []

size = int(input("Cantidad de cursos: "))

for j in range(size):
  score = int(input("Puntos en cada curso: "))
  notas.append(score)
  
average = sum(notas) / size

print(f"Su porcentaje es: {average}")

if average < 70:
  print("No alcanzaste el minimo, lo siento")
else:
  print("Felicidades!")