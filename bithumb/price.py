import requests
import simplejson as json
import urllib3 as url
from db import *

def init() :
    url.disable_warnings()

def insertPrice2DB(coin_info) :
    init();

    r = requests.get('https://api.bithumb.com/public/ticker/' + coin_info[1], verify=False);
    data = json.loads(r.text)['data'];
    insertDayPrice(coin_info[0], 1, data);

