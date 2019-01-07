import requests
import random
from lotto_functions import pick_lotto, get_lotto, am_i_lucky

Draw = int(input('로또 회차를 선택해주세요: '))
Money = int(input('돈을 넣어주세요: '))
count = 0
while(Money>=0):
    if Money >=1000:
        my_number = pick_lotto()
        real_number = get_lotto(Draw)
        print(am_i_lucky(my_number,real_number))
        Money = Money - 1000
        count = count + 1
    else:
        print('------------------------------------------------------------')
        print('금액이 전부 소진되었습니다. 총 러닝횟수는',count, '회 입니다')
        break
    
