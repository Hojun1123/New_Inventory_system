import DB.mipRepository as dao

def getAllMIP():
    dbResult = dao.MIPRepository('getMIP')
    if dbResult == -1:
        return -1
    return dbResult