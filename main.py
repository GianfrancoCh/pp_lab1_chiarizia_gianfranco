import json
import re
from funciones import *

dreamteam = leer_archivo("C:/Users/gianf/OneDrive/Escritorio/UTN/PARCIAL/dt.json")
jugadores = jugadores_equipo(dreamteam) 
# dream_team_app(jugadores)



def cantidad_jugadores_posicion(jugadores:list):
    
    cant_alero = 0
    cant_escolta = 0
    cant_base = 0
    cant_ala = 0
    cant_pivot = 0
    
    for jugador in jugadores:
        if jugador["posicion"] == "Alero":
            cant_alero += 1
        elif jugador["posicion"] == "Escolta":
            cant_escolta += 1
        elif jugador["posicion"] == "Base":
            cant_base += 1
        elif jugador["posicion"] == "Ala-Pivot":
            cant_ala += 1
        elif jugador["posicion"] == "Pivot":
            cant_pivot += 1
    
    print("Base: {0}\nEscolta: {1}\nBase: {2}\nAla-Pivot: {3}\nPivot: {4}".format(cant_alero,cant_escolta,cant_base,cant_ala,cant_pivot))


def mejor_jugadores_por_estadisticas(jugadores:list):
    
    jug_temp = calcular_max_min_dato(jugadores,"estadisticas","temporadas","maximo")
    jug_punt_tot = calcular_max_min_dato(jugadores,"estadisticas","puntos_totales","maximo")
    jug_prom_ppp = calcular_max_min_dato(jugadores,"estadisticas","promedio_puntos_por_partido","maximo")
    jug_reb_tot = calcular_max_min_dato(jugadores,"estadisticas","rebotes_totales","maximo")
    jug_prom_rpp = calcular_max_min_dato(jugadores,"estadisticas","promedio_rebotes_por_partido","maximo")
    jug_asis_tot = calcular_max_min_dato(jugadores,"estadisticas","asistencias_totales","maximo")
    jug_prom_app = calcular_max_min_dato(jugadores,"estadisticas","promedio_asistencias_por_partido","maximo")
    jug_rob_tot = calcular_max_min_dato(jugadores,"estadisticas","robos_totales","maximo")
    jug_bloq_tot = calcular_max_min_dato(jugadores,"estadisticas","bloqueos_totales","maximo")
    jug_porc_tdc = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_de_campo","maximo")
    jug_porc_tl = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_libres","maximo")
    jug_por_tt = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_triples","maximo")

    
    print("Mayor cantidad temporadas: {0} ({1})".format(jug_temp["nombre"],jug_temp["estadisticas"]["temporadas"]))
    print("Mayor cantidad puntos totales: {0} ({1})".format(jug_punt_tot["nombre"],jug_punt_tot["estadisticas"]["puntos_totales"]))
    print("Mayor cantidad promedio por partido: {0} ({1})".format(jug_prom_ppp["nombre"],jug_prom_ppp["estadisticas"]["promedio_puntos_por_partido"]))
    print("Mayor cantidad rebotes totales: {0} ({1})".format(jug_reb_tot["nombre"],jug_reb_tot["estadisticas"]["rebotes_totales"]))
    print("Mayor promedio rebotes por partido: {0} ({1})".format(jug_prom_rpp["nombre"],jug_prom_rpp["estadisticas"]["promedio_rebotes_por_partido"])) 
    print("Mayor cantidad de asistencias totales: {0} ({1})".format(jug_asis_tot["nombre"],jug_asis_tot["estadisticas"]["asistencias_totales"]))
    print("Mayor promedio asistencias por partidos: {0} ({1})".format(jug_prom_app["nombre"],jug_prom_app["estadisticas"]["promedio_asistencias_por_partido"]))
    print("Mayor cantidad robos totales: {0} ({1})".format(jug_rob_tot["nombre"],jug_rob_tot["estadisticas"]["robos_totales"]))
    print("Mayor cantidad bloqueos totales: {0} ({1})".format(jug_bloq_tot["nombre"],jug_rob_tot["estadisticas"]["bloqueos_totales"]))
    print("Mayor cantidad porcentaje tiros de campo: {0} ({1})".format(jug_porc_tdc["nombre"],jug_porc_tdc["estadisticas"]["porcentaje_tiros_de_campo"]))
    print("Mayor cantidad porcentaje tiros libres: {0} ({1})".format(jug_porc_tl["nombre"],jug_porc_tl["estadisticas"]["porcentaje_tiros_libres"]))
    print("Mayor cantidad porcentaje tiros triples: {0} ({1})".format(jug_por_tt["nombre"],jug_por_tt["estadisticas"]["porcentaje_tiros_triples"]))
    
def mejor_estadistica(jugadores:list):
    
    jugadores_estadisticas = []
    flag = True
    
    jug_temp = calcular_max_min_dato(jugadores,"estadisticas","temporadas","maximo")
    jug_punt_tot = calcular_max_min_dato(jugadores,"estadisticas","puntos_totales","maximo")
    jug_prom_ppp = calcular_max_min_dato(jugadores,"estadisticas","promedio_puntos_por_partido","maximo")
    jug_reb_tot = calcular_max_min_dato(jugadores,"estadisticas","rebotes_totales","maximo")
    jug_prom_rpp = calcular_max_min_dato(jugadores,"estadisticas","promedio_rebotes_por_partido","maximo")
    jug_asis_tot = calcular_max_min_dato(jugadores,"estadisticas","asistencias_totales","maximo")
    jug_prom_app = calcular_max_min_dato(jugadores,"estadisticas","promedio_asistencias_por_partido","maximo")
    jug_rob_tot = calcular_max_min_dato(jugadores,"estadisticas","robos_totales","maximo")
    jug_bloq_tot = calcular_max_min_dato(jugadores,"estadisticas","bloqueos_totales","maximo")
    jug_porc_tdc = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_de_campo","maximo")
    jug_porc_tl = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_libres","maximo")
    jug_por_tt = calcular_max_min_dato(jugadores,"estadisticas","porcentaje_tiros_triples","maximo")
    
    for jugador in jugadores:
        jugadores_estadisticas.append({"nombre":jugador["nombre"],"cant_tops":0})
    
    for jugador in jugadores_estadisticas:
        
        if jugador["nombre"] == jug_temp["nombre"]:
            jugador["cant_tops"] += 1
        if jugador["nombre"] == jug_punt_tot["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_prom_ppp["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_reb_tot["nombre"]:
            jugador["cant_tops"] += 1
        if jugador["nombre"] == jug_prom_rpp["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_asis_tot["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_prom_app["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_rob_tot["nombre"]:
            jugador["cant_tops"] += 1
        if jugador["nombre"] == jug_bloq_tot["nombre"]:
            jugador["cant_tops"] += 1
        if jugador["nombre"] == jug_porc_tdc["nombre"]:
            jugador["cant_tops"] += 1 
        if jugador["nombre"] == jug_porc_tl["nombre"]:
            jugador["cant_tops"] += 1
        if jugador["nombre"] == jug_por_tt["nombre"]:
            jugador["cant_tops"] += 1 
            
    for jugador in jugadores_estadisticas: 
        if flag == True or jugador["cant_tops"] > jug_max["cant_tops"]:
            flag = False
            jug_max = jugador
        
    print("El jugador con las mejores estadisticas es {0} con un top en {1} estadisticas".format(jug_max["nombre"],jug_max["cant_tops"]))
    
       
def cantidad_all_star(jugadores:list):
    
    flag = True
    jugadores_allstar = []
    
    for jugador in jugadores:
        for logro in jugador["logros"]:
            if "veces All-Star" in logro:
                numero_all_star = re.findall(r'\d+', logro)
                numero_all_star = int(numero_all_star[0])
                jugadores_allstar.append({"nombre":jugador["nombre"],"cant_all_star":numero_all_star})

    return jugadores_allstar

# cantidad_jugadores_posicion(jugadores)       
# mejor_jugadores_por_estadisticas(jugadores)
# mejor_estadistica(jugadores)
# test = cantidad_all_star(jugadores)
# print(ordenar_lista_clave(test,False,"cant_all_star"))

    
    
    
 