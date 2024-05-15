from queue import Queue
from urllib3 import connection
import threading


def generate_urls():
    BASE_URL = "https://jsonplaceholder.typicode.com/"
    ENDPOINT = "/comments"

    return [f"{BASE_URL}{ENDPOIN}/{number}" for number in range(1, 501)]


def get_url():
    print("url: start request")
    resp = urllib3.request("GET", url)
    print(resp.date)
    print("url: complete")

urls = generate_urls()
tasks = []


urls = generate_urls()

# for url in urls:
#     get_url(url)

q = Queue(10)
