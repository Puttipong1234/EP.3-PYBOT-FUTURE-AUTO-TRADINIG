from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *


from config_dev import API_BINANCE_KEY , API_BINANCE_SECRET

request_client = RequestClient(api_key=API_BINANCE_KEY,secret_key=API_BINANCE_SECRET)


def get_market_data_by_symbol(symbol):
    result = request_client.get_mark_price(symbol=symbol)
    return result.__dict__


def change_leverage(symbol,lev):
    result = request_client.change_initial_leverage(symbol,lev)
    return result.__dict__

def CancelAllOrder(symbol):
    result = request_client.cancel_all_orders(symbol)
    return result.__dict__

def getAssetUSDT():
    result = request_client.get_balance()
    return int(result[1].balance)


def PlaceOrderAtMarket(position,symbol,amount,act_price_percent=2,cb=3,stoploss_Percent = 5):
    """
    position : Long or Short
    amount : จำนวนสินค้า ที่ต้องการซื้อ
    """

    CancelAllOrder(symbol = symbol)

    current_price = float(get_market_data_by_symbol(symbol)["markPrice"])

    if position == "LONG":
        act_price_LONG = current_price * (1 + act_price_percent/100)
        # buy order at market
        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.BUY ,
            positionSide = "BOTH" ,
            ordertype=OrderType.MARKET ,
            quantity = amount
        )
        
        # trailing stop loss
        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.SELL ,
            positionSide = "BOTH" ,
            ordertype = OrderType.TRAILING_STOP_MARKET,
            activationPrice=act_price_LONG,
            callbackRate= cb,
            reduceOnly = True ,
            quantity = amount
        )
        # Initial Stoploss

        stoplosePrice = current_price * (1 - stoploss_Percent/100)

        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.SELL ,
            positionSide = "BOTH" ,
            ordertype = OrderType.STOP_MARKET,
            stopPrice = stoplosePrice,
            reduceOnly=True,
            quantity = amount
        )
    
    elif position == "SHORT":
        act_price_SHORT = current_price * (1 - act_price_percent/100)
        # sell order at market
        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.SELL ,
            positionSide = "BOTH" ,
            ordertype=OrderType.MARKET ,
            quantity = amount
            )
        
        # trailing stop loss
        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.BUY ,
            positionSide = "BOTH" ,
            ordertype = OrderType.TRAILING_STOP_MARKET,
            activationPrice=act_price_LONG,
            callbackRate= cb,
            reduceOnly = True ,
            quantity = amount
        )
        # Initial Stoploss

        stoplosePrice = current_price * (1 + stoploss_Percent/100)

        result = request_client.post_order(
            symbol = symbol ,
            side = OrderSide.BUY ,
            positionSide = "BOTH" ,
            ordertype = OrderType.STOP_MARKET,
            stopPrice = stoplosePrice,
            reduceOnly=True,
            quantity = amount
        )

def getPositionbySymbol(Symbol):
    result = request_client.get_position_v2()
    for i in result:
        if i.symbol == Symbol:
            return i.__dict__

def ClosePositionAtMarket(symbol,positionSide):

    amount = getPositionbySymbol(symbol)['positionAmt']

    if positionSide == "LONG":
        result = request_client.post_order(
            symbol=symbol,
            side=OrderSide.SELL,
            ordertype=OrderType.MARKET,
            positionSide="BOTH",
            quantity=str(abs(float(amount)))
        )
    
    elif positionSide == "SHORT":
        result = request_client.post_order(
            symbol=symbol,
            side=OrderSide.BUY,
            ordertype=OrderType.MARKET,
            positionSide="BOTH",
            quantity=str(abs(float(amount)))
        )

