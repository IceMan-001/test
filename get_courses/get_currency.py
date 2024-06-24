import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class Parser:
    def __init__(self):
        self.html = None
        self.soup = None
        self.data = None

    def get_html(self, url: str):
        user_agent = UserAgent()
        headers = {"User-Agent": user_agent.random}
        response = requests.get(url, headers=headers)
        self.html = response.text

    def get_data(self):
        self.soup = bs(self.html, 'html.parser')
        table = self.soup.find('table', class_="js_sortable")
        rows = table.find_all('tr')
        courser_info = {}
        for row in rows[2:]:
            if 'id' in row.attrs:
                continue
            else:
                number_code = row.find('td', class_='t-center').text.split()[0]
                literal_code = row.find('td', class_="t-center").text.split()[1]
                name = row.find('td', class_='t-left').text.split('\n')[0]
                course = row.find('td', class_='t-right').text.strip('\n')

                courser_info[literal_code] = {
                    "number_code": number_code,
                    "name": name,
                    "course": course
                }

        self.data = courser_info

    def print_data(self):
        for item in self.data.items():
            print(item)

    def get_from_file(self):
        with open('text.txt', 'w') as file:
            for key, value in self.data.items():
                file.write(f'{key}, {value}\n')



url = "https://www.alta.ru/currency/2024-06-21/"
courser_parser = Parser()
courser_parser.get_html(url)
courser_parser.get_data()

courser_parser.print_data()
courser_parser.get_from_file()
