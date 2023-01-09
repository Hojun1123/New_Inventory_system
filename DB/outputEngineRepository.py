import pymysql as db
from DB.dbConnection import dbInfo
def OutputEngineRepository(act, data):
    result = None
    connection = None
    cursor = None

    def insert():
        sql = ("INSERT INTO OUTPUTENGINE" +
              " (barcode, mip, type, input_date, packing_date, output_date, errorflag, exp, destination) " +
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        try:
            cursor.execute(sql, data)
            connection.commit()
        except:
            return -1
        return 1

    def select():
        sql = "SELECT * FROM OUTPUTENGINE;"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return -1

    def selectByDate():
        sql = "SELECT * FROM OUTPUTENGINE WHERE output_date>=%s AND input_date<=%s"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1
        return 1

    def selectByDate2():
        sql = "SELECT * FROM OUTPUTENGINE WHERE output_date>=%s AND input_date<%s"
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

    def selectToday():
        sql = "SELECT * FROM OUTPUTENGINE WHERE output_date=%s;"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1

    def selectBetweenDateI():
        sql = "SELECT * FROM OUTPUTENGINE WHERE input_date>=%s AND input_date<=%s;"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1
        return 1

    def selectBetweenDateO():
        sql = "SELECT * FROM OUTPUTENGINE WHERE output_date>=%s AND output_date<=%s;"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1
        return 1

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
        elif act == 'sd2':
            result = selectByDate2()
        elif act == 'st':
            result = selectToday()
        elif act == 'betweenDateI':
            result = selectBetweenDateI()
        elif act == 'betweenDateO':
            result = selectBetweenDateO()

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
