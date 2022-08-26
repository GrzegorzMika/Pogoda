import asyncio
import json
import logging
from typing import Dict
import motor.motor_asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import aiohttp
import uvloop

logging.basicConfig(level='INFO')
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

params = {
    "appid": "3f096ec5f65dc99c42e1a8c5b785826f",
    "q": "Kraków",
    "lang": "en",
    "units": "metric"
}

conn_str = 'mongodb://root:example@localhost:27018/'


async def get_data(request_parameters: Dict[str, str]) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("http://api.openweathermap.org/data/2.5/weather",
                               params=request_parameters) as response:
            if response.status == 200:
                return await response.text()
            raise ConnectionError('Connection error: %s' % response.status)


async def do_insert(document):
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    db = client.raw_data
    result = await db.test_collection.insert_one(document)
    logging.info('result %s' % repr(result.inserted_id))


async def run():
    result = await get_data(params)
    await do_insert(json.loads(result))


if __name__ == "__main__":
    scheduler = AsyncIOScheduler()
    scheduler.add_job(run, 'interval', seconds=60)
    scheduler.start()

    asyncio.get_event_loop().run_forever()
