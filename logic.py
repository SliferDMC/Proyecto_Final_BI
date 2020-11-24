print('AWS Hola mundo con Python')

import requests
import pandas as pd
import boto3

access_key  = 'AKIAQTCJUV7ZS32U2MP2'
secret_access_key = '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'

# Consulta  a la base de datos
url = 'https://pokeapi.co/api/v2/'
response = requests.get(url+'pokemon?limit=1050&offset=1') #Trae todos los pokemon del 1 al 1050

#Conversion a json, DataFrame y guardado en formato csv
r = response.json()
df = pd.DataFrame(r)
df.to_csv('/home/ubuntu/pokemon.csv')

# Cliente con las credenciales
client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

# Informacion necesaria para cargar al bucket
ruta = '/home/ubuntu/pokemon.csv'
name_bucket = 'bucket1-desarrollo'
save_route = 'Cargas/' + 'pokemon.csv'

#Carga del archivo hacia el bucket
client.upload_file('/home/ubuntu/pokemon.csv', name_bucket, save_route)