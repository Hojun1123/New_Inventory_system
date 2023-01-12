from flask import Blueprint, Flask, render_template, request
from Service.View import generateReport
from Service.View import viewAllEngines
from Service.View import viewTodayEngines
from Service.View import inventoryPayment
viewController = Blueprint("/", __name__, url_prefix="/view")


@viewController.route("/")
def main():
    return render_template("/main.html")


@viewController.route("/report", methods=['GET', 'POST'])
def generateReports():
    if request.method == 'GET':
        return render_template("/report.html", table="<p>날짜를 선택해주세요.</p>")
    else:
        startdate = request.form.get("startdate")
        enddate = request.form.get("enddate")
        table = generateReport.getReport(startdate, enddate)
        if table == -1:
            table = "[ERROR] 데이터 베이스 연결 오류"
        elif table == -2:
            table = "[ERROR] 올바르지 않은 날짜 형식입니다."
        return render_template("/report.html", table=table, startdate=str(startdate), enddate=str(enddate))

@viewController.route("/allEngines", methods=['GET', 'POST'])
def allEngines():
    if request.method == 'GET':
        table = viewAllEngines.getAllEngines("0000:00:00", "9000:00:00")
        if table == -1:
            table = "[ERROR] 데이터 베이스 연결 오류"
        elif table == -2:
            table = "[ERROR] 올바르지 않은 날짜 형식입니다."
        return render_template("/inventory.html", table=table)
    else:
        startdate = request.form.get("startdate")
        enddate = request.form.get("enddate")
        table = viewAllEngines.getAllEngines(startdate, enddate)
        if table == -1:
            table = "[ERROR] 데이터 베이스 연결 오류"
        elif table == -2:
            table = "[ERROR] 올바르지 않은 날짜 형식입니다."
        return render_template("/inventory.html", table=table, startdate=str(startdate), enddate=str(enddate))


@viewController.route("/todayEngines")
def todayEngines():
    inputTable, outputTable = viewTodayEngines.getTodayEngines()
    return render_template("/viewTodayResult.html", inputTable=inputTable, outputTable=outputTable)


@viewController.route("/inventoryPayment", methods=['GET', 'POST'])
def viewInventoryPayment():
    if request.method == 'GET':
        invenList = inventoryPayment.paymentListGet()
        return render_template("/inventoryPayment.html", paymentList=invenList)
    else:
        startDate = request.form.get("startdate")
        endDate = request.form.get("enddate")
        if len(startDate) < 10 or len(endDate) < 10:
            return "<script>alert(\'날짜를 선택해주세요\')\nwindow.history.back()</script>"
        invenList = inventoryPayment.paymentListPost(startDate, endDate)
        return render_template("/inventoryPayment.html", paymentList=invenList)