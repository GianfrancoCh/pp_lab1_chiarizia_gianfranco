import json
import re
from funciones import *

dreamteam = leer_archivo("C:/Users/gianf/OneDrive/Escritorio/UTN/PARCIAL/dt.json")
jugadores = jugadores_equipo(dreamteam) 
dream_team_app(jugadores)

