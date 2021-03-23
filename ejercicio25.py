x=int(input("Ingrese coordenada x"))
y=int(input("Ingrese coordenada y"))
if x>0 and y>0:
    print("Se encuentra en el primer cuadrante")
else:
    if x<0 and y>0:
        print("Se encuentra en el segundo cuadrante")
    else:
        if x<0 and y<0:
            print("Se encuentra en el terce cuadrante")
        else:
            if x>0 and y<0:
                print("Se encuentra en el cuarto cuadrante")
            else:
                print("Se encuentra sobre un eje")
