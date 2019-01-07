import requests
import random

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return numbers

def get_lotto(draw_no):
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=' + str(draw_no)
    
    response = requests.get(url, verify=False)
    lotto_data = response.json() 
    
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
         numbers.append(value)
         
    bonus_number = lotto_data['bnusNo']
    
    final_dict = {
        'numbers' : sorted(numbers), 
        'bonus' :bonus_number
    } 
    return final_dict
    
def am_i_lucky(my_number,real_number):
    set_pick_numbers = set(my_number)
    set_real_numbers = set(real_number['numbers'])
    intersec_numbers= len(set_real_numbers.intersection(set_pick_numbers))
  
    if set_real_numbers == set_pick_numbers:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. 축하합니다! First prize!!!!')
    
    elif intersec_numbers == 4 and real_number['bonus'] in set_pick_numbers:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. 축하합니다! Second Prize!!!')

    elif intersec_numbers == 5:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. 축하합니다! Third prize!!')

    elif intersec_numbers == 4:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. 축하합니다! Fourth prize!')

    elif intersec_numbers == 3:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. 축하합니다! Fifth prize')

    else:
        return('당신의 번호는 '+str(set_pick_numbers) +' 입니다. Next time...')
        
        