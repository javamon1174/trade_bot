# -*- coding: utf-8 -*-

# 거래용
from secret import ACCESS_TOKEN, SECRET_KEY
from coinone.account import Account
from pprint import pprint
from coinone.chart import *
import time

def updatePrice(c_price = 0) :
    price = get_ticker('eth');

    short = get_chart(60*15, 'eth', 'hour')[:-1].to_dict();
    long = get_chart(60*50, 'eth', 'day')[:-1].to_dict();

    short_val = int(sum(short['close'].values())/len(short['close'].values()));
    long_val = int(sum(long['close'].values())/len(long['close'].values()));

    now = time.localtime() # 현재시간 출력
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s);
    print("ma15 : %s" % short_val);
    print("ma50 : %s" % long_val);
    if (short_val > long_val) :
        print('거래봇 알림 : 매수 포지션(매도 대기)');
    #     sendMsg('거래봇 알림 : 매수 포지션(매도 대기)');
    else :
        print('거래봇 알림 : 매도 포지션(매수 대기)');
    #     sendMsg('거래봇 알림 : 매도 포지션(매수 대기)');

    time.sleep(30);

    # 15일 50일 이평선(미리 가격 넣어두기 - 차트보고)
    # echo -e "15,45 * * * * /root/every_30min.sh" | crontab
    #   15,45 * * * * python3 /home/javamon1174/project/tradebot/example_basic_usage.py
    # nohup python3 /home/javamon1174/project/tradebot/example_basic_usage.py

    if (c_price == 0) :
        updatePrice.prev_price = price['last'];
        return updatePrice(price['last']);
    else :
        updatePrice.prev_price = price['last'];
        return updatePrice(price['last']);

def getMV(coin = 'btc', day = 15) :
    import pandas as pd

    data = [
            521000,
            534000,
            539000,
            534000,
            548000,
            567000,
            554000,
            587000,
            564000,
            550000,
            504000,
            585800,
            704000,
            783300,
            786300,
            770000,
            786000,
            814000,
            915000,
            1025000,
            1086000,
            1130000,
            9090000,
            9820000,
            9600000,
            10340000,
            10410000,
            10470000,
            9690000,
            9830000,
            10080000,
            10240000,
            10540000,
            12950000,
            14400000,
            15720000,
            17840000,
            18980000,
            21380000,
            17950000,
            16640000,
            19000000,
            10500000,
            18990000,
            17880000,
            13080000,
            13740000,
            13370000,
            13880000,
            15160000,
            13790000,
    ];
    # 시간봉 기준 / 거래소별
    n = [
         1272000,
         1302000,
         1289000,
         1324500,
         1335000
    ];

    res = sum(n)/5;
    print(res);

if __name__ == "__main__":
    from datetime import datetime

    print('프로그램을 실행합니다.');
    # getMV('eth', 15);
    res = get_ticker('eth');
    print(res['last']);
    print(res['volume']);
    # my = Account(ACCESS_TOKEN, SECRET_KEY);
    # updatePrice();

    # query account informations
    # pprint(my.info()) # 기본 정보
    # pprint(my.balance())
    # pprint(my.daily_balance())
    # pprint(my.deposit_address()) #지갑 주소 조회

    #  complete orders
    # try:
    #     pprint(my.complete_orders('eth'))  # will raise error
    # except Exception as e:
    #     print(e.args)

    # make some insane orders, and cancel them
    # will throw error if you have not enough balance
    # my.buy(price=1000, qty=0.001)
    # my.sell(price=100000000, qty=0.001)
    # print('made 3 orders')
    # orders = my.orders()
    # pprint(orders)
    # my.cancel(**orders[-1])  # cancel the last one
    # print('canceled last one')
    # pprint(my.orders())
    # my.cancel()              # will cancel all orders by default
    # print('canceled remaining')
    # pprint(my.orders())
