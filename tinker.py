from db import *
from coinone.chart import get_ticker

if __name__ == "__main__":
    list_exchange = getExchangeList(); # 거래소 리스트
    list_coin= getCoinList(); # 코인 리스트

    for e in list_exchange:
        for c in list_coin:
            try :
                if (e[1] == 'coinone') : # 코인원
                    res = get_ticker(c[1]);
                    insertRecentPrice(c[0], e[0], res['last'], res['volume']);
            except :
                pass;







