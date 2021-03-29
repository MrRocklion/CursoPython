i=0
Data = {}
while i==0 :
    print(">> 1. Crear Cuenta")
    print(">> 2. Eliminar Cuenta")
    print(">> 3. Cambiar Contraseña")
    print(">> 4. Imprimir Base de datos")
    print(">> 5. Terminar Programa")
    x = int(input("Escoga una opcion entrando el numero :"))
    if x == 1:
        Usuario = input("Ingrese Un Usuario: ")
        Contraseña = input("Ingrese Una Contraseña: ") 
        Data.setdefault(Usuario,Contraseña)
        print(Data)
    elif x == 2:
        print(Data)
        Data.pop(input("ingrese el nombre del usuario que quiere eliminar la cuenta: "))
        print("cuenta eliminada con exito")
        print(Data)
    elif x == 3:
        print(Data)
        name = input("ingrese el usuario que quiere cambiar la contraseña")
        Data[name] = input("ingrese la nueva contraseña: ")
        print("Contraseña Actualizada")
        print(Data)
    elif x == 4:
        print("Base de Datos Actual")
        print(Data)    
    elif x == 5:
        print("termino el programa")
        break    







