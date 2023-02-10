import io
import DB.engineRepository as dao
import csv

def inputEngine(files):
    if files == '':
        return -1

    sucess = 0
    err = 0

    for file in files:
        #받은 파일 데이터스트림화 후 csv 컨버트
        file = file.stream.read()
        file = io.StringIO(file.decode("cp949"), newline=None)
        file = csv.reader(file)

        #csv 컨버트 후 한줄씩 처리
        for line in file:
            #첫줄 제외
            if line[0] == '기종':
                continue
            else:
                #비어있는데이터 있으면 return
                for x in line:
                    if x == '':
                        return -1, -1

                #필요한 데이터 준비
                barcode = line[5] + line[2] + line[1]
                mip = line[1]
                type = line[0]
                inputDate = line[3].replace('.','')
                packingDate = line[4].replace('.','')
                group_id = line[6]
                location = ''
                errflag = '0'
                exp = ''

                #준비된 데이터 리스트화
                data = [barcode, mip, type, inputDate, packingDate, group_id, location, errflag, exp]

                #DB에 삽입
                errflag = dao.EngineRepository('i',data)

                #에러처리
                if errflag == 1:
                    sucess = sucess + 1
                else:
                    err = err + 1

        # 정상완료
        return sucess, err