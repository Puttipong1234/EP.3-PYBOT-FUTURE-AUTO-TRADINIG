import os
API_BINANCE_KEY = os.getenv("API_BINANCE_KEY")
API_BINANCE_SECRET = os.getenv("API_BINANCE_SECRET")

API_LINE_KEY = os.getenv("API_LINE_KEY")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

LINE_BOT_ACCESS_TOKEN = os.getenv("LINE_BOT_ACCESS_TOKEN")
LINE_BOT_CHANNEL_SECRET = os.getenv("LINE_BOT_CHANNEL_SECRET")


from firebase import Firebase

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "pybot-bottrade.firebaseapp.com",
    "projectId": "pybot-bottrade",
    "storageBucket": "pybot-bottrade.appspot.com",
    "messagingSenderId": "966280251835",
    "appId": "1:966280251835:web:a9ceef709f806fee8cdc9e",
    "measurementId": "G-KN2EG9DBH4",
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
    "serviceAccount": "pybot-bottrade-firebase-adminsdk-9em5u-3f01ebd736.json" # นำไฟล์ของท่านมาใส่เองด้วย
  }

firebaseCleint = Firebase(firebaseConfig)
auth = firebaseCleint.auth()

#ทดสอบ
if __name__ == '__main__':
  db = firebaseCleint.database()
  data = {
    "name":"TEST"
  }
  user = auth.refresh(user['refreshToken'])
  results = db.child("users").push(data, user['idToken'])