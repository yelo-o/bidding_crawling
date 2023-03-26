import csv
def save_to_file(file_name,full_wm,full_nm,full_danawa):
  
  file =  open(f"{file_name}.csv", 'w', encoding='utf-8-sig')
  fieldnames = ['날짜', '사이트명', 'i3-3250', 'i3-4370', 'i3-6300', 'i3-7300(주력모델)', 'i3-8100', 'i3-9100', 'i5-3470', 'i5-4570', 'i5-6500', 'i5-7400(주력모델)', 'i5-8400', 'i5-9400', 'i7-3770', 'i7-4770',
                'i7-6700', 'i7-7700(주력모델)', 'i7-8700', 'i7-9700', 'DDR3 4G', 'DDR3 8G', 'DDR3 4G', 'DDR3 8G', 'DDR3 16G', '모니터 LCD 20~23인치', '모니터 LED 22인치', '모니터 LED 23인치', '모니터 LED 24인치', '모니터 LED 27인치', '비고']
  writer = csv.writer(file)
  writer.writerow(fieldnames)
  writer.writerow(full_wm)
  writer.writerow(full_nm)
  writer.writerow(full_danawa)