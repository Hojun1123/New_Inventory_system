import DB.outputEngineRepository as oen
def editOutputEngineData(eid):
   result = oen.OutputEngineRepository('selectById', eid)
   if result == -1:
      return -1
   return result

def editOutputEngineProcess(data):
   #바코드, MIP, 타입, 입고일, 포장일, 출고일, 불량, 비고, 출고지
   if data[1] == '' or data[2] == '' or len(data[3]) != 8 or len(data[4]) != 8 or len(data[5]) != 8:
      return -2
   if data[6] == '':
      data[6] = 0
   result = oen.OutputEngineRepository('u', [data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[0]])
   return result

