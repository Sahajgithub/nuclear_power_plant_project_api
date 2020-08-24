import yaml
import os.path


class Config:
    instance = None

    def __init__(self, config_file):

        path = os.path.dirname(os.path.realpath(__file__)) + '/' + config_file
        # print(os.path.dirname(os.path.realpath(__file__)))

        if config_file is None:
            raise Exception("None file cannot be passed")

        if os.path.isfile(path) is False:
            raise Exception("File doesn't exist")

        try:
            with open(path) as yaml_file:
                Config.instance = yaml.load(yaml_file, Loader=yaml.FullLoader)

        except IOError:
            raise Exception("Configuration file doesn't exist")

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
