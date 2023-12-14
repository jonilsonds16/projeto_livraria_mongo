from pymongo import MongoClient
from pymongo.server_api import ServerApi


class ClientFactory:

    def get_client(self):
        return MongoClient(
            'mongodb+srv://jonilsonds9:QmENRV1ddPg139Mk@cluster0.z1mraoi.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
