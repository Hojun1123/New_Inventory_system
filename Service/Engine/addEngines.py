import DB.engineRepository as dao
import DB.mipRepository as dao2
import time
from datetime import datetime
from collections import defaultdict

def inputEngine(data):
    if data == "" or len(data) < 1:
        return -3
    d = data.replace("\r", "")
    d = d.split("\n")
    result = []
    temp = []
    for i in d:
        #중복인식처리
        if i in temp:
            continue
        if i == "G4FDEH408157G20Y":
            if len(temp) > 0:
                result.append(temp)
                temp = []
        else:
            temp.append(i)

    if len(result) < 1:
        return -3

    #data를 insert
    print(result)

    # barcode / mip / type / input_date / packing_date / group_id / location / errorflag / exp
    insertData = []

    types = defaultdict(str)
    types2 = dao2.MIPRepository('getMIP')
    if types2 == -1:
        #mip테이블 에러
        return -1
    for k, v in types2:
        types[k] = v

    tm = datetime.now()
    input_date = tm.strftime("%Y%m%d")    #20221226 #==packing_date
    for bs in result:
        #현재
        group_id = str(time.time())
        time.sleep(0.001)
        for b in bs:
            mip = b[12:]
            type = types[mip]
            insertData.append((b, mip, type, input_date, input_date, group_id, '', 0, ''))

    print("DB INSERT >> ")
    print(insertData)
    dbResult = dao.EngineRepository('i', insertData)
    return dbResult





