import json
import re
import csv
from funciones import *

dreamteam = leer_archivo("C:/Users/gianf/OneDrive/Escritorio/UTN/PARCIAL/dt.json")
jugadores = jugadores_equipo(dreamteam) 
dream_team_app(jugadores)





# cantidad_jugadores_posicion(jugadores)       
# mejor_jugadores_por_estadisticas(jugadores)
# mejor_estadistica(jugadores)
# test = cantidad_all_star(jugadores)
# print(ordenar_lista_clave(test,False,"cant_all_star"))


