from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import csv

# 함수 정의
def get_nm(url):
    for i in gen_urls:
        response = get(f"{url}{i}")
        if response.status_code != 200:
            print("웹사이트를 불러올 수 없다.")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
        # 이름
        product_names = soup.find_all('td', class_='prdname')
        for td in product_names:
            b_tags = td.find_all('b')
            for b_tag in b_tags:
                li_names.append(b_tag.text)
        # 가격
        prices = soup.find_all('td', class_='price')
        for price in prices:
            st_tags = price.find_all('strong')
            for st_tag in st_tags:
                li_prices.append(st_tag.text.replace("\n", "").replace("\t", ""))
                li_prices = list(filter(lambda x: x != '1' and x != '0', li_prices))


#2.1 나노 메모리 - cpu
url1 = 'http://www.nanomemory.co.kr/product/product.php?ptype=list&catcode='

gen_urls = ["10101700", "10101600", "10101400", "10101300", "10101200", "10101100"]

li_names = []
li_prices = []
new_li_names = []
new_li_prices = []


for i in gen_urls:
    response = get(f"{url1}{i}")
    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
    # 이름
    product_names = soup.find_all('td', class_='prdname')
    for td in product_names:
        b_tags = td.find_all('b')
        for b_tag in b_tags:
            li_names.append(b_tag.text)

    # 가격
    prices = soup.find_all('td', class_='price')
    for price in prices:
        st_tags = price.find_all('strong')
        for st_tag in st_tags:
            li_prices.append(st_tag.text.replace("\n", "").replace("\t", ""))
            li_prices = list(filter(lambda x: x != '1' and x != '0', li_prices))


#2.2 나노 메모리 - RAM
url2 = 'http://www.nanomemory.co.kr/product/product.php?ptype=list&catcode='

gen_urls = ["11201100", "11201200"]

for i in gen_urls:
    response = get(f"{url2}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

    # 이름
    product_names = soup.find_all('td', class_='prdname')
    for sam in product_names:
        samsungelec = sam.text
        if '안내' in samsungelec:
            pass
        else:
            li_names.append(samsungelec.replace("\n", "").replace("\t", ""))

    # 가격
    prices = soup.find_all('td', class_='price')
    for price in prices:
        st_tags = price.find_all('strong')
        for st_tag in st_tags:
            li_prices.append(st_tag.text.replace("\n", "").replace("\t", ""))
            li_prices = list(filter(lambda x: x != '1' and x != '0', li_prices))


#2.3 나노 메모리 - 모니터
url3 = 'http://www.nanomemory.co.kr/product/product.php?ptype=list&catcode='

gen_urls = ["18000000"]

for i in gen_urls:
    response = get(f"{url3}{i}")

    if response.status_code != 200:
        print("웹사이트를 불러올 수 없다.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

    # 이름
    product_names = soup.find_all('td', class_='prdname')
    for td in product_names:
        li_names.append(td.text)

    # 가격
    prices = soup.find_all('td', class_='price')
    for price in prices:
        st_tags = price.find_all('strong')
        for st_tag in st_tags:
            li_prices.append(st_tag.text.replace("\n", "").replace("\t", ""))
        # li_prices = list(
        #   filter(lambda x: x != '1' and x != '0', li_prices))


target_names =  ['3250','3470','3770','4370','4570','4770 / 4770K ','6300 ',
                '6500 ','6700 ','7300 ','7400 ','7700 ','8100 ','8400 ','8700 ',
                '9100 ','9400','9700','삼성전자   DDR3 4G   메모리',
                '삼성전자   DDR3 8G   메모리', '삼성전자   DDR4 16G  PC4-3200A',
                '삼성전자   DDR4 8G  PC4-3200A', '삼성전자   DDR4 4G  PC4-3200A',
                '20~23인치', '  삼성전자  / LG전자 LED 22인치',
                '  삼성전자  / LG전자 LED 23인치', '  삼성전자  / LG전자 LED 24인치',
                '삼성전자  / LG전자 LED 27인치']


for li_name in target_names:
    if li_name in li_names:
        index = li_names.index(li_name)
        new_li_names.append(li_name)
        new_li_prices.append(li_prices[index])
    else:
        new_li_names.append(li_name)
        new_li_prices.append(0)
        
print(new_li_prices)

'''
df = pd.DataFrame({"CPU 이름": new_li_names, "CPU 가격": new_li_prices})
print(df)

# li_names를 모두 csv로 저장하여 target 데이터 만들기
with open('list.csv', 'w', newline='') as file:
    writer = csv.writer(file)  # csv 파일을 작성하기 위한 writer 객체를 생성한다.
    writer.writerow(['Numbers'])  # 첫 번째 행에 'Numbers'를 작성한다.
    for name in li_names:  # list 리스트의 각 요소에 대해 반복한다.
        writer.writerow([name]) # 각 요소를 csv 파일에 작성한다.
        
'''