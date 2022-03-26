piedra= 1
papel= 2
tijera= 3
persona1=int(input("Herramienta jugador 1: "))
persona2=int(input("Herramienta jugador 2: "))
if persona1==piedra and persona2==papel :
    print("piedra es envuelta por el papel, gana el jugador 2")
elif persona1==piedra and persona2==tijera :
    print("piedra daña tijera, gana el jugador 1")
elif persona1==piedra and persona2==piedra :
    print("la piedra no daña a la piedra, nadie gana")
if persona1==papel and persona2==piedra:
    print("el papel envuelve la piedra, gana el jugaodor 1")
elif persona1== papel and persona2== tijera:
    print("el papel es cortado por la tijera, gana el jugador 2")
elif persona1== papel and persona2== papel:
    print("el papel no daña el papel, nadie gana")
if persona1== tijera and persona2== piedra:
    print("la tijera no corta la piedra, gana el jugador 2")
elif persona1== tijera and persona2== papel:
    print("la tijera corta el papel, gana el jugador 1")
elif persona1== tijera and persona2== tijera:
    print("la tjera no corta otra tijera, nadie gana")