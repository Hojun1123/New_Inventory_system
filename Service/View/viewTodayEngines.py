import DB.engineRepository as en
import DB.outputEngineRepository as oen
from datetime import datetime

def getTodayEngines():
    dt = datetime.now()
    today = dt.strftime("%Y%m%d")
    print(today)

    inputEngines = en.EngineRepository('st', today)
    if inputEngines == -1:
        inputEngines = [["[DB ERROR] 데이터 베이스 에러"]]

    outputEngines = oen.OutputEngineRepository('st', today)
    if outputEngines == -1:
        outputEngines = [["[DB ERROR] 데이터 베이스 에러"]]

    return inputEngines, outputEngines
