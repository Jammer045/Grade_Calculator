"""Determina si un alumno paso el examen considerando >95 de aprobacion es graduado con honores, si es >=85 es aprobado, si es >=70 es regular, y si es <70 es desaprobado"""

nota = int(input("Ingrese su nota: "))

if nota >= 95:
    print("Graduado con honores")
elif nota >= 85:
    print("Aprobado, tienes buena nota")
elif nota >= 70:
    print("Regular, échale ganas")
else:
    print("Reprobado")