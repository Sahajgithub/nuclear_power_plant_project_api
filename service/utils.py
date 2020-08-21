from power_plant_data_access.dataAccess.country_data_access import CountryDataAccess
from power_plant_data_access.dataAccess.plant_type_data_access import TypeDataAccess
from power_plant_data_access.dataAccess.status_data_access import StatusDataAccess
from power_plant_data_access.dataAccess.plant_data_access import PlantDataAccess


class Utils:
    @staticmethod
    def map(plant, country, status, plant_type):
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
                    'Country': country.country,
                    'Status': status.status,
                    'PlantType': plant_type.plant_type,
                    'Description': plant_type.description}
        return mapping

    @staticmethod
    def scan(condition, limit):
        ctr = 1
        plants = PlantDataAccess.get_all_plants()
        result = []
        for plant in plants:
            if ctr > limit:
                break
            if plant is not None:
                country = CountryDataAccess.get_country(plant.country_code)
                status = StatusDataAccess.get_status(plant.status_id)
                plant_type = TypeDataAccess.get_plant_type(plant.type_id)
                mapping = Utils.map(plant, country, status, plant_type)

                flag = True
                for key, val in condition.items():
                    if key in mapping.keys():
                        if val is None:
                            continue
                        if mapping[key] is not None:
                            # print(str(mapping[key]).lower())
                            if str(mapping[key]).lower() != str(val).lower():
                                flag = False
                        else:
                            flag = False

                if flag is True:
                    dict = {}
                    for key, val in mapping.items():
                        dict.update({key: val})
                    result.append(dict)
                    ctr = ctr + 1

        return result
