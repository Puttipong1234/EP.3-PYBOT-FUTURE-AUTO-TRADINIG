"""
Example
50000.234 => ...
271.02 => ...

0.222 => ...
0.000234 => ...
we need to know more than 1 or less than 1
"""
import math
def round_down(num,digits):
    factor = 10.0 ** digits
    return math.floor(num * factor) / factor

def calForPosition(price,tp,sl,side,amount_usdt):

    """
    side : LONG or SHORT
    PRICE => case 50000.234
            [50000,234]
    """
    tp_price = ""
    sl_price = ""
    cal_amount = ""

    count_digit = len(price.split(".")[1])
    
    
    cal_tp_price = 0
    cal_sl_price = 0
        
    if side == "LONG":
        cal_tp_price = float(price) * (1 + tp/100)
        cal_sl_price = float(price) * (1 - sl/100)

    elif side == "SHORT":
        cal_tp_price = float(price) * (1 - tp/100)
        cal_sl_price = float(price) * (1 + sl/100)

    # order format compare to price
    tp_price = str(round_down(cal_tp_price,count_digit))
    sl_price = str(round_down(cal_sl_price,count_digit))

    # size cal
    size = amount_usdt/float(price)
    if float(price) > 1000:
        size = round_down(size,3)
    elif 10 < float(price) < 1000:
        size = round_down(size,2)
    elif 1 <= float(price) <= 10:
        size = round_down(size,1)
    elif 0 < float(price) < 1:
        size = int(size)
        
    return tp_price , sl_price , size


# TESTING
prices = ["50213.234","271.23","12.45","5.442","0.13223","0.0000423"]

for price in prices:
    tp , sl , size = calForPosition(price,5,2,"LONG",100)
    print("="*25)
    print(tp)
    print(sl)
    print(size)
    print("="*25)
