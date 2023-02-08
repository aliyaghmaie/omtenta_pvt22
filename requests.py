import requests

def get_nobel_prizes(cat: str):
    return requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=cat).json()

