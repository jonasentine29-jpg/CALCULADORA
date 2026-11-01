
"""from area import cuadrado, rectangulo, triangulo, circulo"""
import area


operacion=input("Ingrese la operación a realizar: ").upper()
v1=float(input("Ingrese el primer valor: "))
v2=float(input("Ingrese el segundo valor: "))

#jonathan xavier sentine de leon 
#23/10/2026
#avance calculadora

def operaciones(v1,v2,operacion):
    if operacion=="SUMA":
        print("suma = ", v1+v2)
    elif operacion=="RESTA":
        print("resta = ", v1-v2)
    elif operacion=="MULTIPLICACION":
        print("multiplicacion = ", v1*v2)
    elif operacion=="DIVISION":
        print("division = ", v1/v2)
    elif operacion=="DIVISION_ENTERA":
            print("division_entera = ", v1//v2)
    elif operacion=="RESIDUO":
        print("residuo = ", v1%v2)
    elif operacion=="POTENCIA":
        print("potencia = ", v1**v2)
    elif operacion=="RAIZ":
        print("raiz = ", v1**(1/v2))

operaciones(v1,v2,operacion)
area.cuadrado(5)
