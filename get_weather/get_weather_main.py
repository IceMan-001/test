"""Устанавливаем библиотеку для парсинга bs4"""
import json

import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_html(url: str) -> str:
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = requests.get(URL, headers=headers)
    print(f"код ответа {response.status_code}")
    return response.text


def get_weather(html: str):
    soup = bs(html, 'html.parser')
    date = soup.find('div', class_='dates short-d').text.split(', ')
    day_of_week = date[0]
    day_of_month = date[1]
    table = soup.find('div', class_='weather-today')
    rows = table.find_all('tr')
    weather_today = {'day_of_week': day_of_week,
                     'day_of_month': day_of_month}
    for row in rows:
        weather_day = row.find('td', class_='weather-day')
        temperature = row.find('td', class_='weather-temperature').text
        atmosfera = row.find('td', class_='weather-temperature').find('div').get('title')
        weather_feeling = row.find('td', class_='weather-probability').text
        probability = row.find('td', class_='weather-probability').text
        wind = row.find('td', class_='weather-wind').find_all('span')[0].get('title')
        wind_ms = row.find('td', class_='weather-wind').find_all('span', class_='tooltip')[1].text
        wind_kch = row.find('td', class_='weather-wind').find_all('span', class_='tooltip')[1].get('title')
        humidity = row.find('td', class_='weather-humidity').text
        weather_today[weather_day] = {
            'temperature': temperature,
            'atmosfera': atmosfera,
            'weather_feeling': weather_feeling,
            'probability': probability,
            'wind': {
                'wind_ms': wind_ms,
                'wind_kch': wind_kch

            },
        }
        return weather_today


URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
html = get_html(URL)
get_weather(html)
weather_json = json.dumps(weather_info)
