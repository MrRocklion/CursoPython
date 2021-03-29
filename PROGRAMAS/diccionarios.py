
lista1= ["nombre","apellido","edad","estudia"]
lista2= ["david","diaz",19,True]
diccionario =  dict(zip(lista1,lista2))
print(diccionario)

dic2={"David":1999}
print(dic2["David"])

dic1={"Alemania":"berlin","francia":"Paris","estados unido":"washington","inglaterra":"Londres","españa":"madrid"}
print(dic1.values()) #imprime los valores 
print(dic1.keys())#imprime las claves 
print(len(dic1))


dic3 = {"David":"Diaz"}
dic4 = dic3.copy()
print(dic4)
dic4.clear()
print(dic4)

dic5 = dict.fromkeys(["m","i","g","u","e","l"],1)
print(dic5)

dic6 = {"m":1,"i":2,"g":3,"u":4,"e":5,"l":6}
x = dic6.get("g")
print(x)


dic7 = {"a":1,"b":2,"c":3,"d":4,"e":5}
print(dic7)
dic8 = {"a":1,"b":39,"c":3,"d":150,"e":5,"f":85}
dic7.update(dic8)
print("este es el diccionario actualizado: ", dic7)
##explicacion del pop)()
dic8 =  {"a":1,"b":2,"c":3,"d":4,"e":5}
print(dic8)
dic8.pop("c")
print(dic8)
##explicacion set default()
dic9 =  {"a":1,"b":2,"c":3,"d":4,"e":5}
print(dic9)
dic9.setdefault("david",1907)
print(dic9)
##cambio de clave
dic10 = {"auto":"BMW","marcha":1 ,"encendido":True,"TemperaturaMotor":35.4}
print(dic10)
dic10["auto"] = "grandvitara"
lista4 = list(dic10.keys())
lista5 = list(dic10.values())

for i in range(len(lista4)):
    print(lista4[i])
