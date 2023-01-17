from Controller import app
from datetime import timedelta
######## 여긴 뭐 쓰지 말 것. ! #############
app.config["SECRET_KEY"] = "sh291hfwnh8@hwqjh2(*@#*Uh2N2920hF@H0Fh@C293"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

if __name__ == '__main__':
    app.run()
