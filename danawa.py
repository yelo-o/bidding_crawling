from danawa_cpu import danawa_cpu_prices
from danawa_ram import danawa_ram_prices

# 다나와가격 = 씨피유가격 + 램 가격
danawa_prices = danawa_cpu_prices + danawa_ram_prices + ['-', '-', '-', '-', '-']

print(danawa_prices, len(danawa_prices))