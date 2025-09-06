anio = int(input("Ingresa un año: "))

if (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
elif (anio % 4 == 0) and (anio % 100 != 0):
    print(f"El año {anio} es bisiesto.")
else:
    print("El año ",anio, " no es bisiesto.")
