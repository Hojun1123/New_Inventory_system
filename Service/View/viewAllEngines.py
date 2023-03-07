import DB.engineRepository as en
import DB.outputEngineRepository as oen
from collections import defaultdict
def getAllEngines(start, end):
    # 올바르지않은 날짜 형식
    if len(start) != 10 or len(end) != 10:
        return -2
    start = str(start[0:4] + start[5:7] + start[8:10])
    end = str(end[0:4] + end[5:7] + end[8:10])
    # 시작일이 종료일 보다 큰 경우
    if int(start) > int(end):
        return -2

    # ENGINE DB 데이터 가져오기
    enData = en.EngineRepository('sd', end)
    if enData == -1:
        return -1
    # OUTPUTENGINE DB 데이터 가져오기
    oenData = oen.OutputEngineRepository('sd', (start, end))
    if oenData == -1:
        return -1

    engineList = []
    #key(최근입고순으로정렬을위한 키), 바코드, mip, type, 입고일, 포장일, 출고일, 같은그룹, 위치, 에러엔진, 비고
    for i in enData:
        barcode, mip, types, inputDate, packingDate, gid, location, errorFlag, exp = i
        errorFlag = "불량엔진" if errorFlag > 0 else ""
        engineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), "", "", errorFlag, exp])
    for i in oenData:
        barcode, mip, types, inputDate, packingDate, outputDate, errorFlag, exp, destination = i
        errorFlag = "불량엔진" if errorFlag > 0 else ""
        engineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), stringToDate(outputDate), destination, errorFlag, exp])

    #최근입고순정렬 > 타입별정렬 > mip별 정렬
    engineList = sorted(engineList, key=lambda x: (x[3], x[2], x[1]))
    return engineList


def getAllUnitsEngines(start, end):
    # 올바르지않은 날짜 형식
    if len(start) != 10 or len(end) != 10:
        return -2
    start = str(start[0:4] + start[5:7] + start[8:10])
    end = str(end[0:4] + end[5:7] + end[8:10])
    # 시작일이 종료일 보다 큰 경우
    if int(start) > int(end):
        return -2

    # ENGINE DB 데이터 가져오기
    enData = en.EngineRepository('sd', end)
    if enData == -1:
        return -1

#    # OUTPUTENGINE DB 데이터 가져오기
#    oenData = oen.OutputEngineRepository('sd', (start, end))
#    if oenData == -1:
#        return -1


    #key(최근입고순으로정렬을위한 키), 바코드, mip, type, 입고일, 포장일, 출고일, 같은그룹, 위치, 에러엔진, 비고
    engineList = defaultdict(list)
    for i in enData:
        barcode, mip, types, inputDate, packingDate, gid, location, errorFlag, exp = i
        engineList[gid].append([barcode[6:12], mip, types, inputDate, packingDate, errorFlag, exp])

    result = defaultdict(list)
    for k, v in engineList.items():
        mip = ''
        types = ''
        inputDate = ''
        packingDate = ''
        location = ''
        errorFlag = 0
        exp = ''
        result[k] = [types, mip, '', '', '', '', inputDate, packingDate, location, errorFlag, exp]
        cnt = 0
        for engine in v:
            b, mip, types, inputDate, packingDate, errorFlag, exp = engine
            if result[k][0] != types and result[k][0] != '':
                result[k][0] = 'TypeError'
            if result[k][1] != mip and result[k][1] != '':
                result[k][1] = 'MipError'
            if (result[k][6] != inputDate and result[k][6] != '') or (result[k][7] != inputDate and result[k][7] != ''):
                result[k][6] = 'DateError'
            result[k][0] = types
            result[k][1] = mip
            result[k][2+cnt] = b
            result[k][6] = stringToDate(inputDate)
            result[k][7] = stringToDate(packingDate)
            result[k][9] += errorFlag
            result[k][10] += (exp+' ')
            cnt = cnt + 1

    return result.values()

#    for i in oenData:
#        barcode, mip, types, inputDate, packingDate, outputDate, errorFlag, exp, destination = i
#        errorFlag = "불량엔진" if errorFlag > 0 else ""
#        engineList.append([barcode, mip, types, stringToDate(inputDate), stringToDate(packingDate), stringToDate(outputDate), destination, errorFlag, exp])

def stringToDate(s):
    s = str(s)
    return s[0:4]+"-"+s[4:6]+"-"+s[6:8]


