import requests
import json
# Consulta  a la base de datos
url = 'https://pokeapi.co/api/v2/'
res = requests.get(url+'pokemon/260') 
res2 = requests.get(url+'pokemon/132')
res3 = requests.get(url+'type?limit=20&offset=0')

r1 = res.json()
r2 = res2.json()
tiposPuchamones = res3.json()

lista = []
lista.append(r1)
lista.append(r2)

## Version pro optimizada
def filtrarPorTipo1(lista, tiposPuchamones):
    jsonTipos = {}
    for tipo in tiposPuchamones['results']:
        jsonTipos[tipo['name']] = []

    for pokemon in lista:     # Recorre los puchamones

            for k in pokemon['types']:  # Recorre los tipos de cada puchamon
                t = k['type']['name']
                jsonTipos[t].append(pokemon)

    s = json.dumps(jsonTipos, indent=4)
    return s

## Version chafa
def filtrarPorTipo2(lista, tiposPuchamones):
    listaPorTipos = []
    listaTipo = []

    for i in tiposPuchamones['results']:  #### Recorre los tipos
        t1 = (i['name'])

        for pokemon in lista:     #### Recorre los puchamones

            for k in pokemon['types']:  ### Recorre los tipos de cada puchamon
                t2 = k['type']['name']

                if t1 == t2:       ### Los tipos son iguales ?
                    listaTipo.append(pokemon)  ### Agrego el puchamon

        listaPorTipos.append({t1:listaTipo})
        listaTipo = []

    x = {'resultados':listaPorTipos}
    s = json.dumps(x, indent=4)
    return s

s = filtrarPorTipo1(lista,tiposPuchamones)
f = open("datos.json", "w")
f.write(s)
f.close()

#s = filtrarPorTipo2(lista,tiposPuchamones)
#f = open("datos.json", "w")
#f.write(s)
#f.close()