import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import os
import cmath
import math
import numpy as np


    #primera parte para calcular el tiro parabolico

def calculo_tiro():
    try:
        m = float(entry_m.get())
        g= float(entry_g.get())
        k= float(entry_k.get())
        Hf= float(entry_Hf.get())
        Ho= float(entry_Ho.get())
        t= float(entry_t.get())
        for theta in range(1, 91):
            L = (12*math.pow(t, 3)) + (5*math.pow(t, 2)) + (3*math.pow(t, 1)) + 10 
            v2 = (-(L * L) * g) / (2 * (math.cos(math.radians(theta)) * math.cos(math.radians(theta))) * (Hf - Ho - (L * math.tan(math.radians(theta)))))
            Xc = round(math.sqrt((m * (v2))/k), ndigits=4)

            if np.isreal(Xc): 
                if Xc > 0 and Xc < 1:
                    break

        result_label2.config(text=f"El angulo es {theta}")
        result_label.config(text=f"La distancia de compresion es {Xc}")

    except ValueError:
        result_label.config(text="Por favor ingresa valores validos")
        result_label2.config(text="Por favor ingresa valores validos")

    #termina parte del calculo del tiro 
    #ahora creamos todo lo que se ve de la calculadora

#Create the main window 
root = tk.Tk()
root.geometry('1000x700')
root.title("Ucalc Interfaz")

  
# Create the entry field for the numbers
entry_m = ttk.Entry(root, width=9 , background="white")
entry_m.pack(pady=5)
entry_m.place(relx=0.25, rely=0.162)

entry_g = ttk.Entry(root, width=9)
entry_g.pack(pady=5)
entry_g.place(relx=0.25, rely=0.212)

entry_k = ttk.Entry(root, width=9)
entry_k.pack(pady=5)
entry_k.place(relx=0.25, rely=0.262)

entry_Ho = ttk.Entry(root, width=9)
entry_Ho.pack(pady=5)
entry_Ho.place(relx=0.25, rely=0.312)

entry_Hf = ttk.Entry(root, width=9)
entry_Hf.pack(pady=5)
entry_Hf.place(relx=0.25, rely=0.362)

entry_t = ttk.Entry(root, width=9)
entry_t.pack(pady=5)
entry_t.place(relx=0.25, rely=0.41)

# Crea una etiqueta para el título "VALORES DE ENTRADA"
title_label = ttk.Label(root, text='VALORES DE ENTRADA')
title_label.pack(pady=10)
title_label.place(relx=0.019, rely=0.1)
# Crea una etiqueta para el título "RESULTADO"
title_label = ttk.Label(root, text='RESULTADO')
title_label.pack(pady=10)
title_label.place(relx=0.5, rely=0.1)

# Crear los botones donde estaran los valores de entrada, donde si les picas, sale que son
def mostrar_masa():
    texto.config(text="Masa del Objeto")
    texto.place(x=55, y=115.09)
button = ttk.Button(root, text='m', style="Accent.TButton", command=mostrar_masa)
button.pack(pady=5)
button.place(relx=0.147, rely=0.162)
texto = ttk.Label(root, text="")
texto.pack()

def mostrar_gravedad():
    texto.config(text="gravedad del Objeto")
    texto.place(x=36, y=152)
button = ttk.Button(root, text='g', style="Accent.TButton", command=mostrar_gravedad)
button.pack(pady=5)
button.place(relx=0.147, rely=0.212)
texto = ttk.Label(root, text="")
texto.pack()

def mostrar_Constante():
    texto.config(text="Constante del resorte")
    texto.place(x=30, y=187)
button = ttk.Button(root, text='K', style="Accent.TButton", command=mostrar_Constante)
button.pack(pady=5)
button.place(relx=0.147, rely=0.262)
texto = ttk.Label(root, text="")
texto.pack()

def mostrar_AlturaInicial():
    texto.config(text="Altura inicial")
    texto.place(x=75, y=218)
button = ttk.Button(root, text='Ho', style="Accent.TButton", command=mostrar_AlturaInicial)
button.pack(pady=5)
button.place(relx=0.147, rely=0.312)
texto = ttk.Label(root, text="")
texto.pack()

def mostrar_AlturaFinal():
    texto.config(text="Altura Final")
    texto.place(x=72, y=248)
button = ttk.Button(root, text='Hf', style="Accent.TButton", command=mostrar_AlturaFinal)
button.pack(pady=5)
button.place(relx=0.147, rely=0.362)
texto = ttk.Label(root, text="")
texto.pack()

def mostrar_Tiempo():
    texto.config(text="Variable a definir")
    texto.place(x=30, y=285)
button = ttk.Button(root, text='T', style="Accent.TButton", command=mostrar_Tiempo)
button.pack(pady=5)
button.place(relx=0.147, rely=0.41)
texto = ttk.Label(root, text="")
texto.pack()

# Crear el botón pa calcular
calcular = ttk.Button(root, text="CALCULAR", style="Accent.TButton", command=calculo_tiro)
calcular.place(relx=0.185, rely=0.51)

#create the label for the result xc
result_label = ttk.Label(root, text='')
result_label.pack(pady=10)
result_label.place(relx=0.5, rely=0.2)

#create the label for the result angulo
result_label2 = ttk.Label(root, text='',)
result_label2.pack(pady=10)
result_label2.place(relx=0.5, rely=0.4)

    #termina la parte de el layout de la calculadora
    #ahora es la parte de definir el movimiento con las flechas

# Función para mover el cursor a la SIGUIENTE SOLO APRETANDO FLECHA HACIA ABAJO
def siguiente_entry(event):
    if event.widget == entry_m:
        entry_g.focus()
    elif event.widget == entry_g:
        entry_k.focus()
    elif event.widget == entry_k:
        entry_Ho.focus()
    elif event.widget == entry_Ho:
        entry_Hf.focus()
    elif event.widget == entry_Hf:
        entry_t.focus()
    elif event.widget == entry_t:
        # Aquí puedes agregar más condicionales para mover el enfoque a más entradas si es necesario
        pass

#FUNCION PARA HACER QUE LA FLECHA HACIA ARRIBA SIRVA PARA IR AL ENTRY ANTERIOR
def entry_pasado(event):
    if event.widget == entry_t:
        entry_Hf.focus()
    elif event.widget == entry_Hf:
        entry_Ho.focus()
    elif event.widget == entry_Ho:
        entry_k.focus()
    elif event.widget == entry_k:
        entry_g.focus()
    elif event.widget == entry_g:
        entry_m.focus()
    elif event.widget == entry_m:
        # Aquí puedes agregar más condicionales para mover el enfoque a más entradas si es necesario
        pass

# Vincular el evento de presionar la tecla "ABAJO" a la función para mover el ENTRY
entry_m.bind('<Down>', siguiente_entry)
entry_g.bind('<Down>', siguiente_entry)
entry_k.bind('<Down>', siguiente_entry)
entry_Ho.bind('<Down>', siguiente_entry)
entry_Hf.bind('<Down>', siguiente_entry)
entry_t.bind('<Down>', siguiente_entry)

#VINCULAR LA FLECHA HACIA ARRIBA PARA IR AL ENTRY DE ARRIBA
entry_t.bind('<Up>', entry_pasado)
entry_Hf.bind('<Up>', entry_pasado)
entry_Ho.bind('<Up>', entry_pasado)
entry_k.bind('<Up>', entry_pasado)
entry_g.bind('<Up>', entry_pasado)
entry_m.bind('<Up>', entry_pasado)

# para poder clcular con enter
root.bind('<Return>', lambda event=None: calcular.invoke())

#para poner el boton de reset
def borrar_campos(event=None):
    entry_m.delete(0, tk.END)
    entry_g.delete(0, tk.END)
    entry_k.delete(0, tk.END)
    entry_Hf.delete(0, tk.END)
    entry_Ho.delete(0, tk.END)
    entry_t.delete(0, tk.END)
    entry_m.focus_set()

# Crea el botón para borrar los campos
boton_borrar = ttk.Button(root, text="Borrar DATOS", command=borrar_campos)
boton_borrar.place(relx=0.5, rely=0.523, anchor="center")

# Asocia el evento de teclado "Shift-Enter" a la función borrar_campos
root.bind('<Shift-Return>', borrar_campos)

    #termina la parte de el layout de la calculadora
    #empieza la parte de las imagenes en la calculadora

# Directorio PRINCIPAL< de las imagenes
carpeta_principal = os.path.dirname(__file__)
# Directorio de imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "carpeta")

#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "logochikito.ico")) 

#Carga imagen del logo EN LA CALCULADORA
imagen = Image.open(os.path.join(carpeta_paisajes, "logo.jpg"))
imagen = imagen.resize((250, 150), Image.ANTIALIAS)  # Cambia el tamaño de la imagen
fondo = ImageTk.PhotoImage(imagen)
# Crea la etiqueta y configura su posición y tamaño
etiqueta = Label(root, image=fondo, width=250, height=150)
etiqueta.place(x=70, y=440)

    #Termina la parte de las imagenes en la calculadora
    #empieza la parte de la ayuda

# Definir la función para abrir ayuda
def abrir_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.geometry("300x200")
    nueva_ventana.title("AYUDA")
    etiqueta = ttk.Label(nueva_ventana, text="Si no sabes que es cada valor, aqui te lo explicamos: \n m= masa del objeto \n g= gravedad \n k= constante del resorte \n Hf= altura final \n Ho= altura inicial  \n t= variable a definir"                               )
    etiqueta.pack()
    nueva_ventana.grab_set()
# Crear un botón para abrir la ayuda
boton_a = ttk.Button(root, text="¿AYUDA?", style="Accent.TButton", command=abrir_ventana)
boton_a.pack()

    #termina la parte de la ayuda
    #empieza la parte para correr el main loop

#run main loop
root.mainloop()