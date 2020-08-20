from power_plant_data_access.config.config import Config
from power_plant_data_access.config.Mongoclient import MongoClient
from power_plant_data_access.models.status import Status


class StatusDataAccess:
    @staticmethod
    def get_all_status():
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['STATUS']]
        status_cursor = collection.find({})
        status = [Status(status_id=status['_id'], status=status['Type']) for status in status_cursor]
        return status

    @staticmethod
    def get_status(status_id):
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['STATUS']]
        status_cursor = collection.find_one({'_id': status_id})
        if status_cursor is None:
            status = Status(status_id='Unknown', status='Unknown')
        else:
            status = Status(status_id=status_cursor['_id'], status=status_cursor['Type'])
        return status
