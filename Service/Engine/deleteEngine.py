import DB.engineRepository as en

def deleteProcess(eid):
    return en.EngineRepository('d', eid)
