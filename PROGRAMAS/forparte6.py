
valido = False
email = input("introduce tu imail: ")
x = len(email)
print(x)
for i in range(len(email)):
    print(email[i])
    if email[i] == "@":
        valido = True 

if valido:
    print("email correcto")

else:

    print("email incorrecto")

#bucles while
i=1
while(i<=10):
    print(i)
    i= i+1

edad = int(input("ingresa tu edad: "))

while edad<5 or edad>100:
    print("dato erroneo: ")
    edad = int(input("ingresa tu edad: "))
print("edad del usuario: "+ str(edad))
