

class Plant:
    def __init__(self, plant_id, name, latitude, longitude, country_code, status_id,
                 type_id, model, construction_start, operational_from, operational_to,
                 capacity, info_source, last_updated):
        self._id = plant_id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        self._country_code = country_code
        self._status_id = status_id
        self._type_id = type_id
        self._model = model
        self._construction_start = construction_start
        self._operational_from = operational_from
        self._operational_to = operational_to
        self._capacity = capacity
        self._info_source = info_source
        self._last_updated = last_updated

    # getters & setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, _latitude):
        self._latitude = _latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, _longitude):
        self._longitude = _longitude

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, _country_code):
        return self._country_code

    @property
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, _status_id):
        self._status_id = _status_id

    @property
    def type_id(self):
        return self._type_id

    @type_id.setter
    def type_id(self, _type_id):
        self._type_id = _type_id

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, _model):
        self._model = _model

    @property
    def construction_start(self):
        return self._construction_start

    @construction_start.setter
    def construction_start(self, _construction_start):
        self._construction_start = _construction_start

    @property
    def operational_from(self):
        return self._operational_from

    @operational_from.setter
    def operational_from(self, _operational_from):
        self._operational_from = _operational_from

    @property
    def operational_to(self):
        return self._operational_to

    @operational_to.setter
    def operational_to(self, _operational_to):
        self._operational_to =_operational_to

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, _capacity):
        self._capacity = _capacity

    @property
    def info_source(self):
        return self._info_source

    @info_source.setter
    def info_source(self, _info_source):
        self._info_source = _info_source

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, _last_updated):
        self._last_updated = _last_updated



