import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")

    params = {
        "q": "Cherkasy",
        "key": API_KEY
    }

    url = "http://api.weatherapi.com/v1/current.json"

    response = requests.get(url, params=params)

    temp = response.json()["current"]["temp_c"]
    return temp

if __name__ == "__main__":
    get_weather()
