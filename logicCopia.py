print('AWS Hola mundo con Python')

import requests
import boto3
import json



# Consulta  a la base de datos
url = 'https://pokeapi.co/api/v2/'
response = requests.get(url+'pokemon?limit=1050&offset=1') #Trae todos los pokemon del 1 al 1050

#Conversion a json
r = response.json()
s = json.dumps(r, indent=4)
f = open("/home/ubuntu/datos.json", "w")
f.write(s)
f.close()

# Cliente con las credenciales
client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

# Informacion necesaria para cargar al bucket
ruta = '/home/ubuntu/datos.json'
name_bucket = 'bucket1-desarrollo'
save_route = 'PrimerasCargas/' + 'datos.json'

#Carga del archivo hacia el bucket
client.upload_file(ruta, name_bucket, save_route)
