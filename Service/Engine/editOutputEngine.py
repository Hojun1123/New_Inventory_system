import DB.outputEngineRepository as oen
def stringToDate(s):
   s = str(s)
   return s[0:4] + "-" + s[4:6] + "-" + s[6:8]
def editOutputEngineData(eid):
   result = oen.OutputEngineRepository('selectById', eid)
   if result == -1:
      return -1
   i = result[0]
   return [i[0], i[1], i[2], stringToDate(i[3]), stringToDate(i[4]), stringToDate(i[5]), i[6], i[7], i[8]]

def editOutputEngineProcess(data):
   #바코드, MIP, 타입, 입고일, 포장일, 출고일, 불량, 비고, 출고지
   if data[1] == '' or data[2] == '' or len(data[3]) != 10 or len(data[4]) != 10 or len(data[5]) != 10:
      return -2
   inputdate = data[3]
   packingdate = data[4]
   outputdate = data[5]
   inputdate = str(inputdate[0:4] + inputdate[5:7] + inputdate[8:10])
   packingdate = str(packingdate[0:4] + packingdate[5:7] + packingdate[8:10])
   outputdate = str(outputdate[0:4] + outputdate[5:7] + outputdate[8:10])
   if data[6] == '':
      data[6] = 0
   result = oen.OutputEngineRepository('u', [data[1], data[2], inputdate, packingdate, outputdate, data[6], data[7], data[8], data[0]])
   return result


