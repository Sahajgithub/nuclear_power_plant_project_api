from power_plant_data_service.service.connection_service import Connect
Connect.connect()
from power_plant_data_service.service.data_service import DataService


def specific_power_plant_data(country=None, status=None, type=None):
    # Default limit on no of records is 10.
    condition = {}
    condition.update({'Country': country})
    condition.update({'Status': status})
    condition.update({'PlantType': type})
    results = DataService.get_specific_power_plants(condition)
    return results


def power_plant_data(current_page=1, page_size=2):

    plants_to_skip = (current_page-1)*page_size
    plants_required = page_size
    results = DataService.get_power_plants(plants_to_skip, plants_required)
    return results


