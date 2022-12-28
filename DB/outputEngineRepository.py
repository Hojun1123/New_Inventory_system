import pymysql as db
from DB.dbConnection import dbInfo
def OutputEngineRepository(act, data):
    result = None
    connection = None
    cursor = None

    def insert():
        return -1

    def select():
        sql = "SELECT * FROM OUTPUTENGINE;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            return -1
        return 1
    def selectByDate():
        sql = "SELECT * FROM OUTPUTENGINE WHERE output_date>=%s AND input_date<=%s"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1
        return 1
    def update():
        return -1

    def delete():
        return -1

    try:
        connection = db.connect(
            host=dbInfo[0],
            user=dbInfo[1],
            port=dbInfo[2],
            password=dbInfo[3],
            database=dbInfo[4]
        )
        cursor = connection.cursor()
        if act == 'i':
            result = insert()
        elif act == 's':
            result = select()
        elif act == 'u':
            result = update()
        elif act == 'd':
            result = delete()
        elif act == 'sd':
            result = selectByDate()
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
