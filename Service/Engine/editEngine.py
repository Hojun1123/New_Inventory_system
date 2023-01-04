import DB.engineRepository as en
def editEngineData(eid):
   result = en.EngineRepository('selectById', eid)
   if result == -1:
      return -1
   return result

def editProcess(data):
   #바코드, MIP, 타입, 입고일, 포장일, 위치, 불량, 비고
   if data[1] == '' or data[2] == '' or len(data[3]) != 8 or len(data[4]) != 8:
      return -2
   if data[6] == '':
      data[6] = 0
   result = en.EngineRepository('u', [data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[0]])
   if result == -1:  #DB 업데이트 오류
      result = editEngineData(data[0])
      if result == -1:
         return -1
      else:
         return result
   result = editEngineData(data[0])
   if result == -1:  #DB select 오류
      return -3
   return result