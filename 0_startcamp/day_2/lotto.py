

import requests
import random

numbers = list(range(1,46))
print(numbers)

lucky_numbers=random.sample(numbers,6)

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url,verify=False) # 인증서에 대한 검증은 하지않고 받겠다.
lotto_data = response.json()

real_numbers = []

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

numbers = list(range(1,46))
print(numbers)

lucky_numbers=random.sample(numbers,6)
sorted_luckynumbers = sorted(lucky_numbers)

count = 0

for number in sorted_luckynumbers:
    if number in real_numbers:
        count +=1
if count ==6:
    print("First prize")
elif count == 5:
    print("Second prize")
elif count == 4:
    print("Third prize")

