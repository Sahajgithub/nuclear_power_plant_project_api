

class Country:
    def __init__(self, country_id, country_code, country):
        self._country_id = country_id
        self._country_code = country_code
        self._country = country

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, _country_code):
        self._country_code = _country_code

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, _country_id):
        self._country_id = _country_id

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, _country):
        self._country = _country