# 크롤링 관련 모듈
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import pandas as pd
from credentials import u_id, u_pw
from get_urls import urls


# 변수 설정
now = datetime.now()
st_now = str(now)
crawling_date = st_now[0:10].replace(':',".")
print(crawling_date)

# ## 어제 16:01 시간 구하기
# yesterday = datetime.now() - timedelta(days=1)
# start_time = datetime(yesterday.year, yesterday.month, yesterday.day, 16, 1)
# ## 오늘 16:00 시간 구하기
# today = datetime.now()
# end_time = datetime(today.year, today.month, today.day, 16, 0)

# 엑셀 열 구성 데이터
time_data = [] # 날짜 + 시간 열
date_column = [] # 날짜 열
time_column = [] # 시간 열
title_data = [] # 제목 열
content_data = [] # 내용 열

# 메인 프로세스(최초 로그인)
def crawling_process():
    global now, st_now, crawling_date, time_data, time_column, date_column, title_data, content_data
    execute_browser() # 브라우저 실행 및 url 이동
    login() # 로그인 화면 이동 및 로그인
    moveToUrl() # 수집한 url로 이동
    
    # print('제목(title_data)<- 게시물 들어가서 뽑은 거',len(title_data))
    # print('제목(title_data)<- 게시물 들어가서 뽑은 거',title_data)
    print('날짜', len(time_data))
    print('날짜', time_data)
    # print('내용',len(content_data))
    # print('내용',content_data)
    
    print('-------------------------')
    
    print('urls',len(urls))
    data_to_excel(crawling_date)  # 데이터 엑셀로 변환
    
    browser.quit() # 브라우저 종료

    

    
# 브라우저 실행 및 url 이동
def execute_browser():
    global browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() # 윈도우 최대로 확대
    url = "https://cafe.naver.com/ak573/"
    browser.get(url)
    
    
def login():
    # 로그인 화면 이동
    btnToLogin = browser.find_element(By.XPATH,'//*[@id="gnb_login_button"]')
    btnToLogin.click()

    # 아이디, 비밀번호 입력
    input_id = browser.find_element(By.XPATH,'//*[@id="id"]')
    input_pw = browser.find_element(By.XPATH,'//*[@id="pw"]')
    btn_lgn = browser.find_element(By.XPATH,'//*[@id="log.login"]')
    input_id.click()
    pyperclip.copy(u_id)
    input_id.send_keys(Keys.CONTROL,'v')
    input_pw.click()
    pyperclip.copy(u_pw)
    input_pw.send_keys(Keys.CONTROL,'v')
    btn_lgn.click()
    

# 수집한 url로 이동
def moveToUrl():
    for i in urls:
        browser.get(i)
        # time.sleep(1)
        browser.implicitly_wait(1)
        collect_data()

# 제목, 내용, 작성시간 수집
def collect_data():
    global content_data, time_data, title_data, date_column, time_column

    # 데이터 받아오기 위한 iframe 전환
    browser.switch_to.frame('cafe_main')
    
    # 타이틀 -> title_data
    try:
        written_title = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3')[0]
        title_data.append(written_title.text)
    except:
        title_data.append("**접근이 불가한 게시판입니다.**")
        pass
    # 글 작성일자 및 시간 -> time_data
    try:
        written_time = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]')[0]
        time_data.append(written_time.text)
    except:
        time_data.append("**접근이 불가한 게시판입니다.**")
        pass
    # 글 내용 -> content_data
    try:
        written_content = browser.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[1]')[0]
        content_data.append(written_content.text)
    except:
        content_data.append("**접근이 불가한 게시판입니다.**")
        pass

# # 엑셀에 데이터 저장
def data_to_excel(crawling_date):
    
    global time_data, start_time, end_time
    
    
    ## 시간 열 나누기 (1개 -> 2개)
    for time in time_data:  # time_data -> date_column, time_column 으로 분할
        global date_column, time_column
        a = time.split()
        date_column.append((a[0]))
        time_column.append((a[1]))
    
    
    # 판다스 데이터 만들기
    index_list = list(range(1, len(urls)+1)) # list(range(1,51)) # 1~50까지 넘버링
    df = pd.DataFrame({"제목" : title_data, "날짜" : date_column, "시간" : time_column, "내용" : content_data, "url" : urls}, index = index_list)
    # df = pd.DataFrame({"제목" : title_data, "날짜" : time_data, "내용" : content_data, "url" : urls}, index = index_list)
    
    
    # 전일 ~ 금일만 필터링
    df['날짜'] = pd.to_datetime(df['날짜'], errors='coerce')
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y.%m.%d.').dt.date
    
    # 어제 날짜 계산하기
    now = pd.Timestamp.now()
    yesterday = now - pd.Timedelta(days=1)
    
    filtered_data = df[df['날짜'] >= yesterday].copy()
    
    
    ## 내림차순 정렬
    # filtered_data.sort_values(by='시간', ascending=False, inplace=True)  # 시간 내림차순 정렬
    filtered_data.sort_values(by='날짜', ascending=False, inplace=True)  # 날짜 내림차순 정렬
    
    
    ## 중복행 제거
    filtered_data.drop_duplicates(keep='first', inplace=True,
                                  ignore_index=True)
    
    filtered_data.index = filtered_data.index + 1  # 0행부터 시작 -> 1행부터 시작
    
    ## 인덱스 이름 No.로 지정 
    filtered_data.index.name = "No."
    
    filtered_data.to_excel(f"{crawling_date} 비딩 키워드 검색.xlsx",index=True)

# 비딩 키워드
crawling_process()