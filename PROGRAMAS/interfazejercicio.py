from tkinter import *
#creacion dela ventana

root = Tk()
root.title("Ventana 1 ")
#declaracion de variables
varOpcion = IntVar()

def ventana():
    #etiquetas
    pantalla =  Label(root,text = "PROGRAMA 1 ")
    pantalla.grid(row =0, columnspan = 2)
    #radiobotones
    Opcion1 = Radiobutton(root, text = "Crear Usuario", variable = varOpcion , value = 1 )
    Opcion1.grid(row = 1, sticky = "w",columnspan = 2)  
    Opcion2 = Radiobutton(root, text = "Eliminar Cuenta",variable = varOpcion , value = 2 )
    Opcion2.grid(row = 2,sticky = "w",columnspan = 2)
    Opcion3 = Radiobutton(root, text = "Cambiar Contraseña", variable = varOpcion , value = 3)
    Opcion3.grid(row = 3,sticky = "w",columnspan = 2)
    Opcion4 = Radiobutton(root, text = "Imprimir Base de datos",variable = varOpcion , value = 4)
    Opcion4.grid(row = 4,sticky = "w",columnspan = 2)
#botones
    Salir = Button(root, text="SALIR",width = 6  )
    Salir.grid(row = 5)
    Continuar = Button(root, text="Continuar",width = 8 , command = lambda:ventana1()  )
    Continuar.grid(row = 5, column = 1)

def ventana1():
    root.withdraw()
    ven1 = Toplevel()
    

ventana()
root.mainloop()