import pymysql as db
from DB.dbConnection import dbInfo
def EngineRepository(act, data):
    result = None
    connection = None
    cursor = None

    def insert():
        sql = ("INSERT INTO ENGINE" +
              " (barcode, mip, type, input_date, packing_date, group_id, location, errorflag, exp) " +
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        try:
            cursor.executemany(sql, data)
            connection.commit()
        except:
            return -2
        return 1

    def select():
        sql = "SELECT * FROM ENGINE;"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return -1

    def selectByDate():
        sql = "SELECT * FROM ENGINE WHERE input_date<=%s;"
        # data = (start_date, end_date)
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1

    def selectValidEngine():
        sql = "SELECT barcode, mip, type, input_date, packing_date, errorflag, exp FROM ENGINE;"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return -1
        return 1


    def update():
        sql = "UPDATE ENGINE SET mip=%s, type=%s, input_date=%s, packing_date=%s, location=%s, errorflag=%s, exp=%s WHERE barcode=%s;"
        try:
            cursor.execute(sql, data)
            connection.commit()
        except:
            return -1
        return 1

    def delete():
        sql = "DELETE FROM ENGINE WHERE barcode=%s;"
        try:
            cursor.execute(sql, data)
            connection.commit()
        except:
            return -1
        return 1

    def selectById():
        sql = "SELECT * FROM ENGINE WHERE barcode=%s;"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1

    def selectToday():
        sql = "SELECT * FROM ENGINE WHERE input_date=%s;"
        try:
            cursor.execute(sql, data)
            return cursor.fetchall()
        except:
            return -1

    def updateErrorFlag():
        sql = "UPDATE ENGINE SET errorflag=%s, exp=%s WHERE barcode=%s;"
        try:
            a = cursor.execute(sql, data)
            connection.commit()
        except:
            return -1
        return a

    def getErrorEngineList():
        sql = "SELECT barcode, mip, type, input_date, exp"

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
        elif act == 'checkBarcode':
            result = selectValidEngine()
        elif act == 'selectById':
            result = selectById()
        elif act == 'st':
            result = selectToday()
        elif act == 'updateErrorFlag':
            result = updateErrorFlag()
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
