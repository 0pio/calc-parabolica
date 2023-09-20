import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
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
        L= float(entry_L.get())
        for theta in range(1, 91): 
            v2 = (-(L * L) * g) / (2 * (math.cos(math.radians(theta)) * math.cos(math.radians(theta))) * (Hf - Ho - (L * math.tan(math.radians(theta)))))
            Xc = round(math.sqrt((m * (v2))/k), ndigits=4)

            if np.isreal(Xc): 
                if Xc > 0 and Xc < 1:
                    break

        result_label2.config(text=f"Angulo {theta}")
        result_label.config(text=f"Compresión (xc) {Xc}")

    except ValueError:
        result_label.config(text="Ingresa numeros ")
        result_label2.config(text="Ingresa numeros")

    #termina parte del calculo del tiro 
    #ahora creamos todo lo que se ve de la calculadora

#Create the main window 
root = tk.Tk()
root.geometry('1920x1080')
root.title("Ucalc Interfaz")
root.configure(bg="white")


  
# Create the entry field for the numbers
entry_m = ttk.Entry(root, width=9  , background="white", font=("Lucida Sans Typewriter", 11))   
entry_m.pack(pady=5)
entry_m.place(relx=0.24, rely=0.1)

entry_g = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_g.pack(pady=5)
entry_g.place(relx=0.24, rely=0.17)

entry_k = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_k.pack(pady=5)
entry_k.place(relx=0.24, rely=0.24)

entry_Ho = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_Ho.pack(pady=5)
entry_Ho.place(relx=0.24, rely=0.31)

entry_Hf = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_Hf.pack(pady=5)   
entry_Hf.place(relx=0.24, rely=0.38)

entry_L = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_L.pack(pady=5)
entry_L.place(relx=0.24, rely=0.45)

entry_x = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_x.pack(pady=5)
entry_x.place(relx=0.03, rely=0.75)

entry_y = ttk.Entry(root, width=9, background="white", font=("Lucida Sans Typewriter", 11))
entry_y.pack(pady=5)
entry_y.place(relx=0.14, rely=0.75)

# Crea una etiqueta para el título "VALORES DE ENTRADA"
valores_entrada_label = ttk.Label(root, text='VALORES DE ENTRADA', font=("Lucida Sans Typewriter", 20),background="white")
valores_entrada_label.pack(pady=10)
valores_entrada_label.place(relx=0.025, rely=0.025)
# Crea una etiqueta para el título "RESULTADO"
resultado_label = ttk.Label(root, text='RESULTADO',font=("Lucida Sans Typewriter", 20), background="white")
resultado_label.pack(pady=10)
resultado_label.place(relx=0.65, rely=0.04)
#crea la etiqueta para el obstaculo
obstaculo_label = ttk.Label(root, text='OBSTACULO',font=("Lucida Sans Typewriter", 20), background="white")
obstaculo_label.pack(pady=10)
obstaculo_label.place(relx=0.07, rely=0.55)
#crear etiquetas de x
obstaculo_label = ttk.Label(root, text='X',font=("Lucida Sans Typewriter", 20), background="white")
obstaculo_label.pack(pady=10)
obstaculo_label.place(relx=0.050, rely=0.65)
#crear etiqueta de y
obstaculo_label = ttk.Label(root, text='Y',font=("Lucida Sans Typewriter", 20), background="white")
obstaculo_label.pack(pady=10)
obstaculo_label.place(relx=0.16, rely=0.65)

# Crear los entries donde estaran los valores de entrada,
texto_masa = ttk.Label(root,text="Masa (m)",font=("Lucida Sans Typewriter", 14), background="white")
texto_masa.place(relx=0.025, rely=0.1)

texto_gravedad = ttk.Label(root,text="Gravedad (g)", font=("Lucida Sans Typewriter", 14), background="white")
texto_gravedad.place(relx=0.025, rely=0.17)

texto_constante = ttk.Label(root,text="Fuerza del resorte (k)", font=("Lucida Sans Typewriter", 14), background="white")
texto_constante.place(relx=0.025, rely=0.24)

texto_alturaInicial = ttk.Label(root,text="Altura inicial (Ho)",font=("Lucida Sans Typewriter", 14), background="white")
texto_alturaInicial.place(relx=0.025, rely=0.31)

texto_alturaFinal = ttk.Label(root,text="Altura final (Hf)", font=("Lucida Sans Typewriter", 14), background="white")
texto_alturaFinal.place(relx=0.025, rely=0.38)

texto_Longitud = ttk.Label(root,text="Longitud (L)", font=("Lucida Sans Typewriter", 14), background="white")
texto_Longitud.place(relx=0.025, rely=0.45)


# Crear el botón pa calcular
calcular = tk.Button(root, text="CALCULAR", command=calculo_tiro,
    bg="blue",          
    fg="white",    
    activebackground="blue", 
    activeforeground="white", 
    borderwidth=2,   
    relief="flat",            
    font=("Lucida Sans Typewriter", 11)
)
calcular.place(relx=0.3, rely=0.60)

#create the label for the result xc
result_label = ttk.Label(root, text='Compresión del resorte',background="white", relief="sunken", width=25,font=("Lucida Sans Typewriter", 14) )
result_label.pack(pady=10,ipadx=10,ipady=10)
result_label.place(relx=0.5, rely=0.15)  

#create the label for the result angulo
result_label2 = ttk.Label(root, text='Angulo del disparo',background="white",relief="sunken",width=25,font=("Lucida Sans Typewriter", 14))
result_label2.pack(pady=10,ipadx=10,ipady=10)
result_label2.place(relx=0.7, rely=0.15)

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
        entry_L.focus()
    elif event.widget == entry_L:
        entry_x.focus()
    elif event.widget == entry_x:
        entry_y.focus()
        # Aquí puedes agregar más condicionales para mover el enfoque a más entradas si es necesario
        pass

#FUNCION PARA HACER QUE LA FLECHA HACIA ARRIBA SIRVA PARA IR AL ENTRY ANTERIOR
def entry_pasado(event):
    if event.widget == entry_y:
        entry_x.focus()
    elif event.widget == entry_x:
        entry_L.focus()
    elif event.widget == entry_L:
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
entry_L.bind('<Down>', siguiente_entry)
entry_x.bind('<Down>', siguiente_entry)
entry_y.bind('<Down>', siguiente_entry)

#VINCULAR LA FLECHA HACIA ARRIBA PARA IR AL ENTRY DE ARRIBA
entry_y.bind('<Up>', entry_pasado)
entry_x.bind('<Up>', entry_pasado)
entry_L.bind('<Up>', entry_pasado)
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
    entry_L.delete(0, tk.END)
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    entry_m.focus_set()

# Crea el botón para borrar los campos
boton_borrar = tk.Button(root, text="Borrar datos", command=borrar_campos, 
    bg="#818181",          
    fg="white",    
    activebackground="#818181", 
    activeforeground="white", 
    borderwidth=2,   
    relief="flat",            
    font=("Lucida Sans Typewriter", 11)
    )
boton_borrar.place(relx=0.33, rely=0.73, anchor="center")

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

#Carga imagen de agyuda
imagen_ayuda = Image.open(os.path.join(carpeta_imagenes, "ayuda.png"))
imagen_ayuda = imagen_ayuda.resize((500, 300), Image.ANTIALIAS)  # Cambia el tamaño de la imagen_logo
ayuda = ImageTk.PhotoImage(imagen_ayuda)
# Crea la etiqueta y configura su posición y tamaño
etiqueta_ayuda = Label(root, image=ayuda, width=500, height=300)
etiqueta_ayuda.place(relx=0.8, rely=0.7)

#Carga imagen_logo del logo EN LA CALCULADORA
imagen_logo = Image.open(os.path.join(carpeta_paisajes, "logo.jpg"))
imagen_logo = imagen_logo.resize((500, 300), Image.ANTIALIAS)  # Cambia el tamaño de la imagen_logo
logo = ImageTk.PhotoImage(imagen_logo)
# Crea la etiqueta y configura su posición y tamaño
etiqueta_logo = Label(root, image=logo, width=500, height=300)  
etiqueta_logo.place(relx=0.44, rely=0.3)

    #Termina la parte de las imagenes en la calculadora
    #empieza la parte de la ayuda

# Definir la función para abrir ayuda
def abrir_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.geometry("300x200")
    nueva_ventana.title("AYUDA")
    etiqueta = ttk.Label(nueva_ventana, text="Si no sabes que es cada valor, aqui te lo explicamos: \n m= masa del objeto \n g= gravedad \n k= constante del resorte \n Hf= altura final \n Ho= altura inicial  \n L= variable a definir"                               )
    etiqueta.pack()
    nueva_ventana.grab_set()
# Crear un botón para abrir la ayuda
boton_ayuda = ttk.Button(root, text="¿AYUDA?", style="Accent.TButton", command=abrir_ventana)
boton_ayuda.pack()
boton_ayuda.place(relx=0.9, rely=0.9)

    #termina la parte de la ayuda
    #empieza la parte para correr el main loop

#run main loop
root.mainloop()