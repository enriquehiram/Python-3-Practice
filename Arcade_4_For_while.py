#Ejercicio 4.1 Two ways ot obtain the below output
#2
#4
#6
#8
#10
for i in range (2,12,2):
 print (i)
print
#for i in range(5):
#    print ((i+1)*2)
#print""


#Ejercicio 4.2 # se pide introducir un numero e imprime el numero y la interaccion
total= 0
for i in range(5):
    new_number = int(input("Introduce un numero: "))
    total += new_number
    print (i)
print ("El total es: ", total)


#Ejercicio 4.3 Este valor hace una sumatoria de 1 hasta 10 (1+2+3+4...)
suma = 0
for i in range(1,11):
    suma = suma + i
print(suma)


#Ejercicio 4.4 Ejercicio para entender y pronosticar el PROCESAMIENTO del for
Cual es el valor de a?
a = 0
for i in range(10):
    a=a+1
    print(a)
print()
# Cual es el valor de a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
print()
# Cual es el valor de a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)
print()


#Arcade 4.5 imprime la potencia de i*2 hasta llegar a i*32
i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2
print ("")


#Arcade 4.6  TEST ALONE PLEASE.
#If you put "n" you will be inside loop, if you tap any other
#then loop finish
salir = 'n'
while salir == 'n':
    salir = input ("Quieres salir? ")
    print("Sigues Dentro eh!!")
print ("Ya saliste")


#Arcade 4.7 TEST ALONE PLEASE
# you will continue inside loop until you press "Y" two times
hecho = False
while not hecho:
    salir = input ("Quieres salir? ")
    if salir == "y" :
        hecho = True;

    ataque = input ("Es que tu elfo ha atacado al dragon ")
    if ataque == "y":
        print ("Pesima opcion, estas muerto.")
        hecho = True;


#Arcade 4.8 Inicia con 0,5 y luego le suma la mitad de 0,5
# y luego la mitad de la mitady así...
valor = 0
incremento = 0.5
while valor < 0.999:
    valor += incremento
    incremento *= 0.5
    print(valor)
print ()
