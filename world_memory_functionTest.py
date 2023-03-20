from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import csv

# 나노메모리 - CPU
# 변수 설정
url1 = 'http://www.worldmemory.co.kr/price/computer.do?ctgry_no1=8&ctgry_no2=9&ctgry_no3='
cpu_urls = ["1188", "1684", "3682", "3838", "3918", "25"]

# 빈 리스트 생성(CPU)
cpu_names = []
cpu_prices = []

# 정렬 시킬 리스트 생성
new_cpu_names = []
new_cpu_prices = []

# 목표로 하는 CPU 이름 지정
target_cpu_names = ['아이비I3 3250','아이비I5 3470','아이비I7 3770',
                    '하스웰I3 4370','하스웰I5 4570','하스웰I7 4770',
                    '스카이I3 6300','스카이I5 6500','스카이I7 6700',
                    '카비I3 7300','카비I5 7400','카비I7 7700',
                    '커피I3 8100','커피I5 8400','커피I7 8700',
                    '커피I3 9100','커피I5 9400','커피I7 9700']

# 함수 설정
def get_wm(url,url_numbers,names,prices):
    for i in url_numbers:
        response = get(f"{url}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        product_names = soup.find_all('td', class_='price_table_prduct_nm')
        for name in product_names:
            names.append(name.text)
        # 가격
        product_prices = soup.find_all('td', class_='price_table_prduct_pc')
        for price in product_prices:
            prices.append(price.text)

def arrange_wm():
    # target_cpu_names의 요소를 하나씩 가져와서 cpu_names에 있는지 확인합니다.
    for cpu_name in target_cpu_names:
        if cpu_name in cpu_names:
            # cpu_names에 있으면 해당 인덱스를 가져와서 new_cpu_names와 new_cpu_prices에 추가합니다.
            index = cpu_names.index(cpu_name)
            new_cpu_names.append(cpu_name)
            new_cpu_prices.append(cpu_prices[index])
    else:
        # cpu_names에 없으면 '-'를 new_cpu_prices에 추가하고 new_cpu_names에는 해당 요소를 추가합니다.
        new_cpu_names.append(cpu_name)
        new_cpu_prices.append('-')

get_wm(url1, cpu_urls,cpu_names,cpu_prices)