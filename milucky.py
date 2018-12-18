
import random
import requests
url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
real_numbers=[]
response = requests.get(url,verify=False)
lotto_data = response.json()
for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = lotto_data['bnusNo']
print(real_numbers)

numbers = list(range(1,46))

pick = random.sample(numbers,6)

print(sorted(pick))

url = 'https://api.darksky.net/forecast/71859e8278db87c8a8a4679177f93ae9/37.501588,%20127.039713'

res = requests.get(url)
data = res.json()
print(data['currently']['summary'])

#darkskylib 설치필요  pip install darkskylib
from darksky import forecast

multicampus = forecast('71859e8278db87c8a8a4679177f93ae9', 37.501588, 127.039713)

print(multicampus['currently']['temperature'])
print(multicampus['currently']['summary'])




#my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real & my 가 5개가 같고, my의 나머지 하나가 bonus_number
# 3등 : real & my 가 5개가 같다
# 4등 : real & my 가 4개가 같다
# 5등 : real & my 가 3개가 같다
# 꽝 : 

# print(random.sample(list(range(1,46)),6))
