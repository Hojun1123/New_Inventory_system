from flask import Blueprint, render_template, request, session, flash
from Service.User import login

userController = Blueprint("user", __name__, url_prefix="/")


# 로그인 페이지
@userController.route('/', methods=['GET', 'POST'])
def loginPage():  # put application's code here
    #### db 테스트용
    if request.method == 'POST':
        result = login.checkUser(request.form.get("id"), request.form.get("pwd"))
        if result:
            session['userid'] = result
            return "<script>location.href='/view/todayEngines';</script>"
        else:
            flash("로그인 정보가 올바르지 않습니다.")
            return render_template("/login.html")
    else:
        if len(session) > 0:
            return "<script>alert('이미 "+session['userid']+" 계정으로 로그인 중 입니다.');location.href='/view/todayEngines';</script>"
        return render_template("/login.html")

@userController.route('/logout')
def logoutPage():
    if len(session) > 0:
        session.clear()
    return render_template("/login.html")
