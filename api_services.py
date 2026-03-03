import aiohttp
import requests
from bs4 import BeautifulSoup


async def get_weather(city: str = "Москва") -> str:
    """Получение погоды через Яндекс Погоду"""
    url = f"https://api.weather.yandex.net/v2/forecast?city={city}&lang=ru_RU"
    headers = {"X-Yandex-API-Key": YANDEX_WEATHER_KEY}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                data = await resp.json()
                temp = data["fact"]["temp"]
                condition = data["fact"]["condition"]
                return f"Погода в {city}: {temp}°C, {condition}"
    except Exception:
        return "Не удалось получить погоду."

def get_currency() -> str:
    """Курсы валют от ЦБ РФ"""
    try:
        response = requests.get(CB_API_URL)
        data = response.json()
        usd = data["Valute"]["USD"]["Value"]
        eur = data["Valute"]["EUR"]["Value"]
        return f"Курсы валют (ЦБ РФ):\nUSD: {usd} ₽\nEUR: {eur} ₽"
    except Exception:
        return "Не удалось получить курсы валют."




