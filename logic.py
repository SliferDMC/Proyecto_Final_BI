#import pandas as pd
import requests
import boto3
import json
import os

def guardarJson2(carpeta, nombre, cantidad, inicial, archivoN):
    # Consulta  a la base de datos
    url = 'https://pokeapi.co/api/v2/'
    response = requests.get(url+nombre+'?limit='+str(cantidad)+'&offset=0') 
    #Conversion a json, DataFrame y guardado en formato csv
    r = response.json()

    dir = 'D:/Pruebas'  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'

    with open(os.path.join(dir+'/Listas/'+carpeta, archivoN+'.json'), 'w') as file:
         json.dump(r, file)

def guardarJson(carpeta, nombre, cantidad):
    guardarJson2(carpeta, nombre, cantidad, 0, nombre)

def guardarJsonDatos(carpeta, nombre, cantidad, inicio):
    url = 'https://pokeapi.co/api/v2/'
    response = requests.get(url+nombre+'/'+str(inicio)) 
    #Conversion a json, DataFrame y guardado en formato csv r= response.json()
    for i in range(inicio,cantidad+1): 
        # Consulta  a la base de datos
        response = requests.get(url+nombre+'/'+str(i)) 
        #Conversion a json, DataFrame y guardado en formato csv r= response.json()
        r= response.json()
        dir = 'D:/Pruebas'  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
        with open(os.path.join(dir+'/Datos/'+carpeta, str(i)+'-'+r['name']+'.json'), 'w') as file:
             json.dump(r, file)

    #r = res.json()

    
        

#credenciales SliferDMC
access_key  = 'AKIAQTCJUV7ZS32U2MP2'
secret_access_key = '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'

#credenciales Danhetx
access_key_D = 'AKIAQTCJUV7Z4JQV6GPY'
secret_access_key_D = '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'

# ----------------------------------------- Pokemon ----------------------------------------------------- #
# habilidades
guardarJson('Pokemon', 'ability', 293)
# Caracteristicas de los pokemon
guardarJson('Pokemon', 'characteristic', 30)
# grupo huevo
guardarJson('Pokemon', 'egg-group', 15)
# genero
guardarJson('Pokemon', 'gender', 3)
# tasa de crecimiento
guardarJson('Pokemon', 'growth-rate', 6)
# naturaleza
guardarJson('Pokemon', 'nature', 25)
# estadisticas de pokeathlon
guardarJson('Pokemon', 'pokeathlon-stat', 5)
# pokemon
guardarJson('Pokemon', 'pokemon', 1117)
# coles de los pokemon
guardarJson('Pokemon', 'pokemon-color', 10)
# figuras de los pokemon
guardarJson('Pokemon', 'pokemon-form', 1123)
# Habitad de los pokemon
guardarJson('Pokemon', 'pokemon-habitat', 9)
# formas de un pokemon
guardarJson('Pokemon', 'pokemon-shape', 14)
# especies
guardarJson('Pokemon', 'pokemon-species', 893)
# estadisticas
guardarJson('Pokemon', 'stat', 8)
# Tipo
guardarJson('Pokemon', 'type', 20)

# --------------------------------------- Movimientos ------------------------------------------------- #
# Movimientos
guardarJson('Movimientos', 'move', 813)
# Estado alterado que inflinge el movimiento
guardarJson('Movimientos', 'move-ailment', 21)
# tipo de movimiento, (atk, def, sup)
guardarJson('Movimientos', 'move-battle-style', 3)
# categorya del movimiento (damg,force-stich,alt-stats)
guardarJson('Movimientos', 'move-category', 14)
# tipo de daño que hace el movimiento (fsc, spc, sta)
guardarJson('Movimientos', 'move-damage-class', 3)
# metodo de aprendizaje del movimiento
guardarJson('Movimientos', 'move-learn-method', 10)
# objetivo del movimiento
guardarJson('Movimientos', 'move-target', 14)

# --------------------------------------- Evolucion ------------------------------------------------- #
# Cadena Evolucion
guardarJson('Evolucion', 'evolution-chain', 419)
# metodo de evolucion
guardarJson('Evolucion', 'evolution-trigger', 4)

# --------------------------------------- Objetos ------------------------------------------------- #
# Objetos
guardarJson('Objetos', 'item', 954)
# atributo del los objetos (consumible, usable en batalla)
guardarJson('Objetos', 'item-attribute', 8)
# categoria de los objetos (medicina,evolitivos)
guardarJson('Objetos', 'item-category', 45)
# estado alterado (efecto) al usar objeto
guardarJson('Objetos', 'item-fling-effect', 7)
# bolsillo en el que se guardan los objetos
guardarJson('Objetos', 'item-pocket', 8)

# --------------------------------------- Encuentros ------------------------------------------------- #
# Metodo de encuentro
guardarJson('Encuentos', 'encounter-method', 19)
# Condiciones de encuentro (lluvia, dia)
guardarJson('Encuentos', 'encounter-condition', 6)
# Valor de la condicion de encuentro (radar, invierno)
guardarJson('Encuentos', 'encounter-condition-value', 20)

# --------------------------------------- Concursos ------------------------------------------------- #
# Tipo de concurso
guardarJson('Concursos', 'contest-type', 5)
# Efecto de un movimiento en un concurso
guardarJson('Concursos', 'contest-effect', 33)
# Efecto de un movimiento en un super concurso 
guardarJson('Concursos', 'super-contest-effect', 22)

# ----------------------------------------- Bayas ----------------------------------------------------- #
# baya
guardarJson('Bayas', 'berry', 64)
# dureza de la baya
guardarJson('Bayas', 'berry-firmness', 5)
# sabor de la baya
guardarJson('Bayas', 'berry-flavor', 5)

# --------------------------------------- Locaciones --------------------------------------------------- #
# Locaciones
guardarJson('Locaciones', 'location', 781)
# Area de ubicacion
guardarJson('Locaciones', 'location-area', 683)
# Area del parque
guardarJson('Locaciones', 'pal-park-area', 5)
# Region
guardarJson('Locaciones', 'region', 8)

# --------------------------------------- Juegos --------------------------------------------------- #
# Generaciones
guardarJson('Juegos', 'generation', 8)
# Pokedex
guardarJson('Juegos', 'pokedex', 24)
# Version del Juego
guardarJson('Juegos', 'version', 34)
# Versiones Agrupadas de los juegos
guardarJson('Juegos', 'version-group', 20)
# idioma
guardarJson('Juegos', 'language', 13)

# ----------------------------------------- Filtros ----------------------------------------------------- #
# pokemon
guardarJson2('zFiltros', 'pokemon', 893, 0, 'pokemon-no-transf')
guardarJson2('zFiltros', 'pokemon', 1117, 894, 'pokemon-transf')
guardarJson2('zFiltros', 'pokemon', 1117, 894, 'pokemon-transf')

# --------------------------------------- GuardarDatos --------------------------------------------------- #
guardarJsonDatos('Pokemon', 'pokemon', 893, 1)
guardarJsonDatos('Pokemon-Transf', 'pokemon', 10219, 10001)
guardarJsonDatos('Objetos', 'item', 666, 1)
guardarJsonDatos('Objetos', 'item', 671, 668)
guardarJsonDatos('Objetos', 'item', 679, 673)
guardarJsonDatos('Objetos', 'item', 749, 681)
guardarJsonDatos('Objetos', 'item', 765, 760)
guardarJsonDatos('Objetos', 'item', 770, 768)
#guardarJsonDatos('Objetos', 'item', 954, 768)
guardarJsonDatos('Movimientos', 'move', 784, 1)
guardarJsonDatos('Movimientos', 'move', 796, 786)
guardarJsonDatos('Movimientos', 'move', 10018, 10001)

print('Datos Guardados')