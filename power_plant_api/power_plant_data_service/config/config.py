import yaml
import os.path
from errors.file_error import InvalidFileError, InvalidPathError, InvalidFormatError
from errors.error_code import ErrorCode


class Config:
    instance = None

    def __init__(self, config_file):

        path = os.path.dirname(os.path.realpath(__file__)) + '/' + config_file

        if config_file is None:
            raise InvalidFileError(ErrorCode.INVALID_FILE, "None file cannot be passed")

        if os.path.isfile(path) is False:
            raise InvalidPathError(ErrorCode.INVALID_PATH, f"path {path} does not exist")

        file_extension = path.split('.')[-1]

        if file_extension != 'yaml':
            raise InvalidFormatError(ErrorCode.INVALID_FORMAT, f"File passed in {file_extension} format")

        with open(path) as yaml_file:
            Config.instance = yaml.load(yaml_file, Loader=yaml.FullLoader)



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
