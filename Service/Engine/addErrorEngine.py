import DB.engineRepository as en
import DB.outputEngineRepository as oen

def setErrorFlag(eid, exp):
    if eid == '':
        return -2
    result = en.EngineRepository('updateErrorFlag', [1, exp, eid])  #result는 성공한 행의 개수를 return
    return result

def getErrorEngineList():
    # ENGINE DB 데이터 가져오기
    enData = en.EngineRepository('getErrorEngines', True)
    if enData == -1:
        return -1
    # OUTPUTENGINE DB 데이터 가져오기
    oenData = oen.OutputEngineRepository('getErrorEngines', True)
    if oenData == -1:
        return -1
    # 바코드, mip, 타입, 입고일, 포장일, 비고란 : 6
    engineList = []
    for i in enData:
        barcode, mip, types, inputDate, packingDate, exp = i
        engineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate),"-" ,"-", exp])
    # 바코드, mip, 타입, 입고일, 포장일, 출고일, 목적지, 비고란 : 8
    for i in oenData:
        barcode, mip, types, inputDate, packingDate, outputDate, destination, exp = i
        if destination=='':
            destination = '-'
        engineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), stringToDate(outputDate),destination ,exp])

    #최근입고순정렬 > 타입별정렬 > mip별 정렬
    engineList = sorted(engineList, key=lambda x: (x[3], x[2], x[1]))
    return engineList

def stringToDate(s):
    s = str(s)
    return s[0:4]+"-"+s[4:6]+"-"+s[6:8]
