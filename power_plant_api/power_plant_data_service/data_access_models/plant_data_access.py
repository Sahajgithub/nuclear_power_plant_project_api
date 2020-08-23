from ..config.config import Config
from ..config.Mongoclient import MongoClient
from ..models.plant import Plant


class PlantDataAccess:
    @staticmethod
    def get_all_plants():
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['PLANT']]
        plant_cursor = collection.find({})
        plants = [Plant(plant_id=plant['_id'], name=plant['Name'], latitude=plant['Latitude'],
                        longitude=plant['Longitude'], country_code=plant['CountryCode'], status_id=plant['StatusId'],
                        type_id=plant['ReactorTypeId'], model=plant['ReactorModel'],
                        construction_start=plant['ConstructionStartAt'], operational_from=plant['OperationalFrom'],
                        operational_to=plant['OperationalTo'], capacity=plant['Capacity'],
                        info_source=plant['Source'], last_updated=plant['LastUpdatedAt']) for plant in plant_cursor]
        return plants
