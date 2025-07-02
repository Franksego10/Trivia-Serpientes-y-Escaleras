
# ---------------------------------------
# CONFIGURACIÓN Y CONSTANTES                
# ---------------------------------------
COLOR_VERDE = (0,255,0)
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (238, 0, 0)
COLOR_AMARILLO = (255, 255, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255,255,255)

# TAMAÑO DE LA PANTALLA (ANCHO, ALTO)
TAMANIO_PANTALLA = (1000,700)
# IMAGEN DE FONDO DE PANTALLA
CORD_IMAGEN_FONDO = (0,0)

# TIEMPO
UNSEGUNDO = 1000

# FUENTES
FUENTE = "./JuegoSerpientesEscaleras/PressStart2P-Regular.ttf"

# TABLERO
TABLERO = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
CORDS_CASILLEROS_TABLERO = [[100, 582], [220, 582], [310, 582], [400, 582], [490, 582], [580, 582],
                            [580, 522], [580, 461], [490, 461], [400, 461], [310, 461], [220, 461], 
                            [130, 461], [130, 400], [130, 338], [130, 270], [130, 202], [130, 140], 
                            [220, 140], [310, 140], [310, 202], [310, 262], [310, 322], [310, 383], 
                            [400, 383], [490, 383], [580, 383], [580, 322], [580, 262], [490, 253], [490, 152]]
TAMANIO_TABLERO_IMG = (600, 520)
CORDENADA_TABLERO_IMG = (50,125)
CASILLEROS_CON_TEXTO = {"inicio": (75,277),
                         "meta": (453,157),
                         "perder": (72,594)}

CASILLEROS_CON_NUMEROS = {"casillero_1": [1, 11, 16, 20, 27],
                           "casillero_2": [14, 23],
                           "casillero_3": [5]}

TEXTOS_CASILLEROS_NUM = {"numero_1": "1",
                      "numero_2": "2",
                      "numero_3": "3"}
                      
TEXTOS_CASILLEROS = {"meta": "META",
                      "inicio": "INICIO",
                      "perder": "PELIGRO"}

# FICHA JUGADOR POSICION INICIAL (15) = (130, 270 )
RADIO_DE_FICHA = 20
POSICION_INICIAL = 15
TAMANIO_FICHA = {"ancho": 40, "alto": 40}

# BOTONES

CORD_BOTON = {"boton_jugar": {"X":438, "Y": 506},
              "boton_salir": {"X":438, "Y": 587},
              "boton_score": {"X":43, "Y": 36},
              "boton_info": {"X":855, "Y": 36},
              "boton_atras": {"X":855, "Y": 36},
              "boton_atras_game": {"X":438, "Y": 464},
              "boton_start": {"X":438, "Y":400}}

TAMANIO_BOTON = {"ancho": 110, "alto": 50}

TAMANIO_BOT_OPCIONES = {"ancho": 300, "alto": 50}
CORD_BOT_OPCIONES = {"a": {"X": 671, "Y": 290},
                     "b": {"X": 671, "Y": 360},
                     "c": {"X": 671, "Y": 430}}

# CORDENADAS DE TEXTOS SUELTOS
CORD_TITULO_INFO = (245, 40)
CORD_TITULO_JUEGO = (70,40)
CORD_PEDIR_USUARIO = (285,200)
CORD_TITULO_SCORE = (400,40)
CORD_TEXTO_FINAL = (70, 30)
CORD_TEXTO_POSICION_FINAL = (80, 70)
CORD_PREGUNTAS = (15, 50)