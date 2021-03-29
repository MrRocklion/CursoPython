def divide():
    try:
        n1 = float(input("introduce el primer numero: "))
        n2 = float(input("introduce el segundo numero: "))
        print("resultado: " + str(n1/n2))
    except ValueError:
        print("error de syntaxis")
    except ZeroDivisionError:
        print("No se puede dividir para cero")
    
    print("calculo finalizado")

divide()
