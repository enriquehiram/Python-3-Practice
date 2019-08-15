# Ejemplos 7.3 iterando en una lista
mi_lista = [101, 20, 102, 10, 50, 60]
mi_lista = ["Cuchara", "Tenedor", "Cuchillo"]
mi_lista = [[2, 3], [4, 3], [6, 7]]
        #Ejemplo bucle "para-cada"  Trabaja con una copia de lo deseado
for item in  mi_lista:
    print (item)
        #Trabajando directamente con los componentes de las listas
for i in range(len(mi_lista))
print(mi_lista[i])



# Ejemplos 7.4 Añadiendo items a una lista
        # The easiest way
mi_lista = [2, 4, 5, 6]
print(mi_lista)
mi_lista.append(9)
print(mi_lista)
        # Requesting items from the keyboard input
mi_lista = [] #lista vacia
for i in range (5):
    entrada_usuario = input("Introducir un número entero: ")
    entrada_usuario = int(entrada_usuario)
    mi_lista.append(entrada_usuario)
    print(mi_lista)
        # Crear un array con 100 ceros
mi_lista = [0] * 100



#Ejemplos 7.5 Sumar o Modificar una Lista
        # Suma acumulada de los valores de una lista v1
mi_lista = [5, 76, 8, 5, 3, 3, 56, 5, 23]
total_lista = 0 # La suma inicial debería ser cero
# Itera desde 0 hasta el total del número de elementos
# en el array:
for i in range(len(mi_lista)):
    # Añade el elemento 0, después el 1, luego el 2, etc.
    total_lista += mi_lista[i]
    print(total_lista) # Imprime el resultado
print()
print()
        # Suma acumulada de los valores de una lista v2
mi_lista = [5, 76, 8, 5, 3, 3, 56, 5, 23]
total_lista = 0 # La suma inicial debería ser cero
# Itera desde 0 hasta el total del número de elementos
# en el array:
for item in mi_lista:
    # Añade cada item
    total_lista += items
print (total_lista)
print()
print()
        #Duplicando los números en una listas
mi_lista = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# Itera desde 0 hasta el total del número de elementos
# en el array:
for i in range(len(mi_lista)):
    #Modifica el elemento duplicándolo
    mi_lista [i] = mi_lista [i] * 2
print (mi_lista)
print()
print()



# Ejemplos 7.6 Dividir cadenas de texto
        # Accede a una cadena de texto como una lista
x = "Esta es una cadena de ejemplo: ñ"
#x = "0123456789"
print("x=", x)
# Acceso a un carácter individual
print("x[0] = ", x[0])
print("x[1] = ", x[1])
# Acceso desde la derecha
print("x[-1] = ", x[-1])
# Acceso 0 - 5
print("x[:6] = ", x[:6])
# Acceso 6
print("x[6:] = ", x[6:])
# Acceso 6 - 8
print("x[6:9] = ", x[6:9])
        # Añadiendo y multiplicando cadenas de texto
a = "Hola"
b = "Qué tal"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))
        # Obtener la longitud de una cadena o de una lista
a = "Hola, qué tal"
print(len(a))
b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))
        # Iterando a través de los elementos de un array
for caracter in "Esto es una prueba":
    print (caracter)
        # Ejercicio para iterar en una cadena
meses = "EneFebMarAbrMayJunJulAgoSepOctNovDic"
n = int(input("Introduce un número de mes: "))
m = (n - 1) * 3
print ("El mes que invocas es:",meses[m:(m+3)])



# Ejemplos 7.7 Criptacion
        # Imprimiendo individualmente cada letra de una cadena de texto
texto_llano = "Esto es una prueba. ABC abc"
for c in texto_llano:
        print (c, end = " ")
print()
print()
        # Convierte cada letra del ejemplo en su valor ordinal
texto_llano = "Esto es una prueba. ABC abc"
for c in texto_llano:
        print (ord(c), end = " ")
print()
print()
        # una vez convertido en su valor ordinal le suma un uno
texto_llano = "Esto es una prueba. ABC abc"
for c in texto_llano:
    x = ord(c)
    x = x + 1
    c2 = chr (x)
    print (c2, end = " ")
print()
print()
        # Simple encryption file
texto_llano = "Esto es una prueba. ABC abc"
texto_cifrado = ""
for c in texto_llano:
    x = ord(c)
    x = x + 1
    c2 = chr (x)
    texto_cifrado = texto_cifrado + c2
print(texto_cifrado)
print()
        # Simple decryptation file
texto_cifrado = "Ftup!ft!vob!qsvfcb/!BCD!bcd"
texto_plano = ""
for c in texto_cifrado:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    texto_plano = texto_plano + c2
print(texto_plano)



# Ejemplo 7.8 Arrays Asociativos
# Crea un array asociativo vacío
# (Observar las llaves.)
x = {}
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1
# Obtener e imprimir un item
print(x["fred"])
