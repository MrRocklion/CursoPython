from tkinter import *
#creacion dela ventana
root = Tk()
root.title("CHERNOBYL Y2K 2021 REMASTERIZADO")
frame1 = Frame(root, width = 1080 , height = 720)
frame1.pack()
#declaracion de variables
numpatalla = StringVar()
resultado = 0
operacion = " "
caso = " "
#declaracion de entrys
#------------------pantalla-------------------------------
pantalla =  Entry(frame1,textvariable = numpatalla)
pantalla.grid(row = 1 , column = 1, padx = 10 , pady = 10 ,columnspan = 4)
pantalla.config(bg ="#354652" , fg =  "white" ,justify = "right")
#-----------------funciones-------------------------------
def numero(num):
    global operacion 
    if(operacion != " "):
        numpatalla.set(num)
        operacion =" "
    else:
        numpatalla.set(numpatalla.get()+ num)
def suma(num):
    global operacion 
    global resultado
    global caso
    resultado += float(num)
    operacion = "suma"
    caso = "suma"
    numpatalla.set(resultado)
def rest(num):
    global operacion
    global resultado
    global caso
    resultado =  float(num) - resultado
    operacion ="resta"
    caso = "resta"
    numpatalla.set(resultado)
def multiplicacion(num):
    global operacion
    global resultado
    global caso
    resultado = 1
    resultado = float(num)*resultado
    operacion ="multiplicacion"
    caso = "multiplicacion"
    numpatalla.set(resultado)
def division(num):
    global operacion
    global resultado
    global caso
    resultado = 1 
    resultado =  float(num)/resultado 
    operacion ="division"
    caso = "division"
    numpatalla.set(resultado)        
def elresultado():
    global resultado
    global operacion
    if(caso == "suma"):
        numpatalla.set(resultado + float(numpatalla.get()))
        resultado = 0
    elif(caso == "resta"):
        numpatalla.set(resultado - float(numpatalla.get()))
        resultado = 0 
    elif(caso == "multiplicacion"):
        numpatalla.set(resultado * float(numpatalla.get()))
        resultado = 0
    elif(caso == "division"):
        numpatalla.set(resultado / float(numpatalla.get()))
        resultado = 0                 
#--------------------fila 1-------------------------------
boton7 = Button(frame1, text="7",width = 3, command = lambda:numero("7") )
boton7.grid(row = 2 , column = 1)
boton8 = Button(frame1, text="8",width = 3, command = lambda:numero("8") )
boton8.grid(row = 2 , column = 2)
boton9 = Button(frame1, text="9",width = 3, command = lambda:numero("9") )
boton9.grid(row = 2 , column = 3)
div = Button(frame1, text="/",width = 3, command = lambda:division(numpatalla.get()))
div.grid(row = 2 , column = 4)
#--------------------fila 2-------------------------------
boton4 = Button(frame1, text="4",width = 3 , command = lambda:numero("4") )
boton4.grid(row = 3 , column = 1)
boton5 = Button(frame1, text="5",width = 3 , command = lambda:numero("5") )
boton5.grid(row = 3 , column = 2)
boton6 = Button(frame1, text="6",width = 3, command = lambda:numero("6")  )
boton6.grid(row = 3 , column = 3)
multi = Button(frame1, text="X",width = 3, command = lambda:multiplicacion(numpatalla.get()))
multi.grid(row = 3 , column = 4)
#--------------------fila 3-------------------------------
boton1 = Button(frame1, text="1",width = 3, command = lambda:numero("1")  )
boton1.grid(row = 4 , column = 1)
boton2 = Button(frame1, text="2",width = 3, command = lambda:numero("2") )
boton2.grid(row = 4 , column = 2)
boton3 = Button(frame1, text="3",width = 3, command = lambda:numero("3")  )
boton3.grid(row = 4 , column = 3)
resta = Button(frame1, text="-",width = 3 , command = lambda:rest(numpatalla.get()))
resta.grid(row = 4 , column = 4)
#--------------------fila 4-------------------------------
boton0 = Button(frame1, text="0",width = 3, command = lambda:numero("0") )
boton0.grid(row = 5 , column = 1)
botonpunto = Button(frame1, text=".",width = 3, command = lambda:numero("c") )
botonpunto.grid(row = 5 , column = 2)
igual = Button(frame1, text="=",width = 3 , command = lambda:elresultado())
igual.grid(row = 5 , column = 3)
mas = Button(frame1, text="+",width = 3, command = lambda:suma(numpatalla.get()) )
mas.grid(row = 5 , column = 4)


root.mainloop()