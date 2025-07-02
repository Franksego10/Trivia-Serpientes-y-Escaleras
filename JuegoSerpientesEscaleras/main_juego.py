import pygame
import random
from copy import deepcopy

from funciones_pygame import *
from reglas_pygame import *
from preguntas import *

from config_trivia import *
#CASILLEROS KEYS
clave1 = "casillero_1"
clave2 = "casillero_2"
clave3 = "casillero_3"
meta = "meta"
inicio = "inicio"
perder = "perder"

# PREGUNTAS
preguntas_copia = deepcopy(preguntas)
random.shuffle(preguntas_copia)
indice_pregunta = 0                         # elemento que va a servir para recorrer la lista de preguntas
incremento_pregunta = 1
pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""

# INICIALIZAR PYGAME
pygame.init()
clock = pygame.time.Clock()
# CREAR PANTALLA
pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)
pygame.display.set_caption("Trivia Serpientes y Escaleras") # Titulo de la ventana

# TIEMPO PREGUNTAS
tiempo_rect = pygame.Rect(705, 155, 228, 70)
timer_segundos_preguntas = pygame.USEREVENT
pygame.time.set_timer(timer_segundos_preguntas, UNSEGUNDO)
segundos = "15"
flag_tiempo = False

# TIEMPO MOSTRAR RESULTADO
tiempo_segundos_resultados = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_segundos_resultados, UNSEGUNDO)
segs_result = "3"

# IMAGEN INICIAL
imagen_principal = pygame.image.load("./JuegoSerpientesEscaleras/FondoPincipioJuego.png")
imagen_principal = pygame.transform.scale(imagen_principal, TAMANIO_PANTALLA)

# IMAGEN FONDO
imagen_fondo = pygame.image.load("./JuegoSerpientesEscaleras/SerpyEscaleras.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, TAMANIO_PANTALLA)

# IMAGEN JUEGO
imagen_tablero = pygame.image.load("./JuegoSerpientesEscaleras/Tablero.png")
imagen_tablero = pygame.transform.scale(imagen_tablero, TAMANIO_TABLERO_IMG)

# FUENTE TEXTOS
botones_fuente = pygame.font.Font(FUENTE, 20)   # FUENTE para los textos adentro de los botones
fuente_titulos = pygame.font.Font(FUENTE, 30)   # FUENTE para los titulos de las pantallas
fuente_textos = pygame.font.Font(FUENTE, 16)    # FUENTE para los textos de las reglas
fuente_preguntas = pygame.font.Font(FUENTE, 15) # Fuente para las preguntas del juego
fuente_opciones = pygame.font.Font(FUENTE, 14)
fuente_inicio = pygame.font.Font(FUENTE, 25)

# BOTONES NORMALES
rect_score = pygame.Rect(CORD_BOTON["boton_score"]["X"],CORD_BOTON["boton_score"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])
texto_score = "SCORE"
rect_jugar = pygame.Rect(CORD_BOTON["boton_jugar"]["X"],CORD_BOTON["boton_jugar"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])
texto_jugar = "JUGAR"
rect_salir = pygame.Rect(CORD_BOTON["boton_salir"]["X"],CORD_BOTON["boton_salir"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])
texto_salir = "SALIR"
rect_info = pygame.Rect(CORD_BOTON["boton_info"]["X"],CORD_BOTON["boton_info"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])
texto_info = "INFO"
rect_atras = pygame.Rect(CORD_BOTON["boton_atras"]["X"],CORD_BOTON["boton_atras"]["Y"] , TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])  # BOTON "ATRAS" PANTALLA DE INFO/SCORE
rect_atras_game = pygame.Rect(CORD_BOTON["boton_atras_game"]["X"], CORD_BOTON["boton_atras_game"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])      # BOTON "ATRAS" EN PANTALLA JUEGO
texto_atras = "ATRAS"
rect_start = pygame.Rect(CORD_BOTON["boton_start"]["X"],CORD_BOTON["boton_start"]["Y"], TAMANIO_BOTON["ancho"], TAMANIO_BOTON["alto"])
texto_start = "START"

# BOTONES OPCIONES
rect_opcion_a = pygame.Rect(CORD_BOT_OPCIONES["a"]["X"], CORD_BOT_OPCIONES["a"]["Y"], TAMANIO_BOT_OPCIONES["ancho"], TAMANIO_BOT_OPCIONES["alto"])
rect_opcion_b = pygame.Rect(CORD_BOT_OPCIONES["b"]["X"], CORD_BOT_OPCIONES["b"]["Y"], TAMANIO_BOT_OPCIONES["ancho"], TAMANIO_BOT_OPCIONES["alto"])
rect_opcion_c = pygame.Rect(CORD_BOT_OPCIONES["c"]["X"], CORD_BOT_OPCIONES["c"]["Y"], TAMANIO_BOT_OPCIONES["ancho"], TAMANIO_BOT_OPCIONES["alto"])

# CORRER JUEGO
pantalla_inicio = True
flag_correr = True

# PANTALLA INFO
titulo_info = "REGLAS DEL JUEGO"
pantalla_info = False

# PANTALLA JUEGO
pantalla_juego = False
empezar_juego = False
titulo_juego = "TRIVIA SERPIENTES Y ESCALERAS"
texto_pedir_usuario = 'Ingrese Nombre del Jugador'
jugador = ""
jugador_rect = pygame.Rect(300, 280, 390, 50)

# FICHA JUGADOR POSICION INICIAL (15) = (130, 270 )
posicion_jugador = POSICION_INICIAL
ficha_rect = pygame.Rect(CORDS_CASILLEROS_TABLERO[posicion_jugador][0], CORDS_CASILLEROS_TABLERO[posicion_jugador][1], TAMANIO_FICHA["ancho"], TAMANIO_FICHA["alto"])
ficha_rect.x = CORDS_CASILLEROS_TABLERO[posicion_jugador][0]
ficha_rect.y = CORDS_CASILLEROS_TABLERO[posicion_jugador][1]

casilleros_movidos = 0
informe_jugador1 = ""
informe_jugador2 = ""
rect_informe1 = pygame.Rect(665, 140, 320, 30)
rect_informe2 = pygame.Rect(665, 190, 320, 30)

# RESPUESTA CORRECTA O INCORRECTA
mostrar_resultado = False

# Fin Del juego
texto_terminar = "TERMINAR"
rect_terminar = pygame.Rect(740, 590, 160, 50)
fin_juego_pendiente = False
fin_juego = False
texto_final = ""

#SCORE
rect_ranking = pygame.Rect(660, 125, 330, 500)
titulo_ranking = "SCORES"
score_flag = True

# PANTALLA SCORE
pantalla_score = False
titulo_score = titulo_ranking
lista_puntajes = listar_scores()
ordenar_lista_puntajes(lista_puntajes)

#SONIDO 
pygame.mixer.init()
volumen = 0.12
sonido_fondo = pygame.mixer.Sound("./JuegoSerpientesEscaleras/A Funny Soul.mp3")
sonido_correcto = pygame.mixer.Sound("./JuegoSerpientesEscaleras/Correcto.mp3")
sonido_correcto.set_volume(0.11)
sonido_incorrecto = pygame.mixer.Sound("./JuegoSerpientesEscaleras/incorrecto.mp3")
sonido_incorrecto.set_volume(0.10)
sonido_fondo.set_volume(volumen)
sonido_fondo.play(-1)
# BUCLE PRINCIPAL
while flag_correr:
    lista_eventos_inicio = pygame.event.get()
    for evento in lista_eventos_inicio:
        if evento.type == pygame.QUIT:                          # ESTE EVENTO FINALIZA EL PROGRAMA SI EL USUARIO TOCA X
            flag_correr = False

        if evento.type == pygame.MOUSEMOTION:
            print(evento.pos)

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if pantalla_inicio:                                 # EVENTOS DE MOUSE EN PANTALLA INICIO
                if rect_salir.collidepoint(evento.pos):
                    flag_correr = False                         # Cerrar el juego si se hace clic en el botón Salir

                elif rect_jugar.collidepoint(evento.pos):
                    pantalla_inicio = False
                    pantalla_juego = True

                elif rect_score.collidepoint(evento.pos):
                    pantalla_score = True                    
                    pantalla_inicio = False

                elif rect_info.collidepoint(evento.pos):    
                    pantalla_inicio = False
                    pantalla_info = True
            
            elif pantalla_info:                                  # EVENTOS DE MOUSE EN PANTALLA INFO
                if rect_atras.collidepoint(evento.pos):
                    pantalla_inicio = True
                    pantalla_info = False
            
            elif pantalla_score:
                if rect_atras.collidepoint(evento.pos):          # EVENTOS DE MOUSE EN PANTALLA SCORE
                    pantalla_inicio = True
                    pantalla_score = False

            elif pantalla_juego:                                 # EVENTOS DE MOUSE EN PANTALLA JUGAR
                if rect_atras_game.collidepoint(evento.pos):
                    pantalla_inicio = True
                    pantalla_juego = False
                    jugador = ""
                elif rect_start.collidepoint(evento.pos):
                    if jugador.strip() != "":
                        pantalla_juego = False
                        empezar_juego = True
            
            if empezar_juego:                                               # EVENTOS DE MOUSE EN PANTALLA DEL JUEGO EMPEZADO
                if fin_juego == False:
                    if rect_terminar.collidepoint(evento.pos):
                        texto_final = "¡FIN DEL JUEGO!"
                        fin_juego = True
                
                    if mostrar_resultado == False:                              
                        respuesta = None
                        if rect_opcion_a.collidepoint(evento.pos):
                            respuesta = "a"
                            mostrar_resultado = True
                        elif rect_opcion_b.collidepoint(evento.pos):
                            respuesta = "b"
                            mostrar_resultado = True
                        elif rect_opcion_c.collidepoint(evento.pos):
                            respuesta = "c"
                            mostrar_resultado = True
                else:
                    if rect_atras.collidepoint(evento.pos):
                        flag_correr = False
        
        if fin_juego == False:                                                              # EVENTO DE TIEMPO (PREGUNTAS)
            if evento.type == pygame.USEREVENT:            
                if evento.type == timer_segundos_preguntas and empezar_juego:
                    if flag_tiempo == False:
                        segundos = int(segundos) - 1
                        if segundos == 0:
                            segundos = "¡TIEMPO!"
                            mostrar_resultado = True

            if mostrar_resultado == True:
                flag_tiempo = True                                                                #EVENTO DE TIEMPO MOSTRAR RESULTADO                       
                if evento.type == pygame.USEREVENT + 1:
                    if evento.type == tiempo_segundos_resultados and empezar_juego:
                    
                        segs_result = int(segs_result) - 1
                        
                        if segs_result == 0:
                            mostrar_resultado = False                         
                            indice_pregunta += incremento_pregunta
                            if indice_pregunta == len(preguntas_copia):
                                fin_juego = True
                                texto_final = "¡Perdiste! Se acabaron las preguntas"
                            pregunta = ""
                            informe_jugador1 = ""
                            informe_jugador2 = ""                            
                            segs_result = "3"
                            if fin_juego_pendiente:
                                fin_juego = True                                                   

        if evento.type == pygame.KEYDOWN:                        # EVENTOS DE TECLADO EN PANTALLA JUGAR
            if pantalla_juego:
                if evento.key == pygame.K_BACKSPACE:
                    jugador = jugador [0:-1]
                elif len(jugador) < 10:                
                    jugador += str(evento.unicode)
        
# ---------------------------------------
#            PANTALLA INICIO               
# ---------------------------------------

    if pantalla_inicio:                    
        pantalla.blit(imagen_principal, CORD_IMAGEN_FONDO) # FUNDE LA IMAGEN DE INICIO (FONDO)
        dibujar_boton(pantalla, rect_score, COLOR_AMARILLO, texto_score, COLOR_NEGRO, botones_fuente)  # DIBUJAR BOTON SCORE
        dibujar_boton(pantalla, rect_jugar, COLOR_AMARILLO, texto_jugar, COLOR_NEGRO, botones_fuente)  # DIBUJAR BOTON JUGAR
        dibujar_boton(pantalla, rect_salir, COLOR_ROJO, texto_salir, COLOR_NEGRO, botones_fuente)      # DIBUJAR BOTON SALIR
        dibujar_boton(pantalla, rect_info, COLOR_AMARILLO, texto_info, COLOR_NEGRO, botones_fuente)    # DIBUJAR BOTON INFO

# ---------------------------------------
#          PANTALLA INFO (REGLAS)               
# --------------------------------------- 

    elif pantalla_info:      
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO) # FUNDE LA IMAGEN DE FONDO  
        dibujar_boton(pantalla, rect_atras, COLOR_AMARILLO, texto_atras, COLOR_NEGRO, botones_fuente)  #DIBUJAR BOTON ATRAS
        titulo_info_render = fuente_titulos.render(titulo_info, True, COLOR_BLANCO)         # renderiza el titulo de la pantalla info
        pantalla.blit(titulo_info_render, CORD_TITULO_INFO)                                        # funde el titulo
        listar_reglas(pantalla, LISTA_REGLAS, fuente_textos, COLOR_BLANCO)                   # renderiza las reglas y las dibuja

# ---------------------------------------
#            PANTALLA SCORE               
# ---------------------------------------

    elif pantalla_score:
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)
        dibujar_boton(pantalla,rect_atras, COLOR_AMARILLO, texto_atras, COLOR_NEGRO, botones_fuente)
        titulo_score_render = fuente_titulos.render(titulo_score, True, COLOR_BLANCO)       #renderiza el titulo Score
        pantalla.blit(titulo_score_render, CORD_TITULO_SCORE)                               
        mostrar_lista_score(pantalla, lista_puntajes, botones_fuente, COLOR_AZUL)           # renderiza la lista de scores y las dibuja

# ---------------------------------------
#    PANTALLA Juego (Ingresar usuario)               
# ---------------------------------------

    elif pantalla_juego:
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)      # FUNDE LA IMAGEN DE FONDO
        
        titulo_juego_reder = fuente_titulos.render(titulo_juego, True, COLOR_BLANCO)        # Renderiza el titulo
        pantalla.blit(titulo_juego_reder, CORD_TITULO_JUEGO)

        texto_pedir_usuario_render = fuente_textos.render(texto_pedir_usuario, True, COLOR_NEGRO)       # renderiza el texto de pedir usuario
        pantalla.blit(texto_pedir_usuario_render, CORD_PEDIR_USUARIO)

        pygame.draw.rect(pantalla, COLOR_BLANCO, jugador_rect, 2)                           # dibuja un rectangulo sin relleno donde pareceran las letras que presione el usuario
        jugador_renderizado = fuente_textos.render(jugador, True, COLOR_NEGRO)          # renderiza las teclas que presiona el usuario
        texto_jugador_rect = jugador_renderizado.get_rect(center = jugador_rect.center)         # Obtiene el Rect del texto que ingresa y lo centra en el Rect principal
        pantalla.blit(jugador_renderizado, texto_jugador_rect)                              # funde al texto renderizado con el rect que se obtuvo

        dibujar_boton(pantalla, rect_atras_game, COLOR_AMARILLO, texto_atras, COLOR_NEGRO, botones_fuente)      # dibuja boton de atras
        dibujar_boton(pantalla, rect_start, COLOR_AMARILLO, texto_start, COLOR_NEGRO, botones_fuente)           # dibuja boton de comenzar

    # ---------------------------------------
    #   PANTALLA JUEGO EMPEZADO (Preguntas)              
    # ---------------------------------------

    elif empezar_juego:                                                             # PANTALLA PREGUNTAS
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)
        pantalla.blit(imagen_tablero, CORDENADA_TABLERO_IMG)                       # Funde la imagen del tablero

        # Todo lo que muestra el juego mientras esta sin terminar de alguna forma
        if fin_juego == False:
            dibujar_boton(pantalla, rect_terminar, COLOR_AZUL, texto_terminar, COLOR_BLANCO, botones_fuente)    # Dibuja boton de Terminar Juego, en caso de que no quiera seguir jugando

            if pregunta == "":                                                               # Condicional para cargar preguntas y respuestas
                pregunta = preguntas_copia[indice_pregunta]["pregunta"]
                respuesta_a = preguntas_copia[indice_pregunta]["respuesta_a"]
                respuesta_b = preguntas_copia[indice_pregunta]["respuesta_b"]
                respuesta_c = preguntas_copia[indice_pregunta]["respuesta_c"]
                color_opcion_a = COLOR_AMARILLO
                color_opcion_b = COLOR_AMARILLO
                color_opcion_c = COLOR_AMARILLO
                segundos = "15"
                flag_tiempo = False                            
                opcion_correcta = preguntas_copia[indice_pregunta]["respuesta_correcta"]
            
            # Si se acabo el tiempo para responder o clickea en unas de las opciones. Te muestra el resultado
            if mostrar_resultado:                                                           
                if respuesta != None:
                    resultado_respuesta = obtener_respuesta_correcta(preguntas_copia, indice_pregunta, respuesta)
                    if resultado_respuesta:
                        sonido_correcto.play()
                    else:
                        sonido_incorrecto.play()

                    posicion_anterior = posicion_jugador
                    posicion_jugador = mover_jugador(TABLERO, posicion_jugador, resultado_respuesta)               
                    casilleros_movidos = posicion_jugador - posicion_anterior
                    ficha_rect.x = CORDS_CASILLEROS_TABLERO[posicion_jugador][0]
                    ficha_rect.y = CORDS_CASILLEROS_TABLERO[posicion_jugador][1]

                    informe_jugador1, informe_jugador2 = mensaje_resultado(casilleros_movidos)

                elif segundos == "¡TIEMPO!":
                    sonido_incorrecto.play()
                    resultado_respuesta = False
                    posicion_anterior = posicion_jugador
                    posicion_jugador = mover_jugador(TABLERO, posicion_jugador, resultado_respuesta)
                    casilleros_movidos = posicion_jugador - posicion_anterior
                    ficha_rect.x = CORDS_CASILLEROS_TABLERO[posicion_jugador][0]
                    ficha_rect.y = CORDS_CASILLEROS_TABLERO[posicion_jugador][1]
                    
                    informe_jugador1, informe_jugador2 = mensaje_resultado(casilleros_movidos)

                    segundos = "15"
               
                if opcion_correcta == "a":
                    color_opcion_a = COLOR_VERDE
                elif opcion_correcta == "b":
                    color_opcion_b = COLOR_VERDE
                elif opcion_correcta == "c":
                    color_opcion_c = COLOR_VERDE

                if respuesta != opcion_correcta:
                    if respuesta == "a":
                        color_opcion_a = COLOR_ROJO
                    elif respuesta == "b":
                        color_opcion_b = COLOR_ROJO
                    elif respuesta == "c":
                        color_opcion_c = COLOR_ROJO
                           
                informe_jugador1_render = botones_fuente.render(informe_jugador1, True, COLOR_NEGRO)
                informe_jugador2_render = fuente_opciones.render(informe_jugador2, True, COLOR_NEGRO)
                texto_informe1_rect = informe_jugador1_render.get_rect(center = rect_informe1.center)
                texto_informe2_rect = informe_jugador2_render.get_rect(center = rect_informe2.center)
                pantalla.blit(informe_jugador1_render, texto_informe1_rect)
                pantalla.blit(informe_jugador2_render, texto_informe2_rect)

            respuesta = None

            pregunta_render = fuente_preguntas.render(pregunta, True, COLOR_NEGRO)
            pantalla.blit(pregunta_render, CORD_PREGUNTAS)
            dibujar_boton(pantalla, rect_opcion_a, color_opcion_a, respuesta_a, COLOR_NEGRO, fuente_opciones)
            dibujar_boton(pantalla, rect_opcion_b, color_opcion_b, respuesta_b, COLOR_NEGRO, fuente_opciones)  
            dibujar_boton(pantalla, rect_opcion_c, color_opcion_c, respuesta_c, COLOR_NEGRO, fuente_opciones)

            if flag_tiempo == False:
                segundos_texto_render = fuente_titulos.render(str(segundos), True, COLOR_BLANCO)
                rect_segundos_texto = segundos_texto_render.get_rect(center = tiempo_rect.center)
                pantalla.blit(segundos_texto_render, rect_segundos_texto)
            
            fin_juego_pendiente = fin_del_juego (posicion_jugador, indice_pregunta, preguntas_copia)            
            texto_final = texto_fin(texto_final, posicion_jugador)

    # ---------------------------------------
    #   PANTALLA JUEGO FINALIZADO              
    # ---------------------------------------

        else:
            posicion_final = f"{jugador} tu posición final es el numero {str(posicion_jugador)}"
            if score_flag:
                guardar_datos(jugador, posicion_jugador)
                lista_puntajes = listar_scores()
                ordenar_lista_puntajes(lista_puntajes)               
                score_flag = False
            
            texto_final_reder = botones_fuente.render(texto_final, True, COLOR_BLANCO)
            pantalla.blit(texto_final_reder, CORD_TEXTO_FINAL)
            dibujar_boton(pantalla, rect_atras, COLOR_AMARILLO, texto_salir, COLOR_NEGRO, botones_fuente)
            posicion_final_render = fuente_textos.render(posicion_final, True, COLOR_AZUL)
            pantalla.blit(posicion_final_render, CORD_TEXTO_POSICION_FINAL)

            titulo_ranking_render = fuente_titulos.render(titulo_ranking, True, COLOR_NEGRO)
            rect_titulo = titulo_ranking_render.get_rect()
            rect_titulo.centerx = rect_ranking.centerx
            rect_titulo.top = rect_ranking.top + 10
            pantalla.blit(titulo_ranking_render, rect_titulo)
            mostrar_top(pantalla, lista_puntajes, fuente_opciones, COLOR_NEGRO)
       #-----------------------------------------------------------------------------------------------------------------------
        numero1_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_1"],True, COLOR_NEGRO)
        numero2_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_2"], True, COLOR_AZUL)
        numero3_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_3"], True, COLOR_ROJO)
        meta_render = fuente_titulos.render(TEXTOS_CASILLEROS["meta"], True, COLOR_VERDE)
        inicio_render = fuente_inicio.render(TEXTOS_CASILLEROS["inicio"], True, COLOR_NEGRO)
        perder_render = fuente_textos.render(TEXTOS_CASILLEROS["perder"], True, COLOR_ROJO)

        dibujar_numero_en_tablero(pantalla, CASILLEROS_CON_NUMEROS, numero1_render, numero2_render, numero3_render, CORDS_CASILLEROS_TABLERO, clave1, clave2, clave3)
        pantalla.blit(perder_render, CASILLEROS_CON_TEXTO["perder"])
        pantalla.blit(inicio_render, CASILLEROS_CON_TEXTO["inicio"])
        pantalla.blit(meta_render, CASILLEROS_CON_TEXTO["meta"])

        pygame.draw.circle(pantalla, COLOR_ROJO, ficha_rect.center, RADIO_DE_FICHA)  

    pygame.display.flip() # Actualizar pantalla
    clock.tick(60)
sonido_fondo.stop()
pygame.quit() # Cerrar Pygame al finalizar el bucle