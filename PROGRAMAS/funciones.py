#manejo de funciones 
def suma(a,b):
    resultado =a+b
    return resultado        
#manejo de listas 
x = suma(19,85)
print(x)
lista = ["a","b","c","d","d","e","f","g","h"]
lista1 = [1,2,3,4]
lista.extend(["i","j","k"])
print(lista[:])
lista.remove("g") #quita el elemento g de la lista
lista.pop() #quita el ultimo elemento de la lista
print(lista[:])
#manejo de tuplas
lista2 = tuple(lista) #convierte la lista en tuppla
lista3 = lista + lista1  #suma dos listas
print(lista3[:])
print(lista2)
print("b" in lista2)
print("k" in lista2) #me dice si esta este elemento en una tupla
print(lista2.count("d"))
print(len(lista2)) #me dice la cantidad de elementos de mi tupla 
print(lista2[3])
#programacion de diccionarios clave:valor
dic1={"Alemania":"berlin","francia":"Paris","estados unido":"washington","inglaterra":"Londres","españa":"madrid"}
print(dic1["francia"])
print(dic1["Alemania"])
print(dic1.values()) #imprime los valores 
print(dic1.keys())#imprime las claves 
#estructuras condicionales
def examen(nota):
    if nota >=7:
        valoracion="aprobado"
    else:
        valoracion = "reprobado"
    return valoracion
resultado = examen(10)
print(resultado)