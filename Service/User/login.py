userList = [
    ['manager', 'manager123!@#', '관리자'],
    ['user', 'user123!@#', '사용자'],
    ['worker', 'worker123!@#', '작업자']
]
# 아이디 가 맞는 지 체크.
def checkUser(id, pw):
    for i in userList:
        if i[0] == id and i[1] == pw:
            return i[2]
    else:
        return False




