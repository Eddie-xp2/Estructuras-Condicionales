cal = int(input("Ingresa tu calificación (0-100): "))

if cal >= 90 and cal <= 100:
    print("Tu calificación en letra es: A")
elif cal >= 80 and cal <= 89:
    print("Tu calificación en letra es: B")
elif cal >= 70 and cal <= 79:
    print("Tu calificación en letra es: C")
elif cal >= 60 and cal <= 69:
    print("Tu calificación en letra es: D")
elif cal >= 0 and cal < 60:
    print("Tu calificación en letra es: F")
else:
    print("Calificación fuera de rango debe estar entre 0 y 100.")
