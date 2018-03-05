from db import *
from coinone.chart import get_ticker
from bithumb.price import insertPrice2DB as bithumb_price;

def StochTinker(coin = 1, exchange = 1, period= 10) :
    # 공식 slow(10 3 3) t=3
    # Slow %K = Fast %D의 t일 이동평균
    # Slow %D = Slow %K = Fast %D의 t일이동평균

    t_l_p = todayLastPrice();  # 오늘 종가
    p_l_p = periodMinPrice(coin, exchange, period);  # N일중 최저가
    p_m_p = periodMaxPrice(coin, exchange, period);  # N일중 최고가

    insertStochTinker(coin, exchange, period, t_l_p - p_l_p, p_m_p - p_l_p);

if __name__ == "__main__":
    bithumb_price([1, 'btc']);
    StochTinker(1, 1, 10);
    StochTinker(1, 1, 5);
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







