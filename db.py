import sys;
import pymysql
from pytz import timezone
import datetime
import numpy as np;

now = datetime.datetime.now(timezone('Asia/Seoul'));
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S');

def getDbConnector() :
    conn = pymysql.connect( # MySQL Connection 연결
        host='104.199.204.41',
        user='javamon',
        password='1111',
        db='trade_bot',
        charset='utf8',
        autocommit=True
    );
    curs = conn.cursor(); # Connection 으로부터 Cursor 생성

    return {'conn': conn, 'curs': curs};

# 유저번호 조회
def getUserId() :
    res = getDbConnector();
    # SQL문 실행
    sql = "select * from tb_user"
    res['curs'].execute(sql)

    # 데이타 Fetch
    rows = res['curs'].fetchall()

    res['conn'].close();
    return rows[0];

# 회원 봇 리스트 조회
def getUserBotList() :
    return 0;
# 가격정보 저장
def insertRecentPrice(coin=1, exchange=1, price=0, volume=0) :
    res = getDbConnector();

    sql = 'INSERT INTO tb_tinker (coin_idx, exchange_idx, price, volume, timestemp) VALUES (%s, %s, %s, %s, %s)'

    result = res['curs'].execute(sql, (coin, exchange, price, volume, nowDatetime));

    res['conn'].close();

    return result;

def insertDayPrice(coin=1, exchange=1, data=[]) :
    res = getDbConnector();

    sql = 'INSERT INTO tb_tinker (coin_idx, exchange_idx, opening_price, closing_price, min_price, max_price, volume) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s)'

    result = res['curs'].execute(sql, (coin,
                                       exchange,
                                       data['opening_price'],
                                       data['closing_price'],
                                       data['min_price'],
                                       data['max_price'],
                                       data['volume_1day'],
                                       ));

    res['conn'].close();

    return result;


#거래소 목록 조회
def getExchangeList():
    res = getDbConnector();
    sql = "select * from tb_exchange";

    res['curs'].execute(sql);
    rows = res['curs'].fetchall();

    res['conn'].close();

    return rows;

#코인 목록 조회
def getCoinList():
    res = getDbConnector();
    sql = "select * from tb_coin";

    res['curs'].execute(sql);
    rows = res['curs'].fetchall();

    res['conn'].close();

    return rows;

# 최근 가격 목록 조회
def getRecentPriceData(coin= 1, exchange= 1, long=15) :
    res = getDbConnector();
    result = list();

    sql = "SELECT price FROM tb_tinker WHERE coin_idx=%s AND exchange_idx=%s ORDER BY idx DESC LIMIT %s"
    res['curs'].execute(sql, (coin, exchange, long));

    rows = res['curs'].fetchall();

    res['conn'].close();

    return rows;

# 최근 시그널 조회

# 현재 시그널 저장
def insertSignal(coin = 1, exchange = 1, type = 'mv', position = 0) :
    # 0 => 판매 / 1 => 구매
    res = getDbConnector();
    sql = 'INSERT INTO `tb_signal` (`coin_idx`, `exchange_idx`, `type`, `position`, `timestamp`) VALUES(%s, %s, %s, %s, %s)';
    result = res['curs'].execute(sql, (coin, exchange, type, position, nowDatetime));
    res['conn'].close();

    return result;

def selectLastSignal(coin = 1, exchange = 1, type = 'mv') :
    res = getDbConnector();

    sql = "SELECT position FROM tb_signal WHERE coin_idx=%s AND exchange_idx=%s AND type=%s order by idx DESC LIMIT 1;";
    res['curs'].execute(sql, (coin, exchange, type));

    rows = res['curs'].fetchone();

    res['conn'].close();

    return rows;

def selectBotListFromUserId(user_id = False) :
    res = getDbConnector();

    sql = "SELECT DISTINCT(b.coin_idx), b.exchange_idx, c.name, b.access_token, b.secret_key FROM tb_user_trade_bot b " \
          "LEFT OUTER JOIN tb_coin c ON b.coin_idx = c.idx WHERE b.user_idx = %s AND b.limit_date > Now() ORDER BY b.exchange_idx ASC;";

    # sql = "SELECT * FROM tb_user_trade_bot WHERE user_idx = %s and limit_date > Now() order by exchange_idx ASC;";
    res['curs'].execute(sql, (user_id));

    rows = res['curs'].fetchall();

    res['conn'].close();

    return rows;

# if __name__ == "__main__":
#     selectBotListFromUserId(1);

# SHELL=/bin/bash
# */2 * * * * source /home/javamon1174/project/tradebot/venv/bin/activate && python3 /home/javamon1174/project/tradebot/tinker.py > /dev/null