
from openpyxl import load_workbook
import openpyxl
from openpyxl.styles import Font, Alignment

full_wm = ['2023-03-20', '월드와이드메모리', '2,000', '6,000', '35,000', '4,000', '15,000', '45,000', '15,000', '37,000', '72,000', '20,000', '50,000', '110,000', '55,000', '70,000', '140,000', '75,000', '100,000', '200,000', '1,000', '11,000', '4,000', '12,000', '28,000', '5,000', '15,000', '20,000', '25,000', '40,000', None]
full_nm = ['2023-03-20', '나노메모리', '-', '9,000', '40,000', '-', '17,000', '45,000', '18,000', '37,000', '80,000', '22,000', '50,000', '110,000', '55,000', '70,000', '140,000', '75,000', '100,000', '210,000', '1,000', '13,000', '30,000', '12,000', '4,000', '-', '15,000', '25,000', '30,000', '-', None]
full_danawa = ['2023-03-20', '다나와', '11,630', '31,400', '40,850', 80000, '85,000', '124,990', '17,290', '27,990', '54,180', '82,970', '123,720', '131,350', '57,900', '81,320', '117,490', '190,510', '217,150', '344,430', '4,400', '21,190', '15,410', '22,620', '57,950', '-', '-', '-', '-', '-', None] 



d = ['2023-03-20', full_danawa[5], 'i3 변동' , full_danawa[11], 'i5 변동', full_danawa[17], None]

e = ['2023-03-20', full_danawa[20], '4g ram 변동', full_danawa[23], '8g ram 변동', None]



# 엑셀 파일 열기
wb = openpyxl.load_workbook('it_data2.xlsx')

# 1번 시트 선택
ws = wb['1. IT 전체 개별단가']

# C열의 셀들 가져오기
cells = ws['C']

# # C열의 마지막 행 찾기
# last_row = max(c.row for c in cells if c.value is not None)

# 마지막 행 번호 구하기
last_row = ws.max_row

# 마지막 행 + 2 아래 행 삭제
ws.delete_rows(last_row-1)

# last_row = ws.max_row

# 리스트의 요소를 하나씩 가져와서 B열의 마지막 행 다음 셀에 넣기
for i in range(len(full_wm)):
    ws.cell(last_row -2, i + 3).value = full_wm[i]

for i in range(len(full_nm)):
    ws.cell(last_row - 1, i + 3).value = full_nm[i]

for i in range(len(full_danawa)):
    ws.cell(last_row, i + 3).value = full_danawa[i]
    
    
# 표 아래에 참고 내용 입력
ws.cell(last_row + 3, 33).value = '*빨간음영 : 주력모델'  # 글자 데이터 입력
ws.cell(last_row + 3, 33).font = Font(color='FF0000', bold=True)  # 색상, 볼드체
ws.cell(last_row + 3, 33).alignment = align = Alignment(horizontal='right')  # 우측 정렬 

# # 2번 시트
ws = wb['2. IT 주력모델 시세현황']


# B열의 셀들 가져오기
cells = ws['B']


# 마지막행 B열 값 확인
last_row = ws.max_row

# B열 (넘버링) 위의 행 번호 + 1 입력 
last_value = ws.cell(row=last_row, column=2).value  # 마지막 값 불러오기
ws.cell(row=last_row+1, column=2, value=last_value + 1)

# M열 (넘버링) 위의 행 번호 + 1 입력
last_value = ws.cell(row=last_row, column=13).value
ws.cell(row=last_row+1, column=13, value=last_value + 1)

for i in range(len(d)):
    ws.cell(last_row + 1, i+3).value = d[i]
    
for i in range(len(e)):
    ws.cell(last_row + 1, i+14).value = e[i]
    
# ws.cell(row=last_row + 1, column=5, value='-') 


# 지정된 곳에 함수 입력
last_row_val = ws.cell(row=last_row+1, column=4).value
prev_row_val = ws.cell(row=last_row, column=4).value

# 마지막 행의 4번째 열에 값 입력하기
ws.cell(row=last_row+1, column=5).value = last_row_val - prev_row_val


# # 변경사항 저장
# wb.save('example2.xlsx')

# 변경된 내용을 저장
wb.save('example.xlsx')
