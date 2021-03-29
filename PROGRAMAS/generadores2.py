def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento
ciudades_devueltas = devuelve_ciudades("loja", "quito" ,"cuenca", "guayaquil")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


