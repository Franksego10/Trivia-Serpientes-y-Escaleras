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
fuente_opciones = pygame.font.Font(FUENTE, 14)  # FUENTE para las opciones de Preguntas
fuente_inicio = pygame.font.Font(FUENTE, 25)    # FUENTE para el inicio

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
sonido_fondo = pygame.mixer.Sound("./JuegoSerpientesEscaleras/A Funny Soul.mp3")
sonido_correcto = pygame.mixer.Sound("./JuegoSerpientesEscaleras/Correcto.mp3")
sonido_correcto.set_volume(VOLUMEN_CORRECTO_INCORRECTO)
sonido_incorrecto = pygame.mixer.Sound("./JuegoSerpientesEscaleras/incorrecto.mp3")
sonido_incorrecto.set_volume(VOLUMEN_CORRECTO_INCORRECTO)
sonido_fondo.set_volume(VOLUMEN_MUSICA)
sonido_fondo.play(-1)
# BUCLE PRINCIPAL
while flag_correr:
    lista_eventos_inicio = pygame.event.get()
    for evento in lista_eventos_inicio:
        if evento.type == pygame.QUIT:                          # ESTE EVENTO FINALIZA EL PROGRAMA SI EL USUARIO TOCA X
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
#-----------------------------------------------------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------------------------------------------------------            
            elif pantalla_info:                                  # EVENTOS DE MOUSE EN PANTALLA INFO
                if rect_atras.collidepoint(evento.pos):
                    pantalla_inicio = True
                    pantalla_info = False
#------------------------------------------------------------------------------------------------------------------------------------------------            
            elif pantalla_score:
                if rect_atras.collidepoint(evento.pos):          # EVENTOS DE MOUSE EN PANTALLA SCORE
                    pantalla_inicio = True
                    pantalla_score = False
#------------------------------------------------------------------------------------------------------------------------------------------------
            elif pantalla_juego:                                 # EVENTOS DE MOUSE EN PANTALLA JUGAR
                if rect_atras_game.collidepoint(evento.pos):
                    pantalla_inicio = True
                    pantalla_juego = False
                    jugador = ""
                elif rect_start.collidepoint(evento.pos):
                    if jugador.strip() != "":
                        pantalla_juego = False
                        empezar_juego = True
#------------------------------------------------------------------------------------------------------------------------------------------------            
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
                    if rect_atras.collidepoint(evento.pos):             # Boton de salir al finalizar el juego
                        flag_correr = False
#------------------------------------------------------------------------------------------------------------------------------------------------        
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
#------------------------------------------------------------------------------------------------------------------------------------------------
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
        textos_sueltos(pantalla, fuente_titulos, COLOR_BLANCO, CORD_TITULO_INFO, titulo_info)                       # renderiza y funde el titulo
        listar_reglas(pantalla, LISTA_REGLAS, fuente_textos, COLOR_BLANCO)                   # renderiza las reglas y las dibuja

# ---------------------------------------
#            PANTALLA SCORE               
# ---------------------------------------

    elif pantalla_score:
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)
        dibujar_boton(pantalla,rect_atras, COLOR_AMARILLO, texto_atras, COLOR_NEGRO, botones_fuente)
        textos_sueltos(pantalla, fuente_titulos, COLOR_BLANCO, CORD_TITULO_SCORE, titulo_score)        # renderiza y dibuja el titulo "SCORE"                             
        mostrar_top(pantalla, lista_puntajes, botones_fuente, COLOR_AZUL, LIMITE_SCORE_PANTALLA, CORD_SCORE_PANTALLA["x"], CORD_SCORE_PANTALLA["y"])           # renderiza la lista de scores y las dibuja

# ---------------------------------------
#    PANTALLA Juego (Ingresar usuario)               
# ---------------------------------------

    elif pantalla_juego:
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)      # FUNDE LA IMAGEN DE FONDO      
        textos_sueltos(pantalla, fuente_titulos, COLOR_BLANCO, CORD_TITULO_JUEGO, titulo_juego)         #renderiza y dibuja el titulo de la pantalla jugar
        textos_sueltos(pantalla, fuente_textos, COLOR_NEGRO, CORD_PEDIR_USUARIO, texto_pedir_usuario)       #renderizza y dibuja el texto para pedir usuario al jugador

        pygame.draw.rect(pantalla, COLOR_BLANCO, jugador_rect, 2)                           # dibuja un rectangulo sin relleno donde pareceran las letras que presione el usuario
        texto_centrado(pantalla, fuente_textos, COLOR_NEGRO, jugador_rect, jugador)         # dibuja centrado en el rectangulo el nombre del jugador que va escribiendo en el teclado

        dibujar_boton(pantalla, rect_atras_game, COLOR_AMARILLO, texto_atras, COLOR_NEGRO, botones_fuente)      # dibuja boton de atras
        dibujar_boton(pantalla, rect_start, COLOR_AMARILLO, texto_start, COLOR_NEGRO, botones_fuente)           # dibuja boton de comenzar

    # ---------------------------------------
    #   PANTALLA JUEGO EMPEZADO (Preguntas)              
    # ---------------------------------------

    elif empezar_juego:                                                             # PANTALLA PREGUNTAS
        pantalla.blit(imagen_fondo, CORD_IMAGEN_FONDO)
        pantalla.blit(imagen_tablero, CORDENADA_TABLERO_IMG)                       # Funde la imagen del tablero

        # Todo lo que muestra el juego mientras no haya terminado
        if fin_juego == False:
            dibujar_boton(pantalla, rect_terminar, COLOR_AZUL, texto_terminar, COLOR_BLANCO, botones_fuente)    # Dibuja boton de Terminar Juego, en caso de que no quiera seguir jugando

            if pregunta == "":                                                               # Condicional para cargar preguntas y respuestas
                pregunta = preguntas_copia[indice_pregunta]["pregunta"]
                respuesta_a = preguntas_copia[indice_pregunta]["respuesta_a"]
                respuesta_b = preguntas_copia[indice_pregunta]["respuesta_b"]
                respuesta_c = preguntas_copia[indice_pregunta]["respuesta_c"]
                color_opciones = {"a": COLOR_AMARILLO, "b": COLOR_AMARILLO, "c": COLOR_AMARILLO}
                segundos = "15"
                flag_tiempo = False                            
                opcion_correcta = preguntas_copia[indice_pregunta]["respuesta_correcta"]
            
            # Si se acabo el tiempo para responder o clickea en unas de las opciones. Te muestra el resultado
            if mostrar_resultado:                                                           
                if respuesta != None:
                    resultado_respuesta = obtener_respuesta_correcta(preguntas_copia, indice_pregunta, respuesta)
                    sonido_respuesta(resultado_respuesta, sonido_correcto, sonido_incorrecto)
                    
                    posicion_jugador, informe_jugador1, informe_jugador2 = procesar_movimiento(TABLERO, resultado_respuesta, CORDS_CASILLEROS_TABLERO, posicion_jugador, ficha_rect, mover_jugador, actualizar_rect_ficha, mensaje_resultado)

                elif segundos == "¡TIEMPO!":
                    sonido_incorrecto.play()
                    resultado_respuesta = False
                    posicion_jugador, informe_jugador1, informe_jugador2 = procesar_movimiento(TABLERO, resultado_respuesta, CORDS_CASILLEROS_TABLERO, posicion_jugador, ficha_rect, mover_jugador, actualizar_rect_ficha, mensaje_resultado)

                    segundos = "15"

                colorear_correcta(opcion_correcta, color_opciones, COLOR_VERDE)               
                colorear_incorrecta(respuesta, color_opciones, COLOR_ROJO, opcion_correcta)
                texto_centrado(pantalla, botones_fuente, COLOR_NEGRO, rect_informe1, informe_jugador1)
                texto_centrado(pantalla, fuente_opciones, COLOR_NEGRO, rect_informe2, informe_jugador2)

                respuesta = None
            textos_sueltos(pantalla, fuente_preguntas, COLOR_NEGRO, CORD_PREGUNTAS, pregunta)                       # Renderiza y dibuja la pregunta

            dibujar_boton(pantalla, rect_opcion_a, color_opciones["a"], respuesta_a, COLOR_NEGRO, fuente_opciones)      # renderiza y dibuja las opciones
            dibujar_boton(pantalla, rect_opcion_b, color_opciones["b"], respuesta_b, COLOR_NEGRO, fuente_opciones)  
            dibujar_boton(pantalla, rect_opcion_c, color_opciones["c"], respuesta_c, COLOR_NEGRO, fuente_opciones)

            if flag_tiempo == False:
                texto_centrado(pantalla, fuente_titulos, COLOR_BLANCO, tiempo_rect, segundos)                       # renderiza y dibuja el tiempo descontandose
            
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
            
            textos_sueltos(pantalla, botones_fuente, COLOR_BLANCO, CORD_TEXTO_FINAL, texto_final)                   # renderiza el texto final una vez terminado el juego
            dibujar_boton(pantalla, rect_atras, COLOR_AMARILLO, texto_salir, COLOR_NEGRO, botones_fuente)           # dibuja el boton salir
            textos_sueltos(pantalla, fuente_textos, COLOR_AZUL, CORD_TEXTO_POSICION_FINAL, posicion_final)          # renderiza y dibuja la posicion final

            titulo_ranking_render = fuente_titulos.render(titulo_ranking, True, COLOR_NEGRO)
            rect_titulo = titulo_ranking_render.get_rect()
            rect_titulo.centerx = rect_ranking.centerx                                                              # renderiza y dibuja el titulo "SCORE"
            rect_titulo.top = rect_ranking.top + 10
            pantalla.blit(titulo_ranking_render, rect_titulo)
            mostrar_top(pantalla, lista_puntajes, fuente_opciones, COLOR_NEGRO, LIMITE_SCORE_FINAL, CORD_SCORE_FINAL["x"], CORD_SCORE_FINAL["y"])                                     # renderiza y dibuja los scores
       #-----------------------------------------------------------------------------------------------------------------------
        numero1_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_1"],True, COLOR_NEGRO)
        numero2_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_2"], True, COLOR_AZUL)
        numero3_render = fuente_titulos.render(TEXTOS_CASILLEROS_NUM["numero_3"], True, COLOR_ROJO)

        dibujar_numero_en_tablero(pantalla, CASILLEROS_CON_NUMEROS, numero1_render, numero2_render, numero3_render, CORDS_CASILLEROS_TABLERO, clave1, clave2, clave3)
        textos_sueltos(pantalla, fuente_textos, COLOR_ROJO, CASILLEROS_CON_TEXTO["perder"], TEXTOS_CASILLEROS["perder"])
        textos_sueltos(pantalla, fuente_inicio, COLOR_NEGRO, CASILLEROS_CON_TEXTO["inicio"], TEXTOS_CASILLEROS["inicio"])
        textos_sueltos(pantalla, fuente_titulos, COLOR_VERDE, CASILLEROS_CON_TEXTO["meta"], TEXTOS_CASILLEROS["meta"])
        pygame.draw.circle(pantalla, COLOR_ROJO, ficha_rect.center, RADIO_DE_FICHA)                     # FICHA

    pygame.display.flip() # Actualizar pantalla
    clock.tick(FPS)
sonido_fondo.stop()
pygame.quit() # Cerrar Pygame al finalizar el bucle