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
search_keyword = ["i3+3250", "i5+3470", "i7+3770"]
with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)

    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception("Login failed.")
    
    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))

    
    for i in search_keyword:
        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get(f'https://search.danawa.com/dsearch.php?query={i}', headers=headers)

        # 페이지 이동 후 수신 데이터 확인
        # print(res.text)

        # bs4 초기화
        soup = BeautifulSoup(res.text,"html.parser")

        # 로그인 성공 여부 체크
        check_name = soup.find('p', class_='user')

        xxx= []
        pd_names = soup.find_all('li', class_='rank_one')
        for pd_name in pd_names:
            sss = pd_name.find_all(class_='price_sect')
            for ss in sss:
                dd = ss.find_all('strong')
                for oo in dd:
                    xx = oo.text
                xxx.append(xx)
                print(xxx[0])