from datetime import datetime
from danawa import danawa_prices
from nanoMemory import new_li_prices
from worldMemory import world_total_prices


now = datetime.now()
cr_today = now.strftime("%Y-%m-%d")

full_wm = [cr_today, '월드와이드메모리'] + world_total_prices + [None]
full_nm = [cr_today, '나노메모리'] + new_li_prices + [None]
full_danawa = [cr_today, '다나와'] + danawa_prices + [None]

print(full_wm, len(full_wm))
print(full_nm, len(full_nm))
print(full_danawa, len(full_danawa))

