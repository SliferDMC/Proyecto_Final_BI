import pymysql
import json

# Credenciales de conexion a la base de datos
endpoint = "database-4.cmquk9u4dzlv.us-east-1.rds.amazonaws.com"
username = "admin"
password = "12345678"
database_name = "datahouse"
# Enlace a la BD
connection = pymysql.connect(endpoint, username, password, database_name)

#cursor.execute("DROP TABLE Habilidades")
cursor = connection.cursor()


#cursor.execute("create table Habilidades ( id INT NOT NULL AUTO_INCREMENT, nombreH nvarchar(255), nombreP nvarchar(255), descrip nvarchar(255), efecto nvarchar(255), generacion nvarchar(255), PRIMARY KEY (id))")
#cursor.execute("DROP TABLE Habilidades")
cursor.execute('insert into Habilidades (nombreH, nombreP, descrip, efecto, generacion) values("impakTrueno", "pikachu", "electrifica", "electrificacion", "milenial")')


cursor.execute('select * from Habilidades')



result = []
rows = cursor.fetchall()
for row in rows:
    result.append(row)

cursor.close()
def lambda_handler(event, context):
    
    return result
