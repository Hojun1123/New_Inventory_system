from flask import Flask
from . import user
from . import engine
from . import mip
from . import view

app = Flask(__name__)

# 로그인, 로그아웃 등 사용자 관련 페이지
app.register_blueprint(user.userController)
# 엔진 입고, 출고, 수정, 삭제(insert, update, delete 등)
app.register_blueprint(engine.engineController)
# mip추가, 삭제
app.register_blueprint(mip.mipController)
# 조회 페이지, 당일조회, 기간조회 등등(select)
app.register_blueprint(view.viewController)
