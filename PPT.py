##############Variables###############



nombre_p1 = input('¿Cómo se llama el Jugador 1?: ')
nombre_p2 = input('¿Cómo se llama el Jugador 2?: ')

p1 = input("Jugador 1 ¿Qué eliges piedra, papel o tijeras?: ")
p2 = input("Jugador 2 ¿Qué eliges piedra, papel o tijeras?: ")
####################
op1 = "piedra"
op2 = "tijeras"
op3 = "papel"
str.lower(op1 and op2 and op3)
####################
condición1 = p1 == op1 and p2 == op2
condición3 = p1 == op3 and p2 == op1
condición2 = p1 == op2 and p2 == op3
###############################

if nombre_p1 == nombre_p2:
    print('Empate cagón')
elif(condición1) or (condición3) or (condición2):
    print(nombre_p1, " gana master")
else:
    print(nombre_p2, " gana master")

###TOdo: Poner mostrar nombre de J1 y J2; cortar el juego si no pickean ninguna de las indicadas####