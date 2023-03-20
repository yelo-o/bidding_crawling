# import csv # csv 모듈을 불러온다.
# from requests import get
# from bs4 import BeautifulSoup
# import pandas as pd


# #1.3 월드메모리 - Monitor
# url3 = 'http://www.worldmemory.co.kr/price/computer.do?ctgry_no1=20&ctgry_no2='
# gen_urls = ["60", "1711"]

# monitor_names = []
# monitor_prices = []
# target_monitor_names = ['23" LCD (삼성,LG)','22" LED (삼성,LG)',
#                         '23" LED(삼성,LG)','24" LED(삼성,LG)',
#                         '27" LED(삼성,LG)']
# new_monitor_names = []
# new_monitor_prices = []

# for i in gen_urls:
#     response = get(f"{url3}{i}")

#     if response.status_code != 200:
#         print("웹사이트를 불러올 수 없다.")
#     else:
#         soup = BeautifulSoup(response.text, "html.parser")

#         product_names = soup.find_all('td', class_='price_table_prduct_nm')
#         for name in product_names:
#             monitor_names.append(name.text)
#         # 3세대 가격
#         prices = soup.find_all('td', class_='price_table_prduct_pc')
#         for price in prices:
#             monitor_prices.append(price.text)
            
# # target_monitor_names 요소를 하나씩 가져와서 ram_names에 있는지 확인합니다.
# for monitor_name in target_monitor_names:
#     if monitor_name in monitor_names:
#         # ram_names에 있으면 해당 인덱스를 가져와서 new_ram_names와 new_ram_prices에 추가합니다.
#         index = monitor_names.index(monitor_name)
#         new_monitor_names.append(monitor_name)
#         new_monitor_prices.append(monitor_prices[index])
#     else:
#         # cpu_names에 없으면 '-'를 new_cpu_prices에 추가하고 new_cpu_names에는 해당 요소를 추가합니다.
#         new_monitor_names.append(monitor_name)
#         new_monitor_prices.append('-')

# # Monitor 데이터프레임 확인
# df = pd.DataFrame({"모니터 이름": new_monitor_names, "모니터 가격": new_monitor_prices})
# print(df)

# datetime 모듈을 불러온다
# import datetime
from datetime import datetime

# 현재 날짜와 시간을 가져온다
now = datetime.now()

# 날짜를 원하는 형식으로 포맷팅한다
cr_today = now.strftime("%Y-%m-%d")

# 결과를 출력한다
print(cr_today)

default_list1 = [cr_today, '월드와이드메모리']
default_list2 = [cr_today, '나노메모리']
default_list3 = [cr_today, '다나와']

print(default_list1)
print(default_list2)
print(default_list3)