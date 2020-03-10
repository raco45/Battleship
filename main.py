from clases import Usuario
from funciones import nombre_de_usuario
from funciones import nombre_completo
from funciones import edad_usuario
from funciones import genero_usuario
from funciones import puntos_acumulados
from funciones import registrar_usuario



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
Datos_de_usuario=[]
resp=True
while resp:
    Entrada=(input(" Si desea ingresar con su username presione 1 , en caso de no estar registrado presione 2: ")).strip()
    if Entrada=="1":
        user=nombre_de_usuario()
       
        if user not in Datos_de_usuario:
            Entrada="2"
    if Entrada== "2":
        registrar_usuario(Datos_de_usuario)
    
    