import yaml
import os.path


class Config:
    instance = None

    def __init__(self, config_file):
        if config_file is None:
            raise Exception("None file cannot be passed")
        if os.path.isfile(config_file) is False:
            raise Exception("File doesn't exist")
        try:
            yaml_file = open(config_file)
            Config.instance = yaml.load(yaml_file, Loader=yaml.FullLoader)
        except:
            raise Exception("File passed is not in correct format")

    @staticmethod
    def get_instance(config=None):
        if config is None:
            if Config.instance is not None:
                return Config.instance
            else:
                raise Exception("None file passed and instance not present")
        elif Config.instance is None:
            Config(config)
        return Config.instance
