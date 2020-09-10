import aiohttp, asyncio, json, os
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv

now = datetime.now()
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
api = os.environ.get("API_KEY")


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        weather = await fetch(session, f'https://api.openweathermap.org/data/2.5/weather?q=jakarta&appid={api}')
        data_weather = json.loads(weather)
        temperature = f"{data_weather['weather'][0]['main']}, {data_weather['weather'][0]['description']}"
        sunrise = datetime.fromtimestamp(data_weather['sys']['sunrise']).strftime("%A, %B %d, %Y %H:%M:%S %p")
        sunset = datetime.fromtimestamp(data_weather['sys']['sunset']).strftime("%A, %B %d, %Y %H:%M:%S %p")
        date_time = now.strftime("%A, %B %d, %Y %H:%M:%S %p")
        print(f"output :")
        print(f"date time       : {date_time}")
        print(f"city            : {data_weather['name']}")
        print(f"temperature     : {data_weather['main']['temp']} Kelvin")
        print(f"weather         : {temperature}")
        print(f"sunrise         : {sunrise}")
        print(f"sunset          : {sunset}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())