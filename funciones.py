import json
import re

def imprimir_dato(dato_a_imprimir:str):
    
    print(dato_a_imprimir)
    
    
def leer_archivo(nombre_archivo:str):
    
    """
    Funcion que recibe un string que representa la ruta de un archivo y
    retorna una lista con sus datos
    -nombre_archivo: ruta
    -lista: lista datos
    """
    diccionario = {}
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        
    return diccionario

def jugadores_equipo(equipo:dict)->list:
    
    """
    Recibe un diccionario que representa un diccionario y devuelve una lista de jugadores
    equipo: diccionario equipo
    jugadores: lista de jugadores
    """
    jugadores = []
    jugadores = equipo["jugadores"]
    
    return jugadores


def capitalizar_palabras(cadena):
    
    palabras_capitalizadas = []
    palabras = cadena.split() 

    for palabra in palabras:
        
        palabras_capitalizadas.append(palabra.capitalize())
        
    cadena_rtn = " ".join(palabras_capitalizadas)
    
    return cadena_rtn

def obtener_nombre_capitalizado(jugador:dict)->str:
    
    jugador["nombre"] = capitalizar_palabras(jugador["nombre"])
    nombre_jugador_capitalizado = "{0}".format(jugador["nombre"])
    
    return nombre_jugador_capitalizado


def imprimir_jugadores_posicion(jugadores:list):
    
    for jugador in jugadores:
        nombre = obtener_nombre_capitalizado(jugador)
        nombre_posicion = "{0} - {1}".format(nombre,jugador["posicion"])
        imprimir_dato(nombre_posicion)
        


def imprimir_lista_jugadores_indice(jugadores:list):
    
    indice = 0
    for jugador in jugadores:
        
        nombre_jugador = obtener_nombre_capitalizado(jugador)
        print("{0} - {1}".format(indice,nombre_jugador))
        indice += 1 


def imprimir_estadisticas_jugador_indice(jugadores:list):
    
    
    imprimir_lista_jugadores_indice(jugadores)
    indice = int(input("\nIngrese un indice del jugador a imprimir sus estadisticas:\n"))
    jugador_a_guardar = jugadores[indice]
    print(jugadores[indice]["estadisticas"])
    
    return jugador_a_guardar


def guardar_jugador_csv(jugador_guardar:dict):
    
    nombre_archivo = "{0}.csv".format(jugador_guardar["nombre"])
    
    with open(nombre_archivo, "w+") as archivo:
        if archivo.write(str(jugador_guardar)):
            print("Se creo el archivo {0}".format(nombre_archivo))
            return True
        else:
            print(f"Error al crear el archivo {0}".format(nombre_archivo))
            return False
        
        
def capitalizar_palabras(cadena):
    
    palabras_capitalizadas = []
    palabras = cadena.split() 

    for palabra in palabras:
        
        palabras_capitalizadas.append(palabra.capitalize())
        
    cadena_rtn = " ".join(palabras_capitalizadas)
    
    return cadena_rtn


def buscar_jugador_nombre(jugadores:dict):
    
    nombre = capitalizar_palabras(input("\nIngrese el nombre del jugador a buscar [Nombre Apellido]:\n"))
    
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
    print("No se encontro el nombre seleccionado")
    
    
def buscar_logros_jugador(jugadores):
    
    jugador = buscar_jugador_nombre(jugadores)
    if jugador:
        print("Logros de {0}:\n".format(jugador["nombre"]))
        print(jugador["logros"])
        
def buscar_salon_fama_jugador(jugadores):
    
    flag = False
    jugador = buscar_jugador_nombre(jugadores)
    if jugador:
        for logro in jugador["logros"]:
            if logro == "Miembro del Salon de la Fama del Baloncesto":     
                flag = True
    if flag:
        print("\nEl jugador {0} es miembro del salon de la fama del baloncesto".format(jugador["nombre"]))
    else:
        print("\nEl jugador {0} NO es miembro del salon de la fama del baloncesto".format(jugador["nombre"]))  
        
def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,True)
    lista_iz.append(pivot) 
    lista_de = quick_sort(lista_de,True)
    lista_iz.extend(lista_de) 
    return lista_iz


def calcular_min(jugadores:list,clave:str,clave_2:str):
    flag = True
    jugador_min = {}
    for jugador in jugadores:
        if flag == True or float(jugador[clave][clave_2]) < float(jugador_min[clave][clave_2]): 
            flag = False   
            jugador_min = jugador
             
    return jugador_min

def calcular_max(jugadores:list,clave:str,clave_2:str):
    flag = True
    jugador_max = {}
    for jugador in jugadores: 
        if flag == True or jugador[clave][clave_2] > jugador_max[clave][clave_2]:
            flag = False
            jugador_max = jugador
             
    return jugador_max

def calcular_max_min_dato(jugadores:list,clave:str,clave_2:str,max_min:str):
   
    jugador_return = {}
    
    if max_min.lower() == "minimo":
        
        jugador_return = calcular_min(jugadores,clave,clave_2)    
         
    elif max_min.lower() == "maximo":
        
        jugador_return = calcular_max(jugadores,clave,clave_2)
    
    return jugador_return


def imprimir_resultado_calculo_max_min(jugadores,clave:str,clave_2:str,max_min:str):
    
    jugador = calcular_max_min_dato(jugadores,clave,clave_2,max_min)
    nombre = obtener_nombre_capitalizado(jugador)
    print("El jugador con el {0} es {1}, con {2} {3}".format(max_min,nombre,jugador[clave][clave_2],clave_2))