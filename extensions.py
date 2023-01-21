from parserExample import keys

class ExchangeException(Exception):
    pass

class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(
                f'Нельзя перевести одинаковые валюты {base}.')
        try:
            quote_ex = keys[quote]
            print(quote_ex)
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')

        try:
            base_ex = keys[base]
            print(base_ex)
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')

        try:
            amount_ex = float(amount)
            print(amount_ex)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')
        total_base = str(round((float(quote_ex)/float(base_ex)*amount_ex),2))
        return total_base