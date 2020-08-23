from power_plant_data_service.service.connection_service import Connect
Connect.connect()
from power_plant_data_service.service.data_service import DataService


def power_plant_data(country=None, status=None, type=None, limit=10):
    # Default limit on no of records is 10.
    condition = {}
    condition.update({'Country': country})
    condition.update({'Status': status})
    condition.update({'PlantType': type})
    results = DataService.get_power_plants(condition, limit)
    return results


def get_all_plants():

    results = DataService.get_all_power_plants(limit=800)
    # for plant in results:
    #     print(plant)

    return results


