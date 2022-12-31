import DB.mipRepository as dao

# data[0]: mip
# data[1]: type
def inputMIP(data):
    if data[0] == "" or data[0] is None:
        return -3
    if data[1] == "" or data[1] is None:
        return -3
    if len(data[0]) != 4:
        return -3

    dbResult = dao.MIPRepository('insert', data)
    return dbResult
