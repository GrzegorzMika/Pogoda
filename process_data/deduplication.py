import logging
import sys

from sqlalchemy import create_engine, MetaData

credentials_path = sys.argv[1]

bigquery = create_engine(
    'bigquery://pogoda-312419/pogoda',
    credentials_path=credentials_path,
    echo=True
)
m = MetaData()
m.reflect(bind=bigquery)
tables = m.tables

for name in tables.keys():
    query = f'CREATE OR REPLACE TABLE {name} AS SELECT DISTINCT * FROM {name}'
    with bigquery.connect() as connection:
        result = connection.execute(query)
    logging.info(result)

