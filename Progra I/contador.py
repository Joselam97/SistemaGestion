materias = ['Espa;ol: ','Matematicas: ','Ciencias: ','Estudios Sociales: ', 'Quimica: ', 'Fisica: ', 'Biologia: ', 'Civica: ']
calificaciones = []

for materia in materias:
    calificacion = int(input('Que calificacion obtuvo en ' + materia))
    calificaciones.append(calificacion)
    
for contador in range(len(materias)):
    if calificaciones[contador] >= 70:
        resultado = "Aprobo"
    else:
        resultado = "Reprobo"
    print(f"\nEn  {materias[contador]} obtuvo {calificaciones[contador]} y {resultado}")


""" 
materias = ['Espa;ol: ','Matematicas: ','Ciencias: ','Estudios Sociales: ', 'Quimica: ', 'Fisica: ', 'Biologia: ', 'Civica: ']
calificaciones = []
for materia in materias:
    Calificacion = input('Que calificacion obtuvo en ' + materia)
    calificaciones.append(Calificacion)
for contador in range(len(materias)):
    print("En " + materias[contador] + " obtuvo " + calificaciones[contador])
"""