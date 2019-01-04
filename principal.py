from modelado.mimodelo import Equipo, Operaciones ,MiArchivo, MiArchivoEscribir

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_equipo = []

for d in lista:
    p = Equipo(d[0], d[1], d[2], d[3])
    lista_equipo.append(p)

operacion = Operaciones(lista_equipo)
lista_ordenada = operacion.ordenar()
print(lista_ordenada)
lista_ordenada2 = operacion.ordenar2()
print(lista_ordenada2)

