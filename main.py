from clases import Usuario
from clases import Barco
from clases import Submarino
from clases import Buque_2_pos
from clases import Buque_3_pos
from funciones import nombre_de_usuario
from funciones import nombre_completo
from funciones import edad_usuario
from funciones import genero_usuario
from funciones import puntos_acumulados
from funciones import registrar_usuario
from funciones import Generar_sub_marino
from funciones import generar_buque_2_pos
from funciones import generar_buque_3_pos
from funciones import editar_informacion
from funciones import rango_edad
from funciones import cant_puntos_genero
from funciones import promedio_disparos
from funciones import insertion_sort
def main():
    Datos_de_usuario=[]

    print(  
    """ 
         _____  ___  ___  ___  ___   _   _        _____   ___  ___  ___ _____ _____  
        /  ___|/ _ \ |  \/  | / _ \ | \ | |      |  __ \ / _ \ |  \/  ||  ___/  ___| 
        \ `--./ /_\ \| .  . |/ /_\ \|  \| |______| |  \// /_\ \| .  . || |__ \ `--.  
         `--. \  _  || |\/| ||  _  || . ` |______| | __ |  _  || |\/| ||  __| `--. \ 
        /\__/ / | | || |  | || | | || |\  |      | |_\ \| | | || |  | || |___/\__/ / 
        \____/\_| |_/\_|  |_/\_| |_/\_| \_/       \____/\_| |_/\_|  |_/\____/\____/  
                                                                                
                                                                                """ 
                                                                                """

    ______                         _        
    | ___ \                       | |       
    | |_/ / __ ___  ___  ___ _ __ | |_ __ _ 
    |  __/ '__/ _ \/ __|/ _ \ '_ \| __/ _` |
    | |  | | |  __/\__ \  __/ | | | || (_| |
    \_|  |_|  \___||___/\___|_| |_|\__\__,_|
                                                                                                                    """                                                                           )

    print("""  
    O)) O))         O)       O))) O))))))      O)       O))      O))            O)              O)))     O))      O)       O))         O))      O)       O))      
    O)    O))      O) ))          O))         O) ))     O))      O))           O) ))            O) O))   O))     O) ))      O))       O))      O) ))     O))      
    O)     O))    O)  O))         O))        O)  O))    O))      O))          O)  O))           O)) O))  O))    O)  O))      O))     O))      O)  O))    O))      
    O))) O)      O))   O))        O))       O))   O))   O))      O))         O))   O))          O))  O)) O))   O))   O))      O))   O))      O))   O))   O))      
    O)     O))  O)))))) O))       O))      O)))))) O))  O))      O))        O)))))) O))         O))   O) O))  O)))))) O))      O)) O))      O)))))) O))  O))      
    O)      O) O))       O))      O))     O))       O)) O))      O))       O))       O))        O))    O) )) O))       O))      O))))      O))       O)) O))      
    O)))) O)) O))         O))     O))    O))         O))O))))))))O))))))))O))         O))       O))      O))O))         O))      O))      O))         O))O))))))))
    """)


    resp=True
    try:                                          #Abrimos el archivo texto.txt donde se van a ir guardano los datos del usuario.
        with open("texto.txt","r") as base_datos: 
            for fila in base_datos: 
                cuenta= (fila.strip()).split(",")
                user_temp=Usuario(cuenta[0],cuenta[1],cuenta[2],cuenta[3],cuenta[4],cuenta[5])
                Datos_de_usuario.append(user_temp)
    except: 
        Datos_de_usuario=[]
    try:                                         # Abrimos el archivo promedio.txt donde se va a guardar la cantidad de partidas y las cantidad de disparos realizados.
        with open("promedio.txt","r") as base_datos_text:
            for base_datos in base_datos_text:
                juegos=int(base_datos.split(",")[0])
                disparos_acum=int(base_datos.split(",")[1])
    except:
        juegos=0
        disparos_acum=0
    print("><"*30)
            
    print("TOP 10")
    datos_ordenados=insertion_sort(Datos_de_usuario)[0:10]
    for user in datos_ordenados:
        print("{} / {} pts / {} disparos".format(user.nombre_de_usuario, user.puntos_acumulados,user.disparos))



    #MODULO 1 

    while resp:                                         
        usernames=[]
        for user in Datos_de_usuario:                     # Si hay usuarios registrados, los nombres de usuarios se agregan una lista(usernames=[]) .
            usernames.append(user.nombre_de_usuario)
        Entrada=(input(""" 
Para ingresar con su username presione 1 
En caso de no estar registrado presione 2 
>>>>> """)).strip()
        if Entrada=="1":                                # si el nombre de usuario se encuentra en la lista de nombres(usernames=[]) el programa procede a imprimir la informacion
            user=nombre_de_usuario()                    # del nombre de usuario registrado y romper el ciclo while.
            if user in usernames:
                #print("Bienvenido {}".format(user))
                user_index= usernames.index(user)
                user_objeto= Datos_de_usuario[user_index]
                print("""  
                        Nombre de usuario: {}
                        Nombre del jugador: {}
                        Edad: {}
                        Genero: {}
                        Puntos: {}""".format(user_objeto.nombre_de_usuario,user_objeto.nombre_completo,user_objeto.edad,user_objeto.genero, user_objeto.puntos_acumulados))
                break       
            if user not in usernames:                                # si el nombre de usuario no se encuentra registrado el programa le pide al usuario que que se registre
                print("Usuario no registrado por favor registrese")  # una vez registrado el usuario se procede a romper el ciclo while. 
                Entrada="2"
        if Entrada== "2":
            Datos_de_usuario,user_objeto = registrar_usuario(Datos_de_usuario,usernames) 
            break 
            
        

    print("><"*61)
    while True:
        print("Bienvenido {} ".format(user_objeto.nombre_de_usuario))
        print("""     
        1) Iniciar el juego 
        2) Ver las estadisticas 
        3) Editar la informacion del usuario 
        4) Cerrar el juego  
        """)
        enter=input(">>>>> ")

        print("><"*61)
            #MODULO 2 
        if enter=="1":

            while True:

                mapa=[
                    [ "|     |" , "|  1  |" , "|  2  |" , "|  3  |" , "|  4  |" , "|  5  |" , "|  6  |" , "|  7  |" , "|  8  |" , "|  9  |" , "| 10  |"],
                    [ "|  A  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  B  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  C  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  D  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  E  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  F  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  G  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  H  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  I  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                    [ "|  J  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |" , "|  O  |"],
                ]
                
                

                lista_submarinos=[]
                lista_buques_2=[]
                lista_carguero=[]
                lista_barcos=[]
                lista_ady=[]
                while len(lista_barcos)<4:
                    Generar_sub_marino(lista_barcos,lista_ady,lista_submarinos)               #se llama a las funciones para generar los barcos en el mapa. 

                generar_buque_2_pos(lista_barcos,lista_ady,lista_buques_2) 
                generar_buque_3_pos(lista_barcos,lista_ady,lista_carguero)


                for lista in mapa:
                    print(lista)
                print("><"*61)
                print(lista_barcos)
                lista_letras = ["A","B","C","D","E","F","G","H","I","J"]                  
                cont=0
                disparos=[]
                repetidos=0
                Puntos=0
                print("""Para reallizar el disparo primero ingrese la letra en la fila que desea disparar y luego un numero en la columna que desea disparar:
Ej:
Fila: A
Columna: 7
Coordenada=A7
                """)
                while len(lista_barcos)>0:
                    letra=input("Fila: ").strip()                                         
                    letra=letra.upper()
                    
                    if not letra in lista_letras and len(letra)==1 and letra.isalpha():
                        print("Fuera de rango")
                        continue
                    elif " " in letra or len(letra)!=1 or not letra.isalpha():
                        print("Por favor ingrese una letra")
                        continue
                    resp=True
                    while resp:
                        disparo=lista_letras.index(letra)+1
                        num=(input("Columna: ")).strip()
                        if not num.isdigit():
                            print("Introduzca un numero")
                            continue       
                        num=int(num)
                        if not num in list(range(1,11)):
                            print("fuera de rango")
                            continue
                        else:
                            resp=False 

                    Shoot= [disparo,num]
                    
                    if Shoot in lista_barcos:
                        print("¡Impacto Certero!  Capitan hemos impactado un barco enemigo")
                        mapa [Shoot[0]] [Shoot[1]]="|  F  |"
                        cont+=1
                        Puntos+=10
                        disparos.append(Shoot)
                        lista_barcos.remove(Shoot)
                        
                        for lista in mapa:
                            print(lista)
                    elif Shoot in disparos:
                        print("Disparo Ya relizado Capitan")
                        repetidos+=1
                        
                    else:
                        print("No le dimos al objetivo, Capitan, indique nuevas coordenadas")
                        mapa [Shoot[0]] [Shoot[1]]="|  X  |"
                        disparos.append(Shoot)
                        cont+=1
                        Puntos-=2
                        for lista in mapa:
                            print(lista)
                        
                    if Puntos<0:
                        Puntos=0

                disparos_acum+=cont
                juegos+=1                                                                 
                if Puntos > int(user_objeto.puntos_acumulados):                  #Se actualiza la cantidad de puntos actuales por los obtenidos en la partida reciente;       
                    user_objeto.disparos=cont
                    pos= Datos_de_usuario.index(user_objeto)                     # si la cantidad de puntos actuales es mayor a la cantidad de puntos obtenidos en la partida reciente     
                    user_objeto.puntos_acumulados= Puntos                        # entonces se mantendra la cantidad de puntos actuales, si este no es el caso los puntos obtenidos en la
                    Datos_de_usuario[pos]=user_objeto                            # la partida reciente se actualizaran como los nuevos puntos del usuario. 
                print(" Felicidades has hundido la flota enemiga  ")
                if cont ==9:
                    print("¿Eres un robot? lo que acabas de hacer es poco probabale...")
                elif cont < 45:
                    print("Excelente Estrategia")
                elif cont < 70:
                    print("Buena Estrategia; pero hay que mejorar")
                else:
                    print("Considerese Perdedor, tiene que mejorar notablemente")  
                print("""   
                Username: {}
                Disparos realizados: {}  
                Puntaje total: {}
                Cantidad de disparos repetidos: {}
                """.format(user_objeto.nombre_de_usuario, cont,Puntos,repetidos))
                print("><"*61 )
                for lista in mapa:
                    print(lista)
                while True:
                    continuar= input("¿Desea volver a jugar? (S/N): ").strip()
                    if continuar.title()== "S":
                        jugar_de_nuevo=True
                        break
                    elif continuar.title()== "N":
                        jugar_de_nuevo=False
                        break
                    else:
                        print("Por favor ingresa S o N")
                        continue 
                if jugar_de_nuevo:
                    continue
                    
                else:
                    break        

        #MODULO 3 
        elif enter=="2":
            rango_edad(Datos_de_usuario)                                        
            cant_puntos_genero(Datos_de_usuario)
            promedio_disparos(disparos_acum,juegos)
            print("><"*61)
            continue
        elif enter=="3":
            editar_informacion(user_objeto,Datos_de_usuario)              
            print("""  
                        Nombre de usuario: {}
                        Nombre del jugador: {}
                        Edad: {}
                        Genero: {}
                        Puntos: {}""".format(user_objeto.nombre_de_usuario,user_objeto.nombre_completo,user_objeto.edad,user_objeto.genero, user_objeto.puntos_acumulados))                            
            print("><"*61)
            continue
                 
            
            
        elif enter=="4":
            print("Hasta la proxima ")
            with open("texto.txt","w") as base_datos:                                    #se abre el archivo texto.txt para poder escribir los nuevos datos del que el usuario desea guardar.  
                for user_temp in Datos_de_usuario:
                    big_string="{},{},{},{},{},{}\n".format(user_temp.nombre_de_usuario,user_temp.nombre_completo,user_temp.edad,user_temp.genero,user_temp.puntos_acumulados,user_temp.disparos)
                    base_datos.write(big_string)
            with open("promedio.txt","w") as base_datos:                                #se abre el archivo promedio.txt para actualizar la cantidad de partidas jugadas y la cantidad de disparos realizados. 
                promedio_string="{},{}".format(juegos,disparos_acum)
                base_datos.write(promedio_string)
            break 
        

main()




            
        


            



    



