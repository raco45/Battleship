#modulo 1 
from clases import Usuario

def nombre_de_usuario():
    """Esta funcion se encarga de pedir el nombre de usuario que se desea utilizar.
    
    Returns:
        string -- nombre de usuario ingresado.
    """    
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
    """ Esta funcion se encarga de pedir el nombre completo del usuario.
    
    Returns:
        String -- Nombre completo ingresedo por el usuario.
    """
    resp=True
    while resp==True:
        nombre= (input(" por favor ingrese su nombre: ")).strip()
        if nombre.isalpha():
            break
        if len(nombre) < 2 or nombre.isdigit() or " " in nombre:
            print("no valido")
            continue
        
    while True:    
        nombre2=(input(" ingrese su segundo nombre (si tiene): ")).strip()
        if nombre2=="":
            break
        if nombre2.isalpha():
            break
        if len(nombre2) < 2 or nombre2.isdigit() or " " in nombre2:
            print("no valido")
            continue
    resp2=True
    while resp2==True:
        apellido= (input(" ingrese su apellido: ")).strip()
        if len(apellido) < 2 or apellido.isdigit() or " " in apellido:
            print("No valido")
            continue
        if apellido.isalpha():
            break
        
    while True:
        apellido2= (input(" ingrese su segundo apellido (opcional): ")).strip()
        if apellido2=="":
            break
        if len(apellido2) < 2 or apellido2.isdigit() or " " in apellido2:
            print('No valido')
            continue
        if apellido2.isalpha():
            break

    Full_name=(" {} {} {} {}".format(nombre.title(),nombre2.title(),apellido.title(),apellido2.title()))
    return Full_name


def edad_usuario():
    """Esta funcion se encarga de pedir la edad al usuario.
    
    Returns:
        String -- Edad ingresada por el usuario.
    """
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
    """Esta funcion se encarga de preguntar el genero del usuario.
    
    Returns:
        String -- Genero ingresado por el usuario.
    """
    resp=True
    while resp:
        genero=(input("""Por favor indique su genero :
        1) Masculino
        2) Femenino
        3) Otro
        ==>  """))
        
        if genero=="1":
            genero="Masculino"
            break
        if genero=="2":
            genero="Femenino"
            break
        if genero=="3":
            genero="Otro"
            break
        
        else:
            print(" ese genero no lo conozco ")
    return genero.strip()

def puntos_acumulados():
    puntos=0 
    return puntos



def registrar_usuario(Datos_de_usuario,usernames):
    """ Esta funcion se encarga de registra la informacion del usuario en una variable tipo objeto.
    
    Arguments:
        Datos_de_usuario {list} -- [En esta lista se va a guardar los variables de usuario tipo objeto]
        usernames {list} -- [En esta lista se guardan los nombres de usuario que se han registrado ]
    
    Returns:
        retorna una lista de objetos y una varible de objetos. 

    """  

    username= nombre_de_usuario()
    if username in usernames:
        print("Nombre de usuario ya registrado")
        indice_del_usuario=usernames.index(username)
        nuevo_usuario= Datos_de_usuario[indice_del_usuario]
        print("""
        Nombre de usuario: {}
        Nombre del jugador: {}
        Edad: {}
        Genero: {}
        Puntos: {}""".format(nuevo_usuario.nombre_de_usuario,nuevo_usuario.nombre_completo,nuevo_usuario.edad,nuevo_usuario.genero,nuevo_usuario.puntos_acumulados))
        return Datos_de_usuario,nuevo_usuario
        
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
    nuevo_usuario= Usuario(username,name,age,gender,points,0)
    Datos_de_usuario.append(nuevo_usuario)
    return Datos_de_usuario,nuevo_usuario

#MODULO 2 

from clases import Barco
from clases import Buque_3_pos
from clases import Buque_2_pos
from clases import Submarino
from random import randint


def Generar_sub_marino(lista_barcos,lista_ady,lista_submarinos):
    """[Esta funcions e encarga de generar las coordenadas en las que los submarinos van a estar colocados.]
    
    Arguments:
        lista_barcos {[lista]} -- [en esta lista se guardan las coordenadas de los barcos una vez generadas.]
        lista_ady {[lista]} -- [en esta lista se guardan las coordenas adyacentes a la coordenada donde se genero el submarino.]
        lista_submarinos {[lista de objetos]} -- [En esta lista se guardan los submarinos como objetos]
    
    
    """

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
    """[Esta funcion se encarga generar las coordenadas en las que el buque de dos posiciones va estar colocado.]
    
    Arguments:
        lista_barcos {[lista]} -- [en esta lista se guardan las coordenadas de los barcos una vez generadas.]
        lista_ady {[lista]} -- [en esta lista se guardan las coordenas adyacentes a la coordenada donde se genero el barco.]
        lista_buques_2 {[lista de objetos]} -- [En esta lista se guardan el buque de dos posiciones como un objeto]
    
    """
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
    """[Esta funcion se encarga generar las coordenadas en las que el buque de tres posiciones va estar colocado.]
    
    Arguments:
        lista_barcos {[lista]} -- [en esta lista se guardan las coordenadas de los barcos una vez generadas.]
        lista_ady {[lista]} -- [en esta lista se guardan las coordenas adyacentes a la coordenada donde se genero el barco.]
        lista_carguero {[lista de objetos]} -- [En esta lista se guarda el buque de 3 posiciones como un objeto]
    
    
    """
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

#MODULO 3 

def editar_informacion(user_objeto, Datos_de_usuario):
    """[Esta funcion se encarga de actualizar la informacion del usuario.]
    
    Arguments:
        user_objeto {[Variable de tipo objeto]} -- [Almacena la informacion de cada usaurio.]
        Datos_de_usuario {[lista]} -- [En esta lista se va a guardar los variables de usuario tipo objeto]
    """   
    while True:
        pos= Datos_de_usuario.index(user_objeto)
        cambio=input("""Que dato quiere cambiar
        1-Nombre completo
        2-Edad
        3-Genero
        >>>>    """)
        if cambio=="1":
            user_objeto.nombre_completo= nombre_completo()
            Datos_de_usuario[pos]=user_objeto
            cont= input("¿Desea continuar editando su informacion? (S/N): ")
            if cont.lower()=="s":
                continue
            if cont.lower()=="n":
                break
        if cambio=="2":
            user_objeto.edad=edad_usuario()
            Datos_de_usuario[pos]= user_objeto
            cont= input("¿Desea continuar editando su informacion? (S/N): ")
            if cont.lower()=="s":
                continue
            if cont.lower()=="n":
                break
        if cambio=="3":
            user_objeto.genero= genero_usuario()
            Datos_de_usuario[pos]=user_objeto
            cont= input("¿Desea continuar editando su informacion? (S/N): ")
            if cont.lower()=="s":
                continue
            if cont.lower()=="n":
                break
def rango_edad(Datos_de_usuario):
    """[Esta funcion se encarga de identificar el rango de edad en la que que ecuentran los jugadores.]
    
    Arguments:
        Datos_de_usuario {[lista]} -- [En esta lista se va a guardar los variables de usuario tipo objeto]
        
        
    """           
    suma_edades=0
    cont_primer_rango=0
    cont_segundo_rango=0
    cont_tercero_rango=0
    cont_cuarto_rango=0
    
    for edad in Datos_de_usuario:
        if int(edad.edad) in range(5,19):
            
            cont_primer_rango+=1
        elif int(edad.edad) in range(19,46):
            cont_segundo_rango+=1
            
        elif int(edad.edad) in range(46,61):
            cont_tercero_rango+=1
            
        elif int(edad.edad) in range(62,101):
            cont_cuarto_rango+=1
            
    if cont_primer_rango > cont_segundo_rango and cont_primer_rango > cont_tercero_rango and cont_primer_rango > cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [5-18] ")
        
    elif cont_segundo_rango > cont_primer_rango and cont_segundo_rango > cont_tercero_rango and cont_segundo_rango > cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [19-45] ")
        
    elif cont_tercero_rango > cont_primer_rango and cont_tercero_rango > cont_segundo_rango and cont_tercero_rango > cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [46-60] ")
        
    elif cont_cuarto_rango > cont_primer_rango and cont_cuarto_rango > cont_segundo_rango and cont_cuarto_rango > cont_tercero_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [61-100] ")
        

    elif cont_primer_rango==cont_segundo_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [5-18] y [19-45] ")
    elif cont_primer_rango==cont_tercero_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [5-18] y [46-60] ")
    elif cont_primer_rango==cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [5-18] y [61-100] ")

    elif cont_segundo_rango==cont_primer_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [19-45] y [5-18] ")
    elif cont_segundo_rango==cont_tercero_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [19-45] y [46-60] ")
    elif cont_segundo_rango==cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [19-45] y [61-100] ")

    elif cont_tercero_rango==cont_primer_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [46-60] y [5-18] ")
    elif cont_tercero_rango==cont_segundo_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [46-60] y [19-45] ")
    elif cont_tercero_rango==cont_cuarto_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [46-60] y [61-100] ")
    
    elif cont_cuarto_rango==cont_primer_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [61-100] y [5-18] ")
    elif cont_cuarto_rango==cont_segundo_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [61-100] y [19-45] ")
    elif cont_cuarto_rango==cont_tercero_rango:
        print("Los usuarios que mas juegan se encuentran entre las edades de [61-100] y [46-60] ")
    
def cant_puntos_genero(Datos_de_usuario):
    """[Esta funcion se encarga de contar la cantidad de puntos hay por genero.]
    
    Arguments:
        Datos_de_usuario {[lista]} -- [En esta lista se va a guardar los variables de usuario tipo objeto]
    
    """
    punt_masc=0
    punt_fem=0
    punt_otro=0 
    for dato in Datos_de_usuario:
        if dato.genero=="Masculino":
            punt_masc+= int(dato.puntos_acumulados)
        if dato.genero=="Femenino":
            punt_fem+=int(dato.puntos_acumulados)
        if dato.genero=="Otro":
            punt_otro+=int(dato.puntos_acumulados)
    print("""    
Puntos totales por genero:
Masculino: {} pts
Femenino: {} pts
Otro: {} pts
""".format(punt_masc,punt_fem,punt_otro))

def promedio_disparos(disparos_acum,juegos):
    """[Esta funcion se encarga de sacar el promedio de disparos que hay por partida.]
    
    Arguments:
        disparos_acum {[int]} -- [se encarga de ir contando la cantidad de disparos que se realizan.]
        juegos {[int]} -- [Se encarga de ir contando las partidas que se han jugado. ]
    
    """
    try:
        prom= float(disparos_acum)/float(juegos)
    except:
        prom=0
    print("""En promedio se necesitan {} disparos para ganar""".format(round(prom,2)))
    


def insertion_sort(arr):
    """[Se utilizo este algoritmo de sorteo para realizar el top 10 de los usuarios con los mejores puntajes]
    
    Arguments:
        arr {[lista]} -- [aqui se guardan los usuarios.]
    
    Returns:
        [lista] -- [Se retorna la lista en orden de mayor a menor puntaje]
    """
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1].puntos_acumulados > cursor.puntos_acumulados:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr[::-1]
        

        




            