import requests
import random

# def pick_numbers(n):
#     lotto_num=[]
#     for games in range(n):
#         k = range(1,46)
#         lotto_num=(random.sample(k,6))
#         lotto_num.sort()
#         print(lotto_num)
    
# pick_numbers(10)

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json() 

real_numbers = []
repeat =0
while(repeat<501):
    repeat=repeat+1
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
         real_numbers.append(value)
    
    sorted_real_numbers=sorted(real_numbers)
    bonus_number = lotto_data['bnusNo']

    numbers = list(range(1, 46))

    pick_numbers = random.sample(numbers, 6)
    pick_numbers.sort()

    set_real_numbers = set(real_numbers)
    set_pick_numbers = set(pick_numbers)
    intersec_numbers= len(set_real_numbers.intersection(set_pick_numbers))

    # print('이번 회차 당첨번호는', sorted_real_numbers, '입니다')
    # print('당신이 선택한 번호는', pick_numbers, '입니다')

    if real_numbers == pick_numbers:
        print('First prize')
    
    elif intersec_numbers == 4 and bonus_number in pick_numbers:
        print('Second prize')

    elif intersec_numbers == 5:
        print('Third prize')

    elif intersec_numbers == 4:
        print('Fourth prize')

    elif intersec_numbers == 3:
        print('Fifth prize')
    else:
        print('Next time...')