from flask import Blueprint, render_template, request, session
from Service.User import login

userController = Blueprint("user", __name__, url_prefix="/user")


# 로그인 페이지
@userController.route('/login', methods=['GET', 'POST'])
def loginPage():  # put application's code here
    #### db 테스트용
    if request.method == 'POST':
        result = login.checkUser(request.form.get("id"), request.form.get("pwd"))
        if result:
            session['userid'] = result
            return render_template("/main.html")
    else:
        return render_template("/login.html")
