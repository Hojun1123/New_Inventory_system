import DB.engineRepository as en
import DB.outputEngineRepository as oen
def selectAllEngines():
    temp = en.EngineRepository('s', True)
    if temp == -1:
        return -1

    result = []
    #바코드, mip, 타입, 입고일, 포장일, 그룹아이디, 위치, 불량, 비고
    for barcode, mip, typ, input_date, output_date, gid, location, error, exp in temp:
        if error == 0:
            error = ''
        else:
            error = "불량"
        result.append([barcode, mip, typ, stringToDate(input_date), stringToDate(output_date), location, error, exp])
    return result


def selectAllOutputEngines():
    temp = oen.OutputEngineRepository('s', True)
    if temp == -1:
        return -1
    result = []
    #바코드, mip, 타입, 입고일, 포장일, 출고일, 불량, 비고, 출고지
    for barcode, mip, typ, inputDate, packingDate, outputDate, error, exp, destination in temp:
        if error == 0:
            error = ''
        else:
            error = "불량"
        result.append([barcode, mip, typ, stringToDate(inputDate), stringToDate(packingDate), stringToDate(outputDate), destination, error, exp])
    return result

def stringToDate(s):
    s = str(s)
    return s[0:4]+"-"+s[4:6]+"-"+s[6:8]