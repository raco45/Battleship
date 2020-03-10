#modulo 1 
from clases import Usuario

def nombre_de_usuario():
    contador= True
    user=(input(" Ingrese su nombre de usuario (en miniscula): ")).strip()
    while contador==True:
        
        if " " in user or len(user) > 30 or not user.islower():
            contador=True
            user= input("ingrese un nombre valido: ").strip()
        else:
            contador=False
            return user
        
            


def nombre_completo():
    resp=True
    while resp==True:
        nombre= (input(" por favor ingrese su nombre: ")).strip()
        
        if len(nombre) < 2 :
            print("no valido")
        else:
            resp=False
    nombre2=(input(" ingrese su segundo nombre (si tiene): ")).strip()    
    resp2=True
    while resp2==True:
        apellido= (input(" ingrese su apellido: ")).strip()
        if len(apellido) < 2:
            print("muy corto")
        else:
            resp2=False
    apellido2= (input(" ingrese su segundo apellido (opcional): ")).strip()
    Full_name=(" {} {} {} {}".format(nombre.title(),nombre2.title(),apellido.title(),apellido2.title()))
    return Full_name


def edad_usuario():
    resp= True
    while resp==True:
        edad= (input(" Ingrese su edad: ")).strip()
        if not edad.isdigit():
            print("Por favor ingresa tu edad")
        elif int(edad) < 5 or int(edad)>100:
            print("intenta otra vez ")
        else: 
            return edad
        
def genero_usuario():
    resp=True
    while resp:
        genero=int(input("""Por favor indique su genero :
        1) Masculino
        2) Femenino
        3) Trans
        4) Loca
        5) otro
        ==>  """))
        if genero==1:
            genero="Masculino"
            break
        if genero==2:
            genero="Femenino"
            break
        if genero==3:
            genero="Trans"
            break
        if genero==4: 
            genero="Loca"
            break
        if genero==5:
            genero="Otro"
            break
        else:
            print(" ese genero no lo conozco ")
    return genero.strip()

def puntos_acumulados():
    puntos=0 
    return puntos

def registrar_usuario(Datos_de_usuario):
    
    username= nombre_de_usuario()
    name=nombre_completo()
    age= edad_usuario()
    gender= genero_usuario()
    points= puntos_acumulados()
    print("""
    Nombre de usuario: {}
    Nombre del jugador: {}
    Edad: {}
    Genero: {}
    Puntos: {}""".format(username,name,age,gender,points))
    # Datos_de_usuario[username]= {}
    # Datos_de_usuario[username] ["Nombre"]= name
    # Datos_de_usuario[username] ["Edad"] = age
    # Datos_de_usuario[username] ["Genero"] = gender
    # Datos_de_usuario[username] ["Puntos"]= points
    nuevo_usuario= Usuario(username,name,age,gender,points)
    Datos_de_usuario.append(nuevo_usuario)
    return Datos_de_usuario,nuevo_usuario



