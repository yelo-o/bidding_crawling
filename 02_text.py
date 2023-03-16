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

        pd_names = soup.find('li', class_='rank_one')
        # print(pd_names)
        sss = pd_names.find_all(class_='price_sect')
        for ss in sss:
            dd = ss.find_all('strong')
            for oo in dd:
                xx = oo.text
            danawa_prices.append(xx)
    # 모든 가격        
    print(danawa_prices)