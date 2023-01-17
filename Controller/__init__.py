from flask import Flask
from . import user
from . import engine
from . import mip
from . import view
from . import etc
from . import admin

app = Flask(__name__)

# 로그인, 로그아웃 등 사용자 관련 페이지
app.register_blueprint(user.userController)
# 엔진 입고, 출고, 수정, 삭제(insert, update, delete 등)
app.register_blueprint(engine.engineController)
# mip추가, 삭제
app.register_blueprint(mip.mipController)
# 조회 페이지, 당일조회, 기간조회 등등(select)
app.register_blueprint(view.viewController)
# 기타 페이지, 바코드 인쇄, 액셀 파일 생성 등
app.register_blueprint(etc.etcController)
# 관리자 권한으로 실행 가능한 페이지들
app.register_blueprint(admin.engineController)
