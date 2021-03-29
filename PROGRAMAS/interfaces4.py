from tkinter import *
#creacion dela ventana
root = Tk()
root.title("CHERNOBYL Y2K 2021 REMASTERIZADO")
frame1 = Frame(root, width = 1080 , height = 720)
frame1.grid()
#declaracion de variables
varOpcion = IntVar()
#funciones
def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text = "masculinoo")
    else:
        etiqueta.config(text = "femenino")
#etiquetas y botones
Label(frame1 , text= "Genero: ").pack()
Radiobutton(frame1, text = "masculino", variable = varOpcion , value = 1, command = imprimir ).pack()
Radiobutton(frame1, text = "femenino",variable = varOpcion , value = 2, command = imprimir).pack()
etiqueta =  Label(frame1)
etiqueta.pack()
root.mainloop()