import json
import boto3

# Credenciales de acceso a s3
access_key  = 'AKIAQTCJUV7Z2HFDW4EW'
secret_access_key = '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'

#Enlace a s3
s3 = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
'''
# Credenciales de conexion a la base de datos
endpoint = "database-4.cmquk9u4dzlv.us-east-1.rds.amazonaws.com"
username = "admin"
password = "12345678"
database_name = "datahouse"

# Enlace a la BD
connection = pymysql.connect(endpoint, username, password, database_name)
'''
def lambda_handler(event, context):
    
    # --------------------------------- Habilidades ------------------------------------------------------- #
    bucket = 'bucket1-desarrollo'
    key = 'Pruebas/Datos/Habilidades/Habilidades-1.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    #for1 = jsonObject['lista']['effect_changes'][0]['effect_entries'][1]['effect']
    result = []
    for i in jsonObject['lista']:
        single = []
        single.append(i['effect_entries'][1]['effect'])
        single.append(i['effect_entries'][1]['short_effect'])
        single.append(i['name'])
        #single.append(i['effect_entries'][7]['short_effect'])
        aux=[]
        for j in i['pokemon']:
            aux.append(j['pokemon']['name'])
        single.append(aux)
        
    
        result.append(single)
    
 # --------------------------------- Locaciones ------------------------------------------------------- #    
    bucket = 'bucket1-desarrollo'
    key = 'Pruebas/Datos/Locaciones/Locaciones-1.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    #for1 = jsonObject['lista']['effect_changes'][0]['effect_entries'][1]['effect']
    resultL = []
    for i in jsonObject['lista']:
        single = []
        single.append(i['id'])
        single.append(i['name'])
        single.append(i['region']['name'])
        resultL.append(single)

    # --------------------------------- Areas ------------------------------------------------------- #    
    bucket = 'bucket1-desarrollo'
    key = 'Pruebas/Datos/Locaciones/Areas/Areas-1.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    #for1 = jsonObject['lista']['effect_changes'][0]['effect_entries'][1]['effect']
    resultA = []
    for i in jsonObject['lista']:
        single = []
        single.append(i['id'])
        single.append(i['name'])
        single.append(i['location']['name'])
        single.append(i['game_index'])
        aux=[]
        for j in i['pokemon_encounters']:
            aux.append(j['pokemon']['name'])
        single.append(aux)
        resultA.append(single)
        
    # --------------------------------- Objetos ------------------------------------------------------- #    
    bucket = 'bucket1-desarrollo'
    key = 'Pruebas/Datos/Objetos/Objetos-1.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())

    #for1 = jsonObject['lista']['effect_changes'][0]['effect_entries'][1]['effect']
    resultO = []
    for i in jsonObject['lista']:
        single = []
        single.append(i['id'])
        single.append(i['name'])
        single.append(i['cost'])
        single.append(i['category']['name'])
        aux=[]
        for j in i['game_indices']:
            aux.append(j['generation']['name'])
        single.append(aux)
        resultO.append(single)
   
    return result