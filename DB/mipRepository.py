import pymysql as db


def getTypes():
    result = None
    connection = None
    try:
        connection = db.connect(
            host="bangwol08.iptime.org",
            user="inven",
            port=50000,
            password="manager123!@#",
            database="InventoryManagement"
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
