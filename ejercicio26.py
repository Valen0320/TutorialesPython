sueldo=int(input("Ingrese el sueldo del empleado:"))
antiguedad=int(input("Ingrese la antiguedad en años:"))
if sueldo<500 and antiguedad>=10:
    aumento=sueldo*0.20
    totalsueldo=sueldo+aumento
    print(totalsueldo)
else:
    if sueldo<500:
        aumento=sueldo*0.05
        totalsueldo=sueldo+aumento
        print(totalsueldo)
    else:
        print(sueldo)
