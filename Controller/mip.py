from Service.Mip import addMIP, getMIP, deleteMIP
from flask import Blueprint, render_template, request, flash, session

mipController = Blueprint("mip", __name__, url_prefix="/mip")

@mipController.before_request
def beforeRequest():
    try:
        if session['userid'] != 'manager':
            return "<script>alert('권한이 없습니다.');location.href='/view/todayEngines';</script>"
    except:
        return "<script>alert('로그인 후 이용해주시길 바랍니다.');location.href='/';</script>"


@mipController.route("/addMIP", methods=['GET', 'POST'])
def addMip():
    if request.method == 'POST':
        m = request.form.get("mip")
        t = request.form.get("type")
        r = addMIP.inputMIP([m, t])
        mipList = getMIP.getAllMIP()
        if r == -1:
            flash("[ERROR] 데이터 베이스 연결 오류")
        elif r == -2:
            flash("[ERROR] 중복 또는 잘못된 데이터 입력")
        elif r == -3:
            flash("[ERROR] 잘못된 데이터 입력")
        if mipList == -1:
            flash("[ERROR] MIP테이블 불러오기 실패")
            return render_template("./addMIP.html")
        return render_template("/addMIP.html", mipList=mipList)
    else:
        mipList = getMIP.getAllMIP()
        if mipList == -1:
            flash("[ERROR] MIP테이블 불러오기 실패")
            return render_template("./addMIP.html")
        return render_template("/addMIP.html", mipList=getMIP.getAllMIP())


@mipController.route("/deleteMIP")
def deleteMip():
    result = deleteMIP.deleteProcess(request.args.get('id'))
    if result == -1:
        flash("[ERROR] 데이터 베이스 연결 오류")
    else:
        flash("정상적으로 삭제되었습니다.")
    return "<script>location.href='/mip/addMIP';</script>"
