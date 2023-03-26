from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def extract_danawa():
  # 변수 설정
  
  # # CPU 이름과 url 리스트
  cpu_names = ['i3 3250', 'i3 4370', 'i3 6300', 'i3 7300', 'i3 8100', 'i3 9100', 'i5 3470',
               'i5 4570', 'i5 6500', 'i5 7400', 'i5 8400', 'i5 9400', 'i7 3770', 'i7 4770',
               'i7 6700', 'i7 7700', 'i7 8700', 'i7 9700']
  cpu_list = ['17870279', '6112509', '5796940', '7812271', '15827978', '14740478', '1725177',
              '4905563', '5684847', '7898218', '12543974', '7893904', '1678801', '6112690',
              '5714311', '7898143', '13360280', '11083932']
  
  # # RAM 이름과 url 리스트
  ram_names = ['RAM ddr3 4G', 'RAM ddr3 8G', 'RAM ddr4 4G', 'RAM ddr4 8G', 'RAM ddr4 16G' ]
  ram_list = ['5545241','5549101','14679644','16524044','17009480']
  
  danawa_cpu_prices= []
  danawa_ram_prices= []
  
  def get_danawa(url_list,danawa_names,danawa_prices):
    browser = webdriver.Chrome(options=options)
    for i in url_list:
      browser.get(f'https://prod.danawa.com/info/?pcode={i}&cate=112752')
    
      soup = BeautifulSoup(browser.page_source, 'html.parser')
  
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
              danawa_prices.append(y.text)
          else:  # 최저가가 최저현금가보다 쌀 때
              danawa_prices.append(e.text)
              
      elif len(qq) != 0:  # '최저가'만 있을 때
          for q in qq:
              ww = q.find_all('span', 'lwst_prc')
              for w in ww:
                  e = w.find('em', class_='prc_c')
                  danawa_prices.append(e.text)
                  
      else:  # '최저현금가'만 있을 때
          for r in rr:
              tt = r.find_all('span', 'lwst_prc')
              for t in tt:
                  y = t.find('em', class_='prc_c')
                  danawa_prices.append(y.text)
  
  # df  = pd.DataFrame({'종류':danawa_names, '가격':danawa_prices})
  
  # CPU    
  get_danawa(cpu_list,cpu_names,danawa_cpu_prices)
  # RAM
  get_danawa(ram_list,ram_names,danawa_ram_prices)
  
  danawa_prices= danawa_cpu_prices + danawa_ram_prices + [0, 0, 0, 0, 0]
  print("다나와 모든 제품 가격들 \n", danawa_prices,len(danawa_prices))
  return danawa_prices
