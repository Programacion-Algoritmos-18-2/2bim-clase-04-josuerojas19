import codecs

#clase Equipo
class Equipo (object):
#constructor que recibe atriutos tipo String e int
    def __init__(self, nom, ciu, camp, numj):
        self.nombre = nom
        self.ciudad = ciu
        self.campeonatos = int(camp)
        self.numjugadores = int(numj)

#metodos agregar y obtener de los atributos
    def agregar_nombre(self, nom):
        """
        """
        self.nombre = nom

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_ciudad(self, ciu):
        """
        """
        self.ciudad = ciu

    def obtener_ciudad(self):
        """
        """
        return self.ciudad

    def agregar_campeonato(self, camp):
        """
        """
        self.campeonatos = int(camp)

    def obtener_campeonato(self):
        """
        """
        return self.campeonatos

    def agregar_numerojuga(self, numj):
        """
        """
        self.numjugadores = int(numj)

    def obtener_numerojuga(self):
        """
        """
        return self.numjugadores

#sSe sobreescribe el metodo str
    def __str__(self):
        """
        """
        return "%s  %s %d %d" % (self.nombre, self.ciudad, self.campeonatos, self.numjugadores)

    def __repr__(self):
        """
        """
        return "%s %s %d %d" % (self.nombre, self.ciudad, self.campeonatos, self.numjugadores)

#clase Operaciones
class Operaciones(object):
    #constructor de la clase
    def __init__(self, listado):
        self.listado_equipo = listado

#metodo ordear, para ordenar la lista de acuerdo al usuario
    def ordenar(self, p):
        """
        """
        if p == "nombre":
            return sorted(self.listado_equipo, key=lambda equipo: equipo.nombre)
        else:
            if p == "campeonato":
                return sorted(self.listado_equipo, key=lambda equipo: equipo.campeonatos)

#clase MiArcchivp
class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("informacion.csv", "r")#abre el rchivo
#metodo para la informacion que se encuentra en el archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("ordenamiento.csv", "a") #crea el archivo

#metodo para agregar la informacion al archivo
    def agregar_informacion(self, c):
        self.archivo.write("%s %s %d %d" % (c.nombre, c.ciudad, c.campeonatos, c.numjugadores))

    def cerrar_archivo(self):
        self.archivo.close()

