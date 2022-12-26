import pymysql as db


def test():
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

        #sql문
        sql = ""
        print(cursor)
    except:
        print("DB 연결 오류")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("DB close")
    return result

'''
TABLE CREATION

CREATE TABLE mip(
	mip varchar(40) not null,
	type varchar(40) not null,
	primary key (mip)
) CHARACTER SET utf8;

CREATE TABLE OUTPUTENGINE(
	barcode varchar(32) not null,
	mip varchar(40) not null,
	type varchar(40) not null,
	input_date int not null,
	packing_date int not null,
	output_date int not null,
	errorflag int not null,
	exp varchar(200),
	destination varchar(100),
	primary key (barcode)
) CHARACTER SET utf8;


CREATE TABLE ENGINE(
	barcode varchar(32) not null,
	mip varchar(40) not null,
	type varchar(40) not null,
	input_date int not null,
	packing_date int not null,
	group_id varchar(32) not null,
	location varchar(32),
	errorflag int not null,
	exp varchar(200),
	primary key (barcode)
) CHARACTER SET utf8;



'''