import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"зачем переводить валюту в валюту?))) {base}")

        try:
            quote_to = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось выполнить конвертацию валюты {quote}")

        try:
            base_to = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")


        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_to}&tsyms={base_to}")
        total_base = json.loads(r.content)[keys[base]]*amount
        return total_base




