from ..config.config import Config
from ..config.Mongoclient import MongoClient


class Connect:
    @staticmethod
    def connect():
        config_file = "power_plant_data_access/config/config.yaml"
        config = Config.get_instance(config_file)
        MongoClient.get_instance(config)


