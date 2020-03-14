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


print(  
""" _____  ___  ___  ___  ___   _   _        _____   ___  ___  ___ _____ _____  
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


#MODULO 1 
resp=True
Datos_de_usuario=[] 
while resp:
    usernames=[]
    for user in Datos_de_usuario:
        usernames.append(user.nombre_de_usuario)
    Entrada=(input(" Si desea ingresar con su username presione 1 , en caso de no estar registrado presione 2: ")).strip()
    if Entrada=="1":
        user=nombre_de_usuario()
        if user in usernames:
            print("Bienvenido {}".format(user))
            user_index= usernames.index(user)
            user_objeto= Datos_de_usuario[user_index]
            print("""  
                    Nombre de usuario: {}
                    Nombre del jugador: {}
                    Edad: {}
                    Genero: {}
                    Puntos: {}""".format(user_objeto.nombre_de_usuario,user_objeto.nombre_completo,user_objeto.edad,user_objeto.genero, user_objeto.puntos_acumulados))
            break       
        if user not in usernames:
            print("Usuario no registrado por favor registrese")
            Entrada="2"
    if Entrada== "2":
        Datos_de_usuario,user_objeto = registrar_usuario(Datos_de_usuario) 
        break 


#MODULO 2 
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
        Generar_sub_marino(lista_barcos,lista_ady,lista_submarinos)

    generar_buque_2_pos(lista_barcos,lista_ady,lista_buques_2) 
    generar_buque_3_pos(lista_barcos,lista_ady,lista_carguero)


    for lista in mapa:
        print(lista)
    print("<>"*60)
    print(lista_barcos)
    lista_letras = ["A","B","C","D","E","F","G","H","I","J"]
    cont=0
    disparos=[]
    repetidos=0
    Puntos=0
    while len(lista_barcos)>0:
        letra=input("Ingrese una letra: ").strip()
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
            num=(input("Introduzca el numero de columna donde desea disparar: "))
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
    print("><"*30 )
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



            
        


            



    



