from coinone.account import Account
from coinone.chart import get_ticker
from db import *

def trade(bot_info, signal) :
    coin_name = bot_info[2].lower();

    if (bot_info[1] == 1) :
        # 코인원 시작
        insure = Account(bot_info[3], bot_info[4]);
        orders = insure.orders(coin_name)
        if (len(orders) > 0): # order init
            for i, order in enumerate(orders):
                insure.cancel(currency=coin_name, **orders[i])

        balance = insure.balance();
        have_won = int(balance['krw']['avail']);
        if ((int(signal[0]) == 1) and (have_won > 10000)) : sell_coinone(insure, coin_name);
        if ((int(signal[0]) == 0) and (have_won < 10000)) : sell_coinone(insure, coin_name);
        # 코인원 끝~

def buy_coinone(insure, coin_name) :
    coin_tinker = get_ticker(coin_name);
    target_price = int(coin_tinker['last']);
    balance = insure.balance();
    krw = int(balance['krw']['avail']);
    target_qty = int(krw/target_price*10000)/10000

    return insure.buy(price=target_price, qty=target_qty, currency=coin_name)

def sell_coinone(insure, coin_name) :
    coin_tinker = get_ticker(coin_name);
    target_price = int(coin_tinker['last']);
    balance = insure.balance();
    coin_qty = (int(float(balance[coin_name]['avail'])*10000))/10000;

    return insure.sell(price=target_price, qty=coin_qty)

if __name__ == "__main__":
    bot_list = selectBotListFromUserId(1);
    for bot_info in bot_list :
        signal = selectLastSignal(bot_info[0], bot_info[1]) # 시그널 체크
        trade(bot_info, signal);
