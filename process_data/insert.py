from google.cloud import firestore

db = firestore.Client()
collection = db.collection(u'raw_data')
