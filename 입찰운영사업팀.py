print("크롤링 프로그램 시작..")

from extractors.worldMemory import extract_wm
from extractors.nanoMemory import extract_nm
from extractors.danawa import extract_danawa
from file import save_to_file

# 오늘 날짜
from datetime import datetime

now = datetime.now()
cr_today = now.strftime("%Y-%m-%d")

full_wm = [cr_today, '월드와이드메모리'] + extract_wm() + [None]
# print("월드와이드메모리 전처리 완료")
# print(full_wm)
full_nm = [cr_today, '나노메모리'] + extract_nm() + [None]
# print("나노메모리 전처리 완료")
# print(full_nm)
full_danawa = [cr_today, '다나와'] + extract_danawa() + [None]
# print("다나와 전처리 완료")
# print(full_danawa)

save_to_file(cr_today,full_wm,full_nm,full_danawa)
print("데이터 csv 파일 저장 완료")