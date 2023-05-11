# se importa tkintery sus funciones
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#se crea la ventana principal ttk
principal= Tk()

#título de la ventana
principal.title=("PLATAFORMA INTEGRA")

#anchor de la ventana
principal.geometry("500x500")

#color de la ventana
principal.config(bg="black")


#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_command(label="Convertir")
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar")

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir")

barra_menu.add_cascade(label="Convertir", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)


#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(principal)
frame_entrada.config(bg="red2", width=480, height=180)
frame_entrada.place(x=10, y=10)

# frame del nombre
nombre= Label(principal, text="Nombre:")
nombre.config(bg = "red2",fg="black", font=("Helvetica", 20))
nombre.place(x=10,y=20)

# caja de texto para nombre
nombre_c = Entry(principal,)
nombre_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=115,y=20)

# frame de la fecha de nacimiento

nacimiento= Label(principal, text="Fecha de nacimiento:")
nacimiento.config(bg = "red2",fg="black", font=("Helvetica", 20))
nacimiento.place(x=10,y=55)

# caja de texto para fecha de nacimiento
nombre_c = Entry(principal,)
nombre_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=55)


# escudo
logo= PhotoImage(file="img/escudo_colegio.png")
logo= Label(frame_entrada, image=logo, bg="white")
logo.place(x=70,y=300)


principal.mainloop()