import codecs


class Equipo (object):

    def __init__(self, nom, ciu, camp, numj):
        self.nombre = nom
        self.ciudad = ciu
        self.campeonatos = int(camp)
        self.numjugadores = int(numj)

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

    def __str__(self):
        """
        """
        return "%s  %s %d %d" % (self.nombre, self.ciudad, self.campeonatos, self.numjugadores)

    def __repr__(self):
        """
        """
        return "%s %s %d %d" % (self.nombre, self.ciudad, self.campeonatos, self.numjugadores)


class Operaciones(object):
    def __init__(self, listado):
        self.listado_equipo = listado

    def ordenar(self):
        """
        """

        return sorted(self.listado_equipo, key=lambda equipo: equipo.nombre)
    def ordenar2(self):
        """
        """

        return sorted(self.listado_equipo, key=lambda equipo: equipo.campeonatos)


class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("ordenamiento.csv", "a")


    def setInformacion(self, p):
        self.archivo.write()

    def cerrar_archivo(self):
        self.archivo.close()

