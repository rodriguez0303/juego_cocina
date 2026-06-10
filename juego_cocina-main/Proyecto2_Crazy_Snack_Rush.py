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

                # Se define la ruta de la imagen de fondo
                ruta_imagen_fondo = os.path.join(self.BASE_DIR,'Imagenes','Fondo1.png')

                # Se abre la imagen
                imagen_fondo = Image.open(ruta_imagen_fondo)

                # Se ajusta el tamaño de la imagen
                imagen_fondo = imagen_fondo.resize((1000, 700))

                # Se convierte la imagen para tkinter
                self.imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

                # Se coloca la imagen de fondo en el canvas
                self.canvas.create_image(0, 0, image=self.imagen_fondo_tk, anchor=NW)
                
                # Se define la ruta de la imagen del botón jugar 
                ruta_boton_jugar = os.path.join(self.BASE_DIR,'Imagenes','Boton_Jugar.png')

                # Se abre la ruta donde se encuentra la imagen del botón jugar
                imagen_boton_jugar = Image.open(ruta_boton_jugar)

                # Se define el tamaño de la imagen (botón) play 
                imagen_boton_jugar = imagen_boton_jugar.resize((250, 100))

                # Se convierte la imagen al formato que tkinter pueda usar 
                self.imagen_boton_jugar_tk = ImageTk.PhotoImage(imagen_boton_jugar)

                # Se define la posición de la imagen del botón jugar dentro del canvas 
                self.boton_jugar = self.canvas.create_image(500, 550, image=self.imagen_boton_jugar_tk)

                # Evento que permite hacer click sobre la imagen del botón jugar 
                self.canvas.tag_bind(self.boton_jugar, "<Button-1>", self.iniciar_juego)
                
                # Mantiene la ventana abierta
                self.ventana.mainloop()

        # Función que destruye la pantalla principal para luego mostrar la pantalla de juegos 
        def iniciar_juego(self, event):
                # Se oculta la pantalla principal
                self.ventana.withdraw()

                # Se abre la ventana de mapas del juego 
                self.pantalla_mapa = Pantalla_mapa(self.ventana)


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
                self.canvas = Canvas(self.ventana_juego, width=1000, height=700, bg="black")
                self.canvas.pack()

                # Ruta de la imagen de fondo del mapa 
                ruta_fondo_mapa = os.path.join(self.BASE_DIR, 'Imagenes', 'Fondo_mapa.png')

                # Se abre la imagen
                imagen_fondo_mapa = Image.open(ruta_fondo_mapa)

                # Se ajusta el tamaño de la imagen del mapa 
                imagen_fondo_mapa = imagen_fondo_mapa.resize((1000, 700))

                # Conversión de la imagen del mapa en un formato que tkinter pueda usar 
                self.imagen_fondo_mapa_tk = ImageTk.PhotoImage(imagen_fondo_mapa)

                # Se coloca la imagen de fondo en el canvas 
                self.canvas.create_image(0, 0, image=self.imagen_fondo_mapa_tk, anchor=NW)
        
                #Ruta de la imagen restaurante pizza que esta sobre el mapa principal 
                ruta_restaurante_americano = os.path.join(self.BASE_DIR, "Imagenes", "Americano.png")

                # Se abre la imagen del restaurante pizza
                imagen_americano = Image.open(ruta_restaurante_americano)

                # Se ajusta el tamaño de la imagen restaurante pizza
                imagen_americano = imagen_americano.resize((240, 100))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_americano_tk = ImageTk.PhotoImage(imagen_americano)

                #Ruta de la imagen restaurante europeo que esta sobre el mapa principal 
                ruta_restaurante_europeo = os.path.join(self.BASE_DIR, "Imagenes", "Europeo.png")
                
                # Se abre la imagen del restaurante Europeo
                imagen_europeo = Image.open(ruta_restaurante_europeo)

                # Se ajusta el tamaño de la imagen restaurante europeo
                imagen_europeo = imagen_europeo.resize((200, 100))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_europeo_tk = ImageTk.PhotoImage(imagen_europeo)

                #Ruta de la imagen restaurante Asiatico que esta sobre el mapa principal 
                ruta_asiatico = os.path.join(self.BASE_DIR, "Imagenes", "Asiatico.png")
                
                # Se abre la imagen del restaurante asiático
                imagen_asiatico = Image.open(ruta_asiatico)

                # Se ajusta el tamaño de la imagen restaurante asiatico
                imagen_asiatico = imagen_asiatico.resize((80, 80))

                # Se convierte la imagen a un formato que tkinter pueda usar
                self.imagen_asiatico_tk = ImageTk.PhotoImage(imagen_asiatico)

                #Se define la ubicación del icono del restaurante americano sobre el mapa 
                self.punto_americano = puntoMapa(self.canvas, 460, 370, self.imagen_americano_tk, self.abrir_americano)
                
                # Se coloca el nombre del restaurante Americano
                self.canvas.create_text(450, 320, text="Restaurante Americano", font=("Arial", 12, "bold"), fill="white")
                                                
                #Se define la ubicación del icono del restaurante europeo sobre el mapa 
                self.punto_europeo = puntoMapa(self.canvas, 238, 130, self.imagen_europeo_tk, self.abrir_europeo)
                
                # Se coloca el nombre del restaurante Europeo
                self.canvas.create_text(230, 70, text="Restaurante Europeo", font=("Arial", 12, "bold"), fill="white")
                
                #Se define la ubicación del icono del restaurante Europeo sobre el mapa 
                self.punto_asiatico = puntoMapa(self.canvas, 720, 140, self.imagen_asiatico_tk, self.abrir_asiatico)
                
                # Se coloca el nombre del restaurante Asiatico
                self.canvas.create_text(710, 80, text="Restaurante Asiatico", font=("Arial", 12, "bold"), fill="white")
        
        # Esta función que inicializa el juego al presionar el botón Play
        def iniciar_juego(self, event):
                self.ventana.withdraw()
                self.pantalla_mapa = Pantalla_mapa(self.ventana)

        # Funcion que abre el mapa de juego del restaurante Americano 
        def abrir_americano(self, event):
                self.ventana_juego.withdraw()
                self.pantalla_americano = Pantalla_Restaurante_Americano(self.ventana_juego)

        # Funcion que abre el mapa de juego del restaurante Europeo
        def abrir_europeo(self, event):
                self.ventana_juego.withdraw()
                self.pantalla_europeo = Pantalla_Restaurante_Europeo(self.ventana_juego)

        # Funcion que abre el mapa de juego del restaurante Asiatico
        def abrir_asiatico(self, event):
                self.ventana_juego.withdraw()
                self.pantalla_asiatico = Pantalla_Restaurante_Asiatico(self.ventana_juego)


# Clase que permite acceder a los diferente restaurantes
class puntoMapa:
    def __init__(self, canvas, coordenada_ejex, coordenada_ejey, imagen_puntomapa, funcion_click):
        self.canvas = canvas
        self.imagen_puntomapa = imagen_puntomapa
        self.icono = self.canvas.create_image(coordenada_ejex, coordenada_ejey, image=self.imagen_puntomapa)
        self.canvas.tag_bind(self.icono, "<Button-1>", funcion_click)
        

# Clase asociada a la funcionaldiades del chef dentro del restaurante
class Chef:
        def __init__(self, canvas, base_dir, nombre, chef_ejex, chef_ejey):
                self.canvas = canvas
                self.BASE_DIR = base_dir
                self.nombre = nombre
                self.puntos = 0
                self.chef_ejex = chef_ejex
                self.chef_ejey = chef_ejey
                self.distancia = 50

                # Variable general para seguir el ingrediente que sostiene el Chef
                self.ingrediente_en_mano = None  

                ruta_chef_abajo = os.path.join(self.BASE_DIR, "Imagenes", "chef_abajo.png")
                imagen_chef_abajo = Image.open(ruta_chef_abajo).resize((70, 100))
                self.imagen_abajo_tk = ImageTk.PhotoImage(imagen_chef_abajo)

                ruta_chef_arriba = os.path.join(self.BASE_DIR, "Imagenes", "chef_arriba.png")
                imagen_chef_arriba = Image.open(ruta_chef_arriba).resize((70, 100))
                self.imagen_arriba_tk = ImageTk.PhotoImage(imagen_chef_arriba)

                ruta_chef_izquierda = os.path.join(self.BASE_DIR, "Imagenes", "chef_izquierda.png")
                imagen_chef_izquierda = Image.open(ruta_chef_izquierda).resize((70, 100))
                self.imagen_izquierda_tk = ImageTk.PhotoImage(imagen_chef_izquierda)

                ruta_chef_derecha = os.path.join(self.BASE_DIR, "Imagenes", "chef_derecha.png")
                imagen_chef_derecha = Image.open(ruta_chef_derecha).resize((70, 100))
                self.imagen_derecha_tk = ImageTk.PhotoImage(imagen_chef_derecha)

                self.chef_canvas = self.canvas.create_image(self.chef_ejex, self.chef_ejey, image=self.imagen_abajo_tk)

        def mostrar_posicion(self):
                columna = self.chef_ejex // 50
                fila = self.chef_ejey // 50
                print("X =", self.chef_ejex, "Y =", self.chef_ejey, "Fila =", fila, "Columna =", columna)

        def mover_arriba(self):
                self.canvas.itemconfig(self.chef_canvas, image=self.imagen_arriba_tk)
                self.chef_ejey -= self.distancia
                self.canvas.move(self.chef_canvas, 0, -self.distancia)
                self.actualizar_ingrediente()
                self.mostrar_posicion()

        def mover_abajo(self):
                self.canvas.itemconfig(self.chef_canvas, image=self.imagen_abajo_tk)
                self.chef_ejey += self.distancia
                self.canvas.move(self.chef_canvas, 0, self.distancia)
                self.actualizar_ingrediente()
                self.mostrar_posicion()

        def mover_izquierda(self):
                self.canvas.itemconfig(self.chef_canvas, image=self.imagen_izquierda_tk)
                self.chef_ejex -= self.distancia
                self.canvas.move(self.chef_canvas, -self.distancia, 0)
                self.actualizar_ingrediente()
                self.mostrar_posicion()

        def mover_derecha(self):
                self.canvas.itemconfig(self.chef_canvas, image=self.imagen_derecha_tk)
                self.chef_ejex += self.distancia
                self.canvas.move(self.chef_canvas, self.distancia, 0)
                self.actualizar_ingrediente()
                self.mostrar_posicion()

        def actualizar_ingrediente(self):
                # Se encarga de reposicionar el ingrediente en la cabeza del chef tras caminar
                if self.ingrediente_en_mano is not None:
                        self.ingrediente_en_mano.mover_ingrediente_con_chef(self)


#Clase que guarda toda la información de los ingredienes de la cocina americana
class ingredientes_restaurante_americano:
        def __init__(self, canvas_ingredientes, base_dir, nombre_ingrediente, archivo_imagen):
                self.canvas_ingredientes = canvas_ingredientes
                self.BASE_DIR = base_dir
                self.nombre_ingrediente = nombre_ingrediente
                self.archivo_imagen = archivo_imagen
                self.objeto_canvas = None

                ruta_imagen = os.path.join(self.BASE_DIR, "Imagenes", self.archivo_imagen)
                imagen = Image.open(ruta_imagen).resize((40, 40))
                self.imagen_tk = ImageTk.PhotoImage(imagen)

        def tomar_ingrediente(self, chef):
                if self.objeto_canvas != None:
                        self.canvas_ingredientes.delete(self.objeto_canvas)
                self.objeto_canvas = self.canvas_ingredientes.create_image(chef.chef_ejex, chef.chef_ejey - 80, image=self.imagen_tk)

        def mover_ingrediente_con_chef(self, chef):
                if self.objeto_canvas != None:
                        self.canvas_ingredientes.coords(self.objeto_canvas, chef.chef_ejex, chef.chef_ejey - 80)

        def soltar_ingrediente(self):
                if self.objeto_canvas != None:
                        self.canvas_ingredientes.delete(self.objeto_canvas)
                        self.objeto_canvas = None

        def obtener_posicion_ingrediente(self):
                if self.objeto_canvas != None:
                        return self.canvas_ingredientes.coords(self.objeto_canvas)
                return None


#Clase que contiene la funcionalidad del restaurante americano 
class Pantalla_Restaurante_Americano:
        def __init__(self, ventana_mapa):
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                self.ventana_restaurante = Toplevel(ventana_mapa)
                self.ventana_restaurante.title("Restaurante Americano")
                self.ventana_restaurante.geometry("1000x700+350+70")
                self.ventana_restaurante.resizable(False, False)

                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")
                self.canvas.pack()

                ruta_cocina_americana = os.path.join(self.BASE_DIR, "Imagenes", "Cocina1.png")
                imagen_cocina_americana = Image.open(ruta_cocina_americana).resize((1000, 700))
                self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_americana)
                self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

                self.ventana_restaurante.bind("a", self.tomar_zanahoria)

                self.matriz_movimiento_americano = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]
                       
                self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 500, 350)
                self.zanahoria = ingredientes_restaurante_americano(self.canvas, self.BASE_DIR, "Zanahoria", "zanahoria.png")

                self.ventana_restaurante.focus_force()
                self.ventana_restaurante.bind("<Key>", self.mover_chef)

        def mover_chef(self, event):
                fila_actual = self.chef.chef_ejey // 50
                columna_actual = self.chef.chef_ejex // 50
                nueva_fila = fila_actual
                nueva_columna = columna_actual

                if event.keysym == "Up": nueva_fila = fila_actual - 1
                elif event.keysym == "Down": nueva_fila = fila_actual + 1
                elif event.keysym == "Left": nueva_columna = columna_actual - 1
                elif event.keysym == "Right": nueva_columna = columna_actual + 1

                if nueva_fila < 0 or nueva_fila >= 14 or nueva_columna < 0 or nueva_columna >= 20:
                        print("Fuera de límites")
                else:
                        if self.matriz_movimiento_americano[nueva_fila][nueva_columna] == 1:
                                if event.keysym == "Up": self.chef.mover_arriba()
                                elif event.keysym == "Down": self.chef.mover_abajo()
                                elif event.keysym == "Left": self.chef.mover_izquierda()
                                elif event.keysym == "Right": self.chef.mover_derecha()
                        else: 
                                print ("Movimiento no válido")

        def tomar_zanahoria(self, event):
                if self.chef.ingrediente_en_mano == None:
                        self.zanahoria.tomar_ingrediente(self.chef)
                        self.chef.ingrediente_en_mano = self.zanahoria


#Clase que contiene la funcionalidad del restaurante Europe 
class Pantalla_Restaurante_Europeo:
        def __init__(self, ventana_mapa):
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                self.ventana_restaurante = Toplevel(ventana_mapa)
                self.ventana_restaurante.title("Restaurante Europeo")
                self.ventana_restaurante.geometry("1000x700+350+70")
                self.ventana_restaurante.resizable(False, False)

                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")
                self.canvas.pack()

                ruta_cocina_europea = os.path.join(self.BASE_DIR, "Imagenes", "Cocina2.png")
                imagen_cocina_europea = Image.open(ruta_cocina_europea).resize((1000, 700))
                self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_europea)
                self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

                self.matriz_movimiento_europeo = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,0,0],
                        [0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0],
                        [0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0],
                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],
                        [0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],
                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],
                        [0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0],
                        [0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]

                self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 350, 350)
                self.ventana_restaurante.focus_force()
                self.ventana_restaurante.bind("<Key>", self.mover_chef)
                        
        def mover_chef(self, event):
                fila_actual = self.chef.chef_ejey // 50
                columna_actual = self.chef.chef_ejex // 50
                nueva_fila = fila_actual
                nueva_columna = columna_actual

                if event.keysym == "Up": nueva_fila = fila_actual - 1
                elif event.keysym == "Down": nueva_fila = fila_actual + 1
                elif event.keysym == "Left": nueva_columna = columna_actual - 1
                elif event.keysym == "Right": nueva_columna = columna_actual + 1

                if nueva_fila < 0 or nueva_fila >= 14 or nueva_columna < 0 or nueva_columna >= 20:
                        print("Fuera de límites")
                else:
                        if self.matriz_movimiento_europeo[nueva_fila][nueva_columna] == 1:
                                if event.keysym == "Up": self.chef.mover_arriba()
                                elif event.keysym == "Down": self.chef.mover_abajo()
                                elif event.keysym == "Left": self.chef.mover_izquierda()
                                elif event.keysym == "Right": self.chef.mover_derecha()
                        else: 
                                print ("Movimiento no válido")


#Clase que contiene la funcionalidad del restaurante Asiático
class Pantalla_Restaurante_Asiatico:
        def __init__(self, ventana_mapa):
                self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                self.ventana_restaurante = Toplevel(ventana_mapa)
                self.ventana_restaurante.title("Restaurante Asiático")
                self.ventana_restaurante.geometry("1000x700+350+70")
                self.ventana_restaurante.resizable(False, False)

                self.canvas = Canvas(self.ventana_restaurante, width=1000, height=700, bg="black")
                self.canvas.pack()

                ruta_cocina_asiatica = os.path.join(self.BASE_DIR, "Imagenes", "Cocina3.png")
                imagen_cocina_asiatica = Image.open(ruta_cocina_asiatica).resize((1000, 700))
                self.imagen_cocina_tk = ImageTk.PhotoImage(imagen_cocina_asiatica)
                self.canvas.create_image(0, 0, image=self.imagen_cocina_tk, anchor=NW)

                # El Chef inicia abajo en la puerta
                self.chef = Chef(self.canvas, self.BASE_DIR, "Jugador 1", 450, 550) 

                # ¡SIMETRÍA HORIZONTAL COMPLETA!
                # - Mostrador Izquierdo: Chef parado en Columna 4 interactúa con la Columna 3 (mira a la izquierda).
                # - Mostrador Derecho: Chef parado en Columna 16 interactúa con la Columna 17 (mira a la derecha).
                self.puestos_ingredientes = {
                        # --- BARRA IZQUIERDA (Chef en Columna 4 -> mira a la Izquierda Columna 3) ---
                        (4, 3): {"nombre": "Arroz", "archivo": "arroz.png"},
                        (5, 3): {"nombre": "Espinaca", "archivo": "espinaca.png"},
                        (6, 3): {"nombre": "Pescado", "archivo": "pescado crudo.png"},
                        (7, 3): {"nombre": "Ajíes", "archivo": "ajies.png"},
                        (8, 3): {"nombre": "Champiñones", "archivo": "champinon.png"},
                        (9, 3): {"nombre": "Huevos", "archivo": "huevos.png"},

                        # --- BARRA DERECHA (Chef en Columna 16 -> mira a la Derecha Columna 17) ---
                        (2, 17): {"nombre": "Carne cruda", "archivo": "carne.png"}, 
                        (3, 17): {"nombre": "Cebollín", "archivo": "cebollin.png"},
                        (4, 17): {"nombre": "Fideos", "archivo": "fideos.png"},
                        (5, 17): {"nombre": "Salsa", "archivo": "salsa.png"},
                        (6, 17): {"nombre": "Tofu", "archivo": "tofu.png"},
                        (7, 17): {"nombre": "Algas", "archivo": "alga.png"}
                }

                # MATRIZ FÍSICA ASÍATICA CORREGIDA:
                # El pasillo derecho es la Columna 16 (libre del todo). La Columna 17 es la pared/estante (bloqueada).
                self.matriz_movimiento_asiatico = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], # Ahora la columna 16 está libre de arriba a abajo
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0], # Muebles negros centrales de madera
                        [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], # Pasillo sur
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], 
                        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], 
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
                ]

                self.ventana_restaurante.focus_force()
                self.ventana_restaurante.bind("<Key>", self.controlador_entrada)

        def controlador_entrada(self, event):
                tecla = event.keysym

                if tecla in ["Up", "Down", "Left", "Right"]:
                        fila_actual = self.chef.chef_ejey // 50
                        columna_actual = self.chef.chef_ejex // 50
                        nueva_fila = fila_actual
                        nueva_columna = columna_actual

                        if tecla == "Up": nueva_fila = fila_actual - 1
                        elif tecla == "Down": nueva_fila = fila_actual + 1
                        elif tecla == "Left": nueva_columna = columna_actual - 1
                        elif tecla == "Right": nueva_columna = columna_actual + 1

                        if 0 <= nueva_fila < 14 and 0 <= nueva_columna < 20:
                                if self.matriz_movimiento_asiatico[nueva_fila][nueva_columna] == 1:
                                        if tecla == "Up": self.chef.mover_arriba()
                                        elif tecla == "Down": self.chef.mover_abajo()
                                        elif tecla == "Left": self.chef.mover_izquierda()
                                        elif tecla == "Right": self.chef.mover_derecha()
                                        
                                        # Actualizar ingrediente cargado
                                        if self.chef.ingrediente_en_mano is not None:
                                                self.chef.ingrediente_en_mano.mover_ingrediente_con_chef(self.chef)
                                else:
                                        print("Movimiento bloqueado por colisión física.")
                
                elif tecla == "space":
                        self.interactuar_mostrador()

        def interactuar_mostrador(self):
                fila_chef = self.chef.chef_ejey // 50
                columna_chef = self.chef.chef_ejex // 50

                # Escanea en cruz las 4 casillas adyacentes
                adyacentes = [
                        (fila_chef - 1, columna_chef),
                        (fila_chef + 1, columna_chef),
                        (fila_chef, columna_chef - 1),
                        (fila_chef, columna_chef + 1)
                ]

                for pos in adyacentes:
                        if pos in self.puestos_ingredientes:
                                datos = self.puestos_ingredientes[pos]
                                
                                # CASO 1: DEVOLVER
                                if self.chef.ingrediente_en_mano is not None:
                                        self.chef.ingrediente_en_mano.soltar_ingrediente()
                                        self.chef.ingrediente_en_mano = None
                                        print(f"Has devuelto el ingrediente al mostrador de {datos['nombre']}.")
                                        return
                                
                                # CASO 2: RECOGER
                                nuevo_ingrediente = ingredientes_restaurante_americano(
                                        self.canvas,
                                        self.BASE_DIR,
                                        datos["nombre"],
                                        datos["archivo"]
                                )
                                nuevo_ingrediente.tomar_ingrediente(self.chef)
                                self.chef.ingrediente_en_mano = nuevo_ingrediente
                                print(f"¡Has recogido exitosamente: {datos['nombre']}!")
                                return
                
                print(f"No hay ningún estante de comida a tu lado. (Fila={fila_chef}, Columna={columna_chef})")


# Se crea el objeto de la clase para ejecutar el programa
principal = Pantalla_Principal()