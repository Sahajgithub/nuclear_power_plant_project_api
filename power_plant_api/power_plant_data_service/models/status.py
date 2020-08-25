

class Status:
    def __init__(self, status_id, status):
        self._status_id = status_id
        self._status = status

    @property
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, _status_id):
        self._status_id = _status_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, _status):
        self._status = _status
