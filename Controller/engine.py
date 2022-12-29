from flask import Blueprint, Flask, render_template, request, flash, session

from Service.Engine import addEngines
from Service.Engine import releaseEngines
engineController = Blueprint("engine", __name__, url_prefix="/engine")


@engineController.route("/addEngine", methods=['GET', 'POST'])
def addEngine():
    if request.method == 'POST':
        r = addEngines.inputEngine(request.form.get("barcode"))
        print(r)
        if r == -1:
            flash("[ERROR] 데이터 베이스 연결 오류")
        elif r == -2:
            flash("[ERROR] 중복 또는 잘못된 데이터 입력")
        elif r == -3:
            flash("[ERROR] 잘못된 데이터 입력")
        return render_template("/readBarcode.html")
    else:
        return render_template("/readBarcode.html")


@engineController.route("/releaseEngine", methods=['GET', 'POST'])
def releaseEngine():
    if request.method == 'POST':
        data = request.form.get("barcode")
        r = releaseEngines.outputEngine(data, session['ValidEngines'])
        outputEngines = session['outputEngines']
        if r == -1:
            flash("[ERROR] 데이터 베이스 연결 오류")
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
            flash("[ERROR] 데이터 베이스 연결 오류")
            return render_template("/releaseEngine.html")
        session['outputEngines'] = []   # 사용자에게 불출한 엔진과 처리결과를 돌려주기 위한 리스트
        session['ValidEngines'] = r
        return render_template("/releaseEngine.html")


