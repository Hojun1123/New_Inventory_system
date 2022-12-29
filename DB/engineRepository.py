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
        return -1

    def delete():
        sql = "DELETE FROM ENGINE WHERE barcode=%s;"
        try:
            cursor.execute(sql, data)
            connection.commit()
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
        elif act == 'checkBarcode':
            result = selectValidEngine()
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
