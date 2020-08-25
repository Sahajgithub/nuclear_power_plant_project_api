import pymongo
from power_plant_data_service.config.config import Config


class MongoClient:
    instance = None

    def __init__(self, config):
        if MongoClient.instance is None:
            url = config['MONGO']['URL']
            MongoClient.instance = pymongo.MongoClient(url)
        else:
            print("Multiple instances can't be generated")

    @staticmethod
    def get_instance(config=None):
        if config is None:
            config = Config.get_instance()
            if config is None:
                raise Exception("Config not instantiated")

        if MongoClient.instance is None:
            MongoClient(config)
        return MongoClient.instance
