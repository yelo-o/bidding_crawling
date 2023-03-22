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

# # 로그인 URL
baseUrl = 'https://auth.danawa.com/login'


ram_names = ['RAM ddr3 4G', 'RAM ddr3 8G', 'RAM ddr4 4G', 'RAM ddr4 8G', 'RAM ddr4 16G' ]
ram_list = ['5545241','5549101','14679644','16524044','17009480']

with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)

    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception("Login failed.")
    
    danawa_ram_prices= []  # 가격 모아놓기
    for i in ram_list:
        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get(f'https://prod.danawa.com/info/?pcode={i}&cate=112752',headers=headers)

        # bs4 초기화
        soup = BeautifulSoup(res.text,"html.parser")

        qq = soup.find_all('div', class_='row lowest_price')  # 최저가
        rr = soup.find_all('div', id='lowPriceCash')  # 최저현금가
        
        
        if len(qq) != 0 and len(rr) != 0:  # 최저가도 있고 최저현금가 동시에 있으면 둘의 가격을 비교해서 저렴한거를 append
            # 최저가
            for q in qq:
                ww = q.find_all('span', 'lwst_prc')
                for w in ww:
                    e = w.find('em', class_='prc_c')
                    lowest_price = int(e.text.replace(',',''))
        
            # 최저가(현금)        
            for r in rr:
                tt = r.find_all('span', 'lwst_prc')
                for t in tt:
                    y = t.find('em', class_='prc_c')
                    lowest_price2 = int(y.text.replace(',',''))
            if lowest_price > lowest_price2:  # 최저가가 최저현금가보다 비쌀 때
                danawa_ram_prices.append(y.text)
            else:  # 최저가가 최저현금가보다 쌀 때
                danawa_ram_prices.append(e.text)
                
        elif len(qq) != 0:  # '최저가'만 있을 때
            for q in qq:
                ww = q.find_all('span', 'lwst_prc')
                for w in ww:
                    e = w.find('em', class_='prc_c')
                    danawa_ram_prices.append(e.text)
                    
        else:  # '최저현금가'만 있을 때
            for r in rr:
                tt = r.find_all('span', 'lwst_prc')
                for t in tt:
                    y = t.find('em', class_='prc_c')
                    danawa_ram_prices.append(y.text)
        
    
    # 데이터프레임 보기        
    df3 = pd.DataFrame({'종류':ram_names, '가격':danawa_ram_prices})
    print(df3)

