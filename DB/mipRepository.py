import pymysql as db
from DB.dbConnection import dbInfo

def MIPRepository(act, data=None):
    result = None
    connection = None
    cursor = None

    def selectAll():
        sql = "select * from MIP;"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return -1

    def insert():
        sql = ("INSERT INTO MIP" + " (mip, type) " + "VALUES (\"" + data[0] + "\",\"" + data[1] + "\");")
        try:
            cursor.execute(sql)
            connection.commit()
        except:
            return -2
        return 1

    def delete():
        sql = "DELETE FROM MIP WHERE mip=%s;"
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

        if act == 'getMIP':
            result = selectAll()
        elif act == 'insert':
            result = insert()
        elif act == 'd':
            result = delete()
    except:
        print("DB 연결 오류")
        return -1
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return result
