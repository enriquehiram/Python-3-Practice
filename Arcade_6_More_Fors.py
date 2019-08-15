# Ejercicio #1, Una linea de asteriscos con diez marcas
print ("Ejercicio #1")
for i in range (0, 10, 1):
    print ('*', end = " ")
print ()
print ()


# Ejercicio #2, 3 lineas de asteriscos, una de 10 otra de  5 y otra de 20 marcas
print ("Ejercicio #2")
for i in range (0, 10, 1):
    print ( '*', end = " " )
print ()
for i in range (0, 5, 1):
    print ( '*', end = " " )
print ()
for i in range (0, 20, 1):
    print ( '*', end = " " )
print ()
print ()


# Ejercicio #3, una cuadricula de asteriscos de 10x10
print ("Ejercicio #3")
for j in range (0, 10, 1):
    for i in range (0, 10, 1):
        print ( '*', end = " " )
    print ()
print ()
print ()


# Ejercicio #4, una cuadricula de asteriscos de 5x10
print ("Ejercicio #4")
for j in range (0, 10, 1):
    for i in range (0, 5, 1):
        print ( '*', end = " " )
    print ()
print ()
print ()


# Ejercicio #5, una cuadricula de asteriscos de 20x5
print ("Ejercicio #5")
for j in range (0, 5, 1):
    for i in range (0, 20, 1):
        print ( '*', end = " " )
    print ()
print ()


# Ejercicio #6, una cuadricula de numeros del 0 al 9  diez veces
print ("Ejercicio #6")
for j in range (0, 10, 1):
    for i in range (0, 10, 1):
        print ( i, end = " " )
    print ()
print ()
print ()


# Ejercicio #7, una cuadricula de numeros del 0 al 9  diez veces, pero cada linea tiene solo un numero
print ("Ejercicio #7")
for j in range (0, 10, 1):
    for i in range (0, 10, 1):
        print ( j, end = " " )
    print ()
print ()
print ()


# Ejercicio #8, una escalera de numeros del 0 al 9  diez veces, empezando en el 0
# e incrementando un numero en cada renglón justificada a la izquierda
print ("Ejercicio #8")
for j in range (0, 10, 1):
    for i in range (j + 1):
        print ( i, end = " " )
    print ()
print ()
print ()


# Ejercicio #9, una escalera de numeros del 0 al 9  diez veces, empezando en toda la enmuneración
# e incrementando un numero en cada renglón, justificada a la derecha
#for j in range (10, 0, -1):
#    for i in range (j):
#        print ( i, end = " " )
#    print ()
#print ()
#print ()
print ("Ejercicio #9")
for j in range (10, 0, -1):
    for i in range (10 - j):
        print ( " ", end = " " )
    for i in range (j):
        print ( i, end = " " )
    print ()
print ()
print ()


# Ejercicio #10, un cuadro donde te muestra las tablas de multiplicar
print ("Ejercicio #10")
for j in range (1, 11, 1):
    for i in range (1, 11, 1):
        if i *j < 10:
            print ("", end =" ")
        print ( i * j, end = " ")
    print ()
print ()
print ()


# Ejercicio #11, doble piramide de números del 1 al 9 y de regreso
print ("Ejercicio #11")
for j in range (0, 9, 1):

    for i in range (8 - j):
        print ( " ", end = " " )

    for i in range (j + 1):
        print ( i + 1, end = " " )
    k = i
    while k > 0:
        print ( k, end = " " )
        k = k - 1
    print ()
print ()
print ()


#Ejercicio #12, cuasi rombo de numeración escalonada o algo asteriscos
print ("Ejercicio #12")
for j in range (0, 9, 1):

    for i in range (8 - j):
        print ( " ", end = " " )

    for i in range (j + 1):
        print ( i + 1, end = " " )
    k = i
    while k > 0:
        print ( k, end = " " )
        k = k - 1
    print ()

for j in range (8, 0, -1):
    for i in range (9 - j):
        print ( " ", end = " " )
    for i in range (j):
        print ( i + 1, end = " " )
    print ()
print ()
print ()

#Ejercicio #13, el rombo completo de numeración escalonada
print ("Ejércicio #13")
for j in range (0, 9, 1):

    for i in range (8 - j):
        print ( " ", end = " " )

    for i in range (j + 1):
        print ( i + 1, end = " " )
    k = i
    while k > 0:
        print ( k, end = " " )
        k = k - 1
    print ()

for j in range (8, 0, -1):

    for i in range (9 - j):
        print ( " ", end = " " )

    for i in range (j):
        print ( i + 1, end = " " )
    x = i
    while x > 0:
        print ( x, end = " " )
        x -= 1
    print ()
print ()
print ()
