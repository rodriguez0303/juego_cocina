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
        ################        
        #######
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
                self.pantalla_americano = Pantalla_Restaurante_Americano(self.ventana_juego)

#######                                
        # Funcion que abre el mapa de juego del restaurante Europeo
        def abrir_europeo(self, event):

                # Se oculta la ventana del mapa
                self.ventana_juego.withdraw()

                # Se abre la ventana del restaurante americano
                self.pantalla_europeo = Pantalla_Restaurante_Europeo(self.ventana_juego)


#######
        # Funcion que abre el mapa de juego del restaurante Asiatico
        def abrir_asiatico(self, event):

               # Se oculta la ventana del mapa
                self.ventana_juego.withdraw()

                # Se abre la ventana del restaurante asiático
                self.pantalla_asiatico = Pantalla_Restaurante_Asiatico(self.ventana_juego)

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
# Clase asociada a la funcionaldiades del chef dentro del restaurante
class Chef:

    def __init__(self, canvas, base_dir,nombre):

        #Guarda el canvas donde se dibujará el chef
        self.canvas = canvas
        
        #Obtiene la ruta donde se encuentra las imagenes del chef 
        self.BASE_DIR = base_dir
        
        #Se guarda el nombre del jugador 
        self.nombre = nombre

        #Guarda el puntaje del jugador inicialmente esta en 0
        self.puntos = 0

        # Define la posición inicial del chef en el eje X
        self.chef_ejex = 500

        # Define la posición inicial del chef en el ejeY
        self.chef_ejey = 350

        # Cantidad de pixeles que se moverá el chef cada vez que se presione la tecla de dirección 
        self.distancia = 15

########
        # Ruta de la imagen del chef viendo hacia abajo
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
        # Ruta de la imagen del chef viendo hacia arriba
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
        # Ruta de la imagen del chef viendo hacia la izquierda
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

    # Función que permite mover el chef hacia arriba
    def mover_arriba(self):

         # Se coloca la imagen del chef de espalda 
        self.canvas.itemconfig(self.chef_canvas,image=self.imagen_arriba_tk)

        # Resta a Y para subir (obtiene la posición actual del chef en el mapa)
        self.chef_ejey = self.chef_ejey - self.distancia

        # Se mueve la imagen del chef
        self.canvas.move(self.chef_canvas, 0, -self.distancia) #chef, desplazamiento en ejex, desplazamiento en ejey

#######
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

#######
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

#######
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
        

#######################################################################################


#Clase que contiene la funcionalidad del restaurante americano 
class Pantalla_Restaurante_Americano:

    def __init__(self, ventana_mapa):

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
         # Se crea el objeto chef dentro del restaurante americano
        self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1")

        # Permite que la ventana del restaurante detecte las teclas
        self.ventana_restaurante.focus_force()

        # Detecta cuando el usuario presiona cualquier tecla de dirección 
        self.ventana_restaurante.bind("<Key>", self.mover_chef)

#########################################

   # Función que determina cual tecla se presionó el jugador para mover el chef
    def mover_chef(self, event):

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



#######################################################################################

#Clase que contiene la funcionalidad del restaurante Europe 
class Pantalla_Restaurante_Europeo:

        def __init__(self, ventana_mapa):

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
                # Se crea el objeto chef dentro del restaurante europeo
                self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1")

                # Permite que el chef se mueva en el restaurante con solo presionar las teclas (sin dar clic)
                self.ventana_restaurante.focus_force()

                # Se identifica cual es la tecla presionada por el usuario 
                self.ventana_restaurante.bind("<Key>", self.mover_chef)
                        
        # Función que determina cuál tecla se presionó para mover el chef
        def mover_chef(self, event):

                # si se presiona la tecla de arriba se mueve el chef haci arriba 
                if event.keysym == "Up":
                        self.chef.mover_arriba()

                # si se presiona la tecla de abajao se mueve el chef hacia abajo
                elif event.keysym == "Down":
                        self.chef.mover_abajo()

                # si se presiona la tecla la izquierda se mueve el chef hacia la izquierda
                elif event.keysym == "Left":
                        self.chef.mover_izquierda()

                # si se presiona la tecla de la derecha se mueve el chef hacia la derecha
                elif event.keysym == "Right":
                        self.chef.mover_derecha()

#######################################################################################


#Clase que contiene la funcionalidad del restaurante Europeo
class Pantalla_Restaurante_Asiatico:

    def __init__(self, ventana_mapa):

        # Se obtiene la ruta donde se encuentra la imagen de la cocina asiática 
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Se crea la ventana secundaria donde estará el restaurante asiático
        self.ventana_restaurante = Toplevel(ventana_mapa)

        # Se coloca el título de la ventana
        self.ventana_restaurante.title("Restaurante Asiático")

        # Se define el tamaño de la ventana
        self.ventana_restaurante.geometry("1000x700+350+70")

        # Se evita que el usuario cambie el tamaño
        self.ventana_restaurante.resizable(False, False)

        # Se crea el canvas donde irá la cocina asiática
        self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")

        # Se coloca el canvas en la ventana
        self.canvas.pack()

        # Se define la ruta de la imagen de cocina asiática
        ruta_cocina_asiatica = os.path.join(self.BASE_DIR, "Imagenes", "Cocina3.png")

        # Se abre la imagen de cocina asiática
        imagen_cocina_asiatica = Image.open(ruta_cocina_asiatica)

        # Se ajusta el tamaño de la imagen
        imagen_cocina_asiatica = imagen_cocina_asiatica.resize((1000, 700))

        # Se convierte la imagen para tkinter
        self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_asiatica)

        # Se coloca la imagen de fondo
        self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

        # Se crea el chef dentro del restaurante asiático
        self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1")

        # Permite mover el chef sin dar clic sobre la ventana
        self.ventana_restaurante.focus_force()

        # Detecta cuando el usuario presiona una tecla de dirección 
        self.ventana_restaurante.bind("<Key>", self.mover_chef)

#######
    # Función que determina cuál tecla se presionó
    def mover_chef(self, event):

         # si se presiona la tecla de arriba se mueve el chef hacia arriba 
        if event.keysym == "Up":
            self.chef.mover_arriba()

        # si se presiona la tecla de abajao se mueve el chef hacia abajo
        elif event.keysym == "Down":
            self.chef.mover_abajo()

        # si se presiona la tecla la izquierda se mueve el chef hacia la izquierda
        elif event.keysym == "Left":
            self.chef.mover_izquierda()

        # si se presiona la tecla de la derecha se mueve el chef hacia la derecha
        elif event.keysym == "Right":
            self.chef.mover_derecha()
#######################################################################################
# Se crea el objeto de la clase para ejecutar el programa
principal = Pantalla_Principal()