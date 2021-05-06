## Procedure Developement

* cmd > pythom -m venv venv
* venv\Scripts\activate | macos - source venv\bin\activate
* pip install -r requirements.txt
* สร้างไฟล์ config_dev.py ขึ้นมาเอง โดยการ Copy มาจาก 

* python app.py สามารถทำตามเนื้อหาได้เลย

## Procedure Production

* gh repo clone Puttipong1234/EP.3-PYBOT-FUTURE-AUTO-TRADINIG หรือ Download as Zip
* cmd ไปที่โฟลเดอร์ 
* อย่าลืม โหลดตัว Firebase Service account .json มาใส่เองด้วย (ตามวิดิโอ)
* ทำการ init git และ heroku Create ตามคลิบวิดิโอ
* add commit push ทำครั้งที่มีการแก้ไข Code เป็นการอัพเดตไปที่ heroku ของเราเลย

## References - 
* binance API : https://python-binance.readthedocs.io/en/latest/
* Firebase : https://pypi.org/project/firebase/