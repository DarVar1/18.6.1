from parserExample import keys

class APIException(Exception):
    pass

class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(
                f'Нельзя перевести одинаковые валюты {base}.')
        try:
            quote_ex = keys[quote]
        except KeyError:
            raise APIException(f'Не смог обработать валюту {quote}')

        try:
            base_ex = keys[base]
        except KeyError:
            raise APIException(f'Не смог обработать валюту {base}')

        try:
            amount_ex = float(amount)
        except ValueError:
            raise APIException(f'Не смог обработать количество {amount}')
        total_base = str(round((float(quote_ex)/float(base_ex)*amount_ex),2))
        return total_base