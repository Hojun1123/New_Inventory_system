import DB.mipRepository as dao

def getAllMIP():
    dbResult = dao.MIPRepository('getMIP')
    return dbResult