from db import *
# 카카오톡용
import yagmail

def sendMsg(msg) : # 메일로 알림 보내기
    try:
        return yagmail.SMTP('javamon1174', 'powqngkmwvygtlse').send('javamon1174@gmail.com', msg)
    except :
        return False;

def getDoubleMV(coin, ex, short, long) : # 이평선 알고리즘
    rows = getRecentPriceData(coin, ex, long);

    list_short = list();
    list_long = list();
    for v in rows[:(short)]:
        list_short.append(int(v[0]));

    for v in rows:
        list_long.append(int(v[0]));

    ma_short = int(sum(list_short) / short);
    ma_long = int(sum(list_long) / long);

    # 숏이 롱 보다 클때 매수포지션(매도 대기) / 롱이 숏보다 클때 매도 포지션(매수 대기)
    return int(ma_short > ma_long), ma_short, ma_long;

if __name__ == "__main__":
    list_exchange = getExchangeList(); # 거래소 리스트
    list_coin= getCoinList(); # 코인 리스트

    for e in list_exchange:
        for c in list_coin:
            try :
                if (e[1] == 'coinone') : # 코인원 # true = 1 / false = 0
                    result = getDoubleMV(c[0], e[0], 19, 27); # 상승장일땐 15:50 하락장일때는 19:27
                    last = selectLastSignal(c[0], e[0]);
                    insertSignal(e[0], c[0], 'mv', int(result[0]));

                    # 트레이딩 모듈로 이동
                    if ((int(last[0]) != int(result[0])) == True) : # 지난 시그널과 현재 시그널 비교 후 알림 전송
                        if (result[0]) :
                            sendMsg('[트레몬 알림] %s - %s : 매수 포지션(매도 대기)'% (e[1], c[1]));
                            # 매수 로직
                        else :
                            sendMsg('[트레몬 알림] %s - %s : 매도 포지션(매수 대기)'% (e[1], c[1]));
                            # 매도 로직
            except :
                pass;
