from tkinter import *
root = Tk()
root.title("CHERNOBYL Y2K 2021 REMASTERIZADO")
frame1 = Frame(root, width = 1080 , height = 720)
frame1.pack()
nombre = StringVar()
#etiquetas 
label1 = Label(frame1 , text = "Nombre: ")
label1.grid(row = 0 , column = 0, sticky = "e", padx = 10 , pady = 10 )
label2 = Label(frame1 , text = "Apellido: ")
label2.grid(row = 1 , column = 0,sticky = "e", padx = 10 , pady = 10 )
label3 = Label(frame1 , text = "Contraseña: ")
label3.grid(row = 2 , column = 0,sticky = "e" , padx = 10 , pady = 10 )
label4 = Label(frame1 , text = "Edad: ")
label4.grid(row = 3 , column = 0,sticky = "e" , padx = 10 , pady = 10 )
label5 = Label(frame1 , text = "Comentarios: ")
label5.grid(row = 4 , column = 0,sticky = "e" , padx = 10 , pady = 10 )
label6 = Label(frame1 , textvariable = nombre )
label6.grid(row = 0 , column = 2, sticky = "e", padx = 10 , pady = 10 )

#cuadros de texto
text1 = Entry(frame1)
text1.grid(row = 0 , column = 1, padx = 10 , pady = 10 )
text2 = Entry(frame1)
text2.grid(row = 1 , column = 1, padx = 10 , pady = 10 )
text3 = Entry(frame1)
text3.grid(row = 2 , column = 1, padx = 10 , pady = 10 )
text4 = Entry(frame1)
text4.grid(row = 3 , column = 1, padx = 10 , pady = 10 )
text5 = Text(frame1, width = 16 , height = 5 )
text5.grid(row = 4 , column = 1, padx = 10 , pady = 10 )
scrolvert = Scrollbar(frame1 , command = text5.yview)
scrolvert.grid(row=4 , column = 2,sticky = "nsew") #configura la barra desplazamiento para que se auto ajuste al texto
text5.config(yscrollcommand= scrolvert.set)
#configuracion del boton
def funcion1():
    nombre.set("funciona")

boton1 = Button(root, text = "enviar", command = funcion1 )
boton1.pack()

root.mainloop()