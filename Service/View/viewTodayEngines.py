import DB.engineRepository as en
import DB.outputEngineRepository as oen
from datetime import datetime

def getTodayEngines():
    dt = datetime.now()
    today = dt.strftime("%Y%m%d")
    inputEngines = en.EngineRepository('st', today)
    inputEngineList = []
    if inputEngines == -1:
        inputEngineList.append["[DB ERROR] 데이터 베이스 에러"]
    prevgid = 0
    groupId = 1000
    for i in range(len(inputEngines)):
        barcode, mip, types, inputDate, packingDate, gid, location, errorFlag, exp = inputEngines[i]
        errorFlag = "불량엔진" if errorFlag > 0 else ""
        inputEngineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), groupId, location, errorFlag, exp])
        if prevgid != gid:
            groupId += 1
        prevgid = gid

    outputEngines = oen.OutputEngineRepository('st', today)
    outputEngineList = []
    if outputEngines == -1:
        outputEngineList.append(["[DB ERROR] 데이터 베이스 에러"])
    for i in outputEngines:
        barcode, mip, types, inputDate, packingDate, outputDate, errorFlag, exp, destination = i
        errorFlag = "불량엔진" if errorFlag > 0 else ""
        outputEngineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), stringToDate(outputDate), destination, errorFlag, exp])

    return inputEngineList, outputEngineList

def stringToDate(s):
    s = str(s)
    return s[0:4]+"-"+s[4:6]+"-"+s[6:8]
