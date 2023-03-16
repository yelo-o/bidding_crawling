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

search_keyword = ["i3 3250", "i5 3470",
                "i7 3770", "i3 4370", "i5 4570", "i7 4770",      
                "i3 6300", "i5 6500", "i7 6700", "i3 7300", 
                "i5 7400", "i7 7700", "i3 8100", "i5 8400", 
                "i7 8700", "i3 9100", "i5 9400", "i7 9700"]

with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)

    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception("Login failed.")
    
    danawa_prices= []  # 가격 모아놓기
    for i in search_keyword:
        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get(f'https://search.danawa.com/dsearch.php?query={i}', headers=headers)

        # 페이지 이동 후 수신 데이터 확인
        # print(res.text)

        # bs4 초기화
        soup = BeautifulSoup(res.text,"html.parser")

        # 로그인 성공 여부 체크
        check_name = soup.find('p', class_='user')
        col1 = []
        col2 = []
        qq = soup.find('div', class_="prod_pricelist")  # 최상단 물건 데이터 불러오기
        ww = qq.find_all('li')  # 정품, 병행수입, 벌크, 중고별 가격 리스트
        for w in ww:
            ee = w.find_all('p', class_='memory_sect')  # 판매 방식 
            for e in ee:
                dd = e.txt
                ddd = e.text.split()
                col1.append(ddd[0])
                # print("종류 : ", ddd[0])
                
            rr = w.find_all('p', class_='price_sect')  # 판매 종류에 따라 형성된 가격 
            for r in rr:
                ff = r.find_all('strong')
                for f in ff:
                    vv = f.text
                    col2.append(vv)
                    # print("가격 : ", vv)
                    
        df3 = pd.DataFrame({'종류':col1, '가격':col2})
        print(df3)
        # df3 = df3[df3['종류'] == "중고"]
        # print(df3)

