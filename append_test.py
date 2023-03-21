
from openpyxl import load_workbook
import openpyxl
a = ['2023-03-20', '월드와이드메모리', '2,000', '6,000', '35,000', '4,000', '15,000', '45,000', '15,000', '37,000', '72,000', '20,000', '50,000', '110,000', '55,000', '70,000', '140,000', '75,000', '100,000', '200,000', '1,000', '11,000', '4,000', '12,000', '28,000', '5,000', '15,000', '20,000', '25,000', '40,000', None]
b = ['2023-03-20', '나노메모리', '-', '9,000', '40,000', '-', '17,000', '45,000', '18,000', '37,000', '80,000', '22,000', '50,000', '110,000', '55,000', '70,000', '140,000', '75,000', '100,000', '210,000', '1,000', '13,000', '30,000', '12,000', '4,000', '-', '15,000', '25,000', '30,000', '-', None]
c = ['2023-03-20', '다나와', '11,630', '31,400', '40,850', '75,000', '85,000', '124,990', '17,290', '27,990', '54,180', '82,970', '123,720', '131,350', '57,900', '81,320', '117,490', '190,510', '217,150', '344,430', '4,400', '21,190', '15,410', '22,620', '57,950', '-', '-', '-', '-', '-', None] 

d = ['2023-03-20', c[5], ]
e = []

# 엑셀 파일 열기
wb = openpyxl.load_workbook('it_data.xlsx')
# wb = openpyxl.load_workbook('rawdata.xlsx')

# # 1번 시트 선택
# ws = wb['1. IT 전체 개별단가']

# # C열의 셀들 가져오기
# cells = ws['C']

# # C열의 마지막 행 찾기
# last_row = max(c.row for c in cells if c.value is not None)

# # 리스트의 요소를 하나씩 가져와서 B열의 마지막 행 다음 셀에 넣기
# for i in range(len(a)):
#     ws.cell(last_row + 1, i + 3).value = a[i]

# for i in range(len(a)):
#     ws.cell(last_row + 2, i + 3).value = b[i]

# for i in range(len(a)):
#     ws.cell(last_row + 3, i + 3).value = c[i]

# 2번 시트
ws = wb['2. IT 주력모델 시세현황']


# B열의 셀들 가져오기
cells = ws['B']

# B열의 마지막 행 찾기
# last_row = max(b.row for b in cells if b.value is not None)

# 마지막행 B열 값 확인
last_row = ws.max_row

# B열 (넘버링)
last_value = ws.cell(row=last_row, column=2).value  # 마지막 값 불러오기
ws.cell(row=last_row+1, column=2, value=last_value+1)

# M열 (넘버링)
last_value = ws.cell(row=last_row, column=13).value
ws.cell(row=last_row+1, column=13, value=last_value+1)

# 변경사항 저장
wb.save('example2.xlsx')

# D : 

# 변경된 내용을 저장
# wb.save('example.xlsx')


