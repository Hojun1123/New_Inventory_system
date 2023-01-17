from flask import Blueprint, Flask, render_template, request, flash, session

#from Service.Engine import addEngines
#from Service.Engine import releaseEngines
from Service.Engine import readAllEngines
from Service.Engine import editEngine
from Service.Engine import editOutputEngine
from Service.Engine import deleteEngine
from Service.Engine import deleteOutputEngine
from Service.Engine import addErrorEngine

engineController = Blueprint("admin", __name__, url_prefix="/engine")

@engineController.before_request
def beforeRequest():
    try:
        if session['userid'] != 'manager':
            return "<script>alert('권한이 없습니다.');location.href='/view/todayEngines';</script>"
    except:
        return "<script>alert('로그인 후 이용해주시길 바랍니다.');location.href='/';</script>"



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