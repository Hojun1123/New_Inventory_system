import DB.outputEngineRepository as oen

def deleteOutputProcess(eid):
    return oen.OutputEngineRepository('d', eid)
