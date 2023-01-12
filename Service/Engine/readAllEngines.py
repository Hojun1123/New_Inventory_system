import DB.engineRepository as en
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
        result.append([barcode, mip, typ, input_date, output_date, location, error, exp])
    return result
