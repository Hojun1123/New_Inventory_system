from flask import Blueprint, render_template, request, flash
from Service.Etc import exportExcel
etcController = Blueprint("etc", __name__, url_prefix="/etc")

@etcController.route("/enginedbExport")
def engineDBExport():
    result = exportExcel.engineDBToExcel()
    if result == -1:
        flash("[ERROR] 데이터 베이스 오류")
    elif result == -2:
        flash("[ERROR] 엑셀 파일 변환 오류")
    else:
        flash(result + " 로 저장되었습니다.")
    return render_template("./main.html")

@etcController.route("/outputenginedbExport")
def outputEngineDBExport():
    result = exportExcel.OutputEngineDBToExcel()
    if result == -1:
        flash("[ERROR] 데이터 베이스 오류")
    elif result == -2:
        flash("[ERROR] 엑셀 파일 변환 오류")
    else:
        flash(result + " 로 저장되었습니다.")
    return render_template("./main.html")
