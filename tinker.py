from db import *
from coinone.chart import get_ticker
from bithumb.price import insertPrice2DB as bithumb_price;

if __name__ == "__main__":
    bithumb_price([1, 'btc']);
    # list_exchange = getExchangeList(); # 거래소 리스트
    # list_coin= getCoinList(); # 코인 리스트
    #
    # for e in list_exchange:
    #     for c in list_coin:
    #         try :
    #             # if (e[1] == 'coinone') : # 코인원
    #             #     res = get_ticker(c[1]);
    #             #     print(res);
    #             if (e[1] == 'bithumb') : # 빗썸
    #                 bithumb_price();
    #             # insertRecentPrice(c[0], e[0], res['last'], res['volume']);
    #         except :
    #             pass;







