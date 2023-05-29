import json
import re

def imprimir_dato(dato_a_imprimir:str):
    '''
    Funcion que recibe un string y lo imprime
    -dato_a_imprimir: string a imprimir
    '''
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


def transformar_texto(texto:str):
    '''
    Funcion que recibe una cadena de texto y retorna una cadena reemplazando los "_"  por espacios
    texto: cadena a separar
    -resultado: cadena separada por "_"
    '''
    palabras = texto.split('_')
    resultado = ' '.join(palabras).capitalize()
    return resultado


def jugadores_equipo(equipo:dict)->list:
    
    """
    Recibe un diccionario que representa un diccionario y devuelve una lista de jugadores
    equipo: diccionario equipo
    -jugadores: lista de jugadores
    """
    jugadores = []
    jugadores = equipo["jugadores"]
    
    return jugadores


def capitalizar_palabras(cadena):
    '''
    Funcion que recibe una cadena y capitaliza cada palabra
    -cadena: cadena de palabras a capitalizar
    -cadena_rtn: cadena con las palabras capitalizadas
    '''
    palabras_capitalizadas = []
    palabras = cadena.split() 

    for palabra in palabras:
        
        palabras_capitalizadas.append(palabra.capitalize())
        
    cadena_rtn = " ".join(palabras_capitalizadas)
    
    return cadena_rtn

    
def obtener_nombre_capitalizado(jugador:list)->str:
    '''
    Funcion que recibe un jugador y capitaliza su nombre
    Retorna el nombre del jugador capitalizado
    -jugador: diccionario que representa un jugador 
    -nombre_jugador_capitalizado: cadena que representa el nombre del jugador capitalizado
    '''
    jugador["nombre"] = capitalizar_palabras(jugador["nombre"])
    nombre_jugador_capitalizado = "{0}".format(jugador["nombre"])
    
    return nombre_jugador_capitalizado


def imprimir_jugadores_posicion(jugadores:list):
    '''
    Recibe una lista de jugadores e imprime la lista de los jugadores con su posicion
    -jugadores: lista de jugadores
    '''
    for jugador in jugadores:
        nombre = obtener_nombre_capitalizado(jugador)
        nombre_posicion = "{0} - {1}".format(nombre,jugador["posicion"])
        imprimir_dato(nombre_posicion)
        


def imprimir_lista_jugadores_indice(jugadores:list):
    '''
    Recibe una lista de jugadores y los imprime con su indice correspondiente
    -jugadores: lista de jugadores a imprimir
    '''
    indice = 0
    for jugador in jugadores:
        
        nombre_jugador = obtener_nombre_capitalizado(jugador)
        print("{0} - {1}".format(indice,nombre_jugador))
        indice += 1 


def imprimir_estadisticas_jugador_indice(jugadores:list)->dict:
    '''
    Funcion que le pide al usuario un indice e imprime las estadisticas del jugador
    correspondiente a ese indice y retorna ese jugador
    -jugadores: lista de jugadores
    -jugador_a_guardar: diccionario correspondiente al jugador del indice seleccionado
    '''
    imprimir_lista_jugadores_indice(jugadores)
    indice = int(input("\nIngrese un indice del jugador a imprimir sus estadisticas:\n"))
    jugador_a_guardar = jugadores[indice]
    print(jugadores[indice]["estadisticas"])
    
    return jugador_a_guardar


def guardar_jugador_csv(jugador_guardar:dict):
    '''
    Recibe un jugador y lo guarda en un CSV con nombre de ese jugador
    -jugador_guardar: diccionario correspondiente al jugador a guardar
    '''
    nombre_archivo = "{0}.csv".format(jugador_guardar["nombre"])
    
    with open(nombre_archivo, "w+") as archivo:
        if archivo.write(str(jugador_guardar)):
            print("Se creo el archivo {0}".format(nombre_archivo))
            return True
        else:
            print(f"Error al crear el archivo {0}".format(nombre_archivo))
            return False
        

def buscar_jugador_nombre(jugadores:list):
    '''
    Funcion que recibe la lista de jugadores y le pide al usuario que ingrese el nombre de un jugador.
    Busca el nombre del jugador en la lista de jugadores y si lo encuentra lo retorna. Si no lo encuentra
    imprime un mensaje de error
    -jugadores: lista de jugadores
    -jugador: retorno del jugador si lo encuentra
    '''
    nombre = capitalizar_palabras(input("\nIngrese el nombre del jugador a buscar [Nombre Apellido]:\n"))
    
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
    print("No se encontro el nombre seleccionado")
    
    
def buscar_logros_jugador(jugadores:list):
    '''
    Recibe lista de jugadores e imprime los logros del jugador buscado
    '''
    jugador = buscar_jugador_nombre(jugadores)
    if jugador:
        print("Logros de {0}:\n".format(jugador["nombre"]))
        print(jugador["logros"])
        
def buscar_salon_fama_jugador(jugadores:list):
    '''
    Recibe lista de jugadores y busca si el jugador esta en el salon de la fama
    '''
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
        
def calcular_min(jugadores:list,clave:str,clave_2:str):
    '''
    Encuentra el jugador con el valor mínimo en una lista de jugadores.
    Parámetros:
    - jugadores (list): Lista de jugadores.
    - clave (str): Clave para acceder al primer nivel del valor numérico dentro de cada jugador.
    - clave_2 (str): Clave para acceder al segundo nivel del valor numérico dentro de cada jugador.
    Retorna:
    - dict: Diccionario con la información del jugador con el valor mínimo. 
    '''
    flag = True
    jugador_min = {}
    for jugador in jugadores:
        if flag == True or float(jugador[clave][clave_2]) < float(jugador_min[clave][clave_2]): 
            flag = False   
            jugador_min = jugador
             
    return jugador_min

def calcular_max(jugadores:list,clave:str,clave_2:str):
    '''
    Encuentra el jugador con el valor maximo en una lista de jugadores.
    Parámetros:
    - jugadores (list): Lista de jugadores.
    - clave (str): Clave para acceder al primer nivel del valor numérico dentro de cada jugador.
    - clave_2 (str): Clave para acceder al segundo nivel del valor numérico dentro de cada jugador.
    Retorna:
    - dict: Diccionario con la información del jugador con el valor mínimo. 
    '''
    flag = True
    jugador_max = {}
    for jugador in jugadores: 
        if flag == True or jugador[clave][clave_2] > jugador_max[clave][clave_2]:
            flag = False
            jugador_max = jugador
             
    return jugador_max

def calcular_max_min_dato(jugadores:list,clave:str,clave_2:str,max_min:str):
    """
    Calcula el máximo o mínimo valor de un dato específico en una lista de jugadores.

    Parámetros:
    - jugadores (list): Lista de jugadores.
    - clave (str): Clave para acceder al primer nivel del valor numérico dentro de cada jugador.
    - clave_2 (str): Clave para acceder al segundo nivel del valor numérico dentro de cada jugador.
    - max_min (str): Indica si se desea calcular el máximo o mínimo valor. Debe ser "maximo" o "minimo".

    Retorna:
    - dict: Diccionario con la información del jugador con el máximo o mínimo valor, según lo especificado.

    """

    jugador_return = {}
    
    if max_min.lower() == "minimo":
        
        jugador_return = calcular_min(jugadores,clave,clave_2)    
         
    elif max_min.lower() == "maximo":
        
        jugador_return = calcular_max(jugadores,clave,clave_2)
    
    return jugador_return


def imprimir_resultado_calculo_max_min(jugadores:list,clave:str,clave_2:str,max_min:str):
    """
    Imprime el resultado del cálculo del máximo o mínimo.
    - jugadores (list): Lista de jugadores.
    - clave (str): Clave para acceder al primer nivel del valor numérico dentro de cada jugador.
    - clave_2 (str): Clave para acceder al segundo nivel del valor numérico dentro de cada jugador.
    - max_min (str): Indica si se desea calcular el máximo o mínimo valor. Debe ser "maximo" o "minimo".
    """
    jugador = calcular_max_min_dato(jugadores,clave,clave_2,max_min)
    nombre = obtener_nombre_capitalizado(jugador)
    print("El jugador con el {0} es {1}, con {2} {3}".format(max_min,nombre,jugador[clave][clave_2],clave_2))
    
def mostrar_jugadores_mayor_valor_estadisticas(jugadores:list,clave:str):
    '''
    Le pide al usuario un valor y devuelve una lista de jugadores que tienen una valor mayor
    a esa estadistica.
    -jugadores: lista de jugadores
    -clave: tipo de estadistica
    Retorna
    -lista_mayor_valor o None: Retorna una lista con los jugadores que cumplan la condicion. 
    Si no hay jugadores en la lista retorna None
    '''
    lista_mayor_valor = []
    valor = int(input("\nIngrese el valor a buscar:\n"))
    for jugador in jugadores:
        if float(jugador["estadisticas"][clave]) > valor:
            lista_mayor_valor.append(jugador)
    
    if len(lista_mayor_valor) == 0:
        return None
    else:
        return lista_mayor_valor
    # if len(lista_mayor_valor) == 0:
    #     print("No hay jugador con mayor de {0} {1}".format(valor,clave))  
    # else:
    #     print(lista_mayor_valor)  


def mostrar_lista_clave(jugadores:list,clave:str):
    '''
    Muestra la lista de jugadores con el valor de la clave espeficada
    -jugadores: lista de jugadores
    -clave: clave del valor a imprimir  
    '''
    lista = mostrar_jugadores_mayor_valor_estadisticas(jugadores,clave)
    clave_print = transformar_texto(clave)
    for jugador in lista:
        print("{0} | {1} {2}".format(jugador["nombre"],clave_print,jugador["estadisticas"][clave]))

def mostrar_mayor_logros(jugadores:list):
    '''
    Muestra el jugador con la mayor cantidad de logros
    -jugadores: lista de jugadores
    '''
    flag = True
    jugador_max_clave = {}
    
    for jugador in jugadores:
        if flag or len(jugador["logros"]) > len(jugador_max_logros["logros"]):
            flag = False
            jugador_max_logros = jugador
    
    print("El jugador con mayor logros es {0} con {1}".format(jugador_max_logros["nombre"],jugador_max_logros["logros"]))
    
    
def sumar_dato_jugador(jugadores:list,clave:str,clave_2:str):
    """
    Suma el valor de las estadisticas de una lista de jugadores
    -jugadores: lista de jugadores
    -clave: primera clave
    -clave_2: segunda clave 
    
    -suma: retorno de la suma de esos valores
    """
    suma = 0 
    for jugador in jugadores:
        if isinstance(jugador,dict) and clave in jugador:
            suma += jugador[clave][clave_2]
        else:
            return -1

    return suma
    
def calcular_promedio_clave_estadisticas(jugadores:list,clave:str,clave_2:str)->float:
    '''
    Calcula el promedio de una clave especifica de la lista de jugadores
    
    -jugadores: lista de jugadores
    -clave: clave primer nivel
    -clave_2: clave segundo nivel
    
    -promedio: promedio a retornar
    '''
    cantidad_jugadores = len(jugadores)
    
    suma = sumar_dato_jugador(jugadores,clave,clave_2)
    
    promedio = dividir(suma,cantidad_jugadores)
    
    return promedio
            
def dividir(dividendo,divisor)->float:
    '''
    Funcion de que hace la division de dos valores
    -dividendo: dividendo
    -divisor: divisor
    
    Retorna el valor de la division o si el divisor es igual a 0
    '''
    if divisor == 0:
        return 0
    else:
        return dividendo/divisor
    
def promedio_puntos_exc_menor(jugadores:list):
    '''
    Calcula el promedio de puntos excluyendo al menor
    -jugadores: lista de jugadores
    -promedio: promedio a retornar
    '''
    jugador_menor_puntos = calcular_max_min_dato(jugadores,"estadisticas","promedio_puntos_por_partido","minimo")
    jugadores_calculo_promedio = []
    
    for jugador in jugadores:
        if jugador != jugador_menor_puntos:
            jugadores_calculo_promedio.append(jugador)
            
    promedio = calcular_promedio_clave_estadisticas(jugadores_calculo_promedio,"estadisticas","promedio_puntos_por_partido")
    
    return promedio 

def ordenar_lista_clave(lista:list,flag_orden:bool,clave:str):
    '''
    Ordena una lista de elementos por el valor una clave especifica
    
    -lista: lista de elementos a ordenar
    -flag_order: indica el tipo de ordenamiento.Si es True, se ordena de forma ascendente. Si es False,
    se ordena de forma descendente.
    -clave: clave de los valores a ordenar
    Retorno
    -lista_orden: lista ordenada
    '''
    rango_a = len(lista) - 1
    lista_orden = lista[:]
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista_orden[indice_A][clave] < lista_orden[indice_A+1][clave] \
             or flag_orden == True and lista_orden[indice_A][clave] > lista_orden[indice_A+1][clave]:
                lista_orden[indice_A],lista_orden[indice_A+1] = lista_orden[indice_A+1],lista_orden[indice_A]
                flag_swap = True
    
    return lista_orden

def listar_clave_ordenado_alfabeticamente(jugadores:list,clave:str):
    '''
    Imprime lista ordenada alfabeticamente
    jugadores: lista de jugadores a ordenar
    clave: valor de clave a listar en la lista
    '''
    lista = ordenar_lista_clave(jugadores,True,"nombre")
    clave_print = transformar_texto(clave)
    
    for jugador in lista: 
        print("El {0} de {1} es {2}".format(clave_print,jugador["nombre"],jugador["estadisticas"][clave]))
        
def mostrar_posicion_mayor_estadisticas(jugadores:list,clave:str):
    '''
    Muestra una lista de jugadores ordenados por posicion que tenga un mayor
    valor de estadistica del ingresado por el usuario. 
    
    -jugadores: lista de jugadores
    -clave: clave del valor de la estadistica a comparar
    '''
    lista = mostrar_jugadores_mayor_valor_estadisticas(jugadores,clave)
    listar_clave_ordenado_alfabeticamente(lista,clave)
    
    
    

#FUNCIONES MENU


def imprimir_menu():
    '''
    Imprime el menu de la aplicación
    '''
    #imprimir menu
    print("\nMenú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team." )
    print("2. Seleccionar un jugador por su indice e imprimir sus estadisticas.")
    print("3. Guardar estadisticas del jugador del punto 2 en un CSV.")
    print("4. Permitir al usuario buscar un jugador por su nombre y mostrar sus logros.")
    print("5. Mostrar el promedio de puntos por partido de todo el equipo del Dream Team.")
    print("6. Ingresar nombre de jugador para saber si es miembro del salon de la fama.")
    print("7. Mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9. Mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. Ingresar cantidad de puntos y mostrar los jugadores con un promedio de puntos mayor.")
    print("11. Ingresar cantidad de rebotes y mostrar los jugadores con un promedio de rebotes mayor.")
    print("12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor")
    print("13. Mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido")
    print("17. Mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("21. SALIR DEL SISTEMA")


def menu_opcion():
    '''
    Valida la opcion del menu y la retorna
    '''
    imprimir_menu()
    
    opcion = input("\nIngrese la opción deseada: \n")
    if re.match(r'^(?:[0-9]|1[0-9]|20|21)$', opcion):
        return int(opcion)
    else:
        return -1
    
 

def dream_team_app(jugadores:list):
    '''
    Gestiona la aplicacion y las diferentes opciones seleccionadas del menú.
    '''
    flag_punto_2 = False
    while True:
        
        opcion = menu_opcion()
        match(opcion):           
            case 1:   
                imprimir_jugadores_posicion(jugadores)            
            case 2:    
                jugador_a_guardar = imprimir_estadisticas_jugador_indice(jugadores)
                flag_punto_2 = True
            case 3:
                if flag_punto_2:
                    guardar_jugador_csv(jugador_a_guardar)
                else:
                    print("Primero se debe seleccionar un jugador en el punto 2")
            case 4:    
                buscar_logros_jugador(jugadores)  
            case 5:  
                listar_clave_ordenado_alfabeticamente(jugadores,"promedio_puntos_por_partido")
            case 6:
                buscar_salon_fama_jugador(jugadores)
            case 7:     
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","rebotes_totales","maximo")
            case 8:
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","porcentaje_tiros_de_campo","maximo")
            case 9:
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","asistencias_totales","maximo")
            case 10:
                mostrar_lista_clave(jugadores,"promedio_puntos_por_partido")
            case 11:
                print(mostrar_jugadores_mayor_valor_estadisticas(jugadores,"promedio_rebotes_por_partido"))
            case 12:
                print(mostrar_jugadores_mayor_valor_estadisticas(jugadores,"promedio_asistencias_por_partido"))
            case 13:
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","robos_totales","maximo")   
            case 14:
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","bloqueos_totales","maximo")
            case 15:
                print(mostrar_jugadores_mayor_valor_estadisticas(jugadores,"porcentaje_tiros_libres"))
            case 16:   
                promedio_puntos_exc_menor(jugadores)
            case 17:
                mostrar_mayor_logros(jugadores)
            case 18:
                print(mostrar_jugadores_mayor_valor_estadisticas(jugadores,"porcentaje_tiros_triples"))
            case 19:
                imprimir_resultado_calculo_max_min(jugadores,"estadisticas","temporadas","maximo")
            case 20:
                mostrar_posicion_mayor_estadisticas(jugadores,"porcentaje_tiros_de_campo")
            case 21:
                print("----------------------------------------------------------------")
                print("--------------------CERRANDO LA APLICACION----------------------")
                print("----------------------------------------------------------------")
                break
            case other:
                print("----------------------------------------------------------------")
                print("---------------------INGRESE OPCION VALIDA----------------------")
                print("----------------------------------------------------------------")