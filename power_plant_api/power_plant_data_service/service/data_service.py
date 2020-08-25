from ..data_access_models.country_data_access import CountryDataAccess
from ..data_access_models.plant_type_data_access import TypeDataAccess
from ..data_access_models.status_data_access import StatusDataAccess
from ..data_access_models.plant_data_access import PlantDataAccess
# from collections import OrderedDict


class DataService:
    @staticmethod
    def map_attributes_to_methods(plant, country, status, plant_type):
        mapping = {'Id': plant.id,
                   'Name': plant.name,
                   'Latitude': plant.latitude,
                   'Longitude': plant.longitude,
                   'CountryCode': plant.country_code,
                   'StatusId': plant.status_id,
                   'TypeId': plant.type_id,
                    'Model': plant.model,
                    'ConstructionStart': plant.construction_start,
                    'OperationalFrom': plant.operational_from,
                    'OperationalTo': plant.operational_to,
                    'Capacity': plant.capacity,
                    'Source': plant.info_source,
                    'LastUpdated': plant.last_updated,
                    'Country': country,
                    'Status': status,
                    'PlantType': plant_type[0],
                    'Description': plant_type[1]}
        return mapping

    @staticmethod
    def get_specific_power_plants(condition, plants_to_skip=0, plants_required=10):
        ctr = 1
        plants = PlantDataAccess.get_limited_plants(plants_to_skip, None)
        result = []
        country_occurred = {}
        status_occurred = {}
        type_occurred = {}
        for plant in plants:
            if ctr > plants_required:
                break
            if plant is not None:

                if plant.country_code in country_occurred.keys():
                    country = {plant.country_code: country_occurred[plant.country_code]}
                else:
                    country = CountryDataAccess.country_from_code(plant.country_code)
                    country_occurred.update(country)
                    plant.country_code = next(iter(country))

                if plant.status_id in status_occurred.keys():
                    status = {plant.status_id: status_occurred[plant.status_id]}
                else:
                    status = StatusDataAccess.status_from_status_id(plant.status_id)
                    status_occurred.update(status)
                    plant.status_id = next(iter(status))

                if plant.type_id in type_occurred.keys():
                    plant_type = {plant.type_id: type_occurred[plant.type_id]}
                else:
                    plant_type = TypeDataAccess.type_from_type_id(plant.type_id)
                    type_occurred.update(plant_type)
                    plant.type_id = next(iter(plant_type))

                mapping = DataService.map_attributes_to_methods(plant, country[plant.country_code],
                                                                status[plant.status_id], plant_type[plant.type_id])

                # check if the plant satisfies given conditions

                flag = True
                for key, val in condition.items():

                    if val is None:
                        continue
                    if mapping[key] is not None:
                        if str(mapping[key]).lower() != str(val).lower():
                            flag = False
                    else:
                        flag = False

                if flag is True:
                    # add plant to the result
                    dict = {}
                    for key, val in mapping.items():
                        dict.update({key: val})
                    result.append(dict)
                    ctr = ctr + 1
        return result

    @staticmethod
    def get_power_plants(plants_to_skip=0, plants_required=500):
        plants = PlantDataAccess.get_limited_plants(plants_to_skip, plants_required)
        result = []
        country_occurred = {}
        status_occurred = {}
        type_occurred = {}
        for plant in plants:
            if plant is not None:

                if plant.country_code in country_occurred.keys():
                    country = {plant.country_code: country_occurred[plant.country_code]}
                else:
                    country = CountryDataAccess.country_from_code(plant.country_code)
                    country_occurred.update(country)
                    plant.country_code = next(iter(country))

                if plant.status_id in status_occurred.keys():
                    status = {plant.status_id: status_occurred[plant.status_id]}
                else:
                    status = StatusDataAccess.status_from_status_id(plant.status_id)
                    status_occurred.update(status)
                    plant.status_id = next(iter(status))

                if plant.type_id in type_occurred.keys():
                    plant_type = {plant.type_id: type_occurred[plant.type_id]}
                else:
                    plant_type = TypeDataAccess.type_from_type_id(plant.type_id)
                    type_occurred.update(plant_type)
                    plant.type_id = next(iter(plant_type))

                mapping = DataService.map_attributes_to_methods(plant, country[plant.country_code],
                                                                status[plant.status_id], plant_type[plant.type_id])

                dict = {}
                for key, val in mapping.items():
                    dict.update({key: val})
                result.append(dict)

        return result
