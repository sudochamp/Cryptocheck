from urllib2 import Request, URLError, urlopen
import json


def btcapi_bitstamp():
    request = Request('https://www.bitstamp.net/api/ticker/')
    try:
        response = urlopen(request)
        price = response.read()
        currentPrice = json.loads(price)["last"]
        highestPrice = json.loads(price)["high"]
        lowestPrice = json.loads(price)["low"]
        return currentPrice, highestPrice, lowestPrice



    except URLError, e:
        print 'Not Found'


def etheruem_price():
    request = Request('https://coinmarketcap-nexuist.rhcloud.com/api/eth')
    try:
        response = urlopen(request)
        price = response.read()
        return json.loads(price)["price"]["usd"]
    except URLError, e:
        print 'Not Found'

