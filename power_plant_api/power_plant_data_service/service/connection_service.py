from ..config.config import Config
from ..config.Mongoclient import MongoClient


class Connect:
    @staticmethod
    def connect():
        config_file = "config.yaml"
        config = Config.get_instance(config_file)
        MongoClient.get_instance(config)


