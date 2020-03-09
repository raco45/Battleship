#modulo 1 

class Usuario:

    def __init__(self, nombre_de_usuario, nombre_completo, edad, genero, puntos_acumulados):
        self.nombre_de_usuario= nombre_de_usuario
        self.nombre_completo= nombre_completo
        self.edad= edad
        self.genero= genero
        self.puntos_acumulados= puntos_acumulados


xanth= Usuario("xanth","Andres",18, "Maculino", 1000)
print(xanth.edad)