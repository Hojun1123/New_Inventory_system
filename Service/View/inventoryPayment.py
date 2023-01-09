import DB.mipRepository as dao
import DB.engineRepository as en
import DB.outputEngineRepository as oen
from collections import defaultdict
from datetime import datetime

# {types : {mip : n, mip2: n, ...}, ...}
def makeMIPDict():
    mip = dao.MIPRepository('getMIP')
    typeDict = defaultdict(dict)
    # mip/type dict
    for r in mip:
        types = r[1]
        typeDict[types] = defaultdict(int)
    for r in mip:
        mips = r[0]
        types = r[1]
        typeDict[types][mips] = 0

    return typeDict

def baseInventory(baseInv, sd, ed):
    tmpInv = baseInv
    eng = en.EngineRepository('sd2', sd)
    engOut = oen.OutputEngineRepository('sd2', [sd, ed])
    for i in eng:
        mips = i[1]
        types = i[2]
        tmpInv[types][mips] += 1
    for i in engOut:
        mips = i[1]
        types = i[2]
        tmpInv[types][mips] += 1

    return tmpInv

def inputInventory(inputInv, sd, ed):
    tmpInv = inputInv
    eng = en.EngineRepository('betweenDate', [sd, ed])
    engOut = oen.OutputEngineRepository('betweenDateI', [sd, ed])
    for i in eng:
        mips = i[1]
        types = i[2]
        tmpInv[types][mips] += 1
    for i in engOut:
        mips = i[1]
        types = i[2]
        tmpInv[types][mips] += 1

    return tmpInv

def outputInventory(outputInv, sd, ed):
    tmpInv = outputInv
    engOut = oen.OutputEngineRepository('betweenDateO', [sd, ed])
    for i in engOut:
        mips = i[1]
        types = i[2]
        tmpInv[types][mips] += 1

    return tmpInv

# method = get
def paymentListGet():
    ret = []
    # baseInv, inputInv, outputInv
    baseInv = makeMIPDict()
    inputInv = makeMIPDict()
    outputInv = makeMIPDict()
    startDate, endDate = datetime.now(), datetime.now()
    startDate, endDate = str(startDate), str(endDate)
    sd = str(startDate[0:4] + startDate[5:7] + startDate[8:10])
    ed = str(endDate[0:4] + endDate[5:7] + endDate[8:10])
#    sd = "20221230"
#    ed = "20221230"

    baseInv = baseInventory(baseInv, sd, ed)
    inputInv = inputInventory(inputInv, sd, ed)
    outputInv = outputInventory(outputInv, sd, ed)

    # make inven list
    for i in baseInv:
        for j in baseInv[i]:
            base, inp, outp = baseInv[i][j], inputInv[i][j], outputInv[i][j]
            inv = base + inp - outp
            if inv < 0:
                return -1
            ret.append( [i, j, base, inp, outp, inv])

    print("get")
    return ret

# method = post
def paymentListPost(startDate, endDate):
    ret = []
    # baseInv, inputInv, outputInv
    baseInv = makeMIPDict()
    inputInv = makeMIPDict()
    outputInv = makeMIPDict()
    startDate, endDate = str(startDate), str(endDate)
    sd = str(startDate[0:4] + startDate[5:7] + startDate[8:10])
    ed = str(endDate[0:4] + endDate[5:7] + endDate[8:10])
#    sd = "20221230"
#    ed = "20221230"

    baseInv = baseInventory(baseInv, sd, ed)
    inputInv = inputInventory(inputInv, sd, ed)
    outputInv = outputInventory(outputInv, sd, ed)

    # make inven list
    for i in baseInv:
        for j in baseInv[i]:
            base, inp, outp = baseInv[i][j], inputInv[i][j], outputInv[i][j]
            inv = base + inp - outp
            if inv < 0:
                return -1
            ret.append([i, j, base, inp, outp, inv])

    print("post")
    return ret