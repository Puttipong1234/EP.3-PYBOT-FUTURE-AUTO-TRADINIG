try:
    from config_dev import firebaseCleint

except:
    from config_prod import firebaseCleint

db = firebaseCleint.database()

def WriteInitialValue(symbols,initialvalue):
    

    # user_n = auth.refresh(user['refreshToken'])
    data = { "initialValue" : initialvalue }
    db.child(symbols).update(data)

def GetInitialValue(symbols):

    # res = db.get().val()[symbols]
    # lastest_data = list(res.keys())[-1]
    # res_data = res[lastest_data]
    # print(res_data)
    
    # Value เริ่มต้น
    try:
        res = db.get().val()[symbols]["initialValue"]
        return res
    
    except KeyError:
        WriteInitialValue(symbols=symbols,initialvalue=0)
        res = db.get().val()[symbols]["initialValue"]
        return res
    

def UpdateBotSetting(key,value):

    if key == "run":
        data = { "run" : value}
        db.child("BOTSETTINGS").update(data)
    
    elif key == "Positionsize":
        data = { "Positionsize" : value}
        db.child("BOTSETTINGS").update(data)

def GetDataBotsetting(key):
    res = db.get().val()["BOTSETTINGS"][key]
    return res