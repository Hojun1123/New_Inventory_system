import DB.engineRepository as en

def setErrorFlag(eid, exp):
    if eid == '':
        return -2
    result = en.EngineRepository('updateErrorFlag', [1, exp, eid])  #result는 성공한 행의 개수를 return
    return result
