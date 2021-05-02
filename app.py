from flask import Flask , request
import json

from BinanceTrade.Trade import ReceiveSignals

app = Flask(__name__)

#@app.route("/START/REBALANCEBOT/SYMBOL")

#@app.route("/STOP/REBALANCEBOT/SYMBOL")

@app.route("/SIGNALS" , methods=['POST'])
def SIGNALS_RECEIVER():
    if request.method == "POST":
        msg = request.data.decode("utf-8")
        json_msg = json.loads(msg)
        print(json_msg) # <-- dictionary

        # get data firebase เพื่อดูว่า Autotrading = True??
        msg = ReceiveSignals(signal_data_dict = json_msg)

        # สร้างฟังก์ชั่น ในการจัดการข้อมูล

        # """
        # { "SYMBOL":"{{TICKER}}",
        # "TIME":{{timenow}},
        # "SIGNALS":"{{strategy.order.action}}",
        # "POSITION_SIZE":{{strategy.order.contracts}} }

        # example data

        # { "SYMBOL":"BTCUSD",
        # "TIME":TIMESTAMP,
        # "SIGNALS":"buy",
        # "POSITION_SIZE":0.34 }
        # """
    return "200"

#Rebalance Sections







if __name__== "__main__":
    app.run(debug=True,port=8080)