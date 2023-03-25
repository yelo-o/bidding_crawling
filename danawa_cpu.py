from bs4 import BeautifulSoup
import pandas as pd
import csv
from fake_useragent import UserAgent
import requests as req

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
    'Referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php'
}

# # 로그인 URL
baseUrl = 'https://auth.danawa.com/login'



cpu_names = ['i3 3250', 'i3 4370', 'i3 6300', 'i3 7300', 'i3 8100', 'i3 9100', 'i5 3470',
             'i5 4570', 'i5 6500', 'i5 7400', 'i5 8400', 'i5 9400', 'i7 3770', 'i7 4770',
             'i7 6700', 'i7 7700', 'i7 8700', 'i7 9700']

cpu_list = ['17870279', '6112509', '5796940', '7812271', '15827978', '14740478', '1725177',
            '4905563', '5684847', '7898218', '12543974', '7893904', '1678801', '6112690',
            '5714311', '7898143', '13360280', '11083932']


with req.session() as s:
    # Request(로그인 시도)
    res = s.post(baseUrl, login_info, headers=headers)

    if res.status_code != 200:
        raise Exception("Login failed.")

    danawa_cpu_prices= []  # 가격 모아놓기
    for i in cpu_list:
        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get(
            f'https://prod.danawa.com/info/?pcode={i}&cate=113973', headers=headers)

        soup = BeautifulSoup(res.text, "html.parser")

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
                danawa_cpu_prices.append(y.text)
            else:  # 최저가가 최저현금가보다 쌀 때
                danawa_cpu_prices.append(e.text)
                
        elif len(qq) != 0:  # '최저가'만 있을 때
            for q in qq:
                ww = q.find_all('span', 'lwst_prc')
                for w in ww:
                    e = w.find('em', class_='prc_c')
                    danawa_cpu_prices.append(e.text)
                    
        else:  # '최저현금가'만 있을 때
            for r in rr:
                tt = r.find_all('span', 'lwst_prc')
                for t in tt:
                    y = t.find('em', class_='prc_c')
                    danawa_cpu_prices.append(y.text)
    
    # 데이터프레임 보기            
    df3 = pd.DataFrame({'종류': cpu_names, '가격': danawa_cpu_prices})
    print(df3)
