from binance.client import Client

try : 
    from config_dev import API_BINANCE_KEY , API_BINANCE_SECRET
except Exception:
    from config_prod import API_BINANCE_KEY , API_BINANCE_SECRET

client = Client( API_BINANCE_KEY , API_BINANCE_SECRET )

def BUY(symbol,position_size):
    pass

def SELL(symbol,position_size=0,sell_all=True):
    pass

def ReceiveSignals(signal_data_dict):

    """
    Example Data
    signal_data_dict
    {
        "message" : "CLOSE LONG",  ----> CLOSE or OPEN / LONG or SHORT
        "symbol" : "BTCUSDT"
    }
    """

    Signal_Type = signal_data_dict["message"].split(" ")[0]
    Signal_Side = signal_data_dict["message"].split(" ")[1]
    Signal_Symbol = signal_data_dict["symbol"]

    msg = ""

    if Signal_Type == "OPEN":
        if Signal_Side == "LONG":
            # function make order --> (Open,Long,symbol)
            print("open order long")
        
        elif Signal_Side == "SHORT":
            # function make order --> (Open,Short,symbol)
            print("open order short")
    
    elif Signal_Type == "CLOSE":
        if Signal_Side == "LONG":
            # function make order --> (close,Long,symbol)
            print("close order long")
        
        elif Signal_Side == "SHORT":
            # function make order --> (close,Short,symbol)
            print("close order short")
    
    return msg