n1=int(input("Ingrese primer nota"))
n2=int(input("Ingrese segunda nota"))
n3=int(input("Ingrese tercera nota"))
promedio=(n1+n2+n3)/3
if promedio>=7:
    print("Promocionado")
else:
    if promedio>=4:
        print("Regular")
    else:
        print("Reprobado")
