import pygame  #importando pygame

# Definiendo colores
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (77, 190, 227)

PI = 3.141592653  #estableciendo pi

pygame.init()  #incializando juego

dimensiones = (700, 500) #Haciendo la ventana del juego
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("This is a test") #poniendole titulo
hecho = False #Hasta que el usuario cierre la aplicacion.
reloj = pygame.time.Clock() #gestionar cuan rapido se actualiza la pantalla
fuente = pygame.font.Font(None, 20) #fuente default , size 20 pts

#-----Bucle principal del programa------
while not hecho:

    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
            hecho = True                # Acabamos y salimos del bucle

    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERIAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LOGICA DEL JUEGO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # TODA LA LOGICA DEL JUEGO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    pantalla.fill(BLANCO) # Primero, limpia la pantalla con blanco.
    # EL CODIGO DE DIBUJO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    pygame.draw.line(pantalla, VERDE, [700, 0], [600,100], 5)
    pygame.draw.line(pantalla, VERDE, [700, 500], [600,400], 5)

    pygame.draw.line(pantalla, VERDE, [0, 0], [100,100], 5)
    for desplazar_y in range (0, 100, 10):
        pygame.draw.line(pantalla, ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)

    pygame.draw.line(pantalla, VERDE, [0, 500], [100,400], 5)
    for desplazar_y in range (0, 100, 10):
        pygame.draw.line(pantalla, ROJO, [0, 490 - desplazar_y], [100, 390 - desplazar_y], 5)
    pygame.draw.rect(pantalla, NEGRO, [100, 100, 500, 300], 5)
    pygame.draw.ellipse(pantalla, VERDE, [100, 100, 500, 300], 5)

    pygame.draw.arc(pantalla, AZUL, [110, 110, 480, 280], PI/2, PI, 5)
    pygame.draw.arc(pantalla, ROJO, [110, 110, 480, 280], 0, PI/2, 5)

    pygame.draw.polygon(pantalla, NEGRO, [[350, 200],[300,250],[400,250]],5)

#    fuente = pygame.font.Font(None, 20) #fuente default , size 20 pts
    mensaje = 'Intentar, intentar, intentar, no me queda de otra en esta vida'
    texto = fuente.render(mensaje, True, NEGRO)
    pantalla.blit(texto, [150,260])
    # EL CODIGO DE DIBUJO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    reloj.tick(60) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
