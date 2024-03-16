from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://AxelEduardo14:Gorditos343@cluster0.lxuhlyq.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_ventas"]
    except ConnectionError:
        print('error de conexion con la base de datos')
    return db