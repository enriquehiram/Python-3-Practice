            # Ejercicio 9.4.2 using return
    # Suma de dos numeros y devuleve el resultado
def suma_dos_numeros(a, b):
    resultado = a + b
    return resultado

mi_resultado = suma_dos_numeros(22, 15)
print (mi_resultado)



            # Ejercicio 9.4.2.1 más ejemplos de return
# Suma de dos numeros e imprime el resultado
def imprime_suma(a, b):
    resultado = a + b
    print (resultado)

# Suma de dos numeros y devuleve el resultado
def devuelve_suma(a, b):
    resultado = a + b
    return resultado

# Esto imprime en pantalla la suma de 4+4
imprime_suma(4, 4)
# Este...también
devuelve_suma(4, 4)
# Esto no introducirá el resultado de la suma en x1
# Obtiene realmente un valor de 'None'
x1 = imprime_suma(4, 4)
# Esto sí lo hará
x2 = devuelve_suma(4, 4)



            # Ejercicio 9.6 Ámbito (scope) de la variable
    # Ejemplo 1
# Define una función elemental que establece que x es igual a 22
def f():
    X=22
# llamada de la función
f()
# FALLA, YA QUE X EXISTE SOLO EN F()
print(x)
    # Ejemplo 2
# Define una función elemental que establece que y es igual a 44
y = 44
def g():
    print (y)
# llamada de la función
g()
# LA FUNCION PUEDE LEER EL VALOR DE LA VARIABLE CREADA ANTES QUE LA FUNCION
# DADO QUE SU VALOR NO CAMBIA
    # Ejemplo 3
# Define una función elemental que establece que w es igual a 44
w = 44
def h():
    w += 1
    print (w)
# Llamamos a la función
h()
# LA FUNCION NO PUEDE LEER EL VALOR DE LA VARIABLE CREADA ANTES QUE LA FUNCION
# DADO QUE SU VALOR CAMBIA



            # Ejercicio 9.7 Pass-by-code
# define una función elemental que imprime x
def f(x):
    x += 1
    print ("x es igual a: ", x)
y = 10 # Establece y
f(y) # Llamada de función
print ("y es igual a: ", y) #imprime y para ver si ha cambiado
# EJEMPLO IMPORTANTE, EL VALOR DE UNA VARIABLE NO CAMBIA DENTRO DE UNA FUNCION
# define una función elemental que imprime x
def f(x):
    x += 1
    print ("x en función es igual a: ", x)
x = 10 # Establece y
f(x) # Llamada de función
print ("x afuera de funcion es igual a: ", x) #imprime y para ver si ha cambiado



            # Ejercicio 9.9
# El usos correcto en que python debe ejecutarse:
def main():
    print("Hola Mundo.")

if __name__ == "__main__":
    main()



            # Ejercicios 9.10
# Ejemplo 1  A
def a():
    print("A")
def b():
    print("B")
def c():
    print ("C")
a()

# Ejemplo 2  C--B--A
def a():
    b()
    print("A")
def b():
    c()
    print("B")
def c():
    print ("C")
a()

# Ejemplo 3  A--B--C
def a():
    print("A")
    b()
def b():
    print("B")
    c()
def c():
    print ("C")
a()

# Ejemplo 4  A--B--C--B--A
def a():
    print("A empieza con")
    b()
    print("A termina con")
def b():
    print("B empieza con")
    c()
    print("B termina con")
def c():
    print ("C empieza y termina con")
a()

# Ejemplo 5  Esta bueno, pruébalo
def a(x):
    print("A empieza con, x = ",x)
    b(x + 1)
    print("A termina con, x = ",x)
def b(x):
    print("B empieza con, x = ",x)
    c(x + 1)
    print("B termina con, x = ",x)
def c(x):
    print("C empieza y termina con, x = ",x)
a(5)

# Ejemplo 6 ¿Cuál será la respuesta?
def a(x):
    x = x + 1
x = 3
a(x)
print (x)

# Ejemplo 7 ¿Y ahora?
def a(x):
    x = x + 1
    return x
x = 3
a(x)
print (x)

# Ejemplo 8 ¿Qué tal ahora? ¿puedes adivinar?
def a(x):
    x = x + 1
    return x
x = 3
x = a(x)
print (x)

# Ejemplo 9 ERROR. ¿por qué?
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)
x = 10
y = 20
a(y, x)
print(z)

# Ejemplo 10 Imprime (aunque no deberia) un 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y
x = 10
y = 20
z = a(x, y)
print(z)

# Ejemplo 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
x = 10
y = 20
z = a(x, y)
print(z)

# Ejemplo 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y
x = 10
y = 20
x2, y2 = a(x, y) # La mayoría de lenguajes de programación no admiten esto
print(x2)
print(y2)

# Ejemplo 13
def a(mis_datos):
    print("función a, mis_datos =  ", mis_datos)
    mis_datos = 20
    print("función a, mis_datos =  ", mis_datos)
mis_datos = 10
print("entorno global, mis_datos = ", mis_datos)
a(mis_datos)
print("entorno global, mis_datos = ", mis_datos)

# Ejemplo 14
def a(mi_lista):
    print("función a, lista =  ", mi_lista)
    mi_lista = [10, 20, 30]
    print("función a, lista =  ", mi_lista)
mi_lista = [5, 2, 4]
print("entorno global, lista = ", mi_lista)
a(mi_lista)
print("entorno global, lista = ", mi_lista)

# Ejemplo 15
# Concepto nuevo!
# Se describe con más detalle en el Capítulo 12
def a(mi_lista):
    print("función a, lista =  ", mi_lista)
    mi_lista[0] = 1000
    print("función a, lista =  ", mi_lista)
mi_lista = [5, 2, 4]
print("entorno global, lista = ", mi_lista)
a(mi_lista)
print("entorno global, lista = ", mi_lista)
