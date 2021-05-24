import sys

from sqlalchemy import MetaData, create_engine, Table, Column, Integer, DateTime, Float, String

if __name__ == '__main__':
    credentials_path = sys.argv[1]

    engine = create_engine(
        'bigquery://pogoda-312419/pogoda',
        credentials_path=credentials_path
    )
    meta = MetaData()

    temperature = Table(
        'temperature', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('temperature', Float),
        Column('feels_like', Float),
        Column('temperature_min', Float),
        Column('temperature_max', Float)
    )
    pressure = Table(
        'pressure', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('pressure', Float),
        Column('sea_level', Float),
        Column('ground_level', Float)
    )
    humidity = Table(
        'humidity', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('humidity', Float)
    )
    wind = Table(
        'wind', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('speed', Float),
        Column('degrees', Float),
        Column('gust', Float)
    )
    clouds = Table(
        'clouds', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('clouds', Float),
        Column('visibility', Float)
    )
    rain = Table(
        'rain', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('rain_1h', Float),
        Column('rain_3h', Float)
    )
    snow = Table(
        'snow', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('snow_1h', Float),
        Column('snow_3h', Float)
    )
    sun = Table(
        'sun', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('sunrise', DateTime),
        Column('sunset', DateTime)
    )
    location = Table(
        'location', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('name', String(128)),
        Column('country', String(2)),
        Column('longitude', Float),
        Column('latitude', Float)
    )
    weather = Table(
        'weather', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, primary_key=True),
        Column('condition_id', Integer),
        Column('group_parameters', String(128)),
        Column('description', String(512)),
        Column('icon', String(3))
    )

    meta.create_all(engine)
