from ..config.config import Config
from ..config.Mongoclient import MongoClient
from ..models.country import Country


class CountryDataAccess:
    @staticmethod
    def get_all_countries():
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['COUNTRY']]
        country_cursor = collection.find({})
        countries = [Country(country_id=country['_id'], country_code=country['Code'],
                             country=country['Name']) for country in country_cursor]
        return countries

    @staticmethod
    def get_country(country_code):
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['COUNTRY']]
        country_cursor = collection.find_one({'Code': country_code})
        if country_cursor is None:
            country = Country(country_id='Unknown', country_code='Unknown',
                              country='Unknown')
        else:
            country = Country(country_id=country_cursor['_id'], country_code=country_cursor['Code'],
                              country=country_cursor['Name'])
        return country

    @staticmethod
    def country_from_code(country_code):
        config = Config.get_instance()
        client = MongoClient.get_instance(config)
        db = client[config['DB']]
        collection = db[config['COLLECTION']['COUNTRY']]
        cursor = collection.find_one({'Code': country_code})

        if cursor is None:
            return {'Unknown': 'Unknown'}
        else:
            # print({country_code: cursor['Name']})
            return {country_code: cursor['Name']}





