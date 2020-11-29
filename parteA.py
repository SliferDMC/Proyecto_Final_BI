#import pandas as pd
import requests
import boto3
import json
import os

# Escribe los Datos en un archivo Json en la ruta especificada
def EscribirJson(aJson, ruta, nArchivo):
    s = json.dumps(aJson, indent=4)
    dir = 'D:/Pruebas/'+ruta  # También es válido 'C:\\Pruebas' o r'C:\Pruebas'
    f = open(dir+nArchivo+'.json', "w")
    f.write(s)
    f.close()

#convierte un arreglo en un Json para escribirlo en una ruta especificada
def EscribirArregloJson(aJson, ruta, nArchivo):
    x={'lista':aJson}
    EscribirJson(x, ruta, nArchivo)

#obtine la lista de las url de la busqueda perdida
def obtenerLista(nombre, cantidad, inicial):
    url = 'https://pokeapi.co/api/v2/'
    response = requests.get(url+nombre+'?limit='+str(cantidad)+'&offset='+str(inicial)).json()
    return response

#obtine la lista de las url de la busqueda perdida desde el primer valor
def obtenerListaI(nombre, cantidad):
    return obtenerLista(nombre, cantidad, 0)

# separa los datos de los Json de 100 en 100 datos
def separar100JsonDatos(lista,nArchivo):
    r=[]
    i=1
    cont=0
    for j in lista:
        r.append(j)
        if (i%100)==0 :
            cont=cont+1
            EscribirArregloJson(r, 'Datos/', nArchivo+'-'+str(cont))
            r=[]
        i=i+1
    if r!=[] :
        if cont==0 :
            EscribirArregloJson(r, 'Datos/', nArchivo)
        else: 
            cont=cont+1
            EscribirArregloJson(r, 'Datos/', nArchivo+'-'+str(cont))

# metodo para filtrar por una caracteristica que sea una lista de Json
def filtrarListaDef(lista,filtroPlural, filtro,ListaFiltro):
    jsonTipos = {}
    for tipo in ListaFiltro['results']:
        jsonTipos[tipo['name']] = []
    for pokemon in lista:
            for k in pokemon[filtroPlural]:
                try:
                    t = k[filtro]['name']
                    jsonTipos[t].append(pokemon)
                except:
                    ""
               
    return jsonTipos

## metdodo que sirver para cualquier filtro indivdual de una lista de Json
def filtroDefinitivo(lista,filtro, ListaFiltro):
    jsonTipos = {}
    for tipo in ListaFiltro['results']:
        jsonTipos[tipo['name']] = []

    for tipo in lista:     # Recorre los puchamones
        try:
            t = tipo[filtro]['name']
            jsonTipos[t].append(tipo)
        except:
            ""
        
    return jsonTipos

# metodo que sirver para filtrar cualquier tipo de lista de Json en donde la carcteriesta este dentro de otra
def filtro2Busquedas(lista,filtro1,filtro2, ListaFiltro):
    jsonTipos = {}
    for tipo in ListaFiltro['results']:
        jsonTipos[tipo['name']] = []

    for tipo in lista:
        try:
            t = tipo[filtro1][filtro2]['name']
            jsonTipos[t].append(tipo)
        except:
            ""
            
    return jsonTipos

#guarda los datos en un arreglo utiizando una lista de datos por medio de su URL
def guardarJsonDatosUrL(nombre, cantidad, inicio):
    listaNombres = obtenerLista(nombre, cantidad, inicio-1)
    r=[]
    for i in listaNombres['results']: 
        # Consulta  a la base de datos
        response = requests.get(i['url']) 
        #Conversion a json, DataFrame y guardado en formato csv r= response.json()
        r.append(response.json())
    return r

# -------------------------------------- Busquedas variadas sin filtros ------------------------------------- #    
#busca y guarda todas las habilidades existentes
listaAb=guardarJsonDatosUrL('ability', 293, 1)
separar100JsonDatos(listaAb,'Habilidades/Habilidades')

#busca y guarda todas las Cadenas Evolutivas de los pokemon
listaPCh=guardarJsonDatosUrL('evolution-chain', 467, 1)
separar100JsonDatos(listaPCh,'Pokemon/CadenasEvolutivas/Evoluciones')

#busca y guarda todas las Localizaciones de las Areas en las que se pueden encontrar pokemon
listaLA=guardarJsonDatosUrL('location-area', 683, 1)
separar100JsonDatos(listaLA,'Locaciones/Areas/Areas')

#busca y guarda todas las Localizaciones en las que se pueden encontrar pokemon
listaL=guardarJsonDatosUrL('location', 781, 1)
separar100JsonDatos(listaL,'Locaciones/Locaciones')

#busca y guarda todos los objetos que hay en los juegos
listaIt=guardarJsonDatosUrL('item', 954, 1)
separar100JsonDatos(listaIt,'Objetos/Objetos')

#busca y guarda todas las especies de pokemon
listaSp=guardarJsonDatosUrL('pokemon-species', 898, 1)
separar100JsonDatos(listaSp,'Pokemon/Especies/especies')

# ------------------------------------------------- Movimientos ----------------------------------------------- #
#busca y guarda todos los movimientos que pueden aprender los pokemon
listaMv=guardarJsonDatosUrL('move', 813, 1)
separar100JsonDatos(listaMv,'Movimientos/movimientos')

#Filtra los movientos separandolos por su tipo
Lfiltro=obtenerListaI('type', 20)
tiposMV=filtroDefinitivo(listaMv,'type',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/Tipos/movimientos-Type-'+tipo['name'])
        num = num+1

#Filtra los movientos separandolos por el objetivo en el que tienen efecto
Lfiltro=obtenerListaI('move-target', 14)
tiposMV=filtroDefinitivo(listaMv,'target',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/Objetivo/movimientos-Type-'+tipo['name'])
        num = num+1

#Filtra los movientos separandolos por su generacion de debut
Lfiltro=obtenerListaI('generation', 8)
tiposMV=filtroDefinitivo(listaMv,'generation',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/Generacion/movimientos-Gen-'+tipo['name'])
        num = num+1

#Filtra los movientos separandolos por el estado alterado que inflingen
Lfiltro=obtenerListaI('move-ailment', 14)
tiposMV=filtro2Busquedas(listaMv,'meta','ailment',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/EstadoAlterado/movimientos-Ailment-'+tipo['name'])
        num = num+1

#Filtra los movientos separandolos por la categoria a la que pertencen
Lfiltro=obtenerListaI('move-category', 14)
tiposMV=filtro2Busquedas(listaMv,'meta','category',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/Categoria/movimientos-Cat-'+tipo['name'])
        num = num+1

#Filtra los movientos separandolos por su el tipo de daño que realizan
Lfiltro=obtenerListaI('move-damage-class', 14)
tiposMV=filtroDefinitivo(listaMv,'damage_class',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposMV[tipo['name']],'Movimientos/ClaseDanio/movimientos-damage-'+tipo['name'])
        num = num+1

# ------------------------------------------------- Pokemon ------------------------------------------------- #

#busca y guarda todos los Pokemon separandolos en las transformaciones y no transformaciones
listaPT=guardarJsonDatosUrL('pokemon', 1117, 899)
separar100JsonDatos(listaPT,'Pokemon-Transf/Pokemon-Transf')
listaPT=guardarJsonDatosUrL('pokemon', 898, 1)
separar100JsonDatos(listaPT,'Pokemon-Transf/Pokemon-NoTransf')

#busca y guarda todos los pokemon sin filtros
listaP=guardarJsonDatosUrL('pokemon', 1117, 1)
separar100JsonDatos(listaP,'Pokemon/Pokemon')

#Filtra los pokemon separandolos por los tipos a los que perteneces
Lfiltro=obtenerListaI('type', 20)
tiposPT=filtrarListaDef(listaP,'types','type',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposPT[tipo['name']],'Pokemon/Tipos/Pokemon-Type-'+tipo['name'])
        num = num+1

#Filtra los pokemon separandolos por las habilidades que tienen
Lfiltro=obtenerListaI('ability', 299)
tiposPT=filtrarListaDef(listaP,'abilities','ability',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposPT[tipo['name']],'Pokemon/Habilidades/Pokemon-Ability-'+tipo['name'])
        num = num+1

print('Datos Guardados')

"""
#Filtra los pokemon separandolos por los movimientos que pueden aprender
Lfiltro=obtenerListaI('move', 813)
tiposPT=filtrarListaDef(listaP,'moves','move',Lfiltro)
num=1
for tipo in Lfiltro['results']:
        separar100JsonDatos(tiposPT[tipo['name']],'Pokemon/Movimientos/Pokemon-Mv-'+tipo['name'])
        num = num+1
"""