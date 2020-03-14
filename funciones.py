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

#MODULO 2 

from clases import Barco
from clases import Buque_3_pos
from clases import Buque_2_pos
from clases import Submarino
from random import randint


def Generar_sub_marino(lista_barcos,lista_ady,lista_submarinos):

    Coordenadas= [randint(1,10), randint(1,10)]
    longitud= 1
    if not Coordenadas in lista_barcos and not Coordenadas in lista_ady:
        lista_barcos.append(Coordenadas)
        lista_ady.append([Coordenadas[0]+1,Coordenadas[1]])
        lista_ady.append([Coordenadas[0]-1,Coordenadas[1]])
        lista_ady.append([Coordenadas[0],Coordenadas[1]+1])
        lista_ady.append([Coordenadas[0],Coordenadas[1]-1])
        lista_ady.append([Coordenadas[0]+1,Coordenadas[1]+1])
        lista_ady.append([Coordenadas[0]-1,Coordenadas[1]-1])
        lista_ady.append([Coordenadas[0]-1,Coordenadas[1]+1])
        lista_ady.append([Coordenadas[0]+1,Coordenadas[1]-1])
        submarinos= Submarino(1,Coordenadas)
        lista_submarinos.append(submarinos)

def generar_buque_2_pos(lista_barcos,lista_ady,lista_buques_2):
    while True:
        Coordenadas= [randint(1,10),randint(1,10)]
        longitud=2
        if Coordenadas in lista_barcos or Coordenadas in lista_ady:
            continue
        if not Coordenadas in lista_barcos and not Coordenadas in lista_ady:
            cont=0 
            lista_xy=[]
            while True:
                cont+=1
                up_down= randint(0,1)
                if up_down==0:
                    if not [Coordenadas[0],Coordenadas[1]+1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]+1] in lista_ady and Coordenadas[1]+1 <=10:
                        Coordenadas_2= [Coordenadas[0],Coordenadas[1]+1]
                        sgda_coordenada= True
                        break
                    elif not [Coordenadas[0],Coordenadas[1]-1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]-1] in lista_ady and Coordenadas[1]-1 >= 1 :
                        Coordenadas_2= [Coordenadas[0],Coordenadas[1]-1]
                        sgda_coordenada= True
                        break
                    else:
                        sgda_coordenada=False
                        up_down=1

                if up_down==1:
                    if not [Coordenadas[0]+1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]+1,Coordenadas[1]] in lista_ady and Coordenadas[0]+1 <=10:
                        Coordenadas_2= [Coordenadas[0]+1,Coordenadas[1]]
                        sgda_coordenada= True
                        break
                    elif not [Coordenadas[0]-1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]-1,Coordenadas[1]] in lista_ady and Coordenadas[0]-1 >= 1 :
                        Coordenadas_2= [Coordenadas[0]-1,Coordenadas[1]]
                        sgda_coordenada= True
                        break
                    else:
                        sgda_coordenada=False
                        up_down=0
                if cont>2: 
                    break
            if sgda_coordenada: 
                break 
            if not sgda_coordenada: 
                continue
    lista_xy.append([Coordenadas,Coordenadas_2])
    lista_barcos.append(Coordenadas)
    lista_barcos.append(Coordenadas_2)
    buque_2pos= Buque_2_pos(longitud,lista_xy)
    lista_buques_2.append(buque_2pos)
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]])
    lista_ady.append([Coordenadas[0],Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0],Coordenadas[1]-1])
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]-1])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]-1])

    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]])
    lista_ady.append([Coordenadas_2[0],Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0],Coordenadas_2[1]-1])
    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]-1])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]-1])
            

def generar_buque_3_pos(lista_barcos,lista_ady,lista_carguero):
    while True:
        Coordenadas= [randint(1,10),randint(1,10)]
        longitud=2
        if Coordenadas in lista_barcos or Coordenadas in lista_ady:
            continue
        if not Coordenadas in lista_barcos and not Coordenadas in lista_ady:
            cont=0 
            lista_xy=[]
            while True:
                cont+=1
                up_down= randint(0,1)
                ir_abajo= False
                ir_boquita= False
                ir_derecha= False
                ir_izquierda= False
                sgda_coordenada=False 
                tra_coordenada= False
                if up_down==0:
                
                    if not [Coordenadas[0],Coordenadas[1]+1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]+1] in lista_ady and Coordenadas[1]+1 <=10:
                        Coordenadas_2= [Coordenadas[0],Coordenadas[1]+1]
                        sgda_coordenada= True 
                        ir_abajo= True
                        break
                    elif not [Coordenadas[0],Coordenadas[1]-1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]-1] in lista_ady and Coordenadas[1]-1 >= 1 :
                        Coordenadas_2= [Coordenadas[0],Coordenadas[1]-1]
                        sgda_coordenada= True
                        ir_boquita= True
                        break
                if up_down==1:
                    if not [Coordenadas[0]+1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]+1,Coordenadas[1]] in lista_ady and Coordenadas[0]+1 <=10:
                        Coordenadas_2= [Coordenadas[0]+1,Coordenadas[1]]
                        sgda_coordenada= True
                        ir_derecha= True
                        break
                    elif not [Coordenadas[0]-1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]-1,Coordenadas[1]] in lista_ady and Coordenadas[0]-1 >= 1 :
                        Coordenadas_2= [Coordenadas[0]-1,Coordenadas[1]]
                        sgda_coordenada= True
                        ir_izquierda= True
                        break
                if cont> 2:
                    break
            if not sgda_coordenada:
                continue
            else:
                if ir_abajo:
                    if not [Coordenadas_2[0],Coordenadas_2[1]+1] in lista_barcos and not [Coordenadas_2[0],Coordenadas_2[1]+1] in lista_ady and Coordenadas_2[1]+1 <= 10:
                        Coordenadas_3=[Coordenadas_2[0],Coordenadas_2[1]+1]
                        tra_coordenada=True
                    elif not [Coordenadas[0],Coordenadas[1]-1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]-1] in lista_ady and Coordenadas[1]-1 >= 1:
                        Coordenadas_3=[Coordenadas[0],Coordenadas[1]-1]
                        tra_coordenada=True
                if ir_boquita:
                    if not [Coordenadas_2[0],Coordenadas_2[1]-1] in lista_barcos and not [Coordenadas_2[0],Coordenadas_2[1]-1] in lista_ady and Coordenadas_2[1]-1 >= 1:
                        Coordenadas_3=[Coordenadas_2[0],Coordenadas_2[1]-1]
                        tra_coordenada=True
                    elif not [Coordenadas[0],Coordenadas[1]+1] in lista_barcos and not [Coordenadas[0],Coordenadas[1]+1] in lista_ady and Coordenadas[1]+1 <= 10:
                        Coordenadas_3=[Coordenadas[0],Coordenadas[1]+1]
                        tra_coordenada=True 
                if ir_derecha:
                    if not [Coordenadas_2[0]+1,Coordenadas_2[1]] in lista_barcos and not [Coordenadas_2[0]+1,Coordenadas_2[1]] in lista_ady and Coordenadas_2[0]+1 <=10:
                        Coordenadas_3= [Coordenadas_2[0]+1,Coordenadas_2[1]]
                        tra_coordenada= True
                    elif not [Coordenadas[0]-1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]-1,Coordenadas[1]] in lista_ady and Coordenadas[0]-1 >= 1 :
                        Coordenadas_3= [Coordenadas[0]-1,Coordenadas[1]]
                        tra_coordenada= True    
                if ir_izquierda:
                    if not [Coordenadas_2[0]-1,Coordenadas_2[1]] in lista_barcos and not [Coordenadas_2[0]-1,Coordenadas_2[1]] in lista_ady and Coordenadas_2[0]-1 >=1:
                        Coordenadas_3= [Coordenadas_2[0]-1,Coordenadas_2[1]]
                        tra_coordenada= True
                    elif not [Coordenadas[0]+1,Coordenadas[1]] in lista_barcos and not [Coordenadas[0]+1,Coordenadas[1]] in lista_ady and Coordenadas[0]+1 <= 10 :
                        Coordenadas_3= [Coordenadas[0]+1,Coordenadas[1]]
                        tra_coordenada= True  

                if not tra_coordenada:
                    continue
                else:
                    break
    lista_xy.append([Coordenadas,Coordenadas_2,Coordenadas_3])
    lista_barcos.append(Coordenadas)
    lista_barcos.append(Coordenadas_2)
    lista_barcos.append(Coordenadas_3)
    buque_3_pos= Buque_3_pos(longitud,lista_xy)
    lista_carguero.append(buque_3_pos)
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]])
    lista_ady.append([Coordenadas[0],Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0],Coordenadas[1]-1])
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]-1])
    lista_ady.append([Coordenadas[0]-1,Coordenadas[1]+1])
    lista_ady.append([Coordenadas[0]+1,Coordenadas[1]-1])

    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]])
    lista_ady.append([Coordenadas_2[0],Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0],Coordenadas_2[1]-1])
    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]-1])
    lista_ady.append([Coordenadas_2[0]-1,Coordenadas_2[1]+1])
    lista_ady.append([Coordenadas_2[0]+1,Coordenadas_2[1]-1])

    lista_ady.append([Coordenadas_3[0]+1,Coordenadas_3[1]])
    lista_ady.append([Coordenadas_3[0]-1,Coordenadas_3[1]])
    lista_ady.append([Coordenadas_3[0],Coordenadas_3[1]+1])
    lista_ady.append([Coordenadas_3[0],Coordenadas_3[1]-1])
    lista_ady.append([Coordenadas_3[0]+1,Coordenadas_3[1]+1])
    lista_ady.append([Coordenadas_3[0]-1,Coordenadas_3[1]-1])
    lista_ady.append([Coordenadas_3[0]-1,Coordenadas_3[1]+1])
    lista_ady.append([Coordenadas_3[0]+1,Coordenadas_3[1]-1])

                      
                        
                         


lista_carguero=[]
lista_buques_2=[]
lista_submarinos=[]
lista_barcos=[]
lista_ady=[]
while len(lista_barcos)<4:
    Generar_sub_marino(lista_barcos,lista_ady,lista_submarinos)

generar_buque_2_pos(lista_barcos,lista_ady,lista_buques_2) 
generar_buque_3_pos(lista_barcos,lista_ady,lista_carguero)

# print(lista_barcos)
# print(lista_ady)
# print(lista_submarinos)
# print(lista_buques_2)
# print(lista_carguero)