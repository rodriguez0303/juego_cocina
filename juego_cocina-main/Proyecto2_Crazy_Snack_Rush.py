#Importación de librerias 
from tkinter import *
import tkinter as tk
import random # Permite escoger recetas e ingredientes de forma aleatoria
import os #Permite acceder a la ruta donde se encuentran las imagenes 
from PIL import Image, ImageTk  #Pillow permite para cargar imágenes JPG
from tkinter import messagebox # permite generar mensajes emergentes 

#Clase que contiene la pantalla principal 
class Pantalla_Principal:
        def __init__(self):

                #Se Obtiene la carpeta donde está el archivo .py (evita problema con la carga de imagenes)
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se crea la ventana principal
                self.ventana = Tk()

                # Se coloca el título de la ventana
                self.ventana.title("Crazy Snack Rush")

                # Se define el tamaño de la ventana (ejex, ejey, ancho, alto)
                self.ventana.geometry("900x690+350+70")

                # Se evita que el usuario cambie el tamaño
                self.ventana.resizable(False, False)

                #A la pantalla principal se le asigna un canvas para que pueda colocarse botones e imagen 
                self.canvas = Canvas(self.ventana, width=1000, height=700, bg="gray")
                self.canvas.pack(fill=tk.BOTH, expand=True)

        #######
                # Se define la ruta de la imagen de fondo
                ruta_imagen_fondo = os.path.join(self.BASE_DIR,'Imagenes','Fondo1.png')

                # Se abre la imagen
                imagen_fondo = Image.open(ruta_imagen_fondo)

                # Se ajusta el tamaño de la imagen
                imagen_fondo = imagen_fondo.resize((1000, 700))

                # Se convierte la imagen para tkinter
                self.imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

        #######
                # Se coloca la imagen de fondo en el canvas
                self.canvas.create_image(
                                                0,
                                                0,
                                                image=self.imagen_fondo_tk,
                                                anchor=NW
                                                )
                
#######
                # Se define la ruta de la imagen del botón jugar 
                ruta_boton_jugar = os.path.join(self.BASE_DIR,'Imagenes','Boton_Jugar.png')

                # Se abre la ruta donde se encuentra la imagen del botón jugar
                imagen_boton_jugar = Image.open(ruta_boton_jugar)

                # Se define el tamaño de la imagen (botón) play 
                imagen_boton_jugar = imagen_boton_jugar.resize((250, 100))

                # Se convierte la imagen al formato que tkinter pueda usar 
                self.imagen_boton_jugar_tk = ImageTk.PhotoImage(imagen_boton_jugar)

                # Se define la posición de la imagen del botón jugar dentro del canvas 
                self.boton_jugar = self.canvas.create_image(

                                                                
                                                                500,# Posición del botón en el eje X
                                                                480,# Posición del botón en el eje Y
                                                                image=self.imagen_boton_jugar_tk # Imagen que tendrá el botón
                                                        )
  
#######
                # Evento que permite hacer click sobre la imagen del botón jugar 
                self.canvas.tag_bind(
                                        self.boton_jugar,# Imagen que funcionará como botón
                                        "<Button-1>", #Permite acceder al juego dando clic izquierdo 
                                        self.iniciar_juego # Se llama a la función que inicializa el juego 


                                )
                
#######
                # Se define la ruta de la imagen del botón Scores
                ruta_boton_scores = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "Boton_Scores.png"
                                                )

                # Se abre la carpeta donde se encuentra la imagen del botón Scores
                imagen_boton_scores = Image.open(ruta_boton_scores)

                # Se define el tamaño del  botón Scores
                imagen_boton_scores = imagen_boton_scores.resize((250, 100))

                # Se convierte la imagen en un formato que Tkinter pueda usar 
                self.imagen_boton_scores_tk = ImageTk.PhotoImage(imagen_boton_scores)

                # Se coloca el botón Scores en pantalla principal 
                self.boton_scores = self.canvas.create_image(
                                                                500,
                                                                540,
                                                                image=self.imagen_boton_scores_tk
                                                        )

                # Se abre la pantalla de Scores al dar clic izquierdo sobre este 
                self.canvas.tag_bind(
                                        self.boton_scores,
                                        "<Button-1>",
                                        self.mostrar_scores
                                )
#######
                # Se define la ruta de la imagen del botón About
                ruta_boton_about = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes", #Nombre de la carpeta que contiene la imagen de fondo del botón about
                                                        "Boton_About.png" #Nombre de la imagen del botón about 
                                                )

                # Se abre la ruta de la imagen del botón About
                imagen_boton_about = Image.open(ruta_boton_about)

                # Se define el tamaño del botón About
                imagen_boton_about = imagen_boton_about.resize((250, 100))

                # Se convierte la imagen en un formato que Tkinter pueda usar
                self.imagen_boton_about_tk = ImageTk.PhotoImage(imagen_boton_about)

                # Se coloca el botón About en pantalla principal
                self.boton_about = self.canvas.create_image(
                                                                500,
                                                                610,
                                                                image=self.imagen_boton_about_tk
                                                        )

                # Se abre la pantalla About al dar clic izquierdo sobre este
                self.canvas.tag_bind(
                                        self.boton_about,
                                        "<Button-1>",
                                        self.about
                                )
                
#######################################################################################
  # Mantiene la ventana abierta
                self.ventana.mainloop()

#######################################################################################
        # Función que destruye la pantalla principal para luego mostrar la pantalla de juegos 
        def iniciar_juego(self, event):

                # Se oculta la pantalla principal
                self.ventana.withdraw()

                # Se abre la pantalla donde el jugador escribe su nombre
                self.pantalla_nombre = Pantalla_Nombre_Jugador(self.ventana)

#######################################################################################

        # Función que muestra los puntajes guardados en la pantalla principal 
        def mostrar_scores(self, event):

                # Ruta de la imagen de fondo
                ruta_fondo_scores = os.path.join(
                                                self.BASE_DIR, #Ruta donde se encuentra la imagen 
                                                "Imagenes", #Carpeta donde esta la imagen de fondo 
                                                "fondo_scores.png" #Nombre de la imagen que se colocará de fondo 
                                        )

                # Se abre la ruta donde se encuentra la imagen de fondo scores
                imagen_fondo_scores = Image.open(ruta_fondo_scores)

                # Se ajusta el tamaño de la imagen de fondo scores
                imagen_fondo_scores = imagen_fondo_scores.resize((800, 600))

                # Se convierte la imagen en un formato que Tkinter pueda usar 
                self.imagen_fondo_scores_tk = ImageTk.PhotoImage(imagen_fondo_scores)

                # Se crea una ventana secundaria para mostrar los puntajes
                ventana_scores = Toplevel(self.ventana)

                # Se coloca el título de la ventana scores
                ventana_scores.title("Scores")

                # Se define el tamaño de la ventana
                ventana_scores.geometry("800x600+450+100")

                # Se evita cambiar el tamaño
                ventana_scores.resizable(False, False)

                # Se crea el texto inicial
                texto_scores = "SCORES\n\n"

                # Se verifica si existe el archivo de puntajes
                if os.path.exists("puntajes.txt"):

                        # Se abre el archivo en modo lectura
                        archivo = open("puntajes.txt", "r")

                        # Se leen todas las líneas
                        lineas = archivo.readlines()

                        # Se cierra el archivo
                        archivo.close()

                        # Lista donde se guardarán los jugadores y puntajes
                        lista_puntajes = []

                        # Se recorre cada línea del archivo
                        for linea in lineas:

                                # Se elimina el salto de línea
                                linea = linea.strip()

                                # Se verifica que la línea no esté vacía
                                if linea != "":

                                        # Se separa nombre y puntaje
                                        datos = linea.split(",")

                                        # Se verifica que existan dos datos (para comparar quien tiene el mayor puntaje y va de primero)
                                        if len(datos) == 2:

                                                # Guarda nombre y puntaje
                                                nombre = datos[0]

                                                puntaje = int(datos[1])

                                                # Se agrega a la lista
                                                lista_puntajes.append([nombre, puntaje])

                        # Ordenamiento  de mayor a menor
                        for i in range(len(lista_puntajes) - 1):

                                for j in range(len(lista_puntajes) - 1 - i):

                                        if lista_puntajes[j][1] < lista_puntajes[j + 1][1]:

                                                auxiliar = lista_puntajes[j]

                                                lista_puntajes[j] = lista_puntajes[j + 1]

                                                lista_puntajes[j + 1] = auxiliar

                        # Se agregan los puntajes ya ordenados al texto
                        for jugador in lista_puntajes:

                                texto_scores += (
                                        jugador[0]
                                        + " - "
                                        + str(jugador[1])
                                        + " puntos\n"
                                )

                else:

                        # Si no hay archivo, se muestra este mensaje
                        texto_scores += "No hay puntajes guardados"

                # Canvas de la ventana
                canvas_scores = Canvas(
                                                        ventana_scores,
                                                        width=800,
                                                        height=600
                                                )
                # Se coloca el canvas en la ventana 
                canvas_scores.pack()

                # Imagen de fondo que tendrá el canvas 
                canvas_scores.create_image(
                                                        0,
                                                        0,
                                                        image=self.imagen_fondo_scores_tk,
                                                        anchor=NW
                                                )
                # Texto que contiene los puntajes de los jugadores 
                canvas_scores.create_text(
                                                        20, #Posición del puntaje en el eje x 
                                                        50, #Posición del puntaje en el eje y 
                                                        text=texto_scores,
                                                        fill="white",
                                                        font=("Arial", 18, "bold"),
                                                        anchor=NW
                                                )
#######################################################################################
        # Función que muestra la información del proyecto
        def about(self, event):

                # Se crea una ventana secundaria
                ventana_about = Toplevel(self.ventana)

                # Se coloca el título
                ventana_about.title("About")

                # Se define el tamaño de la ventana 
                ventana_about.geometry("800x600+450+100")

                # Se evita cambiar el tamaño de la ventana about 
                ventana_about.resizable(False, False)

#######
        # Ruta de la imagen de fondo de la ventana about 
                ruta_fondo_about = os.path.join(
                        self.BASE_DIR, # Se abre la ruta donde se encuentra la imagen de fonro 
                        "Imagenes", #Carpeta donde se encuentra la imagen de fondo 
                        "fondo_about.png" #Nombre de la imagen del fondo de la pantalla about 
                )

                # Se abre la ruta donde se encuentra la imagen de fondo 
                imagen_fondo_about = Image.open(ruta_fondo_about)

                # Se ajusta el tamaño
                imagen_fondo_about = imagen_fondo_about.resize((800, 600))

                # Se convierte la imagen en un formato que pueda usar Tkinter
                self.imagen_fondo_about_tk = ImageTk.PhotoImage(imagen_fondo_about)

                # Se crea el canvas
                canvas_about = Canvas(
                                        ventana_about,
                                        width=800,
                                        height=600
                                )

                # Se coloca el canvas
                canvas_about.pack()

                # Se coloca la imagen de fondo
                canvas_about.create_image(
                                                0,
                                                0,
                                                image=self.imagen_fondo_about_tk,
                                                anchor=NW
                                        )
#######

        # Texto que aparecerá en la pantalla about 
                texto_about = """
        Tecnológico de Costa Rica

        Introducción a la Programación

        Proyecto Programado 2

        Crazy Snack Rush

        Estudiantes:

        Luis Rodríguez M
        Samantha Carmona R 

        Profesor:
        Santiago Ramirez 

        I Semestre 2026

        Visual Studio Code - version 1.125.1

        Version 1.0

        """

                # Se muestra el texto
                canvas_about.create_text(
                                                400, #Posición del texto en el eje x 
                                                324, #Posición del texto en el eje y
                                                text=texto_about,
                                                fill="black", #Color del texto 
                                                font=("Arial", 10, "bold"), # Tipo, tamaño y forma de la letra
                                                justify="center" # Alineación del texto 
                                        )
#######################################################################################

# Clase que permite ingresar el nombre del jugador antes de iniciar el juego
class Pantalla_Nombre_Jugador:

        def __init__(self, ventana_principal):

                # Guarda la ventana principal para poder abrir el mapa después
                self.ventana_principal = ventana_principal

                # Se crea una ventana secundaria para escribir el nombre
                self.ventana_nombre = Toplevel(ventana_principal)

                # Se coloca el título de la ventana nombre del jugador
                self.ventana_nombre.title("Nombre del jugador")

                # Define el tamaño y la posición de la ventana
                self.ventana_nombre.geometry("900x690+350+70")

                # Se evita que el usuario cambie el tamaño de la ventana
                self.ventana_nombre.resizable(False, False)

        #######

                # Se crea un canvas para colocar una imagen de fondo a la pantalla de nombre de usuario
                self.canvas = Canvas(
                                        self.ventana_nombre,
                                        width=900,
                                        height=690
                                )

                # Se coloca el canvas en la ventana
                self.canvas.pack(fill=BOTH, expand=True)

                # Se obtiene la carpeta donde está el archivo .py
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se define la ruta de la imagen de fondo para la pantalla del nombre del jugador
                ruta_fondo = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes", # Carpeta donde se guarda la imagen
                                                "Nombre_jugador.png" # Nombre de la imagen que se colocará de fondo
                                        )

                # Se abre la imagen
                imagen_fondo = Image.open(ruta_fondo)

                # Se ajusta la imagen al tamaño de la ventana
                imagen_fondo = imagen_fondo.resize((900, 690))

                # Se convierte la imagen a un formato que pueda usar tkinter
                self.imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

                # Se coloca la imagen en el canvas
                self.canvas.create_image(
                                                0,
                                                0,
                                                image=self.imagen_fondo_tk,
                                                anchor=NW
                                        )

        #######

                # Crea un texto que le indica al jugador qué debe hacer
                self.label_nombre = Label(
                                                self.ventana_nombre,
                                                text="¿Cuál es tu nombre, chef?",
                                                font=("Arial", 18, "bold"),
                                                fg="white", # Color de la letra
                                                bg="#5B3A29" # Fondo café oscuro
                                                
                                        )

                # Se coloca el label sobre la imagen de fondo
                self.canvas.create_window(
                                                450,
                                                220,
                                                window=self.label_nombre
                                        )

        #######

                # Crea el textbox donde el jugador escribirá su nombre
                self.entrada_nombre = Entry(
                                                self.ventana_nombre,
                                                font=("Arial", 16),
                                                width=25
                                        )

                # Se coloca la caja de texto sobre la imagen de fondo
                self.canvas.create_window(
                                                450,
                                                280,
                                                window=self.entrada_nombre
                                        )

        #######

                # Se crea un label de advertencia inicialmente vacío, para que el usuario no pueda iniciar el juego sino digita su nombre
                self.label_advertencia = Label(
                                                        self.ventana_nombre,
                                                        text="",
                                                        font=("Arial", 12, "bold"),
                                                        fg="white", # Color de la letra
                                                        bg="#5B3A29" # Fondo café oscuro
                                                )

                # Se coloca el label de advertencia sobre la imagen de fondo
                self.canvas.create_window(
                                                450,
                                                340,
                                                window=self.label_advertencia
                                        )

        #######

                # Crea el botón para continuar al mapa de los restaurantes
                self.boton_continuar = Button(
                                                self.ventana_nombre,
                                                text="Continuar",
                                                font=("Arial", 14, "bold"),
                                                command=self.continuar_juego
                                        )

                # Se coloca el botón sobre la imagen de fondo
                self.canvas.create_window(
                                                450,
                                                400,
                                                window=self.boton_continuar
                                        )

########################################
        # Función que valida que se ingrese un nombre de jugador para abrir el mapa de los restaurantes 

        def continuar_juego(self):

                # Se obtiene el texto escrito por el jugador
                nombre_jugador = self.entrada_nombre.get()

                # Se elimina espacios en blanco al inicio y al final del nombre
                nombre_jugador = nombre_jugador.strip()

                # Se Verifica si el jugador dejó el campo vacío
                if nombre_jugador == "":

                        # Muestra un mensaje de advertencia
                        self.label_advertencia.config(
                                text="Debes escribir un nombre para continuar"
                        )

                        # Se detiene la función para que no avance al mapa
                        return

                # Limpia el mensaje de advertencia si el nombre sí fue escrito
                self.label_advertencia.config(text="")

                # Se cierra la ventana donde se escribió el nombre
                self.ventana_nombre.destroy()

                # Abre el mapa y le envía el nombre del jugador
                self.pantalla_mapa = Pantalla_mapa(
                        self.ventana_principal,
                        nombre_jugador
                )
#######################################################################################

# Clase que crea la ventana principal del juego
class Pantalla_mapa:

        def __init__(self, ventana_principal, nombre_jugador):

                 # Se guarda la ventana principal
                self.ventana_principal = ventana_principal

                # Se guarda el nombre del jugador
                self.nombre_jugador = nombre_jugador

                # Puntaje acumulado del jugador durante todos los restaurantes
                self.puntaje_jugador = 0

                # Se controla si el restaurante americano ya fue aprobado para poder iniciar el restaurante Europeo
                        # Se hace para que se acumulen los puntos del restaurante americano y luego el restaurante europeo
                self.americano_aprobado = False

                #Se Obtiene la carpeta donde está el archivo .py (evita problema con la carga de imagenes)
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se utiliza Toplevel para crear una segunda ventana
                self.ventana_juego = Toplevel(ventana_principal)

                # Título de la ventana de mapa
                self.ventana_juego.title("Mapa - Crazy Snack Rush")

                # Se define el tmaño de la Tamaño de la ventana
                self.ventana_juego.geometry("1000x700+350+70")

                # Se evita que se cambie el tamaño de la ventana del mapa  
                self.ventana_juego.resizable(False, False)

                # Canvas donde irá la pantalla de mapa del juego 
                self.canvas = Canvas(
                                        self.ventana_juego,
                                        width=1000,
                                        height=700,
                                        bg="black"
                                        )

                # Se coloca el canvas
                self.canvas.pack()

        #######
                # Ruta de la imagen de fondo del mapa 
                ruta_fondo_mapa = os.path.join(
                                                self.BASE_DIR,
                                                'Imagenes',
                                                'Fondo_mapa.png'
                                                )

                # Se abre la imagen
                imagen_fondo_mapa = Image.open(ruta_fondo_mapa)

                # Se ajusta el tamaño de la imagen del mapa 
                imagen_fondo_mapa= imagen_fondo_mapa.resize((1000, 700))

                # Conversión de la imagen del mapa en un formato que tkinter pueda usar 
                self.imagen_fondo_mapa_tk = ImageTk.PhotoImage(imagen_fondo_mapa)

                # Se coloca la imagen de fondo en el canvas 
                self.canvas.create_image(
                                                0,
                                                0,
                                                image=self.imagen_fondo_mapa_tk,
                                                anchor=NW
                                                )
################        
                #Ruta de la imagen restaurante pizza que esta sobre el mapa principal 
                ruta_restaurante_americano = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "Americano.png"
                                                        )

                # Se abre la imagen del restaurante pizza
                imagen_americano = Image.open(ruta_restaurante_americano)

                # Se ajusta el tamaño de la imagen restaurante pizza
                imagen_americano = imagen_americano.resize((240,100))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_americano_tk = ImageTk.PhotoImage(imagen_americano)

#######
                #Ruta de la imagen restaurante europeo que esta sobre el mapa principal 
                ruta_restaurante_europeo = os.path.join(
                                                                self.BASE_DIR,
                                                                "Imagenes",
                                                                "Europeo.png"
                                                                )
                # Se abre la imagen del restaurante Europeo
                imagen_europeo = Image.open(ruta_restaurante_europeo)

                # Se ajusta el tamaño de la imagen restaurante europeo
                imagen_europeo = imagen_europeo.resize((200,100))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_europeo_tk = ImageTk.PhotoImage(imagen_europeo)

        #######
                #Ruta de la imagen restaurante Asiatico que esta sobre el mapa principal 
                ruta_asiatico = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "Asiatico.png"
                                                        )
                
                # Se abre la imagen del restaurante asiático
                imagen_asiatico = Image.open(ruta_asiatico)

                # Se ajusta el tamaño de la imagen restaurante asiatico
                imagen_asiatico = imagen_asiatico.resize((80,80))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_asiatico_tk = ImageTk.PhotoImage(imagen_asiatico)

        ################        
        #######
                #Se define la ubicación del icono del restaurante americano sobre el mapa 
                self.punto_americano = puntoMapa(
                                                        self.canvas,
                                                        460,
                                                        370,
                                                        self.imagen_americano_tk,
                                                        self.abrir_americano
                                                        )
                
                # Se coloca el nombre del restaurante Americano
                self.canvas.create_text(

                                                450,  # posición del título en el eje x 

                                                320,  # posición del título en el eje y

                                                text="Restaurante Americano",

                                                font=("Arial", 12, "bold"),

                                                fill="white"
                                                )
                                                
#######
                #Se define la ubicación del icono del restaurante europeo sobre el mapa 
                self.punto_europeo = puntoMapa(
                                                        self.canvas,
                                                        238,
                                                        130,
                                                        self.imagen_europeo_tk,
                                                        self.abrir_europeo)
                
                # Se coloca el nombre del restaurante Europeo
                self.canvas.create_text(

                                                230,  # posición del título en el eje x 

                                                70,  # posición del título en el eje y

                                                text="Restaurante Europeo",

                                                font=("Arial", 12, "bold"),

                                                fill="white"
                                                )
                
#######
                #Se define la ubicación del icono del restaurante Europeo sobre el mapa                                        )
                self.punto_asiatico = puntoMapa(
                                                self.canvas,
                                                720,
                                                140,
                                                self.imagen_asiatico_tk,
                                                self.abrir_asiatico
                                                )
                
                # Se coloca el nombre del restaurante Asiatico
                self.canvas.create_text(

                                                710,  # posición del título en el eje x 

                                                80,  # posición del título en el eje y

                                                text="Restaurante Asiatico",

                                                font=("Arial", 12, "bold"),

                                                fill="white"
                                                )
                
########################################
        
        # Esta función que inicializa el juego al presionar el botón Play
        def iniciar_juego(self, event):
                
                # Se oculta la pantalla principal sin destruirla
                        # Esto permite que la ventana siga existiendo en memoria
                self.ventana.withdraw()

                self.pantalla_mapa = Pantalla_mapa(self.ventana)

########################################
        # Funcion que abre el mapa de juego del restaurante Americano 
        def abrir_americano(self, event):

                 # Se oculta la ventana del mapa
                self.ventana_juego.withdraw()

                # Se abre la ventana del restaurante americano
                self.pantalla_americano = Pantalla_Restaurante_Americano(self.ventana_juego,self.nombre_jugador,self)

#######                                
        # Funcion que abre el mapa de juego del restaurante Europeo
        def abrir_europeo(self, event):

                # Se verifica si el restaurante americano ya fue aprobado
                if self.americano_aprobado == False:

                        messagebox.showinfo(
                                "Restaurante bloqueado",
                                "Primero debes completar las 3 recetas del Restaurante Americano"
                        )

                        return

                # Se oculta la ventana del mapa
                self.ventana_juego.withdraw()

                # Se abre la ventana del restaurante europeo
                self.pantalla_europeo = Pantalla_Restaurante_Europeo(self.ventana_juego,self.nombre_jugador,self.puntaje_jugador)


#######
        # Funcion que abre el mapa de juego del restaurante Asiatico
        def abrir_asiatico(self, event):

               # Se oculta la ventana del mapa
                self.ventana_juego.withdraw()

                # Se abre la ventana del restaurante asiático
                self.pantalla_asiatico = Pantalla_Restaurante_Asiatico(self.ventana_juego,self.nombre_jugador)

#######################################################################################

# Clase que permite acceder a los diferente restaurantes
class puntoMapa:

    # Método constructor
    def __init__(self, canvas, coordenada_ejex, coordenada_ejey, imagen_puntomapa, funcion_click):

        # Guarda el canvas donde se colocará la imagen
        self.canvas = canvas

        # Guarda la imagen
        self.imagen_puntomapa = imagen_puntomapa

        # Crea la imagen en el mapa
        self.icono = self.canvas.create_image(
                                                coordenada_ejex,
                                                coordenada_ejey,

                                                image=self.imagen_puntomapa
                                                )

        # Permite hacer clic izquierdo sobre la imagen para abrir el escenario del restaurante 
        self.canvas.tag_bind(
                                self.icono,

                                "<Button-1>",

                                funcion_click
                                )
        
#######################################################################################

# Clase asociada a la funcionaldiades del chef #1 dentro del restaurante
class Chef:

        def __init__(self, canvas, base_dir,nombre,chef_ejex, chef_ejey):

                #Guarda el canvas donde se dibujará el chef
                self.canvas = canvas
                
                #Obtiene la ruta donde se encuentra las imagenes del chef 
                self.BASE_DIR = base_dir
                
                #Se guarda el nombre del jugador 
                self.nombre = nombre

                #Guarda el puntaje del jugador inicialmente esta en 0
                self.puntos = 0

                # Define la posición inicial del chef en el eje X
                self.chef_ejex = chef_ejex

                # Define la posición inicial del chef en el ejeY
                self.chef_ejey = chef_ejey

                # Cantidad de pixeles que se moverá el chef cada vez que se presione la tecla de dirección 
                self.distancia = 50

########
                # Ruta de la imagen del chef#1 viendo hacia abajo
                ruta_chef_abajo = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef_abajo.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef 
                imagen_chef_abajo = Image.open(ruta_chef_abajo)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_abajo = imagen_chef_abajo.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_abajo_tk = ImageTk.PhotoImage(imagen_chef_abajo)

########
                # Ruta de la imagen del chef#1 viendo hacia arriba
                ruta_chef_arriba = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef_arriba.png"
                                                )
                
                # Se abre la ruta que contiene la imagen del chef 
                imagen_chef_arriba = Image.open(ruta_chef_arriba)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_arriba = imagen_chef_arriba.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_arriba_tk = ImageTk.PhotoImage(imagen_chef_arriba)

########
                # Ruta de la imagen del chef#1 viendo hacia la izquierda
                ruta_chef_izquierda = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "chef_izquierda.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef
                imagen_chef_izquierda = Image.open(ruta_chef_izquierda)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_izquierda = imagen_chef_izquierda.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_izquierda_tk = ImageTk.PhotoImage(imagen_chef_izquierda)

########

                # Ruta de la imagen del chef viendo hacia la derecha
                ruta_chef_derecha = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef_derecha.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef
                imagen_chef_derecha = Image.open(ruta_chef_derecha)

                # Se ajusta el tamaño
                imagen_chef_derecha = imagen_chef_derecha.resize((70,100))

                # Se convierte la imagen para tkinter
                self.imagen_derecha_tk = ImageTk.PhotoImage(imagen_chef_derecha)

########
                # Se coloca inicialmente el chef viendo hacia abajo
                self.chef_canvas = self.canvas.create_image(
                                                                self.chef_ejex,
                                                                self.chef_ejey,
                                                                image=self.imagen_abajo_tk
                                                        )

##########################
##########################

        # Función que muestra en consola la posición actual del chef (se utilizará para ver cuanto se puede mover el chef en el restaurante)
        def mostrar_posicion(self):

                # Se imprime la posición actual del chef en X y Y
                print( "X =", self.chef_ejex,"Y =", self.chef_ejey)

                # Se convierte la posición X del chef en columna de la matriz
                columna = self.chef_ejex // 50 # se divide entre 50 porque es el tamaño que tiene cada cuadro en la matriz 

                # Se convierte la posición Y del chef en fila de la matriz
                fila = self.chef_ejey // 50 # se divide entre 50 porque es el tamaño que tiene cada cuadro en la matriz 

                # Se muestra la posición en pixeles y en matriz
                print(
                        "X =", self.chef_ejex,
                        "Y =", self.chef_ejey,
                        "Fila =", fila,
                        "Columna =", columna
                        )



##########################
##########################

        # Función que permite mover el chef hacia arriba
        def mover_arriba(self):

                # Se coloca la imagen del chef de espalda 
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_arriba_tk)

                # Resta a Y para subir (obtiene la posición actual del chef en el mapa)
                self.chef_ejey = self.chef_ejey - self.distancia

                # Se mueve la imagen del chef
                self.canvas.move(self.chef_canvas, 0, -self.distancia) #chef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
##########################

##########################
        # Función que permite mover el chef hacia abajo
        def mover_abajo(self):

                # Se coloca la imagen del chef viendo hacia abajo 
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_abajo_tk)
                
                # Suma a Y para bajar
                        #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejey = self.chef_ejey + self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, 0, self.distancia) #cchef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
##########################
                
##########################
        # Función que permite mover el chef hacia la izquierda
        def mover_izquierda(self):

                # Se coloca la imagen del chef viendo hacia la izquierda
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_izquierda_tk)

                # Resta a X para ir a la izquierda
                        #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejex = self.chef_ejex - self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, -self.distancia, 0)#cchef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
#########################

##########################
        # Función que permite mover el chef hacia la derecha
        def mover_derecha(self):

                # Se coloca la imagen del chef viendo hacia la izquierda
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_derecha_tk)

                # Suma a X para ir a la derecha
                #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejex = self.chef_ejex + self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, self.distancia, 0) #chef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
#########################

#######################################################################################

# Clase asociada a la funcionaldiades del chef #2 dentro del restaurante
class Chef2:

        def __init__(self, canvas, base_dir, nombre, chef_ejex, chef_ejey):

                self.canvas = canvas
                self.BASE_DIR = base_dir
                self.nombre = nombre
                self.puntos = 0

                self.chef_ejex = chef_ejex
                self.chef_ejey = chef_ejey

                self.distancia = 50

########
                # Ruta de la imagen del chef#2 viendo hacia abajo
                ruta_chef_abajo = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef2_abajo.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef 
                imagen_chef_abajo = Image.open(ruta_chef_abajo)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_abajo = imagen_chef_abajo.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_abajo_tk = ImageTk.PhotoImage(imagen_chef_abajo)

########
                # Ruta de la imagen del chef viendo hacia arriba
                ruta_chef_arriba = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef2_arriba.png"
                                                )
                
                # Se abre la ruta que contiene la imagen del chef 
                imagen_chef_arriba = Image.open(ruta_chef_arriba)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_arriba = imagen_chef_arriba.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_arriba_tk = ImageTk.PhotoImage(imagen_chef_arriba)

########
                # Ruta de la imagen del chef viendo hacia la izquierda
                ruta_chef_izquierda = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "chef2_izquierda.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef
                imagen_chef_izquierda = Image.open(ruta_chef_izquierda)

                # Se ajusta el tamaño de la imagen del chef
                imagen_chef_izquierda = imagen_chef_izquierda.resize((70,100))

                # Se convierte la imagen del chef en un formato que usa tkinter 
                self.imagen_izquierda_tk = ImageTk.PhotoImage(imagen_chef_izquierda)

########

                # Ruta de la imagen del chef viendo hacia la derecha
                ruta_chef_derecha = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                "chef2_derecha.png"
                                                )

                # Se abre la ruta que contiene la imagen del chef
                imagen_chef_derecha = Image.open(ruta_chef_derecha)

                # Se ajusta el tamaño
                imagen_chef_derecha = imagen_chef_derecha.resize((70,100))

                # Se convierte la imagen para tkinter
                self.imagen_derecha_tk = ImageTk.PhotoImage(imagen_chef_derecha)

########
                # Se coloca inicialmente el chef viendo hacia abajo
                self.chef_canvas = self.canvas.create_image(
                                                                self.chef_ejex,
                                                                self.chef_ejey,
                                                                image=self.imagen_abajo_tk
                                                        )

##########################

        # Función que muestra en consola la posición actual del chef (se utilizará para ver cuanto se puede mover el chef en el restaurante)
        def mostrar_posicion(self):

                # Se imprime la posición actual del chef en X y Y
                print( "X =", self.chef_ejex,"Y =", self.chef_ejey)

                # Se convierte la posición X del chef en columna de la matriz
                columna = self.chef_ejex // 50 # se divide entre 50 porque es el tamaño que tiene cada cuadro en la matriz 

                # Se convierte la posición Y del chef en fila de la matriz
                fila = self.chef_ejey // 50 # se divide entre 50 porque es el tamaño que tiene cada cuadro en la matriz 

                # Se muestra la posición en pixeles y en matriz
                print(
                        "X =", self.chef_ejex,
                        "Y =", self.chef_ejey,
                        "Fila =", fila,
                        "Columna =", columna
                        )

##########################
##########################

        # Función que permite mover el chef hacia arriba
        def mover_arriba(self):

                # Se coloca la imagen del chef de espalda 
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_arriba_tk)

                # Resta a Y para subir (obtiene la posición actual del chef en el mapa)
                self.chef_ejey = self.chef_ejey - self.distancia

                # Se mueve la imagen del chef
                self.canvas.move(self.chef_canvas, 0, -self.distancia) #chef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
##########################

##########################
        # Función que permite mover el chef hacia abajo
        def mover_abajo(self):

                # Se coloca la imagen del chef viendo hacia abajo 
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_abajo_tk)
                
                # Suma a Y para bajar
                        #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejey = self.chef_ejey + self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, 0, self.distancia) #cchef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
##########################
                
##########################
        # Función que permite mover el chef hacia la izquierda
        def mover_izquierda(self):

                # Se coloca la imagen del chef viendo hacia la izquierda
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_izquierda_tk)

                # Resta a X para ir a la izquierda
                        #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejex = self.chef_ejex - self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, -self.distancia, 0)#cchef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()
##########################
#########################

##########################
        # Función que permite mover el chef hacia la derecha
        def mover_derecha(self):

                # Se coloca la imagen del chef viendo hacia la izquierda
                self.canvas.itemconfig(self.chef_canvas,image=self.imagen_derecha_tk)

                # Suma a X para ir a la derecha
                #Sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.chef_ejex = self.chef_ejex + self.distancia

                # Mueve la imagen del chef
                        #self.distancia tiene el valor por defecto de 15 pixeles eso movera la figura en el eje y ese valor
                        #No depende de self.ejey, esto sirve para tener la ubicación original del chef en el mapa (para que no se salga del mapa)
                self.canvas.move(self.chef_canvas, self.distancia, 0) #chef, desplazamiento en ejex, desplazamiento en ejey

##########################
##########################
                 # Se muestra la posición actual del chef
                self.mostrar_posicion()

#######################################################################################

#Clase que guarda toda la información de los ingredienes de la cocina americana
class ingredientes_restaurante_americano:

        # Constructor de la clase Ingrediente
        def __init__(self, canvas_ingredientes, base_dir, nombre_ingrediente, archivo_imagen):

                # Guarda el canvas donde se dibujarán los ingredientes
                self.canvas_ingredientes = canvas_ingredientes

                # Se define la ruta donde se almacenará las imagenes de los ingredientes 
                self.BASE_DIR = base_dir

                # Variable que guarda el nombre del ingrediente (zanahoria, tomate, queso, etc.)
                self.nombre_ingrediente = nombre_ingrediente

                # Estado inicial del ingrediente cuando se crea
                self.estado_ingrediente = "crudo"

                # Guarda el nombre del archivo de imagen
                self.archivo_imagen = archivo_imagen

                # Aquí se almacenará el objeto gráfico creado en el canvas
                self.objeto_canvas = None

                # Construye la ruta completa de la imagen
                ruta_imagen = os.path.join(self.BASE_DIR,"Imagenes",self.archivo_imagen)

                # Se abre la ruta donde esta almacenadas la imagen de los ingredientes
                imagen = Image.open(ruta_imagen)

                # Tamaño que tendrá la imagenes de los ingredientes 
                imagen = imagen.resize((40, 40))

                # Convierte la imagen en un formato que Tkinter pueda usar
                self.imagen_tk = ImageTk.PhotoImage(imagen)


##########################

        # Función que coloca el ingrediente sobre la cabeza del chef
        def tomar_ingrediente(self, chef):

                # Si ya existe una imagen del ingrediente encima de l la elimina
                if self.objeto_canvas != None:

                        self.canvas_ingredientes.delete(self.objeto_canvas)

                # Crea la imagen del ingrediente encima del chef
                self.objeto_canvas = self.canvas_ingredientes.create_image(
                                                                                chef.chef_ejex, #Posición actual del chef en el eje x 
                                                                                chef.chef_ejey - 120,   # Coloca la imagen 40 píxeles arriba de la cabeza del chef
                                                                                image=self.imagen_tk # Se utiliza la imagen del ingrediente que fue cargada previamente
                                                                                )
##########################

        # Función que hace que el ingrediente siga al chef cuando camina
        def mover_ingrediente_con_chef(self, chef):

                # Verifica que exista un ingrediente dibujado
                if self.objeto_canvas != None:

                # Mueve la imagen del ingrediente junto con el chef
                        #Se obtiene las coordenas del chef 
                        self.canvas_ingredientes.coords(
                                                self.objeto_canvas,#Referencia del objeto o ingrediente que se esta usando 
                                                chef.chef_ejex, #Se coloca el ingrediente del chef en el eje x 
                                                chef.chef_ejey - 120 #Se coloca el ingrediente arriba de la cabeza del chef 
                                                )

##########################

        # Elimina el ingrediente de las manos del chef
        def soltar_ingrediente(self):

                # Se verifica si el chef ya tiene un ingrediente sobre su cabeza
                if self.objeto_canvas != None:

                        # Se elimina la imagen del ingrediente que tiene el chef actualmente 
                        self.canvas_ingredientes.delete(self.objeto_canvas)

                        # Se actualiza el chef, porque ya no está cargando el ingrediente
                        self.objeto_canvas = None

##########################

        # Función que devuelve la posición actual del ingrediente
        def obtener_posicion_ingrediente(self):

                # Se valida que el chef tenga un ingrediente seleccionado 
                if self.objeto_canvas != None:

                        # Se obtiene las coordenadas X,Y del ingrediente
                        return self.canvas_ingredientes.coords(self.objeto_canvas)

                else: 
                        # Si no existe devuelve None
                        return None
                
##########################
        # Función que cambia la imagen del ingrediente crudo a cocinado 
        def imagen_ingrediente_cocinado(self, nuevo_archivo):

                # Guarda el nuevo nombre de imagen
                self.archivo_imagen = nuevo_archivo

                # Ruta donde se encuentra la imagen del ingrediente cocinado 
                ruta_imagen = os.path.join(
                                                self.BASE_DIR,
                                                "Imagenes",
                                                self.archivo_imagen
                                        )

                # Se abre la ruta donde se encuentra el ingrediente cocinado 
                imagen = Image.open(ruta_imagen)

                # Se ajusta el tamaño de la imagen del ingrediene cocinado 
                imagen = imagen.resize((40, 40))

                # Convierte la imagen en un formato que pueda usar  Tkinter
                self.imagen_tk = ImageTk.PhotoImage(imagen)

                # Se valida si el chef ya tiene un ingrediente seleccionado 
                if self.objeto_canvas != None:

                        # Se caambia la imagen que se ve en pantalla
                        self.canvas_ingredientes.itemconfig(
                                                                self.objeto_canvas,
                                                                image=self.imagen_tk
                                                        )

#######################################################################################

#Clase que guadar las posiciones de la cocina en los restaurates  
class Cocina:

        def __init__(self, fila, columna):

                # Guarda la fila donde se encuentra la cocina
                self.fila = fila

                # Guarda la columna donde se encuentra la cocina
                self.columna = columna
#######################################################################################
# Clase que guarda las posiciones de las tablas de picar en los restaurantes 
class tabla_Picar:

        def __init__(self, fila, columna):

                # Se guarda la fila donde está la tabla de picar 
                self.fila = fila

                # Se guarda la columna donde está la tabla de picar
                self.columna = columna
#######################################################################################
# Clase que almacena la posición de una freidora dentro del restaurante
class Freidora:

        def __init__(self, fila, columna):

                # Guarda la fila donde se encuentra la freidora
                self.fila = fila

                # Guarda la columna donde se encuentra la freidora
                self.columna = columna

#######################################################################################
# Clase que guarda un ingrediente y su estado (picado, frito, crudo o cocinado) para la receta 
class Ingrediente_Receta:

        # Constructor de la clase
        def __init__(self, nombre_ingrediente, estado_requerido):

                # Se cuarda el nombre del ingrediente que pide la receta
                self.nombre_ingrediente = nombre_ingrediente

                # Se guarda el estado que debe tener el ingrediente: crudo, picado, cocinado o frito
                self.estado_requerido = estado_requerido

#######################################################################################
# Clase de la receta del juego
class Receta:

        
        def __init__(self, lista_ingredientes, puntos_receta, max_time_receta):

                # Guarda la lista de ingredientes que necesita la receta
                self.lista_ingredientes = lista_ingredientes

                # Guarda los puntos que vale la receta
                self.puntos_receta = puntos_receta

                # Guarda el tiempo máximo para entregar la receta
                self.max_time_receta = max_time_receta


#########################################

        # Función que muestra la receta en consola
        def mostrar_receta(self):

                # Muestra el título de la receta
                print("Orden solicitada:")

                # Recorre cada ingrediente de la receta
                for ingrediente in self.lista_ingredientes:

                        # Muestra el nombre y el estado que necesita ese ingrediente
                        print(ingrediente.nombre_ingrediente, "-", ingrediente.estado_requerido)

                # Muestra los puntos de la receta
                print("Puntos:", self.puntos_receta)

                # Muestra el tiempo máximo de la receta
                print("Tiempo máximo:", self.max_time_receta)

#########################################

        # Función que compara la receta solicitada con los ingredientes entregados por el jugador
        def comparar_receta(self, ingredientes_entregados):


                # Se verifica si la cantidad de ingredientes entregados es diferente a la cantidad de ingredientes de la receta
                if len(ingredientes_entregados) != len(self.lista_ingredientes):

                        # Si la cantidad es diferente, la receta está incorrecta
                        return False

                # Se recorre cada ingrediente que pide la receta
                for ingrediente_receta in self.lista_ingredientes:

                        # Se crea una variable para saber si el ingrediente solicitado fue encontrado
                        ingrediente_encontrado = False

                        # Se muestra el ingrediente de la receta que se está buscando
                        print("Buscando:", ingrediente_receta.nombre_ingrediente, "-", ingrediente_receta.estado_requerido)

                        # Se muestra la lista completa de ingredientes entregados
                        print("----- INGREDIENTES ENTREGADOS -----")

                        # Se recorre cada ingrediente que entregó el jugador
                        for ingrediente_entregado in ingredientes_entregados:
                                print(
                                        ingrediente_entregado.nombre_ingrediente,
                                        "-",
                                        ingrediente_entregado.estado_requerido
                                )

                                # Se muestra qué ingrediente entregó el jugador para comparar
                                print("Comparando con:", ingrediente_entregado.nombre_ingrediente, "-", ingrediente_entregado.estado_requerido)

                                # Se compara si el nombre del ingrediente entregado es igual al nombre del ingrediente solicitado
                                if ingrediente_receta.nombre_ingrediente == ingrediente_entregado.nombre_ingrediente:

                                        # Se compara el estado requerido con el estado entregado ya convertido al mismo formato
                                        if ingrediente_receta.estado_requerido ==  ingrediente_entregado.estado_requerido:
                                                
                                                # Se encontró una coincidencia
                                                print("Coincidencia:", ingrediente_entregado.nombre_ingrediente, "-", ingrediente_entregado.estado_requerido)

                                                # Se indica que el ingrediente sí fue encontrado correctamente
                                                ingrediente_encontrado = True

                # Se verifica si el ingrediente solicitado no fue encontrado
                        if ingrediente_encontrado == False:

                                # Se muestra qué ingrediente no fue encontrado
                                print("No encontrado:", ingrediente_receta.nombre_ingrediente, "-", ingrediente_receta.estado_requerido)

                                # Si falta un ingrediente o está en estado incorrecto, la receta está incorrecta
                                return False

                # Si todos los ingredientes fueron encontrados correctamente, la receta está correcta
                return True


#######################################################################################
#Clase que contiene la funcionalidad del restaurante americano 
class Pantalla_Restaurante_Americano:

        def __init__(self, ventana_mapa, nombre_jugador, pantalla_mapa):

                self.ventana_mapa = ventana_mapa

                # Guarda una referencia del mapa se utilizará como referencia del puntaje 
                        #Puntaje obtenido en el restaurante americano al restaurante europe
                self.pantalla_mapa = pantalla_mapa

                # Se guarda el nombre del jugador actual
                self.nombre_jugador = nombre_jugador

                # Se inicializa el puntaje del jugador en cero
                self.puntaje_jugador = 0

                # Se obtiene la carpeta donde está la imagen de la cocicna americana 
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se crea la ventana secundaria donde estará el restaurante americano 
                self.ventana_restaurante = Toplevel(ventana_mapa)

                # Se coloca el título de la ventana
                self.ventana_restaurante.title("Restaurante Americano")

                # Se define el tamaño de la ventana
                self.ventana_restaurante.geometry("1000x700+350+70")

                # Se evita que el usuario cambie el tamaño de la ventana 
                self.ventana_restaurante.resizable(False, False)

                # Se crea el canvas donde ira la imagen del restaurante americano 
                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")

                # Se coloca el canvas en la ventana
                self.canvas.pack()

                # Se define la ruta de la imagen de cocina
                ruta_cocina_americana = os.path.join(self.BASE_DIR, "Imagenes", "Cocina1.png")

                # Se abre la imagen de cocina
                imagen_cocina_americana = Image.open(ruta_cocina_americana)

                # Se ajusta el tamaño de la imagen del restaurante 
                imagen_cocina_americana = imagen_cocina_americana.resize((1000, 700))

                # Se convierte la imagen para tkinter
                self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_americana)

                # Se coloca la imagen de fondo en el canvas
                self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

#######
                
                # Tiempo inicial de la receta en segundos (1 minuto)
                self.tiempo_restante = 60

                # Texto que muestra el temporizador en pantalla
                self.texto_temporizador = self.canvas.create_text(

                                                                        500, # posición del reloj en el eje x 

                                                                        70, # posición del reloj en el eje y 

                                                                        text="01:00", #Formato de como se mostrará el tiempo en pantalla

                                                                        fill="yellow", #color del texto del reloj

                                                                        font=("Arial", 15, "bold")
                                                                )

                # Inicia la cuenta regresiva
                self.actualizar_temporizador()              

#######
                # Ruta de la imagen que se mostrará cuando la receta sea incorrecta
                ruta_carne_quemada = os.path.join(self.BASE_DIR, "Imagenes", "quemado.png")

                # Se abre la imagen de carne quemada
                imagen_carne_quemada = Image.open(ruta_carne_quemada)

                # Se ajusta el tamaño de la imagen de la carne quemada 
                imagen_carne_quemada = imagen_carne_quemada.resize((100, 100))

                # Se convierte la imagen en un formato que Tkinter pueda usar 
                self.imagen_carne_quemada_tk = ImageTk.PhotoImage(imagen_carne_quemada)
#######

                # Se crea un texto en el canvas para mostrar el nombre del jugador
                self.texto_nombre_jugador = self.canvas.create_text(

                                                                        350, # Posición del nombre del jugador en el eje X

                                                                        30, # Posición del nombre del jugador en el eje Y

                                                                        text="Jugador: " + self.nombre_jugador, # Texto que se mostrará en pantalla

                                                                        fill="white", # Color de las letras

                                                                        font=("Arial", 14, "bold") # Tipo de letra, tamaño y estilo
                                                                )

                # Se crea un texto en el canvas para mostrar el puntaje actual del jugador
                self.texto_puntaje_jugador = self.canvas.create_text(

                                                                        600, # Posición del puntaje del jugador en el eje X

                                                                        30, # Posición del puntaje del jugador en el eje Y

                                                                        text="Puntaje: " + str(self.puntaje_jugador), # Texto que se mostrará en pantalla

                                                                        fill="white", # Color de las letras

                                                                        font=("Arial", 14, "bold") # Tipo de letra, tamaño y estilo
                                                                )

                # Detecta cuando el jugador presiona la tecla A que permite tomar los ingredientes
                self.ventana_restaurante.bind("a", self.escoger_ingrediente_americano)

                # Detecta cuando el jugador presiona la tecla "s" para cocinar
                self.ventana_restaurante.bind("s", self.usar_cocina_americano)

                # Detecta cuando el jugador presiona la tecla "D" para picar ingredientes
                self.ventana_restaurante.bind("d", self.usar_tabla_picar_americano)

                # Detecta cuando el jugador presiona la tecla "F" para freír ingredientes
                self.ventana_restaurante.bind("f", self.usar_freidora_americano)

                # Detecta cuando el jugador presiona la tecla E para entregar un ingrediente
                self.ventana_restaurante.bind("e", self.entregar_ingrediente_americano)

#######
                # Etiquetas que contiene el nombre de los ingredientes del estante izquierdo
                self.canvas.create_text(110, 135, text="Carne", fill="white", font=("Arial", 8, "bold"))
                self.canvas.create_text(115, 170, text="Remolacha", fill="white", font=("Arial", 8, "bold"))
                self.canvas.create_text(100, 205, text="Hongo", fill="white", font=("Arial", 8, "bold"))
                self.canvas.create_text(100, 255, text="Calabaza", fill="white", font=("Arial", 8, "bold"))
                self.canvas.create_text(100, 295, text="Zanahoria", fill="white", font=("Arial", 8, "bold"))
                self.canvas.create_text(80, 345, text="Papa", fill="white", font=("Arial", 8, "bold"))

                # Etiquetas del estante derecho
                self.canvas.create_text(880, 175, text="Tomate", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(880, 210, text="Mayonesa", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(880, 250, text="Queso", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(900, 290, text="Lentejas", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(900, 320, text="Cebolla Morada", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(900, 360, text="Aceitunas", fill="white", font=("Arial", 8, "bold"))

#######
                # Matriz que permite el movimiento en el  restaurante americano 

                self.matriz_movimiento_americano = [
                     

                        # Fila 0
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

                        # Fila 1
                        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],

                        # Fila 2
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],

                        # Fila 3
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 4
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 5
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 6
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 7
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 8
                        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],

                        # Fila 9
                        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],

                        # Fila 10
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0],

                        # Fila 11
                        [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0],

                        # Fila 12
                        [0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0],

                        # Fila 13
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                        ]
                       
#######
                # Se dibuja la cuadrícula sobre la cocina
                        #Se utilizará para definir la matriz de posición (1= hay movimiento y 0 = no hay movimiento)
                #self.dibujar_cuadricula()

#######
               # Se crea el primer chef
                self.chef1 = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 350, 350)

                # Se crea el segundo chef
                self.chef2 = Chef2(self.canvas, self.BASE_DIR, "Jugador 2", 400, 350)

                # Se coloca inicialmente como activo el chef 1
                self.chef = self.chef1

#######
                # Ruta donde se encuentra la imagen del botón para cambiar de chef
                ruta_boton_cambiar = os.path.join(
                                                        self.BASE_DIR,                  # Se obtiene la ruta donde se guardan las imagenes 
                                                        "Imagenes",                     # Carpeta donde están la imagen de cambiar el chef 
                                                        "boton_cambiar_chef.png"        # Nombre de la imagen del botón que permite cambiar entre los chefs 
                                                )

                # Se abre la ruta donde se encuentra la imagen de cambiar chefs 
                imagen_boton_cambiar = Image.open(ruta_boton_cambiar)

                # Se define el tamaño que tendrá el botón de cambiar los chefs 
                imagen_boton_cambiar = imagen_boton_cambiar.resize((140, 140))

                # Se convierte la imagen a un formato que Tkinter pueda utilizar
                self.imagen_boton_cambiar_tk = ImageTk.PhotoImage(imagen_boton_cambiar)

                # Se crea la imagen del botón dentro del canvas
                self.boton_cambiar_chef = self.canvas.create_image(

                                                                        100,     # Posición del botón en el eje X

                                                                        550,     # Posición del botón en el eje Y

                                                                        image=self.imagen_boton_cambiar_tk  # Imagen que tendrá el botón
                                                                )

                # Permite detectar cuando el jugador hace clic sobre la imagen
                self.canvas.tag_bind(

                                        self.boton_cambiar_chef,  # Nombre de la imagen que funcionará como botón

                                        "<Button-1>",             # Detecta clic izquierdo del mouse

                                        self.cambiar_chef         # Llama a la función que cambia entre chef 1 y chef 2
                                )

#######
                # Se guarda el ingrediente que el chef está sosteniendo actualmente
                self.ingrediente_en_mano = None

###############################################       

                # Lista que almacena las posiciones de las cocinas del restaurante americano
                        #Posicione válidas para cocinar la carne 
                self.cocinas = [

                                # Cocina superior derecha
                                Cocina(2, 13),

                                # Cocina superior derecha
                                Cocina(2, 14),

                                # Cocina superior derecha
                                Cocina(3, 14),

                                # Cocina inferior derecha
                                Cocina(9, 13),

                                # Cocina inferior derecha
                                Cocina(9, 14)

                        ]
                
#######
                # Lista que almacena las posiciones donde el chef puede cortar ingredientes
                        # Posicione válidas para cortar ingredientes
                self.tablas_picar = [

                                        # Tabla de picar en la parte superior de la pantalla 
                                        tabla_Picar(2, 5),

                                        #Tabla de picar en la parte inferior de la pantalla 
                                        tabla_Picar(10, 16),
                                        tabla_Picar(10, 17),
                                        ]

#######
                # Lista que almacena las posiciones donde el chef puede usar la freidora
                self.freidoras = [

                                        # Posición frente a la freidora
                                        Freidora(9, 3),

                                        # Posición al costado de la freidora
                                        Freidora(8, 3)
                                ]
                
#######
                # Lista vacía donde se guardarán los ingredientes entregados para la orden actual
                self.ingredientes_entregados = []

                # Lista que almacená las posiciones válidas de la estación de entrega
                self.estaciones_entrega = [

                                                # Posiciones válidas para la entrega de ingredientes finalizados 
                                                (10, 6),
                                                (10, 7),
                                                (11, 6),
                                                (11, 7),
                                        ]

###############################################

                # Se crea el ingrediente carne del restaurante americano
                self.carne = ingredientes_restaurante_americano(
                                                                        self.canvas,       # Canvas donde se dibujará la imagen de la carne
                                                                        self.BASE_DIR,     # Ruta donde se encuentra la carpeta de las imagenes
                                                                        "Carne",           # Nombre del ingrediente que se va a usar 
                                                                        "carne.png"        # Imagen de la carne
                                                                        )
                

#######

                # Se crea el ingrediente remolacha del restaurante americano
                self.remolacha = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de la remolacha
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de las imagenes
                                                                        "Remolacha",           # Nombre del ingrediente que se va a usar 
                                                                        "remolacha.png"        # Imagen de la remolacha
                                                                        )
                


#######
                # Se crea el ingrediente calabaza del restaurante americano
                self.hongo = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de la calabaza
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de las imagenes
                                                                        "Hongo",           # Nombre del ingrediente que se va a usar 
                                                                        "hongo.png"        # Imagen de la calabaza
                                                                        )
                
#######
                # Se crea el ingrediente calabaza del restaurante americano
                self.calabaza = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de la calabaza
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de las imagenes
                                                                        "Calabaza",           # Nombre del ingrediente que se va a usar 
                                                                        "calabaza.png"        # Imagen de la calabaza
                                                                        )
                
        
#######
                # Crea el ingrediente zanahoria del restaurante americano
                self.zanahoria = ingredientes_restaurante_americano(
                                                                        self.canvas, # Canvas donde se dibujará la imagen de la zanahoria
                                                                        self.BASE_DIR, #Ruta donde se encuentra la carpeta de las imagenes 
                                                                        "Zanahoria",# Nombre del ingrediente que se va a usar  
                                                                        "zanahoria.png" # Imagen de la zanahoria
                                                                )
                
#######

                # Se crea el ingrediente papa del restaurante americano
                self.papa = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de la papa
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Papa",               # Nombre del ingrediente que se va a usar
                                                                        "papa.png"            # Imagen de la papa
                                                                )
                
#######

                # Se crea el ingrediente tomate del restaurante americano
                self.tomate = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen del tomate
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Tomate",             # Nombre del ingrediente
                                                                        "tomate.png"          # Imagen del tomate
                                                                )

#######

                # Se crea el ingrediente mayonesa del restaurante americano
                self.mayonesa = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de la mayonesa
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Mayonesa",             # Nombre del ingrediente
                                                                        "mayonesa.png"          # Imagen de la mayonesa
                                                                )
#######
                # Se crea el ingrediente queso del restaurante americano
                self.queso = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen del queso
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Queso",             # Nombre del ingrediente
                                                                        "queso.png"          # Imagen del queso
                                                                )
                
#######
                # Se crea el ingrediente lentejas del restaurante americano
                self.lentejas = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de las lentejas
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Lentejas",             # Nombre del ingrediente
                                                                        "lentejas.png"          # Imagen de las lentejas
                                                                )

#######

                # Se crea el ingrediente cebolla del restaurante americano
                self.cebolla = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de las cebollas
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Cebolla",             # Nombre del ingrediente
                                                                        "cebolla.png"          # Imagen de las cebollas
                                                                )
#######
                # Se crea el ingrediente aceiturna del restaurante americano
                self.aceituna = ingredientes_restaurante_americano(
                                                                        self.canvas,          # Canvas donde se dibujará la imagen de las aceitunas
                                                                        self.BASE_DIR,        # Ruta donde se encuentra la carpeta de imágenes
                                                                        "Aceituna",             # Nombre del ingrediente
                                                                        "aceituna.png"          # Imagen de las aceitunas
                                                                )

#######
                # Permite que la ventana del restaurante detecte las teclas
                self.ventana_restaurante.focus_force()

                # Detecta cuando el usuario presiona cualquier tecla de dirección 
                self.ventana_restaurante.bind("<Key>", self.mover_chef)

#########################################

                # Se inicializa el número de la orden actual
                self.numero_orden = 1

                # Cantidad máxima de órdenes permitidas en este restaurante
                self.maximo_ordenes = 3
                
                # Se genera la receta inicial del restaurante americano
                self.receta_actual = self.generar_receta_americano()

                # Se llama a la función que muestra la orden actual en pantalla
                self.mostrar_orden_americano()


#########################################

        #Función que muestra la orden que debe preparar el chef en la pantalla 
        def mostrar_orden_americano(self):

                # Se verifica si ya existe un rectángulo de una orden anterior
                        #hasattr() es una función de Python que sirve para preguntar si el objeto tiene un atributo
                        # hasattr(objeto, "atributo") devuelve True y False si ya existe un cuadro donde se coloca la receta lo borra para hacerlo para la siguiente receta
                if hasattr(self, "cuadro_orden"):

                        # Se elimina el rectángulo anterior para evitar que se dibuje encima
                        self.canvas.delete(self.cuadro_orden)

                # Se verifica si ya existe el título de una orden anterior
                        #hasattr() es una función de Python que sirve para preguntar si el objeto tiene un atributo
                        # hasattr(objeto, "atributo") devuelve True y False si ya existe el título de la orden, lo borra para hacerlo para la siguiente receta
                if hasattr(self, "titulo_orden"):

                        # Se elimina el título anterior
                        self.canvas.delete(self.titulo_orden)

                # Se verifica si ya existe el texto de ingredientes de una orden anterior
                        #hasattr() es una función de Python que sirve para preguntar si el objeto tiene un atributo
                        # hasattr(objeto, "atributo") devuelve True y False si ya existe el listado con la receta, lo borra para hacerlo para la siguiente receta
                if hasattr(self, "texto_ingredientes_orden"):

                        # Se elimina el texto anterior
                        self.canvas.delete(self.texto_ingredientes_orden)

                # Se crea un rectángulo de fondo para mostrar la orden
                self.cuadro_orden = self.canvas.create_rectangle(

                                                820, # Posición inicial X

                                                10, # Posición inicial Y

                                                995, # Posición final X

                                                150, # Posición final Y

                                                fill="#3B2416", # Color café oscuro

                                                outline="#D2B48C", # Color del borde

                                                width=4 # Grosor del borde
                                        )

#######
                # Se crea un texto con el encabezado de la orden
                self.titulo_orden = self.canvas.create_text(

                                                908, # Posición del texto "orden" en el eje X

                                                25, # Posición del texto "orden"  en el eje Y

                                                text="ORDEN "+ " # " +str(self.numero_orden), # Encabezado de la orden + el consecutivo de la orden 

                                                fill="white",

                                                font=("Arial", 10, "bold")
                                        )

                # Se crea un texto con los ingredientes solicitados
                self.texto_ingredientes_orden = self.canvas.create_text(

                        910, # Posición de los ingredientes en el eje X

                        85, # Posición de los ingredientes en el eje Y

                        text=
                        self.receta_actual.lista_ingredientes[0].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[0].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[1].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[1].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[2].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[2].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[3].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[3].estado_requerido,

                        fill="white",

                        font=("Arial", 10, "bold")
                )

#########################################

        # Función que genera una receta aleatoria (random) para el restaurante americano
        def generar_receta_americano(self):
                

                # Lista de ingredientes que pueden ir fritos
                ingredientes_fritos = ["Papa", "Carne"]

                # Lista de ingredientes que pueden ir picados
                ingredientes_picados = ["Tomate", "Cebolla", "Zanahoria", "Remolacha", "Calabaza", "Hongo", "Papa", "Queso"]

                # Lista de ingredientes que pueden ir cocinados
                ingredientes_cocinados = ["Carne"]

                # Lista de ingredientes que pueden ir crudos
                ingredientes_crudos = ["Mayonesa", "Lentejas", "Aceituna"]

                # Se escoge un ingrediente frito aleatorio
                ingrediente_frito = random.choice(ingredientes_fritos)

                # Se escoge un ingrediente picado aleatorio
                ingrediente_picado = random.choice(ingredientes_picados)

                # Se escoge un ingrediente cocinado aleatorio
                ingrediente_cocinado = random.choice(ingredientes_cocinados)

                # Se escoge un ingrediente crudo aleatorio
                ingrediente_crudo = random.choice(ingredientes_crudos)

                # Se crea la lista de ingredientes de la receta
                lista_ingredientes = [

                        Ingrediente_Receta(ingrediente_frito, "frito(a)"),

                        Ingrediente_Receta(ingrediente_picado, "picado(a)"),

                        Ingrediente_Receta(ingrediente_cocinado, "cocinado(a)"),

                        Ingrediente_Receta(ingrediente_crudo, "crudo(a)")
                ]

                # Se crea la receta con puntos y tiempo máximo
                receta = Receta(lista_ingredientes, 60, 60) #100 puntos, 60 segundos

                # Se muestra la receta en consola para probar
                receta.mostrar_receta()

                # Se retorna la receta creada
                return receta
        
#########################################

        #Función que genera la siguiente receta 
        def generar_nueva_orden_americano(self):

                # Se verifica si todavía quedan órdenes por generar
                if self.numero_orden < self.maximo_ordenes: 

                        # Se aumenta el número consecutivo de la orden
                        self.numero_orden += 1

                        # Se llama a la función que crea recetas de forma aleatoria 
                        self.receta_actual = self.generar_receta_americano()

                        # Se llama a la funcipon que muestra esa nueva receta en pantalla
                        self.mostrar_orden_americano()
                
                # Si ya se completaron las 3 órdenes
                else:

                        print("Todas las órdenes americanas fueron completadas")

                        # Muestra un mensaje emergente
                        messagebox.showinfo(
                                "Restaurante Americano",
                                "¡FELICIDADES!\nCompletaste las 3 recetas correctamente"
                        )

                        # Se guarda el puntaje acumulado en el mapa
                        self.pantalla_mapa.puntaje_jugador = self.puntaje_jugador

                        # Se marca el restaurante americano como aprobado
                        self.pantalla_mapa.americano_aprobado = True

                        # Se cierra la cocina americana
                        self.ventana_restaurante.destroy()

                        # Se vuelve a mostrar el mapa
                        self.ventana_mapa.deiconify()

#########################################

        # Función que permite entregar un ingrediente en la estación de entrega
        def entregar_ingrediente_americano(self, event):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Se verifica si el chef está en una posición válida de entrega
                if (fila, columna) not in self.estaciones_entrega:

                        # Se muestra un mensaje si no está en la estación de entrega
                        print("No estás en la estación de entrega")

                        # Se detiene la función
                        return
                
                # Se verifica si el chef no tiene ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        # Se muestra un mensaje si no lleva ingrediente
                        print("No tienes ingrediente para entregar")

                        # Se detiene la función
                        return
                
                # Se crea una copia del ingrediente para guardar exactamente lo que entrego el chef 
                        # Se guarda el nombre y el estado que tenía al momento de entregarlo
                ingrediente_entregado = Ingrediente_Receta(

                        # Se guarda el nombre del ingrediente que el chef tiene en la mano
                        self.ingrediente_en_mano.nombre_ingrediente,

                        # Se guarda el estado actual del ingrediente con el formato que usa la receta
                        self.ingrediente_en_mano.estado_ingrediente + "(a)"
                )

       
                # Se guarda la copia del ingrediente, no el objeto original (puede ser que el chef tomára inicialmente un ingrediente
                        #  que no era el correcto pero antes de entregarlo se cambio correctamente)
                self.ingredientes_entregados.append(ingrediente_entregado)

                # Se muestra en consola el ingrediente entregado
                print(
                        "Ingrediente entregado:",
                        ingrediente_entregado.nombre_ingrediente,
                        "-",
                        ingrediente_entregado.estado_requerido
                )


                # Se elimina la imagen del ingrediente de la mano del chef
                self.ingrediente_en_mano.soltar_ingrediente()

                # Se limpia la mano del chef
                self.ingrediente_en_mano = None

                # Se muestra cuántos ingredientes se han entregado
                print("Ingredientes entregados:", len(self.ingredientes_entregados))

                # Se verifica si ya se entregó la misma cantidad de ingredientes que pide la receta
                if len(self.ingredientes_entregados) == len(self.receta_actual.lista_ingredientes):

                        # Se muestra un mensaje para indicar que ya se puede validar la receta completa
                        print("Validando receta...")

                        # Se guarda el resultado de comparar la receta actual con los ingredientes entregados
                        receta_correcta = self.receta_actual.comparar_receta(self.ingredientes_entregados)

                        # Se verifica si la receta fue correcta
                        if receta_correcta == True:

                                # Se calculan los puntos ganados según el tiempo restante (si finaliza la receta faltando 35 segundos gana 35 puntos)
                                puntos_ganados = self.tiempo_restante

                                # Se suman los puntos ganados al puntaje total del jugador
                                self.puntaje_jugador += puntos_ganados

                                # Se actualiza el texto del puntaje en pantalla
                                self.canvas.itemconfig(
                                                        self.texto_puntaje_jugador,
                                                        text="Puntaje: " + str(self.puntaje_jugador)
                                                )

                                # Se muestra en consola cuántos puntos ganó
                                print("Puntos ganados:", puntos_ganados)

                                # Se limpian los ingredientes entregados para iniciar una nueva orden
                                self.ingredientes_entregados = []

                                # Se reinicia el tiempo para la nueva orden
                                self.tiempo_restante = 60

                                # Se genera una nueva orden
                                self.generar_nueva_orden_americano()

                        # Si la receta entregada no coincide con la receta solicitada
                        else:

                                # Se indica que la receta fue incorrecta
                                print("Receta incorrecta")

                                # Se elimina la imagen de la receta incorrecta si ya existía
                                if hasattr(self, "imagen_error"):

                                        # Se elimina la imagen anterior
                                        self.canvas.delete(self.imagen_error)

                                # Se muestra la imagen de carne quemada
                                self.imagen_error = self.canvas.create_image(
                                                                                500,
                                                                                120,
                                                                                image=self.imagen_carne_quemada_tk
                                                                        )

                                # El mensaje de receta incorrecta desaparece después de 3 segundos
                                self.ventana_restaurante.after(
                                                                3000,
                                                                self.ocultar_mensaje_error
                                                        )
                                # Se limpian los ingredientes entregados para intentar otra vez
                                self.ingredientes_entregados = []

                # Si todavía no se han entregado todos los ingredientes, no se valida la receta
                else:
                         # Se muestra que todavía faltan ingredientes
                        print("Todavía faltan ingredientes para validar la receta")
                        

#########################################
        # Función que elimina el mensaje de receta incorrecta
        def ocultar_mensaje_error(self):

                # Se valida si en la pantalla aparece la imagen de receta incorrecta 
                if hasattr(self, "imagen_error"):

                        # Elimina la imagen
                        self.canvas.delete(self.imagen_error)        
#########################################
        

        # Función que actualiza el temporizador cada segundo
        def actualizar_temporizador(self):

                # Se calcula los minutos restantes
                minutos = self.tiempo_restante // 60

                # Se calcula los segundos restantes
                segundos = self.tiempo_restante % 60

                # Se actualiza el texto del temporizador
                self.canvas.itemconfig(

                                        self.texto_temporizador,

                                        text=f"{minutos:02d}:{segundos:02d}"
                                )

                # Se verifica si todavía queda tiempo
                if self.tiempo_restante > 0:

                        # Se resta un segundo
                        self.tiempo_restante -= 1

                        # Se vuelve a ejecutar la función dentro de 1 segundo
                        self.ventana_restaurante.after(
                                                        1000,
                                                        self.actualizar_temporizador
                                                )

                else:

                        # Mensaje cuando se acaba el tiempo
                        messagebox.showinfo(
                                                "Tiempo agotado",
                                                "La orden ha expirado"
                                        )
                        
                        # Se limpian los ingredientes entregados porque la orden falló
                        self.ingredientes_entregados = []

                        # Se reinicia el tiempo para la nueva orden
                        self.tiempo_restante = 60

                        # Se genera otra receta, pero se mantiene el mismo número de orden
                        self.receta_actual = self.generar_receta_americano()

                        # Se actualiza la orden en pantalla
                        self.mostrar_orden_americano()

                        # Se devuelve el foco a la ventana del restaurante
                        self.ventana_restaurante.focus_force()

                        # Se vuelve a asegurar que las teclas sigan funcionando
                        self.ventana_restaurante.bind("<Key>", self.mover_chef)

                        # Se vuelve a iniciar el temporizador
                        self.actualizar_temporizador()
#########################################

        # Función que determina cual tecla se presionó el jugador para mover el chef
        def mover_chef(self, event):

                # Se obtiene la fila actual del chef
                fila_actual = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna_actual = self.chef.chef_ejex // 50

                # Se crea una variable temporal para saber hacia que fila se esta moviendose el chef
                nueva_fila = fila_actual

                # Se crea una variable temporal para saber hacia que columna se esta moviendose el chef
                nueva_columna = columna_actual

#######         #Se controla el desplazamiento del chef al subir, bajar, derecha o izquierda 

                 # Flecha arriba
                if event.keysym == "Up":

                        #si el chef esta en al fila 2 y quiere subir se le resta 1 a la fila (-1) actual y queda en la fila 1
                        nueva_fila = fila_actual - 1

                # Flecha abajo
                elif event.keysym == "Down":

                        #Si el chef esta en la fila 2 y quiere bajar se le debe sumar 1 a la fila actual y queda en la fila 3
                        nueva_fila = fila_actual + 1

                # Flecha izquierda
                elif event.keysym == "Left":

                        #Si el chef esta en la columna 4 y se mueve a la izquierda se le resta 1 a la posición actual y queda en la columna 3
                        nueva_columna = columna_actual - 1

                # Flecha derecha
                elif event.keysym == "Right":

                        ##Si el chef esta en la columna 4 y se mueve a la derecha se le suma 1 a la posición actual para pasar a la columnna 5
                        nueva_columna = columna_actual + 1

#######         #Se define los límites de la pantalla donde se puede mover el chef 

                # Se valida que el chef no se salga de la pantalla por la parte superior 
                if nueva_fila < 0:

                        print("el chef no puede salir por la parte superior")

                # Se valida que el chef no se salga de la pantalla por la parte inferior
                elif nueva_fila >= 14:

                        print("el chef no puede salir por abajo")

                # Se valida que el chef no se salga de la pantalla por la parte izquierda
                elif nueva_columna < 0:

                        print("No puede salir por la izquierda")

                # Se valida que el chef no se salga de la pantalla por la parte derecha
                elif nueva_columna >= 20:

                        print("No puede salir por la derecha")

                else:

                        print("Posición válida")
#######
                # Se valida si la  nueva posición del chef está dentro de la matriz
                        if self.matriz_movimiento_americano[nueva_fila][nueva_columna] == 1:

                                # Si la tecla presionada es la flecha hacia arriba
                                if event.keysym == "Up":

                                        # Se mueve el chef hacia arriba
                                        self.chef.mover_arriba()

                                # Si la tecla presionada es la flecha hacia abajo
                                elif event.keysym == "Down":

                                        # Se mueve el chef hacia abajo
                                        self.chef.mover_abajo()

                                # Si la tecla presionada es la flecha hacia la izquierda
                                elif event.keysym == "Left":

                                        # Se mueve el chef hacia la izquierda
                                        self.chef.mover_izquierda()

                                # Si la tecla presionada es la flecha hacia la derecha
                                elif event.keysym == "Right":

                                        # Se mueve el chef hacia la derecha
                                        self.chef.mover_derecha()

                                # Se verifica si el chef está cargando un ingrediente
                                if self.ingrediente_en_mano != None:

                                        # Se mueve el ingrediente junto con el chef para simular que lo está cargando
                                        self.ingrediente_en_mano.mover_ingrediente_con_chef(self.chef)

                                
                        #Movimiento no válido
                        else: 
                                print ("Movimiento no válido")

##########################

        # Función que verifica si el chef está ubicado en una cocina (le permitirá cocinar los ingredientes)
        
        def esta_en_cocina(self):

                # Se obtiene la fila actual del chef activo
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef activo
                columna = self.chef.chef_ejex // 50

                print("Fila:", fila, "Columna:", columna)

                # Se recorre todas las cocinas almacenadas en la lista (almacenadas en la función "Pantalla_Restaurante_Americano")
                for cocina in self.cocinas:

                        # Verifica si la posición del chef coincide con una cocina
                        if fila == cocina.fila and columna == cocina.columna:

                                # Retorna True porque sí está en una cocina
                                return True

                # Si no coincide con la posición de ninguna cocina retorna False
                return False
        
##########################
        # Función que permite cocinar los ingredientes al presionar la tecla "s"
        def usar_cocina_americano(self, event):

                # Se valida si el chef está al frente de una cocina
                if self.esta_en_cocina():

                        # Cocina el ingrediente que tiene en la mano (carne)
                        self.cocinar_ingrediente()

                else:

                        # Si no está en cocina, no cocina nada
                        print("No está en una cocina")

##########################

        # Función que verifica si el chef está en una tabla de picar
        def esta_en_tabla_picar(self):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Muestra la posición actual del chef
                print("Fila:", fila, "Columna:", columna)

                # Recorre todas las posiciones de las tablas de picar
                for tabla in self.tablas_picar:

                        # Se verifica si la posición del chef coincide con una tabla de picar
                        if fila == tabla.fila and columna == tabla.columna:

                                return True

                # Si no coincide con ninguna tabla
                return False

##########################

        # Función que se ejecuta cuando el jugador presiona D
        def usar_tabla_picar_americano(self, event):

                # Verifica si el chef está en una tabla de picar
                if self.esta_en_tabla_picar():

                        # Llama a la función que pica el ingrediente
                        self.picar_ingrediente()

                else:

                        # Si no está en una tabla, no puede picar
                        print("No está en una tabla de picar")

########################## 

        # Función que permite picar el ingrediente que tiene el chef
        def picar_ingrediente(self):

                # Verifica si el chef tiene un ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        print("No tienes ingrediente para picar")

                        return 

                
                # Si el ingrediente ya está picado, no se vuelve a picar
                if self.ingrediente_en_mano.estado_ingrediente == "picado":

                                print("El ingrediente ya está picado")

                                return
# #####                        
                # Se verifica si el ingrediente puede picarse
                if self.ingrediente_en_mano.nombre_ingrediente not in [

                                                                                "Lechuga",
                                                                                "Tomate",
                                                                                "Cebolla",
                                                                                "Zanahoria",
                                                                                "Remolacha",
                                                                                "Calabaza",
                                                                                "Papa",
                                                                                "Queso",
                                                                                "Pan",
                                                                                "Hongo"

                                                                                ]:

                        print("Este ingrediente no se puede picar")

                        return

                # Se cambia el estado del ingrediente a picado
                self.ingrediente_en_mano.estado_ingrediente = "picado"

#######
                # Se Cambia la imagen según el ingrediente picado

                if self.ingrediente_en_mano.nombre_ingrediente == "Lechuga":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("lechuga_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Papa":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("papa_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Hongo":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("hongo_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Zanahoria":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("zanahoria_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Tomate":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("tomate_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Queso":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("queso_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Cebolla":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("cebolla_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Remolacha":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("remolacha_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Calabaza":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("calabaza_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Pan":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pan_picado.png")



                # Muestra mensaje de confirmación
                print(self.ingrediente_en_mano.nombre_ingrediente, "picado")

                # Muestra el nuevo estado
                print("Estado:", self.ingrediente_en_mano.estado_ingrediente)                       

##########################
        # Función que verifica si el chef está ubicado en una freidora
        def esta_en_freidora(self):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Muestra la posición actual del chef
                print("Fila:", fila, "Columna:", columna)

                # Recorre todas las posiciones donde existe una freidora
                for freidora in self.freidoras:

                        # Verifica si la posición actual coincide con una freidora
                        if fila == freidora.fila and columna == freidora.columna:

                                return True

                # Si no coincide con ninguna freidora
                return False


##########################

        # Función que se ejecuta cuando el jugador presiona la tecla F
        def usar_freidora_americano(self, event):

                # Verifica si el chef está ubicado en una freidora
                if self.esta_en_freidora():

                        # Llama a la función que fríe el ingrediente
                        self.freir_ingrediente()

                else:

                        # Se le informa al jugador que no está en una freidora
                        print("No está en una freidora")

##########################

        # Función que permite freír ingredientes en el restaurante americano
        def freir_ingrediente(self):

                # Verifica si el chef tiene un ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        # Se le notifica al jugador que no tiene ingredientes
                        print("No tienes ingrediente para freír")

                        return

                # Verifica si el ingrediente ya fue freído anteriormente
                if self.ingrediente_en_mano.estado_ingrediente == "frito":

                        # Se le informa al jugador que el ingrediente ya está listo
                        print("El ingrediente ya está frito")

                        return

                # Se verifica si el ingrediente puede freírse
                if self.ingrediente_en_mano.nombre_ingrediente not in [

                                                                        "Papa",
                                                                        "Pescado",
                                                                        "Camaron", 
                                                                        "Carne"

                                                                ]:

                        # Se le informa al jugador que ese ingrediente no puede freírse
                        print("Este ingrediente no se puede freír")

                        # El ingrediente desaparece si este no puede freirse
                        self.ingrediente_en_mano.soltar_ingrediente()

                        # Se libera la mano del chef (tras eliminar el ingrediente que no puede freirse las manos del chef quedan libre)
                        self.ingrediente_en_mano = None

                        return

                # Se cambia el estado del ingrediente a frito
                self.ingrediente_en_mano.estado_ingrediente = "frito"

                # Se cambia la imagen según el ingrediente que se está friendo
                if self.ingrediente_en_mano.nombre_ingrediente == "Papa":

                        # Se cambia la imagen de la papa cruda a papa frita
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("papa_frita.png")

                # Se cambia la imagen del pescado crudo a pescado frito
                elif self.ingrediente_en_mano.nombre_ingrediente == "Pescado":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pescado_frito.png")

                # Se cambia la imagen de la carne cruda a carne frita
                elif self.ingrediente_en_mano.nombre_ingrediente == "Carne":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("carne_frita.png")

                # Se cambia la imagen del camaron crudo a camaron frito
                elif self.ingrediente_en_mano.nombre_ingrediente == "Camaron":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("camaron_frito.png")

                # Muestra un mensaje indicando qué ingrediente fue freído
                print(self.ingrediente_en_mano.nombre_ingrediente, "frito")

                # Muestra el nuevo estado del ingrediente
                print("Estado:", self.ingrediente_en_mano.estado_ingrediente)

##########################

        # Función que permite cocinar el ingrediente (proteina) que tiene el chef
        def cocinar_ingrediente(self):

                # Verifica si el chef tiene un ingrediente seleccionado
                if self.ingrediente_en_mano == None:

                        print("No tienes ingrediente para cocinar")

                else:

                        # Se valida si el ingrediente que tiene el chef es una proteína para cocinarlo 
                        if self.ingrediente_en_mano.nombre_ingrediente in [
                                                                                "Carne",
                                                                                "Camaron",
                                                                                "Pescado",
                                                                                "Jamon"
                                                                        ]:

                                # Si ya está cocinado no vuelve a cocinarse
                                if self.ingrediente_en_mano.estado_ingrediente == "cocinado":

                                        print("La proteína ya está cocinada")

                                        return

                                # Se cambia el estado del ingrediente
                                self.ingrediente_en_mano.estado_ingrediente = "cocinado"

                                # Se cambia la imagen de la carne cruda por la carne cocida
                                if self.ingrediente_en_mano.nombre_ingrediente == "Carne":

                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("carne_cocida.png")

                                # Se cambia la imagen del camarón cruda por el camarón cocido
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Camaron":

                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("camaron_cocido.png")

                                # Se cambia la imagen del pescado crudo por el pescado cocido 
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Pescado":

                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pescado_cocido.png")

                                # Se cambia la imagen del jamón crudo por el jamón cocido
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Jamon":

                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("jamon_cocido.png")

                                # Mensaje indicando que la proteína fue cocinada
                                print(
                                        self.ingrediente_en_mano.nombre_ingrediente,"cocinado")

                                # Muestra el estado actual
                                print("Estado:",self.ingrediente_en_mano.estado_ingrediente)

                        # Si no es una proteína se elimina de la mano del chef
                        else:

                                # Mensaje indicando que el ingrediente no puede cocinarse
                                print("Este ingrediente no se puede cocinar")

                                # El ingrediente desaparece de la mano del chef
                                self.ingrediente_en_mano.soltar_ingrediente()

                                # Se libera la mano del chef
                                self.ingrediente_en_mano = None

##########################

        # Función que determina qué ingrediente debe tomar el chef
        def escoger_ingrediente_americano(self, event):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Se guarda la posición actual del chef
                posicion_chef = (fila, columna)

                # Si el chef tiene un ingrediente en la mano lo cambia por el nuevo
                if self.ingrediente_en_mano != None:

                        # Se elimina el ingrediente actual
                        self.ingrediente_en_mano.soltar_ingrediente()

                        # Libera la mano del chef
                        self.ingrediente_en_mano = None

                # Diccionario con las posiciones donde el chef puede tomar ingredientes
                estantes_ingredientes = {

                        # Carne
                        (3, 4): self.carne,
                        #(3, 5): self.carne,

                        # Remolacha
                        (4, 4): self.remolacha,
                        #(4, 5): self.remolacha,

                        # Hongo
                        (5, 4): self.hongo,
                        (5, 5): self.hongo,

                        # Calabaza
                        (6, 4): self.calabaza,
                        (6, 5): self.calabaza,

                        # Zanahoria
                        (7, 4): self.zanahoria,
                        (7, 5): self.zanahoria,

                        # Papa
                        (8, 4): self.papa,
                        (8, 5): self.papa,

                        # Tomate
                        #(3, 15): self.tomate,
                        (3, 16): self.tomate,

                        # Mayonesa
                        #(4, 15): self.mayonesa,
                        (4, 16): self.mayonesa,

                        # Queso
                        (5, 15): self.queso,
                        (5, 16): self.queso,

                        # lentejas
                        (6, 15): self.lentejas,
                        (6, 16): self.lentejas,

                        # cebolla
                        (7, 15): self.cebolla,
                        (7, 16): self.cebolla,

                        # aceituna
                        (8, 15): self.aceituna,
                        (8, 16): self.aceituna,


                }
#######
             
                # Se verifica si la posición actual del chef está en algún estante
                if posicion_chef in estantes_ingredientes:

                        # Obtiene el ingrediente según la posición del chef
                        ingrediente = estantes_ingredientes[posicion_chef]

                        # Se agrega un estado "crudo" cada vez que el chef tome un ingrediente (evita que el estado de la carne quede "cocido" cuando usa la cocina)
                        ingrediente.estado_ingrediente = "crudo"

                        # Al regrear al estánte se cambia la imagen de la carne cocida por la carne cruda 
                        if ingrediente.nombre_ingrediente == "Carne":

                                ingrediente.imagen_ingrediente_cocinado("carne.png")

                        # Si se vuelve a tomar la remolacha, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Remolacha":

                                ingrediente.imagen_ingrediente_cocinado("remolacha.png")
                        
                        elif ingrediente.nombre_ingrediente == "Calabaza":

                                ingrediente.imagen_ingrediente_cocinado("calabaza.png")

                          # Si se vuelve a tomar el hongo, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Hongo":

                                ingrediente.imagen_ingrediente_cocinado("hongo.png")

                        # Si se vuelve a tomar la zanahoria, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Zanahoria":

                                ingrediente.imagen_ingrediente_cocinado("zanahoria.png")

                        # Si vuelve a tomar la papa, se restaura la imagen original (luego de freirla o cocinarla)
                        elif ingrediente.nombre_ingrediente == "Papa":

                                ingrediente.imagen_ingrediente_cocinado("papa.png")

                        # Si se vuelve a tomar el tomate, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Tomate":

                                ingrediente.imagen_ingrediente_cocinado("tomate.png")

                        # Si se vuelve a tomar la mayonesa, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Mayonesa":

                                ingrediente.imagen_ingrediente_cocinado("mayonesa.png")
                        
                        # Si se vuelve a tomar el queso, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Queso":

                                ingrediente.imagen_ingrediente_cocinado("queso.png")

                        # Si se vuelve a tomar la lenteja, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Lentejas":

                                ingrediente.imagen_ingrediente_cocinado("lentejas.png")

                        # Si se vuelve a tomar la cebolla, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Cebolla":

                                ingrediente.imagen_ingrediente_cocinado("cebolla.png")        

                        # Si se vuelve a tomar la aceituna, se restaura la imagen original
                        elif ingrediente.nombre_ingrediente == "Aceituna":

                                ingrediente.imagen_ingrediente_cocinado("aceituna.png")

                        # Si vuelve a tomar el pescado, se restaura la imagen original (luego de freirla o cocinarla)
                        elif ingrediente.nombre_ingrediente == "Pescado":

                                ingrediente.imagen_ingrediente_cocinado("pescado.png")

                        # Si vuelve a tomar camarón, se restaura la imagen original (luego de freirla o cocinarla)
                        elif ingrediente.nombre_ingrediente == "Camaron":

                                ingrediente.imagen_ingrediente_cocinado("camaron.png")

#######

                        # Coloca el ingrediente sobre el chef
                        ingrediente.tomar_ingrediente(self.chef)

                        # Guarda el ingrediente actual
                        self.ingrediente_en_mano = ingrediente

                        # Muestra cuál ingrediente tomó
                        print(ingrediente.nombre_ingrediente, "tomado")

                else:

                        print("No hay ingrediente para tomar")

##########################################

        #Función que permite cambiar entre los dos chefs 
        def cambiar_chef(self, event):

                #Si se tiene seleccionado el chef #1 se cambia por el chef #2
                if self.chef == self.chef1:

                        self.chef = self.chef2
                        print("Chef 2 seleccionado")

                else:
                        #Si se tiene seleccionado el chef #2 se cambia por el chef #1
                        self.chef = self.chef1
                        print("Chef 1 seleccionado")
                
                # Devuelve el foco a la ventana para seguir usando las flechas

                self.ventana_restaurante.focus_force()
                                

##########################################

#Función generada con ChatGPT 
        # Referencia: OpenAI. (2026). ChatGPT (5.5,2026). Recuperado de https:// chatgpt.com
     
# Función que dibuja una cuadrícula sobre la cocina para ubicar los espacios que puede o no caminar el chef 
        def dibujar_cuadricula(self):

                # Se define el tamaño que tendrá cada cuadro de la matriz (define si el chef se puede mover o no en el mapa)
                tamaño_celda = 50

                # Se dibuja líneas verticales sobre la pantalla de la cocina 
                for ejex in range(0, 1000, tamaño_celda):
                        self.canvas.create_line(
                                                        ejex, #Posición inical en el eje X
                                                        0, #Posición inicial en el eje Y
                                                        ejex, #Posición final en el eje X
                                                        700, # Posición final en el eje y (el valor es el del acho de la pantalla del restaurante) 
                                                        fill="white")

                # Se dibuja líneas horizontales sobre la pantalla de la cocina 
                for ejey in range(0, 700, tamaño_celda):
                          self.canvas.create_line(
                                                        0, #Posición inical en el eje X
                                                        ejey, #Posición inicial en el eje Y
                                                        1000, # #Posición final en el eje X (el valor en el largo de la pantalla del restaurante)
                                                        ejey,# Posición final en el eje y
                                                        fill="white"
                                                        )

#######################################################################################

#Clase que contiene la funcionalidad del restaurante Europe 
class Pantalla_Restaurante_Europeo:

        def __init__(self, ventana_mapa, nombre_jugador, puntaje_inicial):

                self.ventana_mapa = ventana_mapa

                # Se guarda el nombre del jugador actual
                self.nombre_jugador = nombre_jugador

                 # Se recibe el puntaje acumulado del restaurante americano
                self.puntaje_jugador = puntaje_inicial

                # Se inicializa el puntaje del jugador en cero
                #self.puntaje_jugador = 0

                # Se obtiene la carpeta donde está la imagen de la cocicna Europea 
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se crea la ventana secundaria donde estará el restaurante Europeo
                self.ventana_restaurante = Toplevel(ventana_mapa)

                # Se coloca el título de la ventana
                self.ventana_restaurante.title("Restaurante Europeo")

                # Se define el tamaño de la ventana
                self.ventana_restaurante.geometry("1000x700+350+70")

                # Se evita que el usuario cambie el tamaño de la ventana 
                self.ventana_restaurante.resizable(False, False)

                # Se crea el canvas donde ira la imagen del restaurante americano 
                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")

                # Se coloca el canvas en la ventana
                self.canvas.pack()

                # Se define la ruta de la imagen de cocina
                ruta_cocina_europea = os.path.join(self.BASE_DIR, "Imagenes", "Cocina2.png")

                # Se abre la imagen de cocina
                imagen_cocina_europea = Image.open(ruta_cocina_europea)

                # Se ajusta el tamaño de la imagen del restaurante 
                imagen_cocina_europea = imagen_cocina_europea.resize((1000, 700))

                # Se convierte la imagen para tkinter
                self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_europea)

                # Se coloca la imagen de fondo en el canvas
                self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

#######
                # Tiempo inicial de la receta en segundos
                self.tiempo_restante = 60

                # Texto que muestra el temporizador en pantalla
                self.texto_temporizador = self.canvas.create_text(
                                                                        500, # Posición del reloj en el eje x
                                                                        70, #Posición del reloj en el eje y
                                                                        text="01:00", # Formato en el que se visualizará el reloj 
                                                                        fill="yellow", # Color del reloj 
                                                                        font=("Arial", 15, "bold")
                                                                )

                # Inicia la cuenta regresiva del restaurante europeo
                self.actualizar_temporizador_europeo()
#######
                # Ruta de la imagen que se mostrará cuando la receta sea incorrecta
                ruta_carne_quemada = os.path.join(self.BASE_DIR, "Imagenes", "quemado.png")

                # Se abre la imagen de carne quemada
                imagen_carne_quemada = Image.open(ruta_carne_quemada)

                # Se ajusta el tamaño de la imagen de la carne quemada 
                imagen_carne_quemada = imagen_carne_quemada.resize((100, 100))

                # Se convierte la imagen en un formato que Tkinter pueda usar 
                self.imagen_carne_quemada_tk = ImageTk.PhotoImage(imagen_carne_quemada)
#######

                                # Se crea un texto en el canvas para mostrar el nombre del jugador
                self.texto_nombre_jugador = self.canvas.create_text(

                                                                        350, # Posición del nombre del jugador en el eje X

                                                                        30, # Posición del nombre del jugador en el eje Y

                                                                        text="Jugador: " + self.nombre_jugador, # Texto que se mostrará en pantalla

                                                                        fill="white", # Color de las letras

                                                                        font=("Arial", 14, "bold") # Tipo de letra, tamaño y estilo
                                                                )

                # Se crea un texto en el canvas para mostrar el puntaje actual del jugador
                self.texto_puntaje_jugador = self.canvas.create_text(

                                                                        600, # Posición del puntaje del jugador en el eje X

                                                                        30, # Posición del puntaje del jugador en el eje Y

                                                                        text="Puntaje: " + str(self.puntaje_jugador), # Texto que se mostrará en pantalla

                                                                        fill="white", # Color de las letras

                                                                        font=("Arial", 14, "bold") # Tipo de letra, tamaño y estilo
                                                                )

                # Creación de matriz para el restaurante europeo
                self.matriz_movimiento_europeo = [

                                                        # Fila 0
                                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

                                                        # Fila 1
                                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

                                                        # Fila 2
                                                        [0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,0,0],

                                                        # Fila 3
                                                        [0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0],

                                                        # Fila 4
                                                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0],

                                                        # Fila 5
                                                        [0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0],

                                                        # Fila 6
                                                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],

                                                        # Fila 7
                                                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],

                                                        # Fila 8
                                                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],

                                                        # Fila 9
                                                        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],

                                                        # Fila 10
                                                        [0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],

                                                        # Fila 11
                                                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0],

                                                        # Fila 12
                                                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],

                                                        # Fila 13
                                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                                                        ]

                #Se dibuja la cuadrícula sobre la imagen de la cocina europea 
                #self.dibujar_cuadricula()

                # Se crea el primer chef
                self.chef1 = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 350, 350)

                # Se crea el segundo chef
                self.chef2 = Chef2(self.canvas, self.BASE_DIR, "Jugador 2", 400, 350)

                # Se coloca como chef activo el chef #1
                self.chef = self.chef1

                # Se inicializa el número de la orden actual
                self.numero_orden = 1

                # Cantidad máxima de órdenes permitidas en este restaurante
                self.maximo_ordenes = 3

                # Se genera la receta inicial del restaurante europeo
                self.receta_actual = self.generar_receta_europeo()

                # Se llama a la función  muestra la orden (receta) en pantalla
                self.mostrar_orden_europeo()

                # Lista donde se almacenan los ingredientes entregados por el jugador
                self.ingredientes_entregados = []

####### 
                # Etiquetas de los ingredientes del estante izquierdo

                self.canvas.create_text(170, 140, text="Carne", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(160, 190, text="Tomate", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(150, 240, text="Lechuga", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(140, 290, text="Queso cubos", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(130, 345, text="Pan", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(120, 395, text="Papa", fill="white", font=("Arial", 8, "bold"))

#######   
                # Etiquetas  de los ingredientes del estante derecho

                self.canvas.create_text(810, 345, text="Camarones", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(810, 395, text="Jamón", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(833, 490, text="Albahaca", fill="white", font=("Arial", 8, "bold"))

                self.canvas.create_text(833, 540, text="Pescado", fill="white", font=("Arial", 8, "bold"))



#######         
#               # Ruta de la imagen del botón para cambiar chef
                ruta_boton_cambiar = os.path.join(
                                                        self.BASE_DIR,
                                                        "Imagenes",
                                                        "boton_cambiar_chef.png"
                                                )

                # Se abre la imagen del botón
                imagen_boton_cambiar = Image.open(ruta_boton_cambiar)

                # Se ajusta el tamaño del botón
                imagen_boton_cambiar = imagen_boton_cambiar.resize((140, 140))

                # Se convierte la imagen para Tkinter
                self.imagen_boton_cambiar_tk = ImageTk.PhotoImage(imagen_boton_cambiar)

                # Se coloca la imagen en el canvas
                self.boton_cambiar_chef = self.canvas.create_image(
                                                                        100,
                                                                        550,
                                                                        image=self.imagen_boton_cambiar_tk
                                                                )

                # Se detecta el clic sobre la imagen
                self.canvas.tag_bind(
                                        self.boton_cambiar_chef, # Imagen que funcionará como botón
                                        "<Button-1>", #Cambia el chef al presionar clic izquiero 
                                        self.cambiar_chef # Se llama a la función que cambia el chef 
                                )           


#######
                # Se guarda el ingrediente que el chef está sosteniendo actualmente
                self.ingrediente_en_mano = None

#######
                # Lista que almacena las posiciones donde el chef puede cocinar en el restaurante europeo
                self.cocinas = [

                                # Cocina izquierda superior
                                Cocina(3, 7),
                                Cocina(4, 7),

                                # Cocina izquierda inferior
                                Cocina(8, 4),
                                Cocina(8, 5),
                                Cocina(8, 6),
                                Cocina(8, 7),

                                Cocina(9, 4),
                                Cocina(9, 5),
                                Cocina(9, 6),
                                Cocina(9, 7),

                                Cocina(10, 3),
                                Cocina(10, 4),
                                Cocina(10, 7),
                                Cocina(10, 8),

                                # Cocina superior derecha
                                Cocina(2, 13)
                                ]
                
#######
                # Lista que almacena las posiciones donde el chef puede picar en el restaurante europeo
                self.tablas_picar = [

                                        # Tabla de picar izquierda
                                        tabla_Picar(6, 5),
                                        tabla_Picar(6, 6),

                                        # Tabla de picar derecha
                                        tabla_Picar(9, 15)
                                ]
                
#######
                # Lista que almacena las posiciones donde el chef puede usar la freidora
                self.freidoras = [

                                         # Posición frente a la freidora
                                        Freidora(5, 15),

                                        # Posición izquierda frente a la freidora
                                        Freidora(6, 14),

                                        # Posición derecha frente a la freidora
                                        Freidora(6, 15)

                                ]            

#######
                # Lista vacía donde se guardarán los ingredientes entregados para la orden actual
                self.ingredientes_entregados = []

                # Lista que almacena las posiciones válidas de la estación de entrega europea
                self.estaciones_entrega = [

                        # Posición válida frente a la estación de entrega
                        (9, 14),

                        # Posición válida frente a la estación de entrega
                        (9, 15),

                        # Posición válida frente a la estación de entrega
                        (10, 14),

                        # Posición válida frente a la estación de entrega
                        (10, 15),

                         # Posición válida frente a la estación de entrega
                        (11, 13),

                        # Posición válida frente a la estación de entrega
                        (11, 15),

                        # Posición válida frente a la estación de entrega
                        (11, 16)
                ]
                
#######
                # Se crea el ingrediente papa del restaurante europeo
                self.papa = ingredientes_restaurante_americano(
                                                                self.canvas,
                                                                self.BASE_DIR,
                                                                "Papa",
                                                                "papa.png"
                                                        )
                
                # Se crea el ingrediente pan del restaurante europeo
                self.pan = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Pan",
                                                                        "pan.png"
                                                                )
                
                # Se crea el ingrediente queso en cubos del restaurante europeo
                self.queso_cubos = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Queso_cubo",
                                                                        "queso_cubos.png"
                                                                )
                
                # Se crea el ingrediente lechuga del restaurante europeo
                self.lechuga = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "lechuga",
                                                                        "lechuga.png"
                                                                )
                
                # Se crea el ingrediente tomate del restaurante europeo
                self.tomate = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Tomate",
                                                                        "tomate.png"
                                                                )
                
                # Se crea el ingrediente carne del restaurante europeo
                self.carne = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Carne",
                                                                        "carne.png"
                                                                )
                
                 # Se crea el ingrediente carne del restaurante europeo
                self.camaron = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Camaron",
                                                                        "camaron.png"
                                                                )
                
                 # Se crea el ingrediente jamon del restaurante europeo
                self.jamon = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Jamon",
                                                                        "jamon.png"
                                                                )
                
                # Se crea el ingrediente albahaca del restaurante europeo
                self.albahaca = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Albahaca",
                                                                        "albahaca.png"
                                                                )
                # Se crea el ingrediente albahaca del restaurante europeo
                self.pescado = ingredientes_restaurante_americano(
                                                                        self.canvas,
                                                                        self.BASE_DIR,
                                                                        "Pescado",
                                                                        "pescado.png"
                                                                )

                # Detecta cuando el jugador presiona la tecla "A" para tomar ingredientes
                self.ventana_restaurante.bind("a", self.escoger_ingrediente_europeo)

                # Detecta cuando el jugador presiona la tecla "S" para cocinar proteínas
                self.ventana_restaurante.bind("s", self.usar_cocina_europeo)

                # Detecta cuando el jugador presiona la tecla "D" para picar ingredientes
                self.ventana_restaurante.bind("d", self.usar_tabla_picar_europeo)

                # Detecta cuando el jugador presiona la tecla "F" para freír ingredientes
                self.ventana_restaurante.bind("f", self.usar_freidora_europeo)

                # Detecta cuando el jugador presiona la tecla E para entregar un ingrediente
                self.ventana_restaurante.bind("e", self.entregar_ingrediente_europeo)



#######
                # Permite que el chef se mueva en el restaurante con solo presionar las teclas (sin dar clic)
                self.ventana_restaurante.focus_force()

                # Se identifica cual es la tecla presionada por el usuario 
                self.ventana_restaurante.bind("<Key>", self.mover_chef)

##########################################
#                       
        # Función que determina cual tecla se presionó el jugador para mover el chef
        def mover_chef(self, event):

                # Se obtiene la fila actual del chef
                fila_actual = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna_actual = self.chef.chef_ejex // 50

                # Se crea una variable temporal para saber hacia que fila se esta moviendose el chef
                nueva_fila = fila_actual

                # Se crea una variable temporal para saber hacia que columna se esta moviendose el chef
                nueva_columna = columna_actual

#######         #Se controla el desplazamiento del chef al subir, bajar, derecha o izquierda 

                 # Flecha arriba
                if event.keysym == "Up":

                        #si el chef esta en al fila 2 y quiere subir se le resta 1 a la fila (-1) actual y queda en la fila 1
                        nueva_fila = fila_actual - 1

                # Flecha abajo
                elif event.keysym == "Down":

                        #Si el chef esta en la fila 2 y quiere bajar se le debe sumar 1 a la fila actual y queda en la fila 3
                        nueva_fila = fila_actual + 1

                # Flecha izquierda
                elif event.keysym == "Left":

                        #Si el chef esta en la columna 4 y se mueve a la izquierda se le resta 1 a la posición actual y queda en la columna 3
                        nueva_columna = columna_actual - 1

                # Flecha derecha
                elif event.keysym == "Right":

                        ##Si el chef esta en la columna 4 y se mueve a la derecha se le suma 1 a la posición actual para pasar a la columnna 5
                        nueva_columna = columna_actual + 1

#######         #Se define los límites de la pantalla donde se puede mover el chef 

                # Se valida que el chef no se salga de la pantalla por la parte superior 
                if nueva_fila < 0:

                        print("el chef no puede salir por la parte superior")

                # Se valida que el chef no se salga de la pantalla por la parte inferior
                elif nueva_fila >= 14:

                        print("el chef no puede salir por abajo")

                # Se valida que el chef no se salga de la pantalla por la parte izquierda
                elif nueva_columna < 0:

                        print("No puede salir por la izquierda")

                # Se valida que el chef no se salga de la pantalla por la parte derecha
                elif nueva_columna >= 20:

                        print("No puede salir por la derecha")

                else:

                        print("Posición válida")

###########
                        print("Intentando ir a:",nueva_fila,nueva_columna,"Valor:",self.matriz_movimiento_europeo[nueva_fila][nueva_columna])
###########

                # Se valida si la  nueva posición del chef está dentro de la matriz
                        if self.matriz_movimiento_europeo[nueva_fila][nueva_columna] == 1:

                                # Si la tecla presionada es la flecha hacia arriba
                                if event.keysym == "Up":

                                        # Se mueve el chef hacia arriba
                                        self.chef.mover_arriba()

                                # Si la tecla presionada es la flecha hacia abajo
                                elif event.keysym == "Down":

                                        # Se mueve el chef hacia abajo
                                        self.chef.mover_abajo()

                                # Si la tecla presionada es la flecha hacia la izquierda
                                elif event.keysym == "Left":

                                        # Se mueve el chef hacia la izquierda
                                        self.chef.mover_izquierda()

                                # Si la tecla presionada es la flecha hacia la derecha
                                elif event.keysym == "Right":

                                        # Se mueve el chef hacia la derecha
                                        self.chef.mover_derecha()

####### 

                                # Se verifica si el chef está cargando un ingrediente
                                if self.ingrediente_en_mano != None:

                                        # Se mueve el ingrediente junto con el chef
                                        self.ingrediente_en_mano.mover_ingrediente_con_chef(self.chef)
        
                                
                        #Movimiento no válido
                        else: 
                                print ("Movimiento no válido")


##########################################
        # Función que genera una receta aleatoria para el restaurante europeo
        def generar_receta_europeo(self):

                # Lista de ingredientes que pueden ir fritos en el restaurante europeo
                ingredientes_fritos = ["Papa", "Pescado", "Camaron", "Carne"]

                # Lista de ingredientes que pueden ir picados en el restaurante europeo
                ingredientes_picados = ["Papa", "Pan", "Queso_cubo", "lechuga", "Tomate", "Albahaca"]

                # Lista de ingredientes que pueden ir cocinados en el restaurante europeo
                ingredientes_cocinados = ["Carne", "Camaron", "Pescado", "Jamon"]

                # Lista de ingredientes que pueden entregarse crudos en el restaurante europeo
                ingredientes_crudos = ["Pan", "Queso_cubo", "lechuga", "Tomate", "Albahaca"]

                # Se escoge un ingrediente frito aleatorio
                ingrediente_frito = random.choice(ingredientes_fritos)

                # Se escoge un ingrediente picado aleatorio
                ingrediente_picado = random.choice(ingredientes_picados)

                # Se escoge un ingrediente cocinado aleatorio
                ingrediente_cocinado = random.choice(ingredientes_cocinados)

                # Se escoge un ingrediente crudo aleatorio
                ingrediente_crudo = random.choice(ingredientes_crudos)

                # Se crea la lista de ingredientes de la receta europea
                lista_ingredientes = [

                        # Ingrediente que debe entregarse frito
                        Ingrediente_Receta(ingrediente_frito, "frito(a)"),

                        # Ingrediente que debe entregarse picado
                        Ingrediente_Receta(ingrediente_picado, "picado(a)"),

                        # Ingrediente que debe entregarse cocinado
                        Ingrediente_Receta(ingrediente_cocinado, "cocinado(a)"),

                        # Ingrediente que debe entregarse crudo
                        Ingrediente_Receta(ingrediente_crudo, "crudo(a)")
                ]

                # Se crea la receta europea con puntos y tiempo máximo
                receta = Receta(lista_ingredientes, 50, 50)

                # Se muestra la receta en consola para probar
                receta.mostrar_receta()

                # Se retorna la receta creada
                return receta
        
##########################################   
     
        # Función que muestra la orden que debe preparar el chef en la pantalla
        def mostrar_orden_europeo(self):

                # Se crea un rectángulo de fondo para mostrar la orden
                self.canvas.create_rectangle(

                                                820, # Posición inicial X

                                                10, # Posición inicial Y

                                                995, # Posición final X

                                                150, # Posición final Y

                                                fill="#3B2416", # Color café oscuro

                                                outline="#D2B48C", # Color del borde

                                                width=4 # Grosor del borde
                                        )

                # Se crea un texto con el encabezado de la orden
                self.canvas.create_text(

                                                900, # Posición del texto en X

                                                25, # Posición del texto en Y

                                                text="ORDEN # " + str(self.numero_orden),

                                                fill="white",

                                                font=("Arial", 10, "bold")
                                        )

                # Se crea un texto con los ingredientes solicitados
                self.canvas.create_text(

                        910, # Posición de los ingredientes en X

                        85, # Posición de los ingredientes en Y

                        text=

                        self.receta_actual.lista_ingredientes[0].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[0].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[1].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[1].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[2].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[2].estado_requerido + "\n" +

                        self.receta_actual.lista_ingredientes[3].nombre_ingrediente + " - " +
                        self.receta_actual.lista_ingredientes[3].estado_requerido,

                        fill="white",

                        font=("Arial", 10, "bold")
                )
##########################################

        # Función que verifica si el chef está ubicado en una cocina
        def esta_en_cocina(self):

                # Se obtiene la fila actual del chef activo
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef activo
                columna = self.chef.chef_ejex // 50

                print("Fila:", fila, "Columna:", columna)

                # Se recorren todas las cocinas almacenadas en la lista
                for cocina in self.cocinas:

                        # Verifica si la posición del chef coincide con una cocina
                        if fila == cocina.fila and columna == cocina.columna:

                                return True

                return False

##########################################

        # Función que permite cocinar al presionar S
        def usar_cocina_europeo(self, event):

                # Verifica si el chef está en una cocina
                if self.esta_en_cocina():

                        self.cocinar_ingrediente()

                else:

                        print("No está en una cocina")

##########################################
        
        # Función que permite cocinar el ingrediente de la cocina europea que tiene el chef (solo proteinas)
        def cocinar_ingrediente(self):

                # Verifica si el chef tiene un ingrediente seleccionado
                if self.ingrediente_en_mano == None:

                        print("No tienes ingrediente para cocinar")

                else:

                        # Se verifica si el ingrediente es una proteína
                        if self.ingrediente_en_mano.nombre_ingrediente in [
                                                                                "Carne",
                                                                                "Camaron",
                                                                                "Pescado",
                                                                                "Jamon"
                                                                        ]:

                                # Si ya está cocinado no vuelve a cocinarse el ingrediente
                                if self.ingrediente_en_mano.estado_ingrediente == "cocinado":

                                        print("La proteína ya está cocinada")
                                        return

                                # Se cambia el estado del ingrediente de "crudo" a "cocinado"
                                self.ingrediente_en_mano.estado_ingrediente = "cocinado"

                                # Se Cambia la imagen de la carne cruda a carne cocinada 
                                if self.ingrediente_en_mano.nombre_ingrediente == "Carne":
                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("carne_cocida.png")

                                # Se Cambia la imagen del camarón crudo a camarón cocinado
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Camaron":
                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("camaron_cocido.png")

                                # Se Cambia la imagen del pescado crudo a pescado cocinado
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Pescado":
                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pescado_cocido.png")

                                # Se Cambia la imagen del jamón crudo a jamón cocinado
                                elif self.ingrediente_en_mano.nombre_ingrediente == "Jamon":
                                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("jamon_cocido.png")

                                print(self.ingrediente_en_mano.nombre_ingrediente, "cocinado")
                                print("Estado:", self.ingrediente_en_mano.estado_ingrediente)

                        else:
                                #Se le notifica al jugador que trato de cocinar un ingrediente que no es una proteina 
                                print("Este ingrediente no se puede cocinar")

                                #Cómo se cocino un ingrediente que no es proteina "se quemo" y por eso se le quita de las manos al chef
                                self.ingrediente_en_mano.soltar_ingrediente()

                                #Se actualiza el estado del ingrediente del chef a none tras cocinarlo no siendo una proteina 
                                self.ingrediente_en_mano = None

##########################################

        # Función que permite entregar un ingrediente en la estación de entrega europea
        def entregar_ingrediente_europeo(self, event):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Se verifica si el chef está en una posición válida de entrega
                if (fila, columna) not in self.estaciones_entrega:

                        # Se muestra un mensaje si no está en la estación de entrega
                        print("No estás en la estación de entrega europea")

                        # Se detiene la función
                        return

                # Se verifica si el chef no tiene ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        # Se muestra un mensaje si no lleva ingrediente
                        print("No tienes ingrediente para entregar")

                        # Se detiene la función
                        return

                # Se crea una copia del ingrediente entregado
                ingrediente_entregado = Ingrediente_Receta(

                        # Se guarda el nombre del ingrediente que el chef tiene en la mano
                        self.ingrediente_en_mano.nombre_ingrediente,

                        # Se guarda el estado actual del ingrediente con el formato que usa la receta
                        self.ingrediente_en_mano.estado_ingrediente + "(a)"
                )

                # Se guarda la copia del ingrediente entregado
                self.ingredientes_entregados.append(ingrediente_entregado)

                # Se muestra en consola el ingrediente entregado
                print(
                        "Ingrediente entregado:",
                        ingrediente_entregado.nombre_ingrediente,
                        "-",
                        ingrediente_entregado.estado_requerido
                )

                # Se elimina la imagen del ingrediente de la mano del chef
                self.ingrediente_en_mano.soltar_ingrediente()

                # Se limpia la mano del chef
                self.ingrediente_en_mano = None

                # Se muestra cuántos ingredientes se han entregado
                print("Ingredientes entregados:", len(self.ingredientes_entregados))

                # Se verifica si ya se entregó la misma cantidad de ingredientes que pide la receta
                if len(self.ingredientes_entregados) == len(self.receta_actual.lista_ingredientes):

                        # Se muestra un mensaje para indicar que ya se puede validar la receta completa
                        print("Validando receta europea...")

                        # Se guarda el resultado de comparar la receta actual con los ingredientes entregados
                        receta_correcta = self.receta_actual.comparar_receta(self.ingredientes_entregados)

                        # Se verifica si la receta fue correcta
                        if receta_correcta == True:

                                # Se muestra que la receta fue correcta
                                print("Receta europea correcta")

                                # Se calculan los puntos ganados según el tiempo restante
                                puntos_ganados = self.tiempo_restante

                                # Se suman los puntos al puntaje total
                                self.puntaje_jugador += puntos_ganados

                                # Se actualiza el texto del puntaje
                                self.canvas.itemconfig(
                                                        self.texto_puntaje_jugador,
                                                        text="Puntaje: " + str(self.puntaje_jugador)
                                                )

                                # Se muestra en consola cuántos puntos ganó
                                print("Puntos ganados en restaurante europeo:", puntos_ganados)

                                # Se limpian los ingredientes entregados para iniciar una nueva orden
                                self.ingredientes_entregados = []

                                # Se reinicia el tiempo para la nueva orden europea
                                self.tiempo_restante = 60
                                
                                # Se genera una nueva orden europea
                                self.generar_nueva_orden_europeo()

                        # Si la receta entregada no coincide con la receta solicitada
                        else:

                                # Se muestra que la receta fue incorrecta
                                print("Receta europea incorrecta")

                                # Se elimina la imagen de receta incorrecta si existe
                                if hasattr(self, "imagen_error"):

                                        self.canvas.delete(self.imagen_error)
                                        
                                # Se muestra la imagen de carne quemada
                                self.imagen_error = self.canvas.create_image(
                                                                                500,
                                                                                120,
                                                                                image=self.imagen_carne_quemada_tk
                                                                        )
                                # El mensaje de receta incorrecta desaparece después de 3 segundos
                                self.ventana_restaurante.after(3000,self.ocultar_mensaje_error)

                                # Reinicia el temporizador
                                self.tiempo_restante = 60

                                # Actualiza el reloj en pantalla
                                self.canvas.itemconfig(
                                                        self.texto_temporizador,
                                                        text="01:00"
                                                )
                                                
                                # Se limpian los ingredientes entregados para intentar otra vez
                                self.ingredientes_entregados = []

                                # Se devuelve el foco a la ventana del restaurante
                                self.ventana_restaurante.focus_force()
                
                # Si todavía no se han entregado todos los ingredientes, no se valida la receta
                else:

                        # Se muestra que todavía faltan ingredientes
                        print("Todavía faltan ingredientes para validar la receta")

##########################################
        # Función que guarda el nombre y puntaje del jugador
        def guardar_resultado(self):

                # Se crea automáticamente el archivo TXT que almacenará el nombre y puntaje 
                        # la letra "a" es un append para almacenar los diferentes jugadores y sus puntajes 
                archivo = open("puntajes.txt", "a")

                # Se guarda nombre,puntaje
                archivo.write(
                                self.nombre_jugador +
                                "," +
                                str(self.puntaje_jugador) +
                                "\n"
                        )

                # Se cierra el archivo
                archivo.close()
##########################################
        # Función que genera la siguiente receta europea
        def generar_nueva_orden_europeo(self):

                # Se verifica si todavía quedan órdenes por generar
                if self.numero_orden < self.maximo_ordenes:
                
                        # Se aumenta el número consecutivo de la orden
                        self.numero_orden += 1

                        # Se genera una nueva receta europea aleatoria
                        self.receta_actual = self.generar_receta_europeo()

                        # Se muestra la nueva orden europea en pantalla
                        self.mostrar_orden_europeo()

                # Si ya se completaron las 3 órdenes
                else:

                        print("Todas las órdenes americanas fueron completadas")

                        # Se llama a la función anterior "guardar_resulado" que guarda el nombre y puntaje de cada jugador 
                        self.guardar_resultado()

                        # Muestra un mensaje emergente
                        messagebox.showinfo(
                                "Restaurante Europeo",
                                "¡FELICIDADES!\nCompletaste las 3 recetas correctamente")

                        # Cierra la cocina europea
                        self.ventana_restaurante.destroy()

                        # Vuelve a mostrar el mapa
                        self.ventana_mapa.deiconify()

                
##########################################
        # Función que verifica si el chef está en una tabla de picar
        def esta_en_tabla_picar(self):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Muestra la posición actual del chef
                print("Fila:", fila, "Columna:", columna)

                # Recorre todas las posiciones de las tablas de picar
                for tabla in self.tablas_picar:

                        # Se verifica si la posición del chef coincide con una tabla de picar
                        if fila == tabla.fila and columna == tabla.columna:

                                return True

                # Si no coincide con ninguna ubicación de tabla de picar 
                return False

##########################################

        # Función que se ejecuta la funcionalidad de picar cuando el jugador presiona D
        def usar_tabla_picar_europeo(self, event):

                # Verifica si el chef está en una tabla de picar
                if self.esta_en_tabla_picar():

                        # Llama a la función que pica el ingrediente
                        self.picar_ingrediente_europeo()

                else:

                        # Si no está en una tabla, no puede picar
                        print("No está en una tabla de picar")

##########################################

        # Función que permite picar el ingrediente que tiene el chef en el restaurante europeo
        def picar_ingrediente_europeo(self):

                # Verifica si el chef tiene un ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        print("No tienes ingrediente para picar")

                        return

                # Si el ingrediente ya está picado, no se vuelve a picar
                if self.ingrediente_en_mano.estado_ingrediente == "picado":

                        print("El ingrediente ya está picado")

                        return

                # Se verifica si el ingrediente puede picarse
                if self.ingrediente_en_mano.nombre_ingrediente not in [

                                                                                "Papa",
                                                                                "Pan",
                                                                                "Queso_cubo",
                                                                                "lechuga",
                                                                                "Tomate",
                                                                                "Albahaca"

                                                                        ]:

                        print("Este ingrediente no se puede picar")

                        return

                # Se cambia el estado del ingrediente a picado
                self.ingrediente_en_mano.estado_ingrediente = "picado"

                # Se cambia la imagen según el ingrediente picado
                if self.ingrediente_en_mano.nombre_ingrediente == "Papa":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("papa_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Pan":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pan_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Queso_cubo":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("queso_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "lechuga":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("lechuga_picada.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Tomate":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("tomate_picado.png")

                elif self.ingrediente_en_mano.nombre_ingrediente == "Albahaca":

                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("albahaca_picada.png")

                # Muestra mensaje de confirmación
                print(self.ingrediente_en_mano.nombre_ingrediente, "picado")

                # Muestra el nuevo estado
                print("Estado:", self.ingrediente_en_mano.estado_ingrediente)

##########################################
        # Función que se ejecuta cuando el jugador presiona la tecla F
        def usar_freidora_europeo(self, event):

                # Verifica si el chef está frente a una freidora 
                if self.esta_en_freidora(): 
                        # se fríe el ingrediente que tiene el chef
                        self.freir_ingrediente_europeo()
                
                else:
                        print("El chef No está frente a una freidora")
##########################################

        # Función que verifica si el chef está frente a una freidora

        def esta_en_freidora(self):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Se recorre todas las posiciones válidas de freidora
                for freidora in self.freidoras:

                        # Si coincide la posición del chef con una freidora
                        if fila == freidora.fila and columna == freidora.columna:

                                return True

                # Si no está frente a ninguna freidora
                return False 

##########################################
        # Función que permite freír ingredientes en el restaurante europeo
        def freir_ingrediente_europeo(self):

                # Se verifica si el chef tiene un ingrediente en la mano
                if self.ingrediente_en_mano == None:

                        print("El chef no tiene ingrediente para freír")

                        return

                # Verifica si el ingrediente ya fue freído anteriormente
                if self.ingrediente_en_mano.estado_ingrediente == "frito":

                        print("El ingrediente ya está frito")

                        return

                # Se verifica si el ingrediente es uno de los que pueden freírse
                if self.ingrediente_en_mano.nombre_ingrediente not in [

                                                                        "Papa",
                                                                        "Pescado",
                                                                        "Camaron",
                                                                        "Jamon",
                                                                        "Carne"

                                                                        ]:

                        print("Ingrediente quemado")

                        self.ingrediente_en_mano.soltar_ingrediente()

                        self.ingrediente_en_mano = None

                        return

                # Se cambia el estado del ingrediente a frito
                self.ingrediente_en_mano.estado_ingrediente = "frito"

                # Se cambia la imagen de la papa cruda a papa frita
                if self.ingrediente_en_mano.nombre_ingrediente == "Papa":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("papa_frita.png")

                # Se cambia la imagen de la carne cruda a carne frita
                elif self.ingrediente_en_mano.nombre_ingrediente == "Carne":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("carne_frita.png")


                # Se cambia la imagen del pescado crudo a pescado frito
                elif self.ingrediente_en_mano.nombre_ingrediente == "Pescado":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("pescado_frito.png")

                # Se cambia la imagen del camarón crudo a camarón frito
                elif self.ingrediente_en_mano.nombre_ingrediente == "Camaron":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("camaron_frito.png")

                # Se cambia la imagen del jamón crudo a jamón frito
                elif self.ingrediente_en_mano.nombre_ingrediente == "Jamon":
                        self.ingrediente_en_mano.imagen_ingrediente_cocinado("jamon_frito.png")

                print(self.ingrediente_en_mano.nombre_ingrediente, "frito")

                print("Estado:", self.ingrediente_en_mano.estado_ingrediente)


##########################################
        # Función que elimina la imagen de receta incorrecta
        def ocultar_mensaje_error(self):

                # Verifica que exista la imagen
                if hasattr(self, "imagen_error"):

                        # Elimina la imagen
                        self.canvas.delete(self.imagen_error)
##########################################

        #Función que permite el cambio de chef en el restaurante 
        def cambiar_chef(self, event):

                if self.chef == self.chef1:

                        #Se intercambia el chef #1 por el chef #2
                        self.chef = self.chef2
                        print("Chef 2 seleccionado")

                else:
                        #Si lo que esta seleccionado es el chef #2 se asigna el chef#1
                        self.chef = self.chef1
                        print("Chef 1 seleccionado")

                self.ventana_restaurante.focus_force()

##########################################
        # Función que permite tomar ingredientes en el restaurante europeo
        def escoger_ingrediente_europeo(self, event):

                # Se obtiene la fila actual del chef
                fila = self.chef.chef_ejey // 50

                # Se obtiene la columna actual del chef
                columna = self.chef.chef_ejex // 50

                # Se guarda la posición actual del chef
                posicion_chef = (fila, columna)

                # Si el chef ya tiene un ingrediente, primero lo suelta
                if self.ingrediente_en_mano != None:

                        # Elimina el ingrediente actual
                        self.ingrediente_en_mano.soltar_ingrediente()

                        # Se deja la mano vacía
                        self.ingrediente_en_mano = None


                # Diccionario con las posiciones donde el chef puede tomar ingredientes
                estantes_ingredientes = {

                        # Papa
                        (8, 3): self.papa,
                        (8, 4): self.papa,

                        # Pan
                        (7, 3): self.pan,
                        (7, 4): self.pan,

                        # Queso_cubos
                        (6, 3): self.queso_cubos,
                        (6, 4): self.queso_cubos,

                        # lechuga
                        (5, 3): self.lechuga,
                        (5, 4): self.lechuga,

                        # tomate
                        (4, 3): self.tomate,
                        (4, 4): self.tomate,

                        # carne
                        (3, 3): self.carne,
                        (3, 4): self.carne,

                        # camaron
                        (7, 15): self.camaron,
                        (7, 16): self.camaron,

                        # jamon
                        (8, 15): self.jamon,
                        (8, 16): self.jamon,

                        # albahaca
                        (10, 15): self.albahaca,
                        (10, 16): self.albahaca,

                        #Pescado 
                        (11, 15): self.pescado,
                        (11, 16): self.pescado,



                }

                # Se verifica si el chef está en una posición con ingrediente
                if posicion_chef in estantes_ingredientes:

                        # Obtiene el ingrediente según la posición del chef
                        ingrediente = estantes_ingredientes[posicion_chef]

                        # Cada vez que se toma un ingrediente del estante vuelve a estar crudo
                        ingrediente.estado_ingrediente = "crudo"

                        #Al regresar al estante se actualiza la imagen de la carne cocida a carne cruda 
                        if ingrediente.nombre_ingrediente == "Carne":

                                ingrediente.imagen_ingrediente_cocinado("carne.png")

                        # Al regresar al estante se actualiza la imagen de la papa picada a papa cruda
                        elif ingrediente.nombre_ingrediente == "Papa":

                                ingrediente.imagen_ingrediente_cocinado("papa.png")

                        # Al regresar al estante se actualiza la imagen del pan picado a pan normal
                        elif ingrediente.nombre_ingrediente == "Pan":

                                ingrediente.imagen_ingrediente_cocinado("pan.png")

                        # Al regresar al estante se actualiza la imagen del queso picado a queso normal
                        elif ingrediente.nombre_ingrediente == "Queso_cubo":

                                ingrediente.imagen_ingrediente_cocinado("queso_cubos.png")

                        # Al regresar al estante se actualiza la imagen de la lechuga picada a lechuga normal
                        elif ingrediente.nombre_ingrediente == "lechuga":

                                ingrediente.imagen_ingrediente_cocinado("lechuga.png")

                        # Al regresar al estante se actualiza la imagen del tomate picado a tomate normal
                        elif ingrediente.nombre_ingrediente == "Tomate":

                                ingrediente.imagen_ingrediente_cocinado("tomate.png")
                        
                        # Al regresar al estante se actualiza la imagen de la albahaca picada a albahaca normal
                        elif ingrediente.nombre_ingrediente == "Albahaca":

                                ingrediente.imagen_ingrediente_cocinado("albahaca.png")

                        #Al regresar al estante se actualiza la imagen del camarón cocida a camarón crudo
                        elif ingrediente.nombre_ingrediente == "Camaron":

                                ingrediente.imagen_ingrediente_cocinado("camaron.png")

                        #Al regresar al estante se actualiza la imagen del pescado cocida al pescado crudo
                        elif ingrediente.nombre_ingrediente == "Pescado":

                                ingrediente.imagen_ingrediente_cocinado("pescado.png")

                        #Al regresar al estante se actualiza la imagen del jamón cocido al jamón crudo
                        elif ingrediente.nombre_ingrediente == "Jamon":

                                ingrediente.imagen_ingrediente_cocinado("jamon.png")

                        # Coloca el ingrediente sobre el chef
                        ingrediente.tomar_ingrediente(self.chef)

                        # Guarda el ingrediente actual
                        self.ingrediente_en_mano = ingrediente

                        # Muestra cuál ingrediente tomó
                        print(ingrediente.nombre_ingrediente, "tomado")

                else:

                        print("No hay ingrediente para tomar")
                               

##########################################
        # Función que actualiza el temporizador del restaurante europeo
        def actualizar_temporizador_europeo(self):

                # Se calculan los minutos restantes
                minutos = self.tiempo_restante // 60

                # Se calculan los segundos restantes
                segundos = self.tiempo_restante % 60

                # Se actualiza el texto del temporizador
                self.canvas.itemconfig(
                                        self.texto_temporizador,
                                        text=f"{minutos:02d}:{segundos:02d}"
                                )

                # Se verifica si todavía queda tiempo
                if self.tiempo_restante > 0:

                        # Se resta un segundo
                        self.tiempo_restante -= 1

                        # Se vuelve a ejecutar la función dentro de 1 segundo
                        self.ventana_restaurante.after(
                                                                1000,
                                                                self.actualizar_temporizador_europeo
                                                        )

                else:

                        # Se muestra que el tiempo terminó
                        print("Tiempo agotado en restaurante europeo")

                        # Se limpian los ingredientes entregados
                        self.ingredientes_entregados = []

                        # Se reinicia el tiempo
                        self.tiempo_restante = 60

                        # Se genera otra receta europea sin aumentar el número de orden
                        self.receta_actual = self.generar_receta_europeo()

                        # Se actualiza la orden en pantalla
                        self.mostrar_orden_europeo()

                        # Se devuelve el foco a la ventana del restaurante
                        self.ventana_restaurante.focus_force()

                        # Se vuelve a asegurar que las teclas sigan funcionando
                        self.ventana_restaurante.bind("<Key>", self.mover_chef)

                        # Se vuelve a iniciar el temporizador
                        self.actualizar_temporizador_europeo()

##########################################

#Función generada con ChatGPT 
        # Referencia: OpenAI. (2026). ChatGPT (5.5,2026). Recuperado de https:// chatgpt.com
     
# Función que dibuja una cuadrícula sobre la cocina para ubicar los espacios que puede o no caminar el chef 
        def dibujar_cuadricula(self):

                # Se define el tamaño que tendrá cada cuadro de la matriz (define si el chef se puede mover o no en el mapa)
                tamaño_celda = 50

                # Se dibuja líneas verticales sobre la pantalla de la cocina 
                for ejex in range(0, 1000, tamaño_celda):
                        self.canvas.create_line(
                                                        ejex, #Posición inical en el eje X
                                                        0, #Posición inicial en el eje Y
                                                        ejex, #Posición final en el eje X
                                                        700, # Posición final en el eje y (el valor es el del acho de la pantalla del restaurante) 
                                                        fill="white")

                # Se dibuja líneas horizontales sobre la pantalla de la cocina 
                for ejey in range(0, 700, tamaño_celda):
                          self.canvas.create_line(
                                                        0, #Posición inical en el eje X
                                                        ejey, #Posición inicial en el eje Y
                                                        1000, # #Posición final en el eje X (el valor en el largo de la pantalla del restaurante)
                                                        ejey,# Posición final en el eje y
                                                        fill="white"
                                                        )

#######################################################################################


class Pantalla_Restaurante_Asiatico:
        def __init__(self, ventana_mapa, nombre_jugador):
                self.ventana_mapa = ventana_mapa
                self.nombre_jugador = nombre_jugador
                self.puntaje_jugador = 0  

                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                # Se crea la ventana para el restaurante Asiático
                self.ventana_restaurante = Toplevel(ventana_mapa)
                self.ventana_restaurante.title("Restaurante Asiático")
                self.ventana_restaurante.geometry("1000x700+350+70")
                self.ventana_restaurante.resizable(False, False)

                # Se crea el canvas
                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")
                self.canvas.pack()

                # Ruta de la imagen de fondo (Cocina Asiática)
                ruta_cocina_asiatica = os.path.join(self.BASE_DIR, "Imagenes", "Cocina3.png")
                try:
                        imagen_cocina_asiatica = Image.open(ruta_cocina_asiatica).resize((1000, 700))
                        self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_asiatica)
                        self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)
                except:
                        self.canvas.create_text(500, 350, text="[Fondo Cocina Asiática]", fill="white")

                # Tiempo inicial de la receta en segundos
                self.tiempo_restante = 300
                self.texto_temporizador = self.canvas.create_text(
                        500, 70, text="01:00", fill="yellow", font=("Arial", 15, "bold")
                )
                self.actualizar_temporizador_asiatico()

                # Textos de información en la interfaz
                self.texto_nombre_jugador = self.canvas.create_text(
                        350, 30, text="Jugador: " + self.nombre_jugador, fill="white", font=("Arial", 14, "bold")
                )
                self.texto_puntaje_jugador = self.canvas.create_text(
                        600, 30, text="Puntaje: " + str(self.puntaje_jugador), fill="white", font=("Arial", 14, "bold")
                )

                # =========================================================================
                # MATRIZ CORREGIDA: Sigue el mapa visual de las zonas blancas transitables.
                # Bloquea la mesa central pero deja pasillos libres alrededor (arriba, abajo, izquierda, derecha).
                # =========================================================================
                self.matriz_movimiento_asiatico = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], # Pasillo superior libre
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], # Mesa central bloqueada (columnas 4 a 9)
                        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], # Pasillos laterales libres
                        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], # Pasillo inferior libre
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
                ]

                # POSICIÓN INICIAL LÓGICA: Ubicados en el pasillo libre (Fila 4 y Fila 9 en Y, columnas libres en X)
                self.chef1 = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 500, 200) # En el pasillo libre superior
                self.chef2 = Chef2(self.canvas, self.BASE_DIR, "Jugador 2", 500, 450) # En el pasillo libre inferior
                self.chef = self.chef1

                # Botón de cambiar Chef
                ruta_boton_cambiar = os.path.join(self.BASE_DIR, "Imagenes", "boton_cambiar_chef.png")
                try:
                        imagen_boton_cambiar = Image.open(ruta_boton_cambiar).resize((140, 140))
                        self.imagen_boton_cambiar_tk = ImageTk.PhotoImage(imagen_boton_cambiar)
                        self.boton_cambiar_chef = self.canvas.create_image(100, 550, image=self.imagen_boton_cambiar_tk)
                        self.canvas.tag_bind(self.boton_cambiar_chef, "<Button-1>", self.cambiar_chef)
                except:
                        pass

                self.ingrediente_en_mano = None

                # Estaciones de Trabajo
                self.cocinas = [Cocina(2, 13), Cocina(2, 14), Cocina(9, 13)]
                self.tablas_picar = [tabla_Picar(2, 5), tabla_Picar(10, 16)]
                self.freidoras = [Freidora(9, 3), Freidora(8, 3)]
                self.estaciones_entrega = [(10, 6), (10, 7), (11, 6), (11, 7)]
                self.ingredientes_entregados = []

                # Carga segura de ingredientes
                def cargar_ingrediente_seguro(nombre, archivo):
                        try:
                                return ingredientes_restaurante_americano(self.canvas, self.BASE_DIR, nombre, archivo)
                        except:
                                print(f"⚠️ Alerta: No se encontró la imagen '{archivo}' para '{nombre}'.")
                                return None

                # Instanciar ingredientes
                self.arroz = cargar_ingrediente_seguro("Arroz", "arroz.png")
                self.lechuga_china = cargar_ingrediente_seguro("Lechuga China", "lechuga_china.png")
                self.pescado = cargar_ingrediente_seguro("Pescado", "pescado.png")
                self.ajies = cargar_ingrediente_seguro("Ajies", "ajies.png")
                self.hongo_asiatico = cargar_ingrediente_seguro("Hongo", "hongo.png")
                self.huevos = cargar_ingrediente_seguro("Huevos", "huevos.png")

                self.carne_asiatica = cargar_ingrediente_seguro("Carne", "carne.png")
                self.cebollin = cargar_ingrediente_seguro("Cebollin", "cebollin.png")
                self.fideos = cargar_ingrediente_seguro("Fideos", "fideos.png")
                self.salsa_soja = cargar_ingrediente_seguro("Salsa Soja", "salsa_soja.png")
                self.tofu = cargar_ingrediente_seguro("Tofu", "tofu.png")
                self.algas = cargar_ingrediente_seguro("Algas", "algas.png")

                # Controles del teclado
                self.ventana_restaurante.bind("a", self.escoger_ingrediente_asiatico)
                self.ventana_restaurante.bind("s", self.usar_cocina_asiatico)
                self.ventana_restaurante.bind("d", self.usar_tabla_picar_asiatico)
                self.ventana_restaurante.bind("f", self.usar_freidora_asiatico)
                self.ventana_restaurante.bind("e", self.entregar_ingrediente_asiatico)

                self.ventana_restaurante.bind("<Up>", self.mover_chef)
                self.ventana_restaurante.bind("<Down>", self.mover_chef)
                self.ventana_restaurante.bind("<Left>", self.mover_chef)
                self.ventana_restaurante.bind("<Right>", self.mover_chef)

              
                # --- SISTEMA DE RECETAS CON PROCESAMIENTO DETALLADO ---
                # Cada ingrediente tiene asignado el estado final requerido: "Crudo", "Picado", "Frito" o "Cocinado"
                self.recetas_asiaticas = {
                        "Sushi Especial": {
                                "Arroz": "Cocinado", 
                                "Pescado": "Picado", 
                                "Algas": "Crudo"
                        },
                        "Ramen de Carne": {
                                "Fideos": "Cocinado", 
                                "Carne": "Frito", 
                                "Huevos": "Cocinado", 
                                "Cebollin": "Picado"
                        },
                        "Salteado de Tofu": {
                                "Tofu": "Frito", 
                                "Lechuga China": "Picado", 
                                "Hongo": "Picado", 
                                "Salsa Soja": "Crudo"
                        },
                        "Arroz Frito Picante": {
                                "Arroz": "Cocinado", 
                                "Carne": "Frito", 
                                "Ajies": "Picado", 
                                "Huevos": "Frito"
                        }
                }
                
                # Seleccionar receta inicial
                self.receta_actual_nombre = random.choice(list(self.recetas_asiaticas.keys()))
                self.requisitos_receta = self.recetas_asiaticas[self.receta_actual_nombre]
                
                

                # Diccionario para rastrear el estado actual de lo que el jugador ya entregó en la mesa
                # Ejemplo: {"Arroz": "Crudo"} o {"Arroz": "Cocinado"}
                self.ingredientes_entregados = {} 

                # Cuadrito Visual de la Receta (Fondo y Texto) en la esquina superior izquierda (X: 20 a 280, Y: 20 a 160)
                self.rectangulo_hud = self.canvas.create_rectangle(20, 20, 280, 160, fill="#1c1c24", outline="cyan", width=2)
                self.texto_hud_titulo = self.canvas.create_text(150, 40, text=f"ORDEN: {self.receta_actual_nombre}", fill="yellow", font=("Arial", 11, "bold"))
                self.texto_hud_detalles = self.canvas.create_text(150, 100, text="", fill="white", font=("Arial", 9, "bold"), justify=LEFT)
                
                # Función interna para refrescar el cuadrito visual
                self.actualizar_cuadrito_receta()

                # --- NUEVO: Control de temporizador de Recetas ---
                self.tiempo_max_receta = 40        # Segundos para completar la orden
                self.tiempo_receta_actual = self.tiempo_max_receta
                self.puntos_receta_actual = 35     # Valor inicial
                self.receta_reducida = False       # Bandera para reducir solo una vez

                # Reloj dinámico dentro del cuadrito HUD (alineado abajo a X:150, Y:145)
                self.texto_reloj_receta = self.canvas.create_text(
                        150, 145, text=f"Tiempo Orden: {self.tiempo_receta_actual}s", 
                        font=("Arial", 10, "bold"), fill="orange"
                )
                
                # Arrancar el reloj de inmediato
                self.iniciar_reloj_receta_asiatica()

                # --- NUEVO: Control de temporizador de Recetas ---
                self.tiempo_max_receta = 40        # Segundos iniciales para la orden
                self.tiempo_receta_actual = self.tiempo_max_receta
                self.puntos_receta_actual = 35     # Valor base de la receta
                self.receta_reducida = False       # Bandera para reducir solo una vez

                # Texto visual en el Canvas para el reloj de la receta
                self.texto_reloj_receta = self.canvas.create_text(
                    150, 145, text=f"Tiempo Orden: {self.tiempo_receta_actual}s", 
                    font=("Arial", 10, "bold"), fill="orange"
                )
                
                # Activar el reloj inmediatamente al iniciar
                self.iniciar_reloj_receta_asiatica()

        # --- TEXTOS INDICADORES SOBRE LOS PUESTOS DE TRABAJO ---
                # Puestos de Cocina (Color Naranja)
                self.canvas.create_text(675, 125, text="COCINAR", fill="#ff7f27", font=("Arial", 9, "bold"))  # Cocina (2, 13)
                self.canvas.create_text(725, 125, text="COCINAR", fill="#ff7f27", font=("Arial", 9, "bold"))  # Cocina (2, 14)
                self.canvas.create_text(675, 475, text="COCINAR", fill="#ff7f27", font=("Arial", 9, "bold"))  # Cocina (9, 13)

                # Puestos de Tabla de Picar (Color Verde)
                self.canvas.create_text(275, 125, text="PICAR", fill="#22b14c", font=("Arial", 9, "bold"))   # Tabla (2, 5)
                self.canvas.create_text(825, 525, text="PICAR", fill="#22b14c", font=("Arial", 9, "bold"))   # Tabla (10, 16)

                # Puestos de Freidora (Color Amarillo)
                self.canvas.create_text(175, 425, text="FREÍR", fill="#fff200", font=("Arial", 9, "bold"))   # Freidora (8, 3)
                self.canvas.create_text(175, 475, text="FREÍR", fill="#fff200", font=("Arial", 9, "bold"))   # Freidora (9, 3)

                # Zona de Entrega / Mesa (Color Magenta/Rosado)
                self.canvas.create_text(325, 525, text="MESA", fill="#ec008c", font=("Arial", 9, "bold"))    # Entrega (10, 6)
                self.canvas.create_text(375, 525, text="MESA", fill="#ec008c", font=("Arial", 9, "bold"))    # Entrega (10, 7)

                # --- TEXTOS PARA LOS INGREDIENTES (ESTANTE IZQUIERDO) ---
                # Columna 1 o 2 en X (aprox pixel 75 o 100) para que quede justo sobre el estante
                self.canvas.create_text(80, 175, text="Arroz", fill="white", font=("Arial", 8, "bold"))          # Fila 3
                self.canvas.create_text(80, 225, text="Lechuga", fill="white", font=("Arial", 8, "bold"))        # Fila 4
                self.canvas.create_text(80, 275, text="Pescado", fill="white", font=("Arial", 8, "bold"))        # Fila 5
                self.canvas.create_text(80, 325, text="Ajíes", fill="white", font=("Arial", 8, "bold"))          # Fila 6
                self.canvas.create_text(80, 375, text="Champi", fill="white", font=("Arial", 8, "bold"))         # Fila 7
                self.canvas.create_text(80, 425, text="Huevo", fill="white", font=("Arial", 8, "bold"))          # Fila 8

                # --- TEXTOS PARA LOS INGREDIENTES (ESTANTE DERECHO) ---
                # Columna 18 o 19 en X (aprox pixel 925) para el extremo derecho
                self.canvas.create_text(925, 175, text="Carne", fill="white", font=("Arial", 8, "bold"))         # Fila 3
                self.canvas.create_text(925, 225, text="Cebollín", fill="white", font=("Arial", 8, "bold"))      # Fila 4
                self.canvas.create_text(925, 275, text="Fideos", fill="white", font=("Arial", 8, "bold"))        # Fila 5
                self.canvas.create_text(925, 325, text="S. Soja", fill="white", font=("Arial", 8, "bold"))       # Fila 6
                self.canvas.create_text(925, 375, text="Tofu", fill="white", font=("Arial", 8, "bold"))          # Fila 7
                self.canvas.create_text(925, 425, text="Algas", fill="white", font=("Arial", 8, "bold"))         # Fila 8

        def entregar_ingrediente_asiatico(self, event):
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                if (fila, columna) in self.estaciones_entrega:
                        if self.ingrediente_en_mano != None:
                                nombre_ing = self.ingrediente_en_mano.nombre_ingrediente
                                
                                # Si el ingrediente no pasó por máquina, asumimos que su estado es "Crudo"
                                estado_actual = getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo')

                                # --- NUEVA VALIDACIÓN: BLOQUEAR SI ESTÁ QUEMADO ---
                                if estado_actual == "Quemado":
                                        messagebox.showerror("Comida Quemada", "¡No puedes entregar ingredientes quemados! Llévalo al basurero.")
                                        return

                                if nombre_ing in self.requisitos_receta:
                                        estado_requerido = self.requisitos_receta[nombre_ing]
                                        
                                        # Validar si el estado de preparación es el correcto
                                        if estado_actual == estado_requerido:
                                                print(f"¡{nombre_ing} ({estado_actual}) entregado correctamente en la mesa!")
                                                self.ingredientes_entregados[nombre_ing] = estado_actual
                                                
                                                # El ingrediente se suelta y desaparece al ponerse en la mesa
                                                self.ingrediente_en_mano.soltar_ingrediente()
                                                self.ingrediente_en_mano = None
                                                
                                                # Actualizar HUD cuadrito
                                                self.actualizar_cuadrito_receta()
                                                
                                                # Validar si la receta entera está lista
                                                completada = True
                                                for ing, est in self.requisitos_receta.items():
                                                        if ing not in self.ingredientes_entregados or self.ingredientes_entregados[ing] != est:
                                                                completada = False
                                                                break
                                                
                                                if completada:
                                                        # CAMBIADO: Añade los puntos dinámicos acumulados del reloj
                                                        self.puntaje_jugador += self.puntos_receta_actual
                                                        self.canvas.itemconfig(self.texto_puntaje_jugador, text="Puntaje: " + str(self.puntaje_jugador))
                                                        messagebox.showinfo("¡Perfecto!", f"¡Receta Completada! Recibes +{self.puntos_receta_actual} PTS")
                                                        
                                                        # CAMBIADO: Reinicia el reloj de forma limpia y crea la nueva orden
                                                        self.forzar_nueva_receta_asiatica()
                                        else:
                                                messagebox.showwarning("Estado Incorrecto", f"El ingrediente {nombre_ing} está {estado_actual}, pero la receta lo pide {estado_requerido}.")
                                else:
                                        print(f"{nombre_ing} no se necesita en esta receta.")
                        else:
                                print("No tienes nada en la mano.")
                else:
                        print("No estás en la mesa de entrega.")

        def iniciar_reloj_receta_asiatica(self):
                def descontar_segundo():
                        if hasattr(self, 'tiempo_receta_actual') and self.tiempo_receta_actual > 0:
                                self.tiempo_receta_actual -= 1
                                
                                # Actualiza el reloj visible abajo en el HUD
                                self.canvas.itemconfig(self.texto_reloj_receta, text=f"Tiempo Orden: {self.tiempo_receta_actual}s")
                                
                                # REGLA: A la mitad del tiempo, los puntos bajan a la mitad
                                if self.tiempo_receta_actual == (self.tiempo_max_receta // 2) and not self.receta_reducida:
                                        self.puntos_receta_actual = self.puntos_receta_actual // 2
                                        self.receta_reducida = True
                                        messagebox.showwarning("¡Tiempo Crítico!", "La orden asiática se está retrasando. ¡Puntos reducidos a la mitad!")
                                
                                # REGLA: Si el tiempo llega a 0, expira y penaliza
                                if self.tiempo_receta_actual <= 0:
                                        messagebox.showerror("Orden Vencida", f"¡La orden expiró! Penalización: -{self.puntos_receta_actual} PTS")
                                        
                                        self.puntaje_jugador -= self.puntos_receta_actual
                                        if self.puntaje_jugador < 0: 
                                                self.puntaje_jugador = 0
                                        
                                        self.canvas.itemconfig(self.texto_puntaje_jugador, text="Puntaje: " + str(self.puntaje_jugador))
                                        self.forzar_nueva_receta_asiatica()
                                else:
                                        # Seguir el bucle cada 1 segundo
                                        self.id_after_receta = self.ventana_restaurante.after(1000, descontar_segundo)
                                        
                if hasattr(self, 'id_after_receta'):
                        self.ventana_restaurante.after_cancel(self.id_after_receta)
                        
                descontar_segundo()

        def forzar_nueva_receta_asiatica(self):
                # Reiniciar los valores del reloj HUD
                self.tiempo_receta_actual = self.tiempo_max_receta
                self.puntos_receta_actual = 35
                self.receta_reducida = False
                
                # Cambiar a la siguiente receta aleatoria
                self.ingredientes_entregados = {}
                self.receta_actual_nombre = random.choice(list(self.recetas_asiaticas.keys()))
                self.requisitos_receta = self.recetas_asiaticas[self.receta_actual_nombre]
                self.actualizar_cuadrito_receta()
                
                # Re-iniciar el temporizador para la nueva receta
                self.iniciar_reloj_receta_asiatica()

        def actualizar_cuadrito_receta(self):
                lineas = []
                for ing, estado_req in self.requisitos_receta.items():
                        # Si ya se entregó y tiene el estado correcto
                        if ing in self.ingredientes_entregados and self.ingredientes_entregados[ing] == estado_req:
                                lineas.append(f"✓ {ing}: {estado_req}")
                        else:
                                lineas.append(f"☐ {ing}: {estado_req}")
                
                texto_final = "\n".join(lineas)
                self.canvas.itemconfig(self.texto_hud_titulo, text=f"ORDEN: {self.receta_actual_nombre}")
                self.canvas.itemconfig(self.texto_hud_detalles, text=texto_final)

        def mover_chef(self, event):
                fila_actual = self.chef.chef_ejey // 50
                columna_actual = self.chef.chef_ejex // 50
                nueva_fila = fila_actual
                nueva_columna = columna_actual

                if event.keysym == "Up": nueva_fila = fila_actual - 1
                elif event.keysym == "Down": nueva_fila = fila_actual + 1 
                elif event.keysym == "Left": nueva_columna = columna_actual - 1
                elif event.keysym == "Right": nueva_columna = columna_actual + 1
                else: return

                if 0 <= nueva_fila < len(self.matriz_movimiento_asiatico) and 0 <= nueva_columna < len(self.matriz_movimiento_asiatico[0]):
                        if self.matriz_movimiento_asiatico[nueva_fila][nueva_columna] == 1:
                                if event.keysym == "Up": self.chef.mover_arriba()
                                elif event.keysym == "Down": self.chef.mover_abajo()
                                elif event.keysym == "Left": self.chef.mover_izquierda()
                                elif event.keysym == "Right": self.chef.mover_derecha()
                                
                                # Si lleva un ingrediente, mover el ingrediente y actualizar su etiqueta visual
                                if self.ingrediente_en_mano != None:
                                        self.ingrediente_en_mano.mover_ingrediente_con_chef(self.chef)
                                        
                                        # Borrar etiqueta de estado anterior si existe para que no se duplique
                                        if hasattr(self, 'texto_estado_ingrediente'):
                                                self.canvas.delete(self.texto_estado_ingrediente)
                                        
                                        # Si el ingrediente ya no está crudo, dibujamos su estado encima de la cabeza del chef
                                        estado = getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo')
                                        if estado != "Crudo":
                                                colores_estado = {"Picado": "#22b14c", "Frito": "#fff200", "Cocinado": "#ff7f27"}
                                                color = colores_estado.get(estado, "white")
                                                
                                                # Dibujar el estado flotando arriba del chef (ajustado a sus ejes X e Y)
                                                self.texto_estado_ingrediente = self.canvas.create_text(
                                                        self.chef.chef_ejex + 25, self.chef.chef_ejey - 15, 
                                                        text=f"[{estado.upper()}]", fill=color, font=("Arial", 8, "bold")
                                                )
                        else:
                                print("Movimiento bloqueado por obstáculo.")
                                
        def cambiar_chef(self, event):
                if self.chef == self.chef1: self.chef = self.chef2
                else: self.chef = self.chef1
                print("Cambiando de chef")

        def actualizar_temporizador_asiatico(self):
                if self.tiempo_restante > 0:
                        self.tiempo_restante -= 1
                        minutos = self.tiempo_restante // 60
                        segundos = self.tiempo_restante % 60
                        self.canvas.itemconfig(self.texto_temporizador, text=f"{minutos:02d}:{segundos:02d}")
                        self.ventana_restaurante.after(1000, self.actualizar_temporizador_asiatico)
                else:
                        messagebox.showinfo("Tiempo Agotado", "¡Se acabó el tiempo en la cocina asiática!")
                        self.ventana_restaurante.destroy()
                        self.ventana_mapa.deiconify()

        def escoger_ingrediente_asiatico(self, event):
                # Se obtiene la fila y columna actual del chef según la cuadrícula
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                # Si el chef ya tiene algo en la mano, primero lo suelta
                if self.ingrediente_en_mano != None:
                        self.ingrediente_en_mano.soltar_ingrediente()
                        self.ingrediente_en_mano = None

                # --- ESTANTE VERTICAL IZQUIERDO ---
                # Si el chef está pegado al extremo izquierdo de la cocina
                if columna <= 4:
                        if fila <= 3:
                                self.ingrediente_en_mano = self.arroz
                        elif fila == 4:
                                self.ingrediente_en_mano = self.lechuga_china
                        elif fila == 5:
                                self.ingrediente_en_mano = self.pescado
                        elif fila == 6:
                                self.ingrediente_en_mano = self.ajies
                        elif fila == 7:
                                self.ingrediente_en_mano = self.hongo_asiatico
                        elif fila >= 8:
                                self.ingrediente_en_mano = self.huevos

                # --- ESTANTE VERTICAL DERECHO ---
                # Si el chef está pegado al extremo derecho de la cocina
                elif columna >= 15:
                        if fila <= 3:
                                self.ingrediente_en_mano = self.carne_asiatica
                        elif fila == 4:
                                self.ingrediente_en_mano = self.cebollin
                        elif fila == 5:
                                self.ingrediente_en_mano = self.fideos
                        elif fila == 6:
                                self.ingrediente_en_mano = self.salsa_soja
                        elif fila == 7:
                                self.ingrediente_en_mano = self.tofu
                        elif fila >= 8:
                                self.ingrediente_en_mano = self.algas

                # Si se logró recolectar un ingrediente válido, se asigna al chef
                if self.ingrediente_en_mano != None:
                        self.ingrediente_en_mano.tomar_ingrediente(self.chef)
                        print("Recogiste con éxito:", self.ingrediente_en_mano.nombre_ingrediente)
                else:
                        print("No estás pegado a los estantes laterales. Fila:", fila, "Columna:", columna)

        def usar_cocina_asiatico(self, event):
                if self.ingrediente_en_mano != None:
                        print(f"Cocinando {self.ingrediente_en_mano.nombre_ingrediente}...")
                        # Aquí puedes cambiar el estado del ingrediente a 'cocinado' si tu clase ingrediente lo permite
                else:
                        print("No tienes ningún ingrediente en la mano para cocinar.")

        def iniciar_barra_progreso(self, x, y, duracion, callback):
                # Desactivar temporalmente los controles para que el chef no se mueva mientras procesa
                self.ventana_restaurante.unbind("<Up>")
                self.ventana_restaurante.unbind("<Down>")
                self.ventana_restaurante.unbind("<Left>")
                self.ventana_restaurante.unbind("<Right>")

                # Crear el fondo gris de la barra y el relleno verde
                fondo_barra = self.canvas.create_rectangle(x - 25, y - 40, x + 25, y - 32, fill="gray", outline="black")
                relleno_barra = self.canvas.create_rectangle(x - 25, y - 40, x - 25, y - 32, fill="#22b14c", outline="")

                pasos = 20
                tiempo_paso = int(duracion / pasos)

                def animar(paso_actual):
                        if paso_actual <= pasos:
                                # Calcular el nuevo ancho de la barra verde
                                ancho = (paso_actual / pasos) * 50
                                self.canvas.coords(relleno_barra, x - 25, y - 40, (x - 25) + ancho, y - 32)
                                self.ventana_restaurante.after(tiempo_paso, lambda: animar(paso_actual + 1))
                        else:
                                # Limpiar la barra del canvas al terminar
                                self.canvas.delete(fondo_barra)
                                self.canvas.delete(relleno_barra)
                                
                                # Reactivar los controles de movimiento
                                self.ventana_restaurante.bind("<Up>", self.mover_chef)
                                self.ventana_restaurante.bind("<Down>", self.mover_chef)
                                self.ventana_restaurante.bind("<Left>", self.mover_chef)
                                self.ventana_restaurante.bind("<Right>", self.mover_chef)
                                
                                # Ejecutar la acción final (cambiar estado del ingrediente)
                                callback()

                animar(1)

        def usar_tabla_picar_asiatico(self, event):
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                if (fila == 3 and columna == 5) or (fila == 9 and columna == 16) or (fila == 10 and columna == 16):
                        if self.ingrediente_en_mano != None:
                                if getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo') == "Crudo":
                                        def finalizar_picar():
                                                self.ingrediente_en_mano.estado_coccion = "Picado"
                                                messagebox.showinfo("Procesado", f"{self.ingrediente_en_mano.nombre_ingrediente} ahora está: PICADO")
                                        
                                        # Llama a la animación (2000 milisegundos = 2 segundos de carga)
                                        self.iniciar_barra_progreso(self.chef.chef_ejex + 25, self.chef.chef_ejey, 2000, finalizar_picar)
                                else:
                                        messagebox.showwarning("Atención", "Este ingrediente ya fue procesado.")
                        else:
                                messagebox.showwarning("Atención", "No tienes nada en la mano para picar.")
                else:
                        print("No estás frente a una Tabla de Picar.")

        def usar_freidora_asiatico(self, event):
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                if (fila == 8 and columna == 3) or (fila == 9 and columna == 3):
                        if self.ingrediente_en_mano != None:
                                if getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo') == "Crudo":
                                        def finalizar_freir():
                                                self.ingrediente_en_mano.estado_coccion = "Frito"
                                                messagebox.showinfo("Procesado", f"{self.ingrediente_en_mano.nombre_ingrediente} ahora está: FRITO")
                                        
                                        self.iniciar_barra_progreso(self.chef.chef_ejex + 25, self.chef.chef_ejey, 2000, finalizar_freir)
                                else:
                                        messagebox.showwarning("Atención", "Este ingrediente ya fue procesado.")
                        else:
                                messagebox.showwarning("Atención", "No tienes nada en la mano para freír.")
                else:
                        print("No estás frente a una Freidora.")

        def usar_cocina_asiatico(self, event):
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                if (fila == 3 and (columna == 13 or columna == 14)) or (fila == 8 and columna == 13):
                        if self.ingrediente_en_mano != None:
                                if getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo') == "Crudo":
                                        def finalizar_cocinar():
                                                self.ingrediente_en_mano.estado_coccion = "Cocinado"
                                                messagebox.showinfo("Procesado", f"{self.ingrediente_en_mano.nombre_ingrediente} ahora está: COCINADO")
                                        
                                        self.iniciar_barra_progreso(self.chef.chef_ejex + 25, self.chef.chef_ejey, 2000, finalizar_cocinar)
                                else:
                                        messagebox.showwarning("Atención", "Este ingrediente ya fue procesado.")
                        else:
                                messagebox.showwarning("Atención", "No tienes nada en la mano para cocinar.")
                else:
                        print("No estás frente a una Cocina.")

        def entregar_ingrediente_asiatico(self, event):
                fila = self.chef.chef_ejey // 50
                columna = self.chef.chef_ejex // 50

                if (fila, columna) in self.estaciones_entrega:
                        if self.ingrediente_en_mano != None:
                                nombre_ing = self.ingrediente_en_mano.nombre_ingrediente
                                
                                # Si el ingrediente no pasó por máquina, asumimos que su estado es "Crudo"
                                estado_actual = getattr(self.ingrediente_en_mano, 'estado_coccion', 'Crudo')

                                # --- NUEVA VALIDACIÓN: SI ESTÁ QUEMADO BLOQUEA LA ENTREGA ---
                                if estado_actual == "Quemado":
                                        messagebox.showerror("Comida Quemada", "¡No puedes entregar ingredientes quemados! Llévalo al basurero.")
                                        return

                                if nombre_ing in self.requisitos_receta:
                                        estado_requerido = self.requisitos_receta[nombre_ing]
                                        
                                        # Validar si el estado de preparación es el correcto
                                        if estado_actual == estado_requerido:
                                                print(f"¡{nombre_ing} ({estado_actual}) entregado correctamente en la mesa!")
                                                self.ingredientes_entregados[nombre_ing] = estado_actual
                                                
                                                # El ingrediente se suelta y desaparece al ponerse en la mesa
                                                self.ingrediente_en_mano.soltar_ingrediente()
                                                self.ingrediente_en_mano = None
                                                
                                                # Actualizar HUD cuadrito
                                                self.actualizar_cuadrito_receta()
                                                
                                                # Validar si la receta entera está lista
                                                completada = True
                                                for ing, est in self.requisitos_receta.items():
                                                        if ing not in self.ingredientes_entregados or self.ingredientes_entregados[ing] != est:
                                                                completada = False
                                                                break
                                                
                                                if completada:
                                                        # MODIFICADO: Suma el puntaje acumulado actual (dinámico por el tiempo)
                                                        self.puntaje_jugador += self.puntos_receta_actual
                                                        self.canvas.itemconfig(self.texto_puntaje_jugador, text="Puntaje: " + str(self.puntaje_jugador))
                                                        messagebox.showinfo("¡Perfecto!", f"¡Receta Completada con éxito! +{self.puntos_receta_actual} PTS")
                                                        
                                                        # MODIFICADO: Llama al limpiador y regenerador del reloj
                                                        self.forzar_nueva_receta_asiatica()
                                        else:
                                                messagebox.showwarning("Estado Incorrecto", f"El ingrediente {nombre_ing} está {estado_actual}, pero la receta lo pide {estado_requerido}.")
                                else:
                                        print(f"{nombre_ing} no se necesita en esta receta.")
                        else:
                                print("No tienes nada en la mano.")
                else:
                        print("No estás en la mesa de entrega.")
#######################################################################################
# Se crea el objeto de la clase para ejecutar el programa
principal = Pantalla_Principal()