from flask import Blueprint, Flask, render_template, request, flash

from Service.Engine import addEngines
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

