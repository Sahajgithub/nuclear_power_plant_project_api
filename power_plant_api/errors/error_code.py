from enum import Enum, unique


@unique
class ErrorCode(Enum):
    INVALID_FILE = 'invalid_file', 1, ""
    INVALID_PATH = 'invalid_path', 2, ""
    INVALID_FORMAT = 'invalid_format', 3, ""
    UNKNOWN = 'unknown', 100, ""

    def __init__(self, name, identity, description):
        self._names = name
        self._identity = identity
        self._description = description
