import pandas as pd
import DB.engineRepository as en
import DB.outputEngineRepository as oen
from datetime import datetime
import openpyxl
def engineDBToExcel():
    result = en.EngineRepository('s', True)
    if result == -1:    #db error
        return -1
    try:
        #tm = datetime.now()
        #fname = './ibgo' + str(tm.strftime("%Y%m%d%S"))+'_'+str(tm.strftime("%H%M%S")) + '.xlsx'
        fname = './ibgo.xlsx'
        result = pd.DataFrame(data=result, columns=["바코드", "MIP", "기종", "입고일", "포장일", "위치", "그룹", "상태", "비고"])
        result.to_excel(excel_writer=fname, sheet_name='입고된 엔진', index=False)
    except Exception as e:
        print(e)
        return -2
    return fname

def OutputEngineDBToExcel():
    result = oen.OutputEngineRepository('s', True)
    if result == -1:  # db error
        return -1
    try:
        #tm = datetime.now()
        #fname = './chulgo' + str(tm.strftime("%Y%m%d"))+'_'+str(tm.strftime("%H%M%S")) + '.xlsx'
        fname = './chulgo.xlsx'
        result = pd.DataFrame(data=result, columns=["바코드", "MIP", "기종", "입고일", "포장일", "출고일", "상태", "비고", "출고지"])
        result.to_excel(excel_writer=fname, sheet_name='출고된 엔진', index=False)
    except Exception as e:
        print(e)
        return -2
    return fname
