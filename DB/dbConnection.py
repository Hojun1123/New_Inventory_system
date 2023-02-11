import pymysql as db

#### db 연결 정보 ######

########

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
