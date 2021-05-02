import os
API_BINANCE_KEY = os.getenv("API_BINANCE_KEY")
API_BINANCE_SECRET = os.getenv("API_BINANCE_SECRET")

API_LINE_KEY = os.getenv("API_LINE_KEY")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")


from firebase import Firebase

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "pybot-bottrade.firebaseapp.com",
    "projectId": "pybot-bottrade",
    "storageBucket": "pybot-bottrade.appspot.com",
    "messagingSenderId": "966280251835",
    "appId": "1:966280251835:web:a9ceef709f806fee8cdc9e",
    "measurementId": "G-KN2EG9DBH4",
    "databaseURL": os.getenv("FirebaseDatabaseURL")
  }

firebaseCleint = Firebase(firebaseConfig)
auth = firebaseCleint.auth()
user = auth.sign_in_with_email_and_password(os.getenv("FIREBASE_EMAIL_AUTH"), os.getenv("FIREBASE_PASSWORD"))

#ทดสอบ
if __name__ == '__main__':
  db = firebaseCleint.database()
  data = {
    "name":"TEST"
  }
  user = auth.refresh(user['refreshToken'])
  results = db.child("users").push(data, user['idToken'])