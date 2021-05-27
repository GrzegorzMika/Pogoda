import sys

from google.cloud import firestore
from tqdm import tqdm

from data_processor import DataProcessor

db = firestore.Client()
collection = db.collection(u'raw_data')

if __name__ == '__main':
    credentials_path = sys.argv[1]
    data_processor = DataProcessor(credentials_path)

    with data_processor.bigquery.connect() as conn:
        res = conn.execute('SELECT max(dt) AS last_dt FROM time;')
    last_dt = res.fetchone()['last_dt']

    docs = collection.where(u'dt', u'>', last_dt).stream()

    for doc in tqdm(docs):
        data_processor(doc.to_dict())
