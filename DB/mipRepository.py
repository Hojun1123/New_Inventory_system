import pymysql as db
from DB.dbConnection import dbInfo

def getTypes():
    result = None
    connection = None
    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        sql = "SELECT * FROM MIP;"
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print("DB 연결 오류")
        return -1
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("DB close")
    return result
