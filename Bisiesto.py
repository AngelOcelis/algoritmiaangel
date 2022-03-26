año=int(input("Digite el Año: "))
if año%400==0:
    print("El Año es Bisiesto")
else:
    if año%4==0 and año%100!=0:
       print("El Año es Bisiesto")
    else:
       print("El Año No es Bisiesto")
    
 