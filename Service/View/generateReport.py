import DB.engineRepository as en
import DB.outputEngineRepository as oen
from collections import defaultdict
from datetime import date, timedelta

def getReport(start, end):
    #올바르지않은 날짜 형식
    if len(start) != 10 or len(end) != 10:
        return -2
    start = str(start[0:4] + start[5:7] + start[8:10])
    end = str(end[0:4] + end[5:7] + end[8:10])
    #시작일이 종료일 보다 큰 경우
    if int(start) > int(end):
        return -2

    #ENGINE DB 데이터 가져오기
    enData = en.EngineRepository('sd', end)
    if enData == -1:
        return -1
    #OUTPUTENGINE DB 데이터 가져오기
    oenData = oen.OutputEngineRepository('sd', (start, end))
    if oenData == -1:
        return -1


    # 날짜 테이블
    datelist = []
    s = date(int(start[0:4]), int(start[4:6]), int(start[6:8]))
    e = date(int(end[0:4]), int(end[4:6]), int(end[6:8]))
    delta = e - s
    for i in range(delta.days + 1):
        datelist.append((s + timedelta(days=i)).strftime("%Y%m%d"))

    # mip:type 해시테이블
    typeTables = defaultdict(set)
    mergeTablesIn = defaultdict(lambda: defaultdict(int))
    mergeTablesOut = defaultdict(lambda: defaultdict(int))
    mergeTables = defaultdict(lambda: defaultdict(int))
    IN, OUT, STOCK = defaultdict(int), defaultdict(int), defaultdict(int)
    for row in enData:
        x, y, z = row[1], row[2], str(row[3])
        mergeTablesIn[z][x] += 1
        mergeTablesIn[z][y] += 1
        typeTables[y].add(x)
        IN[z] += 1
    for row in oenData:
        x, y, z, p = row[1], row[2], str(row[3]), str(row[5])
        mergeTablesIn[z][x] += 1
        mergeTablesOut[p][x] += 1
        mergeTablesIn[z][y] += 1
        mergeTablesOut[p][y] += 1
        typeTables[y].add(x)
        IN[z] += 1
        OUT[p] += 1
    for d in datelist:
        for row in enData:
            if row[3] <= int(d):
                mergeTables[d][row[1]] += 1
                mergeTables[d][row[2]] += 1
                STOCK[d] += 1
        for row in oenData:
            if row[3] <= int(d) < row[5]:
                mergeTables[d][row[1]] += 1
                mergeTables[d][row[2]] += 1
                STOCK[d] += 1

    #print(mergeTablesIn)
    #print(mergeTablesOut)
    #print(mergeTables)
    #print(typeTables)
    #print(enData)
    #print(oenData)
    #print(IN)
    #print(OUT)
    #print(STOCK)

    colors = ["#eeb7b4", "#f2cfa5", "#aee4ff", "#b5c7ed", "#c4f4fe", "#bee9b4",
              "#fcc6f7", "#caa6fe", "#ffafd8", "#afffba", "#e2ffaf", "#fcffb0", "#f2cfa5", "#ffe4af"]

    ##### 헤더 #####
    resultTable = "<table>"
    resultTable += "<thead><tr><td colspan='2'>엔진사양</td><td class='rt-br'>구분</td><td class='rt-td-55'>이월재고</td>"
    for d in datelist:
        resultTable += "<td>" + d[4:6] + "/" + d[6:] + "</td>"
    resultTable += "<td class='rt-bl rt-td-45'>합계</td></tr></thead>"

    #### 바디 #####
    def tostr(num):
        return '-' if num == 0 else str(num)
    def body(key, values, c):
        tmp = "<tr><td colspan='2' rowspan='3' class='rt-bt' style='background-color:" + c + "'>" + key + "</td><td class='rt-td-60 rt-bt rt-br'>입고계</td><td class='rt-bt'></td>"
        asum = 0
        for dd in datelist:
            a = mergeTablesIn[dd][key]
            asum += a
            tmp += "<td class='rt-bt'>" + tostr(a) + "</td>"
        tmp += "<td class='rt-bt rt-bl'>" + str(asum) + "</td></tr><tr><td class='rt-td-60 rt-br'>불출계</td><td></td>"
        asum = 0
        for dd in datelist:
            a = mergeTablesOut[dd][key]
            asum += a
            tmp += "<td>" + tostr(a) + "</td>"
        tmp += "<td class='rt-bl'>" + str(asum) + "</td></tr><tr><td class='rt-td-60 rt-br'>재고계</td>"
        tmp += "<td style='background-color:#FDFD96'>" + str(mergeTables[datelist[0]][key]-mergeTablesIn[datelist[0]][key]+mergeTablesOut[datelist[0]][key]) + "</td>"
        for dd in datelist:
            tmp += "<td>" + tostr(mergeTables[dd][key]) + "</td>"
        tmp += "<td class='rt-bl' style='background-color:#FDFD96'>" + str(mergeTables[datelist[-1]][key]) + "</td></tr>"
        return tmp + mipBody(values)

    def mipBody(values):
        rowl = len(values)
        tmp = "<tr><td rowspan='" + str(rowl * 3) + "'>&nbsp;&nbsp;&nbsp;&nbsp;</td>"
        for v in values:
            tmp += "<td rowspan='3'>" + v + "</td><td class='rt-br'>입고</td><td></td>"
            asum = 0
            for dd in datelist:
                a = mergeTablesIn[dd][v]
                asum += a
                tmp += "<td>" + tostr(a) + "</td>"
            tmp += "<td class='rt-bl'>" + str(asum) + "</td></tr><tr><td class='rt-br'>출고</td><td></td>"
            asum = 0
            for dd in datelist:
                a = mergeTablesOut[dd][v]
                tmp += "<td>" + tostr(a) + "</td>"
            tmp += "<td class='rt-bl'>" + str(asum) + "</td></tr><tr><td class='rt-br'>재고</td>"
            tmp += "<td style='background-color:#FFFFDD'>" + str(mergeTables[datelist[0]][v]-mergeTablesIn[0][v]+mergeTablesOut[0][v]) + "</td>"
            for dd in datelist:
                tmp += "<td>" + tostr(mergeTables[dd][v]) + "</td>"
            tmp += "<td class='rt-bl' style='background-color:#FFFFDD'>" + str(mergeTables[datelist[-1]][v]) + "</td></tr>"
        return tmp

    cnt = 0
    for tk, tv in typeTables.items():
        resultTable += body(tk, tv, colors[cnt%14])
        cnt += 1

    resultTable += "<tr><td colspan='2' rowspan='3' class='rt-bt' style='background-color:#fff037'>엔진 계</td><td class='rt-td-60 rt-bt rt-br' style='background-color:#fff037'>입고계</td><td class='rt-bt'></td>"
    for d in datelist:
        resultTable += "<td class='rt-bt'>" + tostr(IN[d]) + "</td>"
    resultTable += "<td class='rt-bt rt-bl'>" + str(sum(IN.values())) + "</td></tr><tr><td class='rt-td-60 rt-br' style='background-color:#fff037'>불출계</td><td></td>"
    for d in datelist:
        resultTable += "<td>" + tostr(OUT[d]) + "</td>"
    resultTable += "<td class='rt-bl'>" + str(sum(OUT.values())) + "</td></tr><tr><td class='rt-td-60 rt-br' style='background-color:#fff037'>재고계</td>"
    resultTable += "<td style='background-color:#fff037'>" + str(STOCK[datelist[0]] + OUT[datelist[0]] - IN[datelist[0]]) + "</td>"
    for d in datelist:
        resultTable += "<td>" + tostr(STOCK[d]) + "</td>"
    return resultTable + "<td class='rt-bl' style='background-color:#fff037'>" + str(STOCK[datelist[-1]]) + "</td></tr>"
