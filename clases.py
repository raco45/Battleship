#modulo 1 

class Usuario:

    def __init__(self, nombre_de_usuario, nombre_completo, edad, genero, puntos_acumulados,disparos):
        self.nombre_de_usuario= nombre_de_usuario
        self.nombre_completo= nombre_completo
        self.edad= edad
        self.genero= genero
        self.puntos_acumulados= puntos_acumulados
        self.disparos = disparos

#MODULO2 

class Barco():

    def __init__(self,longitud, coordenadas):
        self.longitud= longitud
        self.coordenadas= coordenadas
    
class Submarino(Barco):
    def __init__(self,longitud,coordenadas):
        Barco.__init__(self,longitud,coordenadas)
    
    def Sumergirse(self):
        print("Tiene la capacidad de poder sumergirse y emerger del agua ")

class Buque_2_pos(Barco):
    def __init__(self,longitud,coordenadas):
        Barco.__init__(self, longitud,coordenadas)
   
    def Comunicacion(self):
        print("Tiene la capacidad de comunicarse con tierra y los otros miembros de la flota")

class Buque_3_pos(Barco):
    def __init__(self,longitud,coordenadas):
        Barco.__init__(self,longitud,coordenadas) 
    
    def Transporte(self):
        print("Cuenta con un helipuerto para el transporte de tropas")
    