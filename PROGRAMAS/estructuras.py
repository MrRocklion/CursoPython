print("Alumnos Aprobados y Reprobados")
for i in [0,1,2]:
    nombre = input("nombre del estudiante: ")
    nota = input("Ingresa Una calificacion: ")
    def examen(nota):
        if nota >=7:
            valor = "aprobado"
        else:
            valor = "reprobado"
        return valor
    estado = examen(int(nota))
    list = [nombre,int(nota),estado]
    list3 = list
    list2.append(list)
print(list3[0])
for i in range(5)
