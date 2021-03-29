def Generador(limites):
    num=1;
    milista1 = []
    while num<limites :
        milista1.append(num*2)
        num = num+1
    return milista1
print(Generador(20))

def ge(limites):
    num=1;
    milista1 = []
    while num<limites :
        yield num*2
        num = num+1
devuelve = ge(10)

print(next(devuelve))
print(next(devuelve))
print(next(devuelve))