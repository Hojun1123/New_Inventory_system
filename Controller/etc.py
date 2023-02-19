from flask import Blueprint, render_template, request, flash, session, send_file
from Service.Etc import exportExcel
etcController = Blueprint("etc", __name__, url_prefix="/etc")
from datetime import datetime

@etcController.before_request
def beforeRequest():
    try:
        if 'userid' not in session:
            return "<script>alert('로그인 후 이용해주시길 바랍니다.');location.href='/';</script>"
    except:
        return "location.href='/';</script>"

@etcController.route("/enginedbExport")
def engineDBExport():
    result = exportExcel.engineDBToExcel()
    if result == -1:
        flash("[ERROR] 데이터 베이스 오류")
    elif result == -2:
        flash("[ERROR] 엑셀 파일 변환 오류")
    else:
        #flash(result + " 로 저장되었습니다.")
        filename = "입고" + datetime.now().strftime("_%Y%m%d_%H%M") + ".xlsx"
        return send_file("../ibgo.xlsx", download_name=filename)
    return render_template("./viewTodayResult.html")

@etcController.route("/outputenginedbExport")
def outputEngineDBExport():
    result = exportExcel.OutputEngineDBToExcel()
    if result == -1:
        flash("[ERROR] 데이터 베이스 오류")
    elif result == -2:
        flash("[ERROR] 엑셀 파일 변환 오류")
    else:
        #flash(result + " 로 저장되었습니다.")
        filename = "출고" + datetime.now().strftime("_%Y%m%d_%H%M") + ".xlsx"
        return send_file("../chulgo.xlsx", download_name=filename)
    return render_template("./viewTodayResult.html")
