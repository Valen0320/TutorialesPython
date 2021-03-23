preguntas=int(input("Ingrese el total de preguntas"))
correctas=int(input("Ingrese el total de preguntas correctas"))
porcentaje=correctas*100 / preguntas
if porcentaje>=90:
    print("Nivel maximo")
else:
    if porcentaje>=75:
        print("Nivel medio")
    else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
