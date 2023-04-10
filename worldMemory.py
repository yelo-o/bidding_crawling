from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import csv


#1.1 월드 메모리 - cpu
url1 = 'http://www.worldmemory.co.kr/price/computer.do?ctgry_no1=8&ctgry_no2=9&ctgry_no3='

gen_urls = ["1188", "1684", "3682", "3838", "3918", "25"]

cpu_names = []
cpu_prices = []

target_cpu_names = ['아이비I3 3250', '아이비I5 3470', '아이비I7 3770',
                        '하스웰I3 4370', '하스웰I5 4570', '하스웰I7 4770',
                        '스카이I3 6300', '스카이I5 6500', '스카이I7 6700',
                        '카비I3 7300', '카비I5 7400', '카비I7 7700',
                        '커피I3 8100', '커피I5 8400', '커피I7 8700',
                        '커피I3 9100', '커피I5 9400', '커피I7 9700']

# cpu_names와 target_cpu_names의 순서를 맞추기 위해 새로운 리스트를 만듭니다.
new_cpu_names = []
new_cpu_prices = []

for i in gen_urls:
    response = get(f"{url1}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        product_names = soup.find_all('td', class_='price_table_prduct_nm')
        for name in product_names:
            cpu_names.append(name.text)
        # 가격
        prices = soup.find_all('td', class_='price_table_prduct_pc')
        for price in prices:
            cpu_prices.append(price.text)


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


# 결과값으로 new_cpu_names와 new_cpu_prices를 반환합니다.
# df = pd.DataFrame({"CPU 이름": new_cpu_names, "CPU 가격": new_cpu_prices})
# print(df)



#1.2 월드메모리 - RAM
url2 = 'http://www.worldmemory.co.kr/price/computer.do?ctgry_no1=1&ctgry_no2=2&ctgry_no3='
gen_urls = ["651", "3608"]

ram_names = []
ram_prices = []
target_ram_names = ['4G DDR3 삼성 12800','8G DDR3 삼성 12800','4G DDR4 삼성 25600(3200)',
                    '8G DDR4 삼성 25600(3200)','16G DDR4 삼성 25600(3200)']
new_ram_names = []
new_ram_prices = []


for i in gen_urls:
    response = get(f"{url2}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        product_names = soup.find_all('td', class_='price_table_prduct_nm')
        for name in product_names:
            ram_names.append(name.text)
        # 가격
        prices = soup.find_all('td', class_='price_table_prduct_pc')
        for price in prices:
            ram_prices.append(price.text)
            
# target_ram_names의 요소를 하나씩 가져와서 ram_names에 있는지 확인합니다.
for ram_name in target_ram_names:
    if ram_name in ram_names:
        # ram_names에 있으면 해당 인덱스를 가져와서 new_ram_names와 new_ram_prices에 추가합니다.
        index = ram_names.index(ram_name)
        new_ram_names.append(ram_name)
        new_ram_prices.append(ram_prices[index])
    else:
        # cpu_names에 없으면 '-'를 new_cpu_prices에 추가하고 new_cpu_names에는 해당 요소를 추가합니다.
        new_ram_names.append(ram_name)
        new_ram_prices.append('-')

# # 결과값으로 new_cpu_names와 new_cpu_prices를 반환합니다.
# df = pd.DataFrame({"RAM 이름": new_ram_names, "RAM 가격": new_ram_prices})
# print(df)

#1.3 월드메모리 - Monitor
url3 = 'http://www.worldmemory.co.kr/price/computer.do?ctgry_no1=20&ctgry_no2='
gen_urls = ["60", "1711"]

monitor_names = []
monitor_prices = []
target_monitor_names = ['23" LCD (삼성,LG)','22" LED (삼성,LG)',
                        '23" LED(삼성,LG)','24" LED(삼성,LG)',
                        '27" LED(삼성,LG)']
new_monitor_names = []
new_monitor_prices = []

for i in gen_urls:
    response = get(f"{url3}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        product_names = soup.find_all('td', class_='price_table_prduct_nm')
        for name in product_names:
            monitor_names.append(name.text)
        # 가격
        prices = soup.find_all('td', class_='price_table_prduct_pc')
        for price in prices:
            monitor_prices.append(price.text)
            
# target_monitor_names 요소를 하나씩 가져와서 ram_names에 있는지 확인합니다.
for monitor_name in target_monitor_names:
    if monitor_name in monitor_names:
        # ram_names에 있으면 해당 인덱스를 가져와서 new_ram_names와 new_ram_prices에 추가합니다.
        index = monitor_names.index(monitor_name)
        new_monitor_names.append(monitor_name)
        new_monitor_prices.append(monitor_prices[index])
    else:
        # cpu_names에 없으면 '-'를 new_cpu_prices에 추가하고 new_cpu_names에는 해당 요소를 추가합니다.
        new_monitor_names.append(monitor_name)
        new_monitor_prices.append('-')

# # Monitor 데이터프레임 확인
# df = pd.DataFrame({"모니터 이름": new_monitor_names, "모니터 가격": new_monitor_prices})
# print(df)

total_names = new_cpu_names + new_ram_names + new_monitor_names
world_total_prices = new_cpu_prices + new_ram_prices + new_monitor_prices

# ' 원' 제거
world_total_prices = [i.replace(' 원', '') for i in world_total_prices]

df = pd.DataFrame({"이름":total_names, "가격":world_total_prices})
print(df)