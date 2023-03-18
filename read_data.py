# pandas 라이브러리를 불러온다
import pandas as pd

# 데이터프레임으로 변환할 엑셀 파일 경로를 지정한다
file_path = './rawdata.xlsx'

# 엑셀 파일을 데이터프레임으로 변환한다
df = pd.read_excel(file_path)

# 데이터프레임을 출력한다
print(df)


# csv 파일로 저장
df.to_csv('data.csv',encoding='utf-8-sig', index=False)

