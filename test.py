# 크롤링 관련 모듈
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import pandas as pd
from credentials import u_id, u_pw

title_data = ['라이센스 관련 문의', 'office 라이선스 문의', 'IT분야취업연계과정 | 스마트팩토리 SW개발자양성과정(부산) 온라인설명회가 2월 16일 진행됩니다!', '임직원 pc 보유 현황 관리', '[프리랜서,재택근무] 채용담당자 모집', 'PC 렌탈 문의드려요-', '구글드라이브 vs 원드라이브 고민입니다.', '[드림어스컴퍼니/FLO] HR Manager 채용', '[헤딩] 당산 오피스 / \ufeff신입, 주니어, 경력 헤드헌터(프리랜서)분들을 모십니다!!', '복합기 렌탈 견적 부탁드립니다', '사내간식 및 전산장비 제안요청', 'PC 컴퓨터 및 모니터 견적 문의', '사내 자산 ( PC, 노트북 ) 보안프로그램 문의 [ 40명분 ]', '[플리토] HR 담당 채용 (총무/인사) _ 2/13 24:00 까지', 'PC 및 모니터 납품 업체 견적 문의드리고자 합니다.']
time_data = ['2023.02.15. 21:10', '2023.02.15. 17:35', '2023.02.15. 13:40', '2023.02.15. 10:37', '2023.02.14. 01:14', '2023.02.13. 18:02', '2023.02.13. 13:52', '2023.02.10. 16:36', '2023.02.10. 16:26', '2023.02.09. 17:58', '2023.02.08. 13:58', '2023.02.06. 17:14', '2023.02.05. 15:17', '2023.02.03. 13:00', '2023.02.02. 15:10']


yesterday = datetime.now() - timedelta(days=1)
start_time = datetime(yesterday.year, yesterday.month, yesterday.day, 16, 1)
print("start_time : ",start_time)
## 오늘 16:00 시간 구하기
today = datetime.now()
end_time = datetime(today.year, today.month, today.day, 16, 0)
print("end_time : ", end_time)


df = pd.DataFrame({"제목" : title_data, "날짜" : time_data })
print(df)
df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')
print(df)
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y.%m.%d. %H:%M')
print(df)

df.sort_values(by='날짜', ascending=False, inplace=True)  # 날짜 내림차순 정렬
print(df)


ftd = df.loc[(df['날짜'] >= start_time) & (df['날짜'] <= end_time)]
print(ftd)