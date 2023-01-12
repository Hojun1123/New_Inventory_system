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
        tm = datetime.now()
        fname = './입고' + str(tm.strftime("%Y%m%d%S"))+'_'+str(tm.strftime("%H%M%S")) + '.xlsx'
        result = pd.DataFrame(data=result, columns=["바코드", "MIP", "TYPE", "입고일", "포장일", "Location", "GroupId", "불량", "비고란"])
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
        tm = datetime.now()
        fname = './불출' + str(tm.strftime("%Y%m%d"))+'_'+str(tm.strftime("%H%M%S")) + '.xlsx'
        result = pd.DataFrame(data=result, columns=["바코드", "MIP", "TYPE", "입고일", "포장일", "출고일", "불량", "비고란", "목적지"])
        result.to_excel(excel_writer=fname, sheet_name='출고된 엔진', index=False)
    except Exception as e:
        print(e)
        return -2
    return fname
