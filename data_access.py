from power_plant_data_access.service.service import Connect
Connect.connect()
from power_plant_data_access.service.utils import Utils


def data_access(country=None, status=None, type=None, limit=10):
    # default limit is 10.
    condition = {}
    condition.update({'Country': country})
    condition.update({'Status': status})
    condition.update({'PlantType': type})
    results = Utils.scan(condition, limit=limit)
    return results
