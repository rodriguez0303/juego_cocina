#Importación de librerias 
from tkinter import *
import tkinter as tk
import os #Permite acceder a la ruta donde se encuentran las imagenes 
from PIL import Image, ImageTk  #Pillow permite para cargar imágenes JPG

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
                                                                550,# Posición del botón en el eje Y
                                                                image=self.imagen_boton_jugar_tk # Imagen que tendrá el botón
                                                        )
        #######
                # Evento que permite hacer click sobre la imagen del botón jugar 
                self.canvas.tag_bind(
                                        self.boton_jugar,# Imagen que funcionará como botón
                                        "<Button-1>", #Permite acceder al juego dando clic izquierdo 
                                        self.iniciar_juego # Se llama a la función que inicializa el juego 


                                )
                
#######################################################################################
  # Mantiene la ventana abierta
                self.ventana.mainloop()

#######################################################################################
        # Función que destruye la pantalla principal para luego mostrar la pantalla de juegos 
        def iniciar_juego(self, event):

         # Se oculta la pantalla principal
                self.ventana.withdraw()

        # Se abre la ventana de mapas del juego 
                self.pantalla_mapa = Pantalla_mapa(self.ventana)

#######################################################################################

# Clase que crea la ventana principal del juego
class Pantalla_mapa:

    def __init__(self, ventana_principal):

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

#######################################################################################
    # Esta función que inicializa el juego al presionar el botón Play
    def iniciar_juego(self, event):
            
            # Se oculta la pantalla principal sin destruirla
                # Esto permite que la ventana siga existiendo en memoria
            self.ventana.withdraw()

            self.pantalla_mapa = Pantalla_mapa(self.ventana)

#######################################################################################
# Se crea el objeto de la clase para ejecutar el programa
principal = Pantalla_Principal()