#Актуальные значения ValCurs с Foreign Currency Market
from urllib.request import urlopen
from xml.etree import ElementTree as etree

def getValueEUR():
    with urlopen('http://www.cbr.ru/scripts/XML_daily.asp/Valute', timeout=10) as r:
        value = (etree.parse(r).findtext('.//Valute'+'[@ID="R01239"]'+'/Value'))
        value= value.replace(',', '.')
        return value
    
def getValueUSD():
    with urlopen('http://www.cbr.ru/scripts/XML_daily.asp/Valute', timeout=10) as r:
        value = (etree.parse(r).findtext('.//Valute'+'[@ID="R01235"]'+'/Value'))
        value= value.replace(',', '.')
        return value
    
eur = getValueEUR()
usd = getValueUSD()
keys = {
    "eur": "",
    "usd": "",
    "rub": "1",
}
keys["eur"] = eur
keys["usd"] = usd





