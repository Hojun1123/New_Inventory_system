from flask import Blueprint, Flask, render_template, request
from Service.View import generateReport
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
        return render_template("/report.html", table=table, startdate=str(startdate), enddate=str(enddate))


@viewController.route("/allEngines", methods=['GET', 'POST'])
def allEngines():
    if request.method == 'GET':
        return render_template("/inventory.html", table="")
    else:
        startdate = request.form.get("startdate")
        enddate = request.form.get("enddate")
        return render_template("/inventory.html", table="", startdate=str(startdate), enddate=str(enddate))


