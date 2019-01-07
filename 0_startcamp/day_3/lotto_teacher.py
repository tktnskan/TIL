# import requests
# import random



# url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

# response = requests.get(url, verify=False)
# lotto_data = response.json() 

# real_numbers = []
# repeat =0
# while(repeat<501):
#     repeat=repeat+1
#     for key, value in lotto_data.items():
#         if 'drwtNo' in key:
#          real_numbers.append(value)
    
#     set_real_numbers =set(real_numbers)
#     bonus_number = lotto_data['bnusNo']

#     numbers = list(range(1, 46))
#     pick_numbers = random.sample(numbers, 6)
#     set_pick_numbers = set(pick_numbers)
    
# diff = len(set_pick_numbers - set_real_numbers)
# print(diff)

# if diff == 0:
#     print('1등')

# elif diff == 1:
#     print('2등')

# else:
#     print('다음 기회에')





# match_count = len(my_numbers & real_numbers)
# print(match_count)

# if match_count == 6:
#     print('1등')

# elif match_count == 5 and bonus in my_numbers:
#     print('2등')

# else:
#     print('다음 기회에')










# count = 0
# for my_number in my_numbers:
#     for real_number in real_numbers:
#         if my_number == real_number:
#             count += 1
# print(count)

# if count == 6:
#     print(1)
# elif count == 5 and bonus in my_numbers:
#     print(2)
# elif count == 5:
#     print(3)
    
    


# def am_i_lucky(pick,draw):
#     match = set(pick) & set(draw['numbers'])
#     if len(match) == 6:
#         return('grand prize')
#     elif len(match) == 5 and draw['bpnus'] in pick:
#         return('third prize')
#     else:
#         return('next time...')
    
# result = am_i_lucky([1,2,3,4,5,6], [1,2,3,4,5,6])
# print(result)


# list_1 = [1,2,3,4,5,6]
# dict_1 = {
#     'numbers' : [1,2,3,4,5,7],
#     'bonus' : 6
# }


# my_number = pick_lotto()
# real_number = get_lotto(837)

# result = am_i_lucky(my_number,real_number)
# #result = am_i_lucky(pick_lotto(),get_lotto(837))
# print(result)