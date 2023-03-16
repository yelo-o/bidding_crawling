# BeautifulSoup은 HTML 과 XML 파일로부터 데이터를 수집하는 라이브러리
# pip install bs4
# pip install requests
# pip install fake-useragent
 
from bs4 import BeautifulSoup 
import requests as req
from fake_useragent import UserAgent
import csv
 
# 로그인 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://www.danawa.com/member/myPage.php',
    'loginMemberType': 'general',
    'id': 'etinnov',
    'isSaveId': 'true',
    'password': 'gurtlsruddud1!'
} 
 
# 헤더 정보
headers = { 
    'User-agent': UserAgent().chrome,
    'Referer' : 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php' 
}
 
# 로그인 URL
baseUrl = 'https://auth.danawa.com/login'
 
with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)
 
    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception("Login failed.")
    
    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))
 
    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)
 
    # 페이지 이동 후 수신 데이터 확인
    # print(res.text)
 
    # bs4 초기화
    soup = BeautifulSoup(res.text,"html.parser")
 
    # 로그인 성공 여부 체크
    check_name = soup.find('p', class_='user')
    # print(check_name)
 
    # 선택자 사용
    info_list = soup.select('div.my_info.no_sub_info > div > ul > li')
    # print(info_list) # 확인
 
    # 제목
    print()
    print('-' * 50)
 
    myshoppingList = []
    for v in info_list:
        # 속성 메소드 확인
        # print(dir(v))
 
        # 필요한 텍스트 추출
        proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
        print('{} : {}'.format(proc,val))
 
        # 파일 저장 목적 변수에 저장
        temp = []
        temp.append(v.find('span').string.strip())
        temp.append(v.find('strong').string.strip())
        myshoppingList.append(temp)
 
    print('-' * 50)
 
    with open('myshoppingList.csv',"w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(myshoppingList)
        print('CSV File created!')
    f.close
 