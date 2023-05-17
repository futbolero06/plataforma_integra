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
principal.geometry("900x900")

#color de la ventana
principal.config(bg="black")

#imagenes globales
global logo_notas
global logo_salud
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
# frame entrada
#--------------------------------
frame_entrada = Frame(principal)
frame_entrada.config(bg="blue3", width=410, height=600)
frame_entrada.place(x=480, y=10)

#--------------------------------
# frame datos
#--------------------------------
frame_datos = Frame(principal)
frame_datos.config(bg="red3", width=450, height=600)
frame_datos.place(x=10, y=10)    

# texto nombre_opciones    

text_nombre= Label(frame_entrada,text=("OPCIONES"))
text_nombre.config(bg="blue3", fg="black", font=("Helvetica", 20))
text_nombre.place(x=10,y=130)

# texto de la plataforma
nombre= Label(frame_entrada, text="PLATAFORMA")
nombre.config(bg = "blue3",fg="black", font=("Helvetica", 20))
nombre.place(x=150,y=40)


# texto registro
nombre= Label(frame_datos, text="REGISTRO")
nombre.config(bg = "red3",fg="green3", font=("Helvetica", 40))
nombre.place(x=80,y=20)

# texto nombre
nombre= Label(frame_datos, text="Nombre:")
nombre.config(bg = "red3",fg="black", font=("Helvetica", 20))
nombre.place(x=10,y=80)

# caja de texto para nombre
nombre_c = Entry(frame_datos,)
nombre_c.config(bg="green3", fg="blue3", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=80)

# texto fecha nc

nacimiento= Label(frame_datos, text="Fecha de nacimiento:")
nacimiento.config(bg = "red3",fg="black", font=("Helvetica", 20))
nacimiento.place(x=10,y=120)


# caja de texto para fecha de nacimiento
nombre_c = Entry(frame_datos,)  
nombre_c.config(bg="green3", fg="blue3", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=120)

# texto grado

nacimiento= Label(frame_datos, text="Grado:")
nacimiento.config(bg = "red3",fg="black", font=("Helvetica", 20))
nacimiento.place(x=10,y=160)

# caja de texto para grado
nombre_c = Entry(frame_datos,)  
nombre_c.config(bg="green3", fg="blue3", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=160)

# texto especialidad

nacimiento= Label(frame_datos, text="Especialidad:")
nacimiento.config(bg = "red3",fg="black", font=("Helvetica", 20))
nacimiento.place(x=10,y=200)

# caja de texto para especialidad
nombre_c = Entry(frame_datos,)  
nombre_c.config(bg="green3", fg="blue3", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=200)

# boton para img
bt_img = Button(frame_entrada,image=logo_salud, command=salir)
bt_img.config(bg="White", fg="black", font=("Helvetica", 20))
bt_img.place(x=335, y=35, width=100, height=30)

# logo guanenta
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="blue3")
lb_logo.place(x=10,y=20)

# registro
registro= PhotoImage(file="img/3534139-removebg-preview.png")
lb_regitro= Label(frame_datos, image=registro)
lb_regitro.place(x=110,y=310)



principal.mainloop()