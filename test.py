from requests import get
from bs4 import BeautifulSoup
import pandas as pd

target_cpu_names = ['3250','3470','3770','4370','4570','4770 / 4770K ','6300 ','6500 ','6700 ','7300 ','7400 ','7700 ','8100 ','8400 ','8700 ','9100 ','9400','9700']

cpu_names = ['3770K', '3770', '3570 / 3570K', '3550', '3470', '3450', '3330', '3220 이상', 'G2020 이상', 'G1610 이상 ', '4790K', '4790', '4770 / 4770K ', 
            '4690 / 4690K ', '4670 / 4670K ', '4590', '4570', '4460', '4430 / 4440 ', '4330 이상 ', '4130 이상 ', 'G3420 이상 ', 'G3220 이상 ', 'G1820 이상',
            '6700K ', '6700 ', '6600K ', '6600 ', '6500 ', '6400 ', '6320 ', '6300 ', '6100 ', 'G4520 ', 'G4500 ', 'G4400 ', 'G3900 ', '7700K ', '7700 ', '7600K ', '7600 ', 
            '7500 ', '7400 ', '7320 ', '7300 ', '7100 ', 'G4620 ', 'G4600 ', 'G4560 ', 'G3950 ', 'G3930', '8700K ', '8700 ', '8600K ', '8600 ', '8500 ', '8400 ', '8350K ', 
            '8100 ', 'G5400 ', 'G4900 ', '9900K', '9900KF', '9900', '9700K', '9700KF', '9700', '9700F', '9600K', '9600KF', '9600', '9500', '9500F', '9400', '9400F ', '9100 ', '9100F ', 'G5620 ', 'G5420 ', 'G4930 ']

cpu_prices = ['45,000', '40,000', '11,000', '10,000', '9,000', '5,000', '5,000', '2,000', '100', '100', '50,000', '45,000', '45,000', '20,000', '18,000', '17,000', '17,000',
             '15,000', '13,000', '4,000', '4,000', '500', '500', '100', '85,000', '80,000', '40,000', '38,000', '37,000', '35,000', '18,000', '18,000', '17,000', '3,000', 
             '3,000', '4,000', '500', '125,000', '110,000', '55,000', '55,000', '55,000', '50,000', '22,000', '22,000', '22,000', '4,000', '4,000', '4,000', '500', '500', '155,000', 
             '140,000', '75,000', '75,000', '75,000', '70,000', '57,000', '55,000', '17,000', '8,000', '300,000', '250,000', '270,000', '210,000', '180,000', '210,000', '160,000', 
             '90,000', '90,000', '95,000', '110,000', '90,000', '100,000', '90,000', '75,000', '45,000', '17,000', '17,000', '15,000']

# cpu_names와 target_cpu_names의 순서를 맞추기 위해 새로운 리스트를 만듭니다.
new_cpu_names = []
new_cpu_prices = []

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
df = pd.DataFrame({"CPU 이름": new_cpu_names, "CPU 가격": new_cpu_prices})
print(df)


# 모니터 이름 리스트를 생성합니다.
monitor_names = ['[ 안내 ] 모니터는 2016년 제품 이후부터 매입 진행 가능합니다.', '  삼성전자  / LG전자 LED 34인치', '  삼성전자  / LG전자 LED 32인치', '  삼성전자  / LG전자 LED 27인치',
                 '  삼성전자  / LG전자 LED 24인치', '  삼성전자  / LG전자 LED 23인치', '  삼성전자  / LG전자 LED 22인치', '  삼성전자  / LG전자 LED 20인치', '[ 안내 ] 모니터는 2016년 제품 이후부터 매입 진행 가능합니다.',
                 '  중소기업 LED 32인치', '  중소기업 LED 27인치', '  중소기업 LED 24인치', '  중소기업 LED 23인치', '  중소기업 LED 22인치', '  중소기업 LED 20인치']

# 모니터 가격 리스트를 생성합니다.
monitor_prices = ['0', '50,000', '40,000', '35,000', '30,000', '25,000', '15,000', '5,000', '0', '35,000', '30,000', '20,000', '15,000', '10,000', '5,000']

# 타겟 모니터 이름 리스트를 생성합니다.
target_monitor_names = ['20~23인치', '  삼성전자  / LG전자 LED 22인치', '  삼성전자  / LG전자 LED 23인치', '  삼성전자  / LG전자 LED 24인치','  삼성전자  / LG전자 LED 27인치']

# 새로운 모니터 이름과 가격 리스트를 생성합니다.
new_monitor_names = []
new_monitor_prices = []

# 타겟 모니터 이름 리스트를 순회하면서 모니터 이름과 가격을 가져옵니다.
for monitor_name in target_monitor_names:
    if monitor_name in monitor_names:
        # monitor_names에 있으면 해당 인덱스를 가져와서 new_monitor_names와 new_monitor_prices에 추가합니다.
        index = monitor_names.index(monitor_name)
        new_monitor_names.append(monitor_name)
        new_monitor_prices.append(monitor_prices[index])
    else:
        # monitor_names에 없으면 '-'를 new_monitor_prices에 추가하고 new_monitor_names에는 해당 요소를 추가합니다.
        new_monitor_names.append(monitor_name)
        new_monitor_prices.append('-')
        
# 새로운 모니터 이름과 가격 리스트를 데이터프레임으로 만들어 출력합니다.
df = pd.DataFrame({"모니터 이름": new_monitor_names, "CPU 가격": new_monitor_prices})
print(df)

