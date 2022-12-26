import pymysql as db

def EngineRepository(act, data):
    result = None
    connection = None

    def insert():
        return 1

    def select():
        return -1

    def update():
        return -1

    def delete():
        return -1

    try:
        connection = db.connect(
            host="bangwol08.iptime.org",
            user="inven",
            port=50000,
            password="manager123!@#",
            database="InventoryManagement"
        )
        cursor = connection.cursor()
        if act == 'i':
            result = insert()
        elif act == 's':
            result = select()
        elif act == 'u':
            result = update()
        else:
            result = delete()
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
