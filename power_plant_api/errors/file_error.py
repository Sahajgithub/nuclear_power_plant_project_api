class Error(Exception):
    def __init__(self, error_code, message=None):
        self._error_code = error_code
        self._message = message

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value


class InvalidFileError(Error):
    def __init__(self, error_code, message=None):
        super().__init__(error_code, message)


class InvalidPathError(Error):
    def __init__(self, error_code, message=None):
        super().__init__(error_code, message)


class InvalidFormatError(Error):
    def __init__(self, error_code, message=None):
        super().__init__(error_code, message)

