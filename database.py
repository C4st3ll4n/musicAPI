from urllib.parse import quote_plus

from pymongo import MongoClient

_password = quote_plus("!@#H3nr1qu3!@#")
_username = quote_plus("castellan")
url = f"mongodb+srv://{_password}:{_username}@cluster0.dhw7s.mongodb.net/music?retryWrites=true&w=majority"
#client = MongoClient(url)

"""
    Recuperando a referencia do banco
"""
#db = client.get_database("music")

"""
   Criando as coleções 
"""
#db.create_collection("albuns")