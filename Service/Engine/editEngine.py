import DB.engineRepository as en

def stringToDate(s):
   s = str(s)
   return s[0:4] + "-" + s[4:6] + "-" + s[6:8]

def editEngineData(eid):
   result = en.EngineRepository('selectById', eid)
   if result == -1:
      return -1
   i = result[0]
   return [i[0], i[1], i[2], stringToDate(i[3]), stringToDate(i[4]), i[5], i[6], i[7], i[8]]

def editProcess(data):
   #바코드, MIP, 타입, 입고일, 포장일, 위치, 불량, 비고
   if data[1] == '' or data[2] == '' or len(data[3]) != 10 or len(data[4]) != 10:
      return -2
   inputdate = data[3]
   packingdate = data[4]
   inputdate = str(inputdate[0:4] + inputdate[5:7] + inputdate[8:10])
   packingdate = str(packingdate[0:4] + packingdate[5:7] + packingdate[8:10])
   if data[6] == '':
      data[6] = 0
   result = en.EngineRepository('u', [data[1], data[2], inputdate, packingdate, data[5], data[6], data[7], data[0]])
   return result


