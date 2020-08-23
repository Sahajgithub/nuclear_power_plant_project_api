

class PlantType:
    def __init__(self, type_id, plant_type, description):
        self._type_id = type_id
        self._plant_type = plant_type
        self._description = description

    @property
    def type_id(self):
        return self._type_id

    @type_id.setter
    def type_id(self, _type_id):
        self._type_id = _type_id

    @property
    def plant_type(self):
        return self._plant_type

    @plant_type.setter
    def plant_type(self, _plant_type):
        self._plant_type = _plant_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, _description):
        self._description = _description