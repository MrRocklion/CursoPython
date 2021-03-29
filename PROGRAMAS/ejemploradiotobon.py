from tkinter import *
from tkinter import messagebox as MessageBox
Data = {}
class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()       
class StartPage(Frame):
    def __init__(self, master):
        def seleccion(valor):
            x = valor
            if x == 1:
                master.switch_frame(Page1)
            elif x == 2:
                master.switch_frame(Page2)
            elif x == 3:
                master.switch_frame(Page3)
            elif x == 4:
                master.switch_frame(Page4)
            
        Frame.__init__(self, master)
        pantalla =  Label(self,text = "PROGRAMA 1 ")
        varOpcion = IntVar()
        pantalla.grid(row =0, columnspan = 2)
        Opcion1 = Radiobutton(self, text = "Crear Cuenta",variable = varOpcion,  value = 1 )
        Opcion1.grid(row = 1, sticky = "w",columnspan = 2)
        Opcion2 = Radiobutton(self, text = "Eliminar Cuenta",variable = varOpcion, value = 2 )
        Opcion2.grid(row = 2,sticky = "w",columnspan = 2)
        Opcion3 = Radiobutton(self, text = "Cambiar Contraseña",variable = varOpcion, value = 3)
        Opcion3.grid(row = 3,sticky = "w",columnspan = 2)
        Opcion4 = Radiobutton(self,text = "Imprimir Base de datos",variable = varOpcion, value = 4)
        Opcion4.grid(row = 4,sticky = "w",columnspan = 2)
        Salir = Button(self, text="SALIR",width = 6 , command =  lambda: master.destroy())
        Salir.grid(row = 5)
        Continuar = Button(self, text="Continuar",width = 8,command=lambda: seleccion(varOpcion.get()))
        Continuar.grid(row = 5, column = 1)
class Page1(Frame):
    def __init__(self, master):
        def crearlista(usuario, Contraseña):
            Data.setdefault(usuario,Contraseña)
            master.switch_frame(StartPage)
            print(Data)
        Frame.__init__(self, master)
        label1 = Label(self, text = "Usuario: ")
        label1.grid(row = 0 , column = 0, sticky = "e")
        text1 = Entry(self)
        text1.grid(row = 0 , column = 1)
        label2 = Label(self, text = "Contraseña: ")
        label2.grid(row = 1 , column = 0, sticky = "e")
        text2 = Entry(self)
        text2.grid(row = 1 , column = 1)
        Continuar = Button(self, text="Siguiente",command=lambda: crearlista(text1.get(),text2.get()))
        Continuar.grid(row=2,columnspan = 2)

class Page2(Frame):
    def __init__(self, master):
        def DelUsuario(usuario, Contraseña):
            if Data.get(usuario) == Contraseña:
                Data.pop(usuario)
                MessageBox.showinfo("Eliminacion de Usuario","Eliminacion Exitosa")
                master.switch_frame(StartPage) #hay que modificar los mensajes de advertencias
            else:
                MessageBox.showerror("Error", "Contraseña  o Usuario Incorrectos")
        Frame.__init__(self, master)
        label0 = Label(self, text = "Ingrese el usuario a eliminar")
        label0.grid(row = 0 , column = 0, columnspan = 2)
        label1 = Label(self, text = "Usuario: ")
        label1.grid(row = 1 , column = 0, sticky = "e")
        text1 = Entry(self)
        text1.grid(row = 1 , column = 1)
        label2 = Label(self, text = "Contraseña: ")
        label2.grid(row = 2 , column = 0, sticky = "e")
        text2 = Entry(self)
        text2.grid(row = 2 , column = 1)
        eliminar = Button(self, text="Eliminar",command=lambda: DelUsuario(text1.get(), text2.get()))
        eliminar.grid(row= 3, column = 1)
        Regresar = Button(self, text="Regresar",command=lambda: master.switch_frame(StartPage))
        Regresar.grid(row=3,column = 0)
class Page3(Frame):
    def __init__(self, master):
        def Contraseña(usuario, Contraseña,ncontraseña):
            if Data.get(usuario) == Contraseña:
                Data[usuario] =  ncontraseña
                MessageBox.showinfo("Cambio de Contraseña","Cambio de Contraseña Exitoso")
                master.switch_frame(StartPage) #hay que modificar los mensajes de advertencias
                print(Data)
            else:
                MessageBox.showerror("Error", "Contraseña  o Usuario Incorrectos")
        Frame.__init__(self, master)
        label0 = Label(self, text = "Cambie la Contraseña")
        label0.grid(row = 0 , column = 0, columnspan = 3)
        label1 = Label(self, text = "Usuario: ")
        label1.grid(row = 1 , column = 0, sticky = "e")
        text1 = Entry(self)
        text1.grid(row = 1 , column = 1)
        label2 = Label(self, text = "Contraseña: ")
        label2.grid(row = 2 , column = 0, sticky = "e")
        text2 = Entry(self)
        text2.grid(row = 2 , column = 1)
        label3 = Label(self, text = "Nueva Contraseña: ")
        label3.grid(row = 3 , column = 0, sticky = "e")
        text3 = Entry(self)
        text3.grid(row = 3, column = 1)
        Continuar = Button(self, text="Cambiar",command=lambda:Contraseña(text1.get(),text2.get(),text3.get()))
        Continuar.grid(row=4,column = 1)
        Regresar = Button(self, text="Regresar",command=lambda: master.switch_frame(StartPage))
        Regresar.grid(row=4,column = 0)
class Page4(Frame):
    def __init__(self, master):
        lista1 = list(Data.keys())
        lista2 = list(Data.values())
        Frame.__init__(self, master)
        titulo = Label(self, text = "Base De Datos: ")
        titulo.grid(row = 0 , columnspan = 2)
        titulo1 = Label(self, text = "Usuarios: ")
        titulo1.grid(row = 1 , column = 0)
        titulo2 = Label(self, text = "Contraseñas: ")
        titulo2.grid(row = 1 , column = 1)
        Usuarios = Label(self, text = "\n".join(lista1))
        Usuarios.grid(row = 2 , column = 0)
        Contraseñas = Label(self, text = "\n".join(lista2))
        Contraseñas.grid(row = 2 , column = 1)
        Regresar = Button(self, text="Regresar",command=lambda: master.switch_frame(StartPage))
        Regresar.grid(row=4,column = 0)
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()