from tkinter import *
raiz = Tk()
raiz.title("CHERNOBYL Y2K 2021 REMASTERIZADO")
raiz.iconbitmap("rem.ico.ico")
frame1 = Frame(raiz)
frame1.pack(fill = "both", expand= "True")
frame1.config(width ="1080" , height = "720", bg ="#354652" )
#textos
Label(frame1, text ="INTERFAZ GRAFICA 1",fg="white",bg ="#354652" ,font=(18)).place(x=470, y=100)
#imagenes
imagen1 = PhotoImage(file = "megumin1.png")
imagen1_sub = imagen1.subsample(3)
Label(frame1, image = imagen1_sub,bg ="#354652").place(x = 100 , y = 100)
imagen2 = PhotoImage(file = "waifu1.png")
imagen2_sub = imagen2.subsample(3)
Label(frame1, image = imagen2_sub,bg ="#354652").place(x = 800 , y = 100)
#cuadros de texto
text1 = Entry(frame1)
text1.place(x=490 , y= 130)

raiz.mainloop()