import pygame

# DIBUJA BOTONES CON UN TEXTO DENTRO
def dibujar_boton(screen, rect_boton, color_boton, texto_boton, color_texto, fuente_texto):
    """
    Dibuja Botones con su respectivo nombre.
    Parametro 1: (Surface)
    Parametro 2: Rect
    Parametro 3: Tuple (COLOR) para el boton
    Parametro 4: Texto str
    Parametro 5: Tuple (COLOR) para el texto
    Parametro 6: Fuente del texto para renderizar
    """
    pygame.draw.rect(screen, color_boton, rect_boton)                                  # dibuja un rectangulo 
    texto_boton_renderizado = fuente_texto.render(texto_boton, True, color_texto)      # renderiza el texto (convierte texto a imagen)
    texto_rect = texto_boton_renderizado.get_rect(center = rect_boton.center)          # Crea un "rectangulo" del tamaño del texto, lo centra en el primer rectangulo creado
    screen.blit(texto_boton_renderizado, texto_rect)                                   # Funde el texto junto el rectangulo a la pantalla


# OBTIENE LA RESPUESTA CORRECTA EN TRUE O FALSE
def obtener_respuesta_correcta(lista:list, e_elemento:int, respuesta:str)->bool:
    """
    Verifica si la respuesta es correcta y devuelve un valor booleano. True si es correcta, False si no.
    Parametro 1: lista
    Parametro 2: indice del elemento a verificar (int).
    Parametro 3: respuesta del usuario (str).
    Retorna True o False (correcto, incorrecto).
    """
    return respuesta == lista[e_elemento]["respuesta_correcta"]

# MUEVE LA POSICION DE LA FICHA
def mover_jugador(tablero:list, posicion:int, respuesta:bool)->int:
    """
    Incrementa la posicion del jugador a 1 si acerto la respuesta, ademas, si cae en un casillero con numero incrementa la posicion de este una vez mas dependiendo el numero en que haya caido.
    Si la respuesta es incorrecta, decrementa la posicion del jugador a 1, ademas, si cae en un casillero con numero decrementa la posicion de este una vez mas dependiendo el numero en que haya caido.
    Parametro 1: tablero (lista).
    Parametro 2: posicion del jugador (int).
    Parametro 3: respuesta del jugador (bool).
    Retorna un entero (la nueva posicion del jugador).
    """
    movimiento = 1
    if respuesta == False:
        movimiento = -1
    
    posicion += movimiento
        
    while tablero[posicion] != 0:
        mover = (tablero[posicion] * movimiento)
        posicion += mover  # Si cae en un casillero con número, se mueve según el valor de ese casillero
        if mover < 0:
            print(f"\n¡Has caído en una serpiente! Retrocedes {abs(mover)} casilleros.")
        else:
            print(f"\n¡Has subido por una escalera! Avanzas {mover} casilleros.")
    return posicion

# VERIFICA SI EL JUEGO TERMINO DE ALGUNA MANERA
def fin_del_juego(posicion:int, elemento:int, lista_preguntas:list)-> bool:
    """
    Verifica si hay algun motivo para terminar el juego. Si lo encuentra pone una bandera en False, sino sera True.
    Parametros 1: Entero (posicion del jugador).
    Parametros 2: Entero (indice del elemento actual en la lista de preguntas).
    Parametros 3: Lista de preguntas.
    Retorna un booleano.
    """
    ganador = 30
    perdedor = 0
    finjuego = False
    if posicion == ganador:
        finjuego = True #"¡Felicidades! Has llegado a la meta y ganado el juego."
        
    elif posicion == perdedor:
        finjuego = True #"¡Lo siento! Has perdido, se acabaron los casilleros :("
        
    elif elemento > len(lista_preguntas) - 1:
        finjuego = True #"¡Perdiste! Has respondido todas las preguntas y no has llegado a la meta."
        
    return finjuego


# GUARDAR DATOS EN LISTA CSV
def guardar_datos(nombre:str, posicion:int):
    """
    Crea un archivo cvs si no esta creado. En caso de que ya exista, agrega el nombre del jugador y su posicion final al archivo.
    Parametro 1: nombre (str).
    Parametro 2: posicion (int).
    Ningun retorno.
    """
    try:
        with open("score.csv", "r+") as score:
            contenido = score.readline()  # Lee la primera línea para no sobrescribir el archivo si ya existe
            if contenido == None:
                score.write("JUGADOR, POSICION\n")               
            score.write(f"{nombre},{posicion}\n")  # Guarda el nombre del jugador y su posición final en el archivo score.csv
    except FileNotFoundError:
        with open("score.csv", "w") as score:
            score.write("JUGADOR, POSICION\n")
            score.write(f"{nombre},{posicion}\n")

# GUARDAR EN LISTA LOS DATOS DEL ARCHIVO CSV (NOMBRE, POSICION)
def listar_scores()->list:
    """
    Muestra los datos de los usuarios. Su nombre y su posicion.
    Parametros ninguno.
    Ningun retorno.
    """
    lista_scores = []
    try:
        with open("score.csv", "r") as score:
            next(score)
            for linea in score:
                nombre, posicion = linea.strip().split(",")
                lista_scores.append((nombre, int(posicion)))
    except FileNotFoundError:
        pass
    
    return lista_scores

# ORDENA DE MAYOR A MENOR
def ordenar_lista_puntajes(lista:list):
    """
    Ordena la lista de mayor a menor. Utilizando el metodo de burbujeo
    Parametro 1: Lista
    No Retorna nada.
    """
    puntos = 1
    lista_aux = []
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][puntos] < lista[j][puntos]:
                lista_aux = lista[i]
                lista[i] = lista[j]
                lista[j] = lista_aux


# DIBUJAR TOP SCORE AL FINALIZAR EL JUEGO
def mostrar_top(screen, lista:list, fuente, color:tuple):
    """
    Renderiza y dibuja una lista en la pantalla (Top score (1-5)).
    Parametro 1: Surface
    Parametro 2: Lista a mostrar
    Parametro 3: Fuente
    Parametro 3: Tuple (Color) para el texto
    Sir Retorno
    """
    puntos = 1
    nombres = 0
    espacio = 40
    x = 697
    y = 219

    for i in range(len(lista)):
        if i == 5:
            break
        texto = f"{str(lista[i][nombres])} ---- {str(lista[i][puntos])}"
        texto_render = fuente.render(texto, True, color)
        screen.blit(texto_render, (x, y + i * espacio))

# DIBUJAR LISTA DE REGLAS EN LA PANTALLA INFO
def listar_reglas (screen, lista:list, fuente, color):
    """
    Renderiza y dibuja una lista de reglas.
    Parametro 1: Surface
    Parametro 2: Lista (Reglas)
    Parametro 3: Fuente
    Parametro 4: Color
    Sin retorno.
    """
    for i in range (len(lista)):
        espacio = 30
        x = 50
        y = 120
        texto_reglas_render = fuente.render(lista[i], True, color)       
        screen.blit(texto_reglas_render, (x, y + i * espacio))


# DIBUJAR RANKING SCORE (1-10) EN LA PANTALLA SCORE
def mostrar_lista_score(screen, lista:list, fuente, color:tuple):
    """
    Renderiza y dibuja una lista en la pantalla (Top score (1-10)).
    Parametro 1: Surface
    Parametro 2: Lista a mostrar
    Parametro 3: Fuente
    Parametro 3: Tuple (Color) para el texto
    Sir Retorno
    """
    puntos = 1
    nombres = 0
    espacio = 40
    x = 335
    y = 140

    for i in range(len(lista)):
        if i == 10:
            break
        texto = f"{str(lista[i][nombres])} ---- {str(lista[i][puntos])}"
        texto_render = fuente.render(texto, True, color)
        screen.blit(texto_render, (x, y + i * espacio))

def mensaje_resultado (movimiento:int)->str:
    """
    Guarda el resultado de movimientos que hizo el jugador para mostrarlo
    Parametro 1: INT
    Retorna 2 variables que contienen STR
    """
    informe1 = ""
    if movimiento == 1:
        informe2 = f"¡Avanzas {movimiento} casillero!"
    elif movimiento == -1:
        informe2 = f"¡Retrocedes {abs(movimiento)} casillero!"
    elif movimiento > 1:
        informe1 = "¡ESCALERA!"
        informe2 = f"¡Avanzas {movimiento} casilleros!"
    elif movimiento < -1:
        informe1 = "¡SERPIENTE!"
        informe2 = f"¡Retrocedes {abs(movimiento)} casilleros!"
    else:
        informe2 = ""
    return informe1, informe2

def dibujar_numero_en_tablero(screen, diccionario, texto_render1, texto_render2, texto_render3, cordenadas, key1,key2,key3):
    """
    Dibuja en la pantalla 3 str (numeros) en diferentes cordenadas del tablero
    Parametro 1: Surface
    Parametro 2: Diccionario (contiene los numeros de casilleros donde estaran los numeros que se quieren dibujar)
    Parametro 3: Texto 1 str
    Parametro 4: Texto 2 str
    Parametro 5: Texto 3 str
    Parametro 6: Lista que contiene las cordenadas de los casilleros
    Parametro 7: str (Key para acceder al value del diccionario)
    Parametro 8: str (Key para acceder al value del diccionario)
    Parametro 9: str (Key para acceder al value del diccionario)
    Sin Retorno.
    """
    for casillero1 in diccionario[key1]:
        screen.blit(texto_render1, cordenadas[casillero1])
    for casillero2 in diccionario[key2]:
        screen.blit(texto_render2, cordenadas[casillero2])
    for casillero3 in diccionario[key3]:
        screen.blit(texto_render3, cordenadas[casillero3])

def texto_fin(texto:str, posicion:int)->str:
    """
    Verifica si gano o perdio para guardar en una variable un mensaje.
    Parametro 1: texto str
    Parametro 2: Posicion (int)
    Retorna el texto
    """
    texto = texto
    ganador = 30
    perdedor = 0

    if posicion == perdedor:
        texto = "¡Lo siento! ¡Has perdido! :("
    elif posicion == ganador:
        texto = "¡Felicidades! ¡Has llegado a la META!"
    return texto