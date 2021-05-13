from sqlalchemy import MetaData, create_engine, Table, Column, Integer, DateTime
import os

password = os.environ['SQL_PASSWORD']


engine = create_engine(f'postgresql+psycopg2://postgres:{password}@34.116.240.161/pogoda', echo = True)
meta = MetaData()

temperature = Table(
    'temperature', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
pressure = Table(
    'pressure', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
humidity = Table(
    'humidity', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
wind = Table(
    'wind', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
clouds = Table(
    'clouds', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
rain = Table(
    'rain', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
snow = Table(
    'snow', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
sun = Table(
    'sun', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
location = Table(
    'location', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)
weather = Table(
    'weather', meta,
    Column('ID', Integer, primary_key=True),
    Column('Timestamp', DateTime, primary_key=True),
)