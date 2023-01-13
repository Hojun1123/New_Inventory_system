import DB.engineRepository as en
import DB.outputEngineRepository as oen
import time
from datetime import datetime
from collections import defaultdict
import winsound

#### data 받아서 출고. ### 기능
### 요구사항
# 1. engine에서 삭제
# 2. outputengine에 추가
# 3. 유효성 검사
#   공백인지, 존재하지않는 엔진을 삭제하려하는지, 불량엔진을 삭제하려하는지 !!!!!
#


# 미리 해당 페이지 방문시, 세션에 엔진데이터를 로드 해둠.
def getValidEngines():
    result = en.EngineRepository('checkBarcode', True)
    if result == -1:
        return -1
    d = defaultdict(list)
    for r in result:
        d[r[0]] = r[1:]
    return d


def outputEngine(data, validEngines):
    #존재하지않는엔진
    if data not in validEngines.keys():
        return -2
    #불량엔진, errorflag와 비교
    if validEngines[data][4] > 0:
        return -3
    result = en.EngineRepository('d', data)     #ENGINE테이블에서 삭제
    if result == -1:
        return -1
    #mip, type, input_date, packing_date, errorflag
    a, b, c, d, e, f = validEngines[data]
    tm = datetime.now()
    output_date = tm.strftime("%Y%m%d")
    insertData = [data, a, b, c, d, output_date, e, f, '']
    return oen.OutputEngineRepository('i', insertData)

def playbeep(result):
    if result >= 0:     #정상
        winsound.Beep(frequency=2500, duration=350)  # milliseconds)
    else:               #불출금지, DB에러, 없는엔진불출시도
        winsound.Beep(frequency=4000, duration=2000)



