from power_plant_data_access.config.config import Config
from power_plant_data_access.config.Mongoclient import MongoClient
from power_plant_data_access.models.plant_type import PlantType


class TypeDataAccess:
    @staticmethod
    def get_all_types():
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['TYPE']]
        type_cursor = collection.find({})
        plant_types = [PlantType(type_id=type['_id'], plant_type=type['Type'],
                                 description=type['Description']) for type in type_cursor]
        return plant_types

    @staticmethod
    def get_plant_type(type_id):
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['TYPE']]
        type_cursor = collection.find_one({'_id': type_id})
        if type_cursor is None:
            plant_type = PlantType(type_id='Unknown', plant_type='Unknown',
                                   description='Unknown')
        else:
            plant_type = PlantType(type_id=type_cursor['_id'], plant_type=type_cursor['Type'],
                                   description=type_cursor['Description'])
        return plant_type

