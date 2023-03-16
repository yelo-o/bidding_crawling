from bs4 import BeautifulSoup 
import requests as req
from fake_useragent import UserAgent
import csv
import pandas as pd

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

# search_keyword = ["i3 6300"]  # 테스트용 키보드

cpu_names = ["i3 3250", "i5 3470",
                "i7 3770", "i3 4370", "i5 4570", "i7 4770",      
                "i3 6300", "i5 6500", "i7 6700", "i3 7300", 
                "i5 7400", "i7 7700", "i3 8100", "i5 8400", 
                "i7 8700", "i3 9100", "i5 9400", "i7 9700"]
print(len(cpu_names))
cpu_list = ['17870279','1678801','5796940','7898218','13360280','1725177','6112509',
            '5684847','7898143','14740478','4905563','5714311','15827978','7893904',
            '6112690','7812271','12543974','11083932']
# cpu_list = ['7812271','12543974']
print(len(cpu_list))
ram_list = ['5545241','5549101','14679644','16524044','17009480']

with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)

    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception("Login failed.")
    
    danawa_prices= []  # 가격 모아놓기
    for i in cpu_list:
        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get(f'https://prod.danawa.com/info/?pcode={i}&cate=113973', headers=headers)

        # 페이지 이동 후 수신 데이터 확인
        # print(res.text)

        # bs4 초기화
        soup = BeautifulSoup(res.text,"html.parser")

        # 로그인 성공 여부 체크
        check_name = soup.find('p', class_='user')
        col1 = []
        col2 = []
        qq = soup.find_all('div', class_='row lowest_price')
        
        
        if len(qq) == 0:
            danawa_prices.append('-')
        else:
            for q in qq:
                ww = q.find_all('span', 'lwst_prc')
                for w in ww:
                    e = w.find('em', class_='prc_c' )
                    print(e)
                    print(e.text)
                    danawa_prices.append(e.text)
                        
            print(danawa_prices, len(danawa_prices))
    df3 = pd.DataFrame({'종류':cpu_names, '가격':danawa_prices})
    print(df3)

