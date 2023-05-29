import json
import re
from funciones import *



def imprimir_menu():
    
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
    
    imprimir_menu()
    
    opcion = int(input("\nIngrese la opción deseada: "))
    
    return opcion
 

def dream_team_app(lista:list):
    
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
            case other:
                print("INVALIDO")

dreamteam = leer_archivo("C:/Users/gianf/OneDrive/Escritorio/UTN/PARCIAL/dt.json")

jugadores = jugadores_equipo(dreamteam)       
  
dream_team_app(jugadores)

#1
# imprimir_jugadores_posicion(jugadores)

# def obtener_nombre_y_dato(jugadores:dict,clave:str)->str:
    
#     nombre = obtener_nombre_capitalizado(jugadores)
#     dato_clave = capitalizar_palabras(clave)
#     nombre_dato = "{0} | {1} ".format(nombre,clave_mayuscula,jugadores[clave])
    
#     return nombre_dato

   
#def guardar_jugador_estadisticas_csv(jugador:list,flag_punto_2:bool):      
    

# def es_genero(heroe:dict,genero_buscar:str)->bool:
    
#     genero_buscar = genero_buscar.upper()
    
#     if genero_buscar in ["F","M","NB"]:
        
#         if heroe["genero"] == genero_buscar:
#             return True
#         else:
#             return False
#     else:
#         print("GENERO INVALIDO")
        
# def stark_guardar_heroe_genero(lista_heroes:dict,genero:str):
    
#     nombre_archivo = "heroes_{0}.csv".format(genero)
#     lista_guardar = []
    
#     for heroe in lista_heroes:
#         if es_genero(heroe,genero):
#             nombre = obtener_nombre_capitalizado(heroe)
#             imprimir_dato(nombre)
#             lista_guardar.append(nombre)
    
#     cadena_nombres = ", ".join(lista_guardar)
    
#     if guardar_archivo(nombre_archivo, cadena_nombres):
#         return True
#     else:
#         return False  