from flask import Blueprint, Flask, render_template, request, flash, session

from Service.Engine import addEngines
from Service.Engine import releaseEngines
#from Service.Engine import readAllEngines
#from Service.Engine import editEngine
#from Service.Engine import editOutputEngine
#from Service.Engine import deleteEngine
#from Service.Engine import deleteOutputEngine
#from Service.Engine import addErrorEngine

engineController = Blueprint("engine", __name__, url_prefix="/engine")

@engineController.before_request
def beforeRequest():
    try:
        if 'userid' not in session:
            return "<script>alert('로그인 후 이용해주시길 바랍니다.');location.href='/';</script>"
    except:
        return "location.href='/';</script>"

@engineController.route("/addEngine", methods=['GET', 'POST'])
def addEngine():
    if request.method == 'POST':
        sucess, err, blank = addEngines.inputEngine(request.files.getlist("file[]"))
        #파일형식이 맞지 않는 오류처리
        if sucess == -1 and err == -1 and blank == -1:
            flash(f'선택한 파일이 형식에 맞지 않습니다. 다시 확인해 주세요.')
        else: #오류가 나지 않았을때
            if blank >= 1: #빈칸이 하나라도 있다면
                flash(f'누락되어있는 정보가 {blank}건의 처리가 보류되었습니다. 파일에 오류가 있다면 수정 후 다시 시도해주세요.')
            flash(f'입고성공 : {sucess} 중복엔진 : {err} 빈칸보류 : {blank}')
        return render_template("/inputEngine.html")
    else:
        return render_template("/inputEngine.html")


@engineController.route("/releaseEngine", methods=['GET', 'POST'])
def releaseEngine():
    if request.method == 'POST':
        data = request.form.get("barcode")
        r = releaseEngines.outputEngine(data, session['ValidEngines'])
        outputEngines = session['outputEngines']
        if r == -1:
            flash("[ERROR] 데이터 베이스 오류")
            outputEngines.append(data + " : DB에러")
        elif r == -2:
            flash("[ERROR] 존재하지않는 바코드 입니다.")
            outputEngines.append(data + " : 존재하지않는 엔진")
        elif r == -3:
            flash("[ERROR] 불출 금지 엔진입니다.")
            outputEngines.append(data + " : 출고금지 엔진!!!")
        else:
            outputEngines.append(data + " : 정상출고")

        session['outputEngines'] = outputEngines
        return render_template("/releaseEngine.html", el=session['outputEngines'], length=len(session['outputEngines']))
    else:
        r = releaseEngines.getValidEngines()
        if r == -1:
            flash("[ERROR] 데이터 베이스 오류")
            return render_template("/releaseEngine.html")
        session['outputEngines'] = []   # 사용자에게 불출한 엔진과 처리결과를 돌려주기 위한 리스트
        session['ValidEngines'] = r
        return render_template("/releaseEngine.html")




'''
@engineController.route("/editEngines", methods=['GET', 'POST'])
def editEngines():
    if request.method == 'GET':
        table = readAllEngines.selectAllEngines()
        if table == -1:
            table = []
            flash("[ERROR] 데이터 베이스 오류")
        return render_template("/editEngine.html", table=table)


@engineController.route("/editForm", methods=['GET', 'POST'])
def editForm():
    if request.method == 'GET':
        result = editEngine.editEngineData(request.args.get('eid'))
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류")
            return "<script>location.href='/engine/editEngines';</script>"
        else:
            return render_template("/editForm.html", engine=result[0])
    else:
        eid = request.args.get('eid')
        input_date = request.form.get('input_date')
        packing_date = request.form.get('packing_date')
        mip = request.form.get('mip')
        typ = request.form.get('type')
        locaion = request.form.get('location')
        errorflag = request.form.get('errorflag')
        exp = request.form.get('exp')
        result = editEngine.editProcess([eid,  mip, typ, input_date, packing_date, locaion, errorflag, exp])
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류")
        elif result == -2:
            flash("[ERROR] 올바르지 않은 데이터")
        else:
            flash("정상적으로 수정되었습니다.")
        result = editEngine.editEngineData(eid)
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류2")
        return "<script>location.href='/engine/editEngines';</script>"


@engineController.route("/deleteProcess")
def deleteProcess():
    result = deleteEngine.deleteProcess(request.args.get('eid'))
    if result == -1:
        flash("[ERROR] 엔진삭제, 데이터 베이스 오류")
    else:
        flash("정상적으로 삭제되었습니다.")
    table = readAllEngines.selectAllEngines()
    if table == -1:
        flash("[ERROR] 테이블로드, 데이터 베이스 오류")
    return "<script>location.href='/engine/editEngines';</script>"


@engineController.route("/setInvalidEngine", methods=["GET", "POST"])
def setInvalidEngine():
    table = addErrorEngine.getErrorEngineList()
    if table == -1:
        table = [["[ERROR] 데이터 베이스 오류"]]
    if request.method == 'GET':
        return render_template("/setInvalidEngine.html", table=table)
    else:
        eid = request.form.get('eid')
        exp = request.form.get('exp')
        result = addErrorEngine.setErrorFlag(eid, exp)
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류")
        elif result == -2 or result == 0:
            flash("[ERROR] 존재하지 않는 바코드입니다.")
        return render_template("/setInvalidEngine.html", table=table)

########################
####### 출고 엔진 수정 삭제 #####
@engineController.route("/editOutputEngines", methods=['GET', 'POST'])
def editOutputEngines():
    if request.method == 'GET':
        table = readAllEngines.selectAllOutputEngines()
        if table == -1:
            table = []
            flash("[ERROR] 데이터 베이스 오류")
        return render_template("/editOutputEngine.html", table=table)


@engineController.route("/editOutputEngineForm", methods=['GET', 'POST'])
def editOutputEngineForm():
    if request.method == 'GET':
        result = editOutputEngine.editOutputEngineData(request.args.get('eid'))
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류")
            return "<script>location.href='/engine/editOutputEngines';</script>"
        else:
            return render_template("/editOutputEngineForm.html", engine=result[0])
    else:
        eid = request.args.get('eid')
        input_date = request.form.get('input_date')
        packing_date = request.form.get('packing_date')
        output_date = request.form.get('output_date')
        mip = request.form.get('mip')
        typ = request.form.get('type')
        errorflag = request.form.get('errorflag')
        exp = request.form.get('exp')
        destination = request.form.get('destination')
        result = editOutputEngine.editOutputEngineProcess([eid,  mip, typ, input_date, packing_date, output_date, errorflag, exp, destination])
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류")
        elif result == -2:
            flash("[ERROR] 올바르지 않은 데이터")
        else:
            flash("정상적으로 수정되었습니다.")
        result = editOutputEngine.editOutputEngineData(eid)
        if result == -1:
            flash("[ERROR] 데이터 베이스 오류2")
        return "<script>location.href='/engine/editOutputEngines';</script>"


@engineController.route("/deleteOutputEngineProcess")
def deleteOutputEngineProcess():
    result = deleteOutputEngine.deleteOutputProcess(request.args.get('eid'))
    if result == -1:
        flash("[ERROR] 엔진삭제, 데이터 베이스 오류")
    else:
        flash("정상적으로 삭제되었습니다.")
    table = readAllEngines.selectAllOutputEngines()
    if table == -1:
        flash("[ERROR] 테이블로드, 데이터 베이스 오류")
    return "<script>location.href='/engine/editOutputEngines';</script>"

'''