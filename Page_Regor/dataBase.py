from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb://mongo:IamrWxebtCvxKCXQsIDYZaAsPWeGCqCD@viaduct.proxy.rlwy.net:46899"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_ventas"]
    except ConnectionError:
        print('error de conexion con la base de datos')
    return db
