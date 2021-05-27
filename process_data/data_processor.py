import logging
from datetime import datetime

from sqlalchemy import create_engine, MetaData


class DataProcessor:
    def __init__(self, credentials_path):
        self.methods = {
            'temperature': self.get_temperature_info,
            'pressure': self.get_pressure_info,
            'humidity': self.get_humidity_info,
            'wind': self.get_wind_info,
            'clouds': self.get_clouds_info,
            'rain': self.get_rain_info,
            'snow': self.get_snow_info,
            'sun': self.get_sun_info,
            'location': self.get_location_info,
            'weather': self.get_weather_info,
            'time': self.get_time_info
        }
        self.bigquery = create_engine(
            'bigquery://pogoda-312419/pogoda',
            credentials_path=credentials_path,
            echo=True
        )
        m = MetaData()
        m.reflect(bind=self.bigquery)
        self.tables = m.tables

    def __call__(self, response):
        for key, function in self.methods.items():
            self.insert_data(response, key, function)

    def insert_data(self, response, key, function):
        data = function(response)
        identifier = self.get_key(response)
        to_insert = identifier + data
        table = self.tables[key]
        ins = table.insert().values(to_insert)
        with self.bigquery.connect() as connection:
            result = connection.execute(ins)
        logging.info(result)

    @staticmethod
    def get_temperature_info(response):
        try:
            return [
                response.get('main').get('temp'),
                response.get('main').get('feels_like'),
                response.get('main').get('temp_min'),
                response.get('main').get('temp_max')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None, None, None]

    @staticmethod
    def get_pressure_info(response):
        try:
            return [
                response.get('main').get('pressure'),
                response.get('main').get('sea_level'),
                response.get('main').get('grnd_level')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None, None]

    @staticmethod
    def get_humidity_info(response):
        try:
            return [response.get('main').get('humidity')]
        except AttributeError as e:
            logging.error(e)
            return [None]

    @staticmethod
    def get_wind_info(response):
        try:
            return [
                response.get('wind').get('speed'),
                response.get('wind').get('deg'),
                response.get('wind').get('gust')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None, None]

    @staticmethod
    def get_clouds_info(response):
        try:
            return [
                response.get('clouds').get('all'),
                response.get('visibility')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]

    @staticmethod
    def get_rain_info(response):
        try:
            return [
                response.get('rain').get('1h'),
                response.get('rain').get('3h')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]

    @staticmethod
    def get_snow_info(response):
        try:
            return [
                response.get('snow').get('1h'),
                response.get('snow').get('3h')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]

    @staticmethod
    def get_sun_info(response):
        try:
            return [
                datetime.utcfromtimestamp(response.get('sys').get('sunrise') + response.get('timezone')).strftime("%Y-%m-%d %H:%M:%S"),
                datetime.utcfromtimestamp(response.get('sys').get('sunset') + response.get('timezone')).strftime("%Y-%m-%d %H:%M:%S")
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]

    @staticmethod
    def get_location_info(response):
        try:
            return [
                response.get('name'),
                response.get('sys').get('country'),
                response.get('coord').get('lon'),
                response.get('coord').get('lat')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None, None, None]

    @staticmethod
    def get_weather_info(response):
        try:
            return [
                response.get('weather')[0].get('id'),
                response.get('weather')[0].get('main'),
                response.get('weather')[0].get('description'),
                response.get('weather')[0].get('icon')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None, None, None]

    @staticmethod
    def get_key(response):
        try:
            return [
                response.get('id'),
                datetime.utcfromtimestamp(response.get('dt') + response.get('timezone')).strftime("%Y-%m-%d %H:%M:%S")
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]

    @staticmethod
    def get_time_info(response):
        try:
            return [
                response.get('dt'),
                response.get('timezone')
            ]
        except AttributeError as e:
            logging.error(e)
            return [None, None]
