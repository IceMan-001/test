"""Устанавливаем библиотеку для парсинга bs4"""
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def get_html(url: str) -> str:
    user_agent = UserAgent()
    headers = {}
    return html


URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
