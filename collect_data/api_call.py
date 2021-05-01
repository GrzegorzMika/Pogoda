import sched
import time

import requests
# from pymongo import MongoClient
from google.cloud import firestore

s = sched.scheduler(time.time, time.sleep)
delay = 900
params = {
    "appid": "3f096ec5f65dc99c42e1a8c5b785826f",
    "q": "Kraków",
    "lang": "en",
    "units": "metric"
}

# client = MongoClient('mongodb://127.0.0.1:27017')
# db = client.pogoda
db = firestore.Client()
collection = db.collection(u'raw_data')


def run_calls():
    try:
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/weather", params=params)
        # result = db.raw_data.insert_one(response.json())
        # print(result.inserted_id)
        collection.add(response.json())
    except ConnectionError as e:
        print(e)
    s.enter(delay, 1, run_calls)


s.enter(delay, 1, run_calls)
s.run()
