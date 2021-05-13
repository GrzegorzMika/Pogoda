from datetime import datetime


class DataProcessor:
    def __init__(self):
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
            'weather': self.get_weather_info
        }

    def __call__(self, response):
        for key, function in self.methods:
            self.insert_data(response, key, function)

    def insert_data(self, response, key, function):
        pass

    @staticmethod
    def get_temperature_info(response):
        return [
            response.get('main').get('temp'),
            response.get('main').get('feels_like'),
            response.get('main').get('temp_min'),
            response.get('main').get('temp_max')
        ]

    @staticmethod
    def get_pressure_info(response):
        return [
            response.get('main').get('pressure'),
            response.get('main').get('sea_level'),
            response.get('main').get('grnd_level')
        ]

    @staticmethod
    def get_humidity_info(response):
        return response.get('main').get('humidity')

    @staticmethod
    def get_wind_info(response):
        return [
            response.get('wind').get('speed'),
            response.get('wind').get('deg'),
            response.get('wind').get('gust')
        ]

    @staticmethod
    def get_clouds_info(response):
        return [
            response.get('clouds').get('all'),
            response.get('visibility')
        ]

    @staticmethod
    def get_rain_info(response):
        return [
            response.get('rain').get('1h'),
            response.get('rain').get('3h')
        ]

    @staticmethod
    def get_snow_info(response):
        return [
            response.get('snow').get('1h'),
            response.get('snow').get('3h')
        ]

    @staticmethod
    def get_sun_info(response):
        return [
            response.get('sys').get('sunrise'),
            response.get('sys').get('sunset')
        ]

    @staticmethod
    def get_location_info(response):
        return [
            response.get('name'),
            response.get('sys').get('country'),
            response.get('coord').get('lon'),
            response.get('coord').get('lat')
        ]

    @staticmethod
    def get_weather_info(response):
        return [
            response.get('weather')[0].get('id'),
            response.get('weather')[0].get('main'),
            response.get('weather')[0].get('description'),
            response.get('weather')[0].get('icon')
        ]

    @staticmethod
    def get_key(response):
        return [
            response.get('id'),
            datetime.utcfromtimestamp(response.get('dt') + response.get('timezone')).strftime("%Y-%m-%d %H:%M:%S")
        ]
