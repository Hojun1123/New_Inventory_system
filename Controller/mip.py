from Service.Engine import addMIP, getMIP
from flask import Blueprint, Flask, render_template, request, flash

mipController = Blueprint("mip", __name__, url_prefix="/mip")


@mipController.route("/addMIP", methods=['GET', 'POST'])
def addMip():
    if request.method == 'POST':
        m = request.form.get("mip")
        t = request.form.get("type")
        r = addMIP.inputMIP([m, t])
        #print(r)
        if r == -1:
            flash("[ERROR] 데이터 베이스 연결 오류")
        elif r == -2:
            flash("[ERROR] 중복 또는 잘못된 데이터 입력")
        elif r == -3:
            flash("[ERROR] 잘못된 데이터 입력")
        return render_template("/addMIP.html", mipList=getMIP.getAllMIP())
    else:
        return render_template("/addMIP.html", mipList=getMIP.getAllMIP())