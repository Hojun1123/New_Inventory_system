import io
import DB.engineRepository as dao
import csv

def inputEngine(files):
    if files == '':
        return -1

    sucess = 0
    err = 0
    blank = 0
    blankFlag = False

    for file in files:
        print(file)
        #받은 파일 데이터스트림화 후 csv 컨버트
        file = file.stream.read()
        file = io.StringIO(file.decode("cp949"), newline=None)
        file = csv.reader(file)

        #csv 컨버트 후 한줄씩 처리
        for line in file:
            #첫줄 제외
            if line[0] == '기종':
                # csv파일 형식이 맞지 않으면 오류 배출
                if line[0] == '기종' and line[1] == 'MIP' and line[2] == 'ENG_NO' and line[3] == '입고일자' and line[4] == '포장일자' and line[5] == '비고' and line[6] == 'LOG':
                    continue
                else:
                    return -1, -1, -1
            else:
                #비어있는데이터 확인 후 플래그 변경
                for x in line:
                    if x == '':
                        blank = blank + 1
                        blankFlag = True
                        break

                #플래그 확인 후 True일 경우 break
                if blankFlag:
                    blankFlag = False
                    continue

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
    return sucess, err, blank