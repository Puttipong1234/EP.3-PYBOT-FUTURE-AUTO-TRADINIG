from BinanceTrade.FutureTrade import *

if __name__ == "__main__":
    # res = get_market_data_by_symbol(symbol = "BTCUSDT")
    # print(res["markPrice"])

    # change_leverage(symbol="BTCUSDT", lev=5)

    # balance = getAssetUSDT()
    # print(balance)

    PlaceOrderAtMarket(
        position='LONG',
        symbol='BTCUSDT',
        amount=0.002
    )

    # res = getPositionbySymbol(Symbol="BTCUSDT")
    # print(res['positionAmt'])

    # ClosePositionAtMarket(symbol="BTCUSDT", positionSide="SHORT")
