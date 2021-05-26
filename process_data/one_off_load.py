import sys

from tqdm import tqdm
from google.cloud import firestore

from data_processor import DataProcessor

db = firestore.Client()
collection = db.collection(u'raw_data')
docs = collection.stream()

if __name__ == '__main__':
    credentials_path = sys.argv[1]

    data_processor = DataProcessor(credentials_path)
    for doc in tqdm(docs):
        data_processor(doc.to_dict())
