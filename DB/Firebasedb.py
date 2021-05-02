try:
    from config_dev import firebaseCleint

except:
    from config_prod import firebaseCleint

db = firebaseCleint.database()

def WriteInitialValue(symbols,initialvalue):
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
