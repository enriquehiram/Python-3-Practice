import pygame  #importando pygame

#Definiendo colores
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

rect_x = 50         #Posicion de partida del rectangulo en x
rect_y = 50         #Posicion de partida del rectangulo en y
rect_cambio_x = 4
rect_cambio_y = 4
PI = 3.141592653  #estableciendo pi

pygame.init()  #initializating

#Haciendo la cochina ventana
dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("This is a test") #poniendole titulo

#Hasta que el usuario cierre la aplicacion.
hecho = False

#gestionar cuan rapido se actualiza la pantalla
reloj = pygame.time.Clock()

#-----Bucle principal del programa------
while not hecho:

    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
            hecho = True                # Acabamos y salimos del bucle

    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERIAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LOGICA DEL JUEGO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # TODA LA LOGICA DEL JUEGO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    # EL CODIGO DE DIBUJO DEBERIA IR DEBAJO DE ESTE COMENTARIO
     # EL CODIGO DE DIBUJO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    pantalla.fill(NEGRO) # Primero, limpia la pantalla con negro.
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y

    if rect_y > 450 or rect_y < 0:
        rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x * -1


    pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    reloj.tick(60) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
