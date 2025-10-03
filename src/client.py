from src.constants import Currency

import asyncio
import requests


class Client:
    def __init__(self) -> None:
        self.client = requests

    def get(self, url, params):
        result = self.client.get(url=url, params=params)
        return result


class Case:
    def __init__(self, name, price, item_id):
        self.name = name
        self.price = price
        self.item_id = item_id

    def get_price(self):
        url = f'https://steamcommunity.com/market/itemordershistogram?country=UA&language=english&currency={Currency.UAH.value}&item_nameid={self.item_id}'
        result = requests.get(url=url)
        result = result.json()
        price = result.get('buy_order_graph')
        self.price = price[0][0]
        return price[0][0]

    def get_data(self):
        return [self.name, self.price]
