from modelado.mimodelo import Equipo, Operaciones ,MiArchivo, MiArchivoEscribir #importacion de las clases en el archivo mimodelo
#declaracion de objetos
m = MiArchivo()
c = MiArchivoEscribir()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_equipo = []
#for para recorrer la lista
for d in lista:
    e = Equipo(d[0], d[1], d[2], d[3])
    lista_equipo.append(e)
#creacion de objeto tipo Operaciones
operacion = Operaciones(lista_equipo)
opc = input("Desea ordenar por nombre o campeonato: ")
lista_ordenada = operacion.ordenar(opc)

#for que recorre la lista ordenada
for g in lista_ordenada:
    c.agregar_informacion(g)#manda la informacion del objeto al metodo agregar informacion
    print(g)

m.cerrar_archivo()
c.cerrar_archivo()





